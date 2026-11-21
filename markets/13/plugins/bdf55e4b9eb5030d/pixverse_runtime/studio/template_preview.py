"""Cache a small selection of official template previews for local chat display."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from http.client import HTTPException
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

PREVIEW_HOSTS = {"media.pixverse.ai", "media.pixverse.cn"}
IMAGE_LIMIT = 12 * 1024 * 1024
VIDEO_LIMIT = 64 * 1024 * 1024


def _validate_url(url: str) -> None:
    if not isinstance(url, str):
        raise ValueError("Preview URL must be a string")
    parsed = urlsplit(url)
    if (
        parsed.scheme != "https"
        or parsed.hostname not in PREVIEW_HOSTS
        or parsed.username
        or parsed.password
        or parsed.port not in {None, 443}
    ):
        raise ValueError("Preview URL must use the official PixVerse HTTPS media host")


class _PreviewRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        _validate_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _media_suffix(prefix: bytes, kind: str) -> str:
    if kind == "video":
        if prefix[4:8] == b"ftyp":
            return ".mp4"
    else:
        if prefix.startswith(b"\x89PNG\r\n\x1a\n"):
            return ".png"
        if prefix.startswith(b"\xff\xd8\xff"):
            return ".jpg"
        if prefix.startswith((b"GIF87a", b"GIF89a")):
            return ".gif"
        if prefix.startswith(b"RIFF") and prefix[8:12] == b"WEBP":
            return ".webp"
    raise ValueError(f"Preview response is not a supported {kind} file")


def cache_preview(url: str, *, template_id: int, kind: str, directory: Path) -> dict[str, Any]:
    """Download with no account credentials; validate, bound and atomically cache bytes."""
    _validate_url(url)
    directory.mkdir(parents=True, exist_ok=True)
    stem = f"{template_id}-{kind}-{hashlib.sha256(url.encode()).hexdigest()[:16]}"
    metadata = directory / f"{stem}.json"
    limit = VIDEO_LIMIT if kind == "video" else IMAGE_LIMIT
    try:
        saved = json.loads(metadata.read_text())
        if saved["suffix"] not in {".jpg", ".png", ".gif", ".webp", ".mp4"}:
            raise ValueError("Invalid cached preview format")
        local = directory / (stem + saved["suffix"])
        if saved["source_url"] == url and local.is_file() and 0 < local.stat().st_size <= limit:
            content = local.read_bytes()
            if (
                hashlib.sha256(content).hexdigest() == saved["sha256"]
                and _media_suffix(content[:32], kind) == saved["suffix"]
            ):
                return {"status": "cached", "local_path": str(local.resolve()), "source_url": url}
    except (OSError, ValueError, KeyError, TypeError):
        pass

    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; PixVerseAgentPlugin)",
            "Referer": "https://app.pixverse.ai/",
            "Accept": "video/*" if kind == "video" else "image/*",
        },
    )
    temporary: Path | None = None
    try:
        with build_opener(_PreviewRedirects()).open(request, timeout=30) as response:
            _validate_url(response.geturl())
            length = response.headers.get("Content-Length")
            expected = int(length) if length is not None else None
            if expected is not None and (expected <= 0 or expected > limit):
                raise ValueError("Preview exceeds the download size limit or is empty")
            size = 0
            digest = hashlib.sha256()
            prefix = b""
            with tempfile.NamedTemporaryFile(
                dir=directory, prefix=stem + ".", suffix=".part", delete=False
            ) as file:
                temporary = Path(file.name)
                while True:
                    chunk = response.read(64 * 1024)
                    if not chunk:
                        break
                    size += len(chunk)
                    if size > limit:
                        raise ValueError("Preview exceeds the download size limit")
                    if len(prefix) < 32:
                        prefix = (prefix + chunk)[:32]
                    digest.update(chunk)
                    file.write(chunk)
            if expected is not None and size != expected:
                raise ValueError("Preview download is incomplete")
            suffix = _media_suffix(prefix, kind)
            local = directory / (stem + suffix)
            os.replace(temporary, local)
            metadata.write_text(
                json.dumps({"source_url": url, "suffix": suffix, "sha256": digest.hexdigest()})
            )
            return {"status": "ready", "local_path": str(local.resolve()), "source_url": url}
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def _name(item: dict[str, Any]) -> str:
    try:
        labels = json.loads(item.get("i18n_json") or "{}")
        translated = (labels.get("en-US") or labels.get("en") or {}).get("display_name")
    except (TypeError, ValueError, AttributeError):
        translated = None
    return str(translated or item.get("display_name") or item["template_id"])


def _inputs(item: dict[str, Any]) -> str:
    fields = item.get("input_fields")
    if isinstance(fields, list) and fields:
        return ", ".join(
            str(f.get("content_type") or "input")
            + (" (optional)" if f.get("required") is False else "")
            for f in fields
            if isinstance(f, dict)
        )
    count = str(item.get("effect_type") or "0")
    return "Text" if count == "0" else f"{count} image(s)"


def template_previews(
    catalog: Path, ids: list[int], *, project_path: Path, videos: bool = False
) -> dict[str, Any]:
    if not ids or len(ids) > 8 or len(set(ids)) != len(ids) or any(i <= 0 for i in ids):
        raise ValueError("Select 1 to 8 distinct positive template IDs")
    if catalog.stat().st_size > 16 * 1024 * 1024:
        raise ValueError("Template catalog is too large; use a smaller catalog page")
    data = json.loads(catalog.read_text(encoding="utf-8"))
    items = data.get("items", data.get("data", [data])) if isinstance(data, dict) else data
    if not isinstance(items, list):
        raise ValueError("Expected a template search/list/detail JSON response")
    by_id = {str(item.get("template_id")): item for item in items if isinstance(item, dict)}
    if any(str(i) not in by_id for i in ids):
        raise ValueError("Selected template ID is absent from the supplied catalog")
    directory = project_path / "reference" / "template-previews"
    results = []
    for template_id in ids:
        item = by_id[str(template_id)]
        row = {
            "template_id": template_id,
            "name": _name(item),
            "output_type": "image" if item.get("template_type") == 2 else "video",
            "inputs": _inputs(item),
        }
        sources = {
            "image": next(
                (item.get(k) for k in ("web_thumbnail_url", "app_thumbnail_url") if item.get(k)), ""
            ),
            "animation": next(
                (
                    item.get(k)
                    for k in ("web_thumbnail_gif_url", "app_thumbnail_gif_url")
                    if item.get(k)
                ),
                "",
            ),
            "video": next(
                (
                    item.get(k)
                    for k in ("web_thumbnail_video_url", "app_thumbnail_video_url")
                    if item.get(k)
                ),
                "",
            ),
        }
        for kind in ("image", "animation", "video"):
            url = sources[kind]
            try:
                if url:
                    _validate_url(url)
            except ValueError as exc:
                row[kind] = {"status": "failed", "local_path": "", "error": str(exc)}
                continue
            if kind == "animation" and row["output_type"] == "image":
                row[kind] = {"status": "not_requested"}
            elif (
                kind == "video"
                and not videos
                and (row["output_type"] == "image" or row["animation"].get("local_path"))
            ):
                row[kind] = {"status": "not_requested", "source_url": url}
            elif not url:
                row[kind] = {"status": "not_available", "local_path": ""}
            else:
                try:
                    row[kind] = cache_preview(
                        url, template_id=template_id, kind=kind, directory=directory
                    )
                except (OSError, ValueError, HTTPException) as exc:
                    row[kind] = {
                        "status": "failed",
                        "local_path": "",
                        "source_url": url,
                        "error": str(exc),
                    }
        results.append(row)
    result = {
        "items": results,
        "project_path": str(project_path.resolve()),
        "ok": all(
            any(row[k].get("local_path") for k in ("image", "animation", "video"))
            and (not videos or row["video"]["status"] != "failed")
            for row in results
        ),
    }
    directory.mkdir(parents=True, exist_ok=True)
    report = directory / "selection.json"
    report.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def previews_markdown(result: dict[str, Any]) -> str:
    def cell(value: Any) -> str:
        return (
            str(value)
            .replace("|", "\\|")
            .replace("\n", " ")
            .replace("\r", " ")
            .replace("[", "\\[")
            .replace("]", "\\]")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

    items = result["items"]
    lines = [
        "| " + " | ".join(f"{n}. {cell(row['name'])}" for n, row in enumerate(items, 1)) + " |",
        "| " + " | ".join("---" for _ in items) + " |",
    ]
    images = []
    links = []
    for row in items:
        local = (
            (row.get("animation", {}).get("local_path") or row["video"].get("local_path"))
            if row["output_type"] == "video"
            else None
        )
        local = local or row["image"].get("local_path")
        images.append(
            f"![Template {row['template_id']}](<{local}>)" if local else "Preview unavailable"
        )
        video = row["video"].get("local_path") or row["video"].get("source_url")
        links.append(f"[View example](<{video}>)" if video else "No motion example")
    for cells in (images, [f"{r['output_type']} / {cell(r['inputs'])}" for r in items], links):
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)
