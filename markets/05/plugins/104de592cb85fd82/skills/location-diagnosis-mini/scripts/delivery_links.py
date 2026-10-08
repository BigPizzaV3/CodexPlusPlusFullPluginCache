"""Build final-answer links from verified files, not panel-opening receipts."""

from pathlib import Path


def file_link(label: str, path: Path) -> str:
    path = path.expanduser().resolve()
    if not path.is_file():
        raise OSError(f"納品fileが見つかりません: {path}")
    target = str(path).replace("<", "%3C").replace(">", "%3E").replace("\n", "%0A").replace("\r", "%0D")
    # The standard cloud file runtime uses sandbox links; local Codex uses absolute links.
    if path.is_relative_to(Path('/mnt/data')):
        target = "sandbox:" + target
    return f"[{label}](<{target}>)"


def delivery_markdown(html_path: Path, pdf_path: Path | None = None) -> str:
    links = [file_link("PDFを開く", pdf_path)] if pdf_path else []
    links.append(file_link("HTMLを開く", html_path))
    return "\n\n".join(links)
