"""Completion evidence for an editor handoff; no generation and no network.

This checks coverage, provenance declarations and media containers. It cannot
judge artistic quality or prove an agent's statements true. Human/agent visual
review and host playback checks are therefore recorded separately.
"""
from __future__ import annotations
from pathlib import Path
import struct
import hashlib
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit

KINDS = {"illustration", "photo", "diagram", "chart", "text_card", "video", "brand_asset"}
METHODS = {"image_generation", "video_generation", "layout", "user_provided", "motion_graphics"}
MODES = {"square", "full", "motion", "overlay"}
CAP_STATUSES = {"verified", "unavailable", "not_needed", "not_tested"}
ROLES = {"intro", "ending", "gift"}
MEDICAL_STYLES = {"anatomical", "cute", "schematic", "context", "metaphor"}
MEDICAL_IMAGES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".avif", ".svg"}


def mp4_video_probe(path):
    """Check real ISO BMFF video tracks and payload, not just an ftyp header.

    Deliberately does not claim decoded frames or playback. Fragmented MP4 is
    accepted when it has a video track, moof and nonempty media payload.
    """
    result = {"file": path.name, "container_checked": False, "playback_checked": False}
    try:
        size = path.stat().st_size
        with path.open("rb") as stream:
            def boxes(start, end):
                offset = start
                while offset + 8 <= end:
                    stream.seek(offset)
                    length, kind = struct.unpack(">I4s", stream.read(8))
                    header = 8
                    if length == 1:
                        if offset + 16 > end:
                            raise ValueError("truncated extended box")
                        length = struct.unpack(">Q", stream.read(8))[0]
                        header = 16
                    elif length == 0:
                        length = end - offset
                    if length < header or offset + length > end:
                        raise ValueError("invalid box bounds")
                    yield kind, offset + header, offset + length
                    offset += length
                if offset != end:
                    raise ValueError("trailing incomplete box")

            top = list(boxes(0, size))
            has_payload = any(k == b"mdat" and end > start for k, start, end in top)
            fragmented = any(k == b"moof" for k, _, _ in top)
            tracks = []
            for kind, start, end in top:
                if kind != b"moov":
                    continue
                for tk, ts, te in boxes(start, end):
                    if tk != b"trak":
                        continue
                    is_video, samples = False, 0
                    def scan(a, b):
                        nonlocal is_video, samples
                        for k, s, e in boxes(a, b):
                            if k in {b"mdia", b"minf", b"stbl"}:
                                scan(s, e)
                            elif k == b"hdlr" and e - s >= 12:
                                stream.seek(s + 8)
                                is_video |= stream.read(4) == b"vide"
                            elif k in {b"stsz", b"stz2"} and e - s >= 12:
                                stream.seek(s + 8)
                                samples = max(samples, struct.unpack(">I", stream.read(4))[0])
                    scan(ts, te)
                    if is_video:
                        tracks.append(samples)
            result.update(container_checked=True, video_tracks=len(tracks),
                          sample_count=sum(tracks), fragmented=fragmented,
                          has_media_payload=has_payload,
                          valid=bool(has_payload and tracks and (sum(tracks) > 0 or fragmented)))
    except (OSError, ValueError, struct.error) as exc:
        result.update(valid=False, error=str(exc))
    return result


def member(value, allowed):
    return isinstance(value, str) and value in allowed


def file_hash(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for data in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(data)
    return value.hexdigest()



def medical_image_container(path):
    """Recognize an image container, not its pixels or medical correctness.

    The normal handoff input validator also performs path and SVG safety checks.
    This additional check prevents a nonselected alternative from passing merely
    because a text file has been named .png and given a review declaration.
    """
    with path.open("rb") as stream:
        head = stream.read(64)
    suffix = path.suffix.lower()
    if suffix == ".svg":
        try:
            return ET.parse(path).getroot().tag.rsplit("}", 1)[-1] == "svg"
        except (ET.ParseError, UnicodeError):
            return False
    return {
        ".png": head.startswith(b"\x89PNG\r\n\x1a\n"),
        ".jpg": head.startswith(b"\xff\xd8\xff"),
        ".jpeg": head.startswith(b"\xff\xd8\xff"),
        ".gif": head.startswith((b"GIF87a", b"GIF89a")),
        ".webp": head.startswith(b"RIFF") and head[8:12] == b"WEBP",
        ".avif": b"ftyp" in head[:32] and any(x in head for x in (b"avif", b"avis")),
    }.get(suffix, False)


def assess_medical_variants(scene, root, capabilities, issue):
    """Check all declared alternatives, including those not selected.

    Returns whether the scene declares a variant group. Medical review is a
    recorded human/agent judgement only; this code does not validate anatomy.
    """
    if "medical_variants" not in scene:
        return False
    sid = scene.get("id", "unknown")
    def problem(code, message):
        issue("medical_variants." + code, message, sid)
    def nonempty(value):
        return isinstance(value, str) and bool(value.strip())
    group = scene["medical_variants"]
    if not isinstance(group, dict):
        problem("invalid", "medical_variants は目標数・候補ID・理由を含むオブジェクトにしてください。")
        return True
    target = group.get("target_count")
    if type(target) is not int or not 3 <= target <= 5:
        problem("count", "医学説明の比較候補は3〜5案を指定してください。")
    if not nonempty(group.get("reason")):
        problem("reason", "この場面で比較候補を作る理由を記録してください。")
    ids = group.get("option_ids")
    if (not isinstance(ids, list) or not ids or
            any(not nonempty(value) for value in ids)):
        problem("ids", "option_ids は空でない候補IDの配列にしてください。")
        return True
    if len(ids) != len(set(ids)) or len(ids) != target:
        problem("ids", "候補IDは重複せず、target_count と同じ数が必要です。")
    options = scene.get("options", [])
    if not isinstance(options, list):
        options = []
    matches = {oid: [o for o in options if isinstance(o, dict) and o.get("id") == oid] for oid in ids}
    if any(len(values) != 1 for values in matches.values()):
        problem("unknown_option", "option_ids の各IDに対応する候補が一つずつ必要です。")
    # A documented decision to omit the whole scene removes the obligation to
    # manufacture unused images. Structural group errors above still surface.
    omitted = (scene.get("omit") is True and scene.get("selected") is None and
               member(scene.get("omission_basis"), {"user", "not_applicable"}) and
               nonempty(scene.get("omission_reason")))
    if omitted:
        return True
    # The comparison group controls what must be produced, not the user's
    # final choice. A ready extra option (for example a video) may be selected;
    # the ordinary selected-media checks below still apply to that option.
    styles, paths_seen, hashes_seen = set(), set(), set()
    root = Path(root).resolve()
    for oid, values in matches.items():
        if len(values) != 1:
            continue
        option = values[0]
        prefix = f"{oid}: "
        if option.get("status") != "ready":
            problem("pending", prefix + "未採用案も含め、比較する全候補の実画像制作が必要です。")
        if (option.get("mode") == "motion" or
                not member(option.get("kind"), {"illustration", "photo", "diagram", "chart", "text_card"})):
            problem("image_required", prefix + "医学説明の画像比較には静止画の候補を指定してください。動画は別候補として扱います。")
        medical = option.get("medical_visual")
        if not isinstance(medical, dict):
            medical = {}
        style = medical.get("style")
        if not member(style, MEDICAL_STYLES):
            problem("style", prefix + "医学説明の表現区分が未記録または不正です。")
        else:
            styles.add(style)
        if not nonempty(medical.get("explanation")):
            problem("explanation", prefix + "何を示し、何を簡略化したかを記録してください。")
        review = medical.get("review")
        if not isinstance(review, dict):
            review = {}
        if review.get("status") != "passed" or not nonempty(review.get("evidence")):
            problem("medical_review", prefix + "説明内容と誤解の有無を確認した記録が未完了です。")
        references = review.get("references")
        if (not isinstance(references, list) or any(not nonempty(ref) for ref in references) or
                (style == "anatomical" and not references)):
            problem("references", prefix + "参照した資料の説明・所在を配列で記録してください。解剖重視案には1件以上必要です。")
        production = option.get("production")
        if not isinstance(production, dict):
            production = {}
        method = production.get("method")
        if (not member(method, {"image_generation", "layout", "user_provided"}) or
                not nonempty(production.get("tool")) or not nonempty(production.get("evidence"))):
            problem("production", prefix + "各候補の実際の制作方法・使用機能・生成結果の記録が必要です。")
        if (member(style, {"anatomical", "cute"}) and option.get("kind") != "illustration" or
                member(option.get("kind"), {"illustration", "photo"}) and not member(method, {"image_generation", "user_provided"})):
            problem("illustration_required", prefix + "解剖重視案と可愛い案には実イラストが必要です。イラスト・写真を図形や文字だけで代用できません。")
        if method == "image_generation":
            cap = capabilities.get(method, {})
            if not isinstance(cap, dict) or cap.get("status") != "verified":
                problem("tool_unverified", prefix + "画像生成機能の実行成功が未確認です。")
        visual_review = production.get("review")
        if not isinstance(visual_review, dict):
            visual_review = {}
        if visual_review.get("status") != "passed" or not nonempty(visual_review.get("evidence")):
            problem("visual_review", prefix + "比較用の実画像を目視確認した記録が必要です。")
        reviewed_files = visual_review.get("files_sha256")
        if not isinstance(reviewed_files, dict):
            reviewed_files = {}
        files = option.get("files")
        if not isinstance(files, list) or not files or any(not nonempty(rel) for rel in files):
            problem("files", prefix + "比較候補の空でない実画像ファイル一覧が必要です。")
            continue
        found_image = False
        for rel in files:
            try:
                path = (root / rel).resolve()
                if not path.is_relative_to(root) or not path.is_file() or not path.stat().st_size:
                    raise ValueError("missing or outside root")
                digest = file_hash(path)
                if reviewed_files.get(rel) != digest:
                    problem("review_stale", prefix + "目視確認のSHA-256と実ファイルが一致しません。")
                if path.suffix.lower() not in MEDICAL_IMAGES:
                    continue
                if not medical_image_container(path):
                    problem("image_format", prefix + "画像の拡張子とファイル形式が一致しません。")
                    continue
                found_image = True
                if path in paths_seen or digest in hashes_seen:
                    problem("duplicate_image", prefix + "同じ画像ファイル・同じ内容のコピーを別案として数えられません。")
                paths_seen.add(path)
                hashes_seen.add(digest)
            except (OSError, ValueError, RuntimeError):
                problem("missing_file", prefix + "比較用の実ファイルを読み取れません。")
        if not found_image:
            problem("image_required", prefix + "参照画像や案の説明だけでなく、完成した比較用画像が必要です。")
    if not {"anatomical", "cute"}.issubset(styles):
        problem("required_styles", "医学説明の比較候補には解剖重視案と可愛いイラスト案の両方が必要です。")
    return True


def assess_quality(case, root):
    """Return blockers instead of preventing useful draft output.

    Existing cases lacking evidence remain renderable but cannot be labelled
    complete. Callers must preserve this report in both preview and ZIP.
    """
    blockers, warnings, probes = [], [], []
    report = {"schema_version": 1, "status": "needs_review", "blockers": blockers,
              "warnings": warnings, "media_probes": probes, "host_checks": {},
              "limits": "記録された制作・目視確認とファイル構造の検査です。美的品質、医学的正確さ、Webでの生成・再生を自動保証しません。"}

    def issue(code, message, sid=None):
        entry = {"code": code, "message": message}
        if sid:
            entry["scene_id"] = sid
        blockers.append(entry)

    def nonempty(value):
        return isinstance(value, str) and bool(value.strip())

    quality = case.get("quality")
    if not isinstance(quality, dict) or quality.get("version") != 1:
        issue("quality.missing", "制作・目視確認の記録がありません。旧形式の下書きとして表示します。")
        return report
    if quality.get("source_sha256") != case.get("source", {}).get("sha256"):
        issue("quality.source_changed", "品質確認が現在の原稿に紐付いていません。原稿変更後に構成・発話位置を再確認してください。")
    caps = quality.get("capabilities", {})
    if not isinstance(caps, dict):
        caps = {}
    for name in ("image_generation", "video_generation", "file_output"):
        item = caps.get(name, {})
        if not isinstance(item, dict):
            item = {}
        if not member(item.get("status"), CAP_STATUSES) or not nonempty(item.get("evidence")):
            issue("capability.evidence", f"{name}: 実行確認・制約・不要理由の記録が必要です。")
        if item.get("status") == "verified" and not nonempty(item.get("tool")):
            issue("capability.tool", f"{name}: 実際に使用した機能を記録してください。")
        if name == "file_output" and item.get("status") != "verified":
            issue("capability.files", "実ファイルを出力・読み戻しできたことを確認してください。")

    requirements = quality.get("requirements", {})
    if not isinstance(requirements, dict):
        requirements = {}
    for field, allowed in (("required_kinds", KINDS), ("required_modes", MODES), ("required_profile_roles", ROLES)):
        value = requirements.get(field, [])
        if not isinstance(value, list) or any(not isinstance(v, str) or v not in allowed for v in value):
            issue("requirements.invalid", f"requirements.{field}: 許可された分類の配列が必要です。")
            requirements = dict(requirements, **{field: []})

    chosen, selected_by_id = [], {}
    scenes = case.get("scenes", [])
    for scene in scenes:
        sid = scene.get("id", "unknown")
        if not nonempty(scene.get("purpose")):
            issue("scene.purpose", "この場面で視聴者に伝える内容が未記録です。", sid)
        if assess_medical_variants(scene, root, caps, issue):
            report["medical_variant_review"] = "全比較候補の実ファイル・制作記録・目視確認と医学説明確認の申告を検査。解剖学的正しさの自動判定ではありません。"
        if scene.get("omit"):
            if not member(scene.get("omission_basis"), {"user", "not_applicable"}) or not nonempty(scene.get("omission_reason")):
                issue("scene.omission", "素材を使わない本人指定、または不要な理由が未記録です。生成不能による省略はpendingにしてください。", sid)
            continue
        option = next((o for o in scene.get("options", []) if o.get("id") == scene.get("selected")), None)
        if not option or option.get("status") != "ready":
            issue("scene.pending", "採用する実素材が未完成です。", sid)
            continue
        selected_by_id[sid] = option
        chosen.append(option)
        kind = option.get("kind")
        if not member(kind, KINDS):
            issue("media.kind", "採用素材の表現種類が未記録です。", sid)
        if not nonempty(option.get("reason")):
            issue("media.reason", "採用する表現の理由を記録してください。", sid)
        prod = option.get("production", {})
        if not isinstance(prod, dict):
            prod = {}
        method = prod.get("method")
        if not member(method, METHODS) or not nonempty(prod.get("tool")) or not nonempty(prod.get("evidence")):
            issue("media.provenance", "実際の制作方法・機能・生成結果または原本の記録が必要です。", sid)
        if member(kind, {"illustration", "photo"}) and not member(method, {"image_generation", "user_provided"}):
            issue("media.illustration_substitution", "イラスト・写真を図形や文字カードだけで代用できません。", sid)
        if kind == "video" and option.get("mode") != "motion":
            issue("media.video_mode", "動画の採用にはmotionと実動画が必要です。", sid)
        if option.get("mode") == "motion" and kind != "video":
            issue("media.video_kind", "動画の表現種類はvideoにしてください。", sid)
        if kind == "video" and not member(method, {"video_generation", "user_provided", "motion_graphics"}):
            issue("media.video_method", "開始画像や文字カードを完成動画として数えられません。", sid)
        if member(method, {"image_generation", "video_generation"}):
            cap = caps.get(method, {})
            if not isinstance(cap, dict) or cap.get("status") != "verified":
                issue("media.tool_unverified", f"{method}: 実際の生成成功が未確認です。", sid)
        review = prod.get("review", {})
        if not isinstance(review, dict) or review.get("status") != "passed" or not nonempty(review.get("evidence")):
            issue("media.visual_review", "採用する実物の目視確認が未完了です。", sid)
        reviewed_files = review.get("files_sha256", {}) if isinstance(review, dict) else {}
        if not isinstance(reviewed_files, dict):
            reviewed_files = {}
        for rel in option.get("files", []):
            path = (Path(root) / rel).resolve()
            if not path.is_relative_to(Path(root).resolve()) or not path.is_file():
                issue("media.review_file", "目視確認した実ファイルを読み取れません。", sid)
            elif reviewed_files.get(rel) != file_hash(path):
                issue("media.review_stale", "目視確認のSHA-256が実ファイルと一致しません。修正した実物を再確認してください。", sid)
        if kind == "video":
            video_files = [p for p in option.get("files", []) if Path(p).suffix.lower() in {".mp4", ".webm"}]
            if not video_files:
                issue("media.video_missing", "実MP4/WebMがありません。静止プレビューは完成動画に数えられません。", sid)
            for rel in video_files:
                path = (Path(root) / rel).resolve()
                if not path.is_relative_to(Path(root).resolve()) or not path.is_file():
                    issue("media.video_missing", "動画ファイルを読み取れません。", sid)
                elif path.suffix.lower() == ".mp4":
                    probe = mp4_video_probe(path)
                    probes.append(dict(probe, scene_id=sid))
                    if not probe.get("valid"):
                        issue("media.video_container", "再生可能な動画トラック・映像データを含むMP4を確認できません。", sid)
                else:
                    warnings.append({"code": "media.webm_review", "scene_id": sid, "message": "WebMの映像・再生は目視確認記録とホストで確認してください。"})
    if not chosen:
        issue("media.none", "採用・完成済みの実素材がありません。素材一式として完了できません。")
    kinds = {o.get("kind") for o in chosen if isinstance(o.get("kind"), str)}
    modes = {o.get("mode") for o in chosen}
    for k in requirements.get("required_kinds", []):
        if k not in kinds:
            issue("requirements.kind_missing", f"必要な素材種類 {k} が完成していません。未制作の別案では要件を満たしません。")
    for m in requirements.get("required_modes", []):
        if m not in modes:
            issue("requirements.mode_missing", f"必要な表示形式 {m} が完成していません。")

    profile = quality.get("profile_assets", [])
    if not isinstance(profile, list):
        profile = []
    seen = set()
    for item in profile:
        if not isinstance(item, dict):
            issue("profile.invalid", "本人素材の確認記録はオブジェクトにしてください。")
            continue
        role, status = item.get("role"), item.get("status")
        if not member(role, ROLES) or role in seen:
            issue("profile.role", "本人素材の役割が不正または重複しています。")
            continue
        seen.add(role)
        if not member(status, {"verified", "not_applicable", "waived", "missing"}) or not nonempty(item.get("evidence")):
            issue("profile.evidence", f"{role}: 原本確認・不要理由・本人による省略指定を記録してください。")
        if status == "missing":
            issue("profile.missing", f"{role}: 本人の原本素材が不足しています。別素材へ無断で代替できません。")
        if role in requirements.get("required_profile_roles", []) and not member(status, {"verified", "waived"}):
            issue("profile.required", f"{role}: 必須の本人素材が未確認です。")
        if status == "verified":
            ids = item.get("scene_ids", [])
            if not isinstance(ids, list) or not ids or any(not isinstance(sid, str) or sid not in selected_by_id or selected_by_id[sid].get("kind") != "brand_asset" for sid in ids):
                issue("profile.scene_missing", f"{role}: 確認した本人素材を使う完成済みbrand_assetの場面が必要です。")
    for role in ROLES - seen:
        issue("profile.unchecked", f"{role}: 本人素材の必要性・取得状態が未確認です。")

    reviews = quality.get("reviews", {})
    if not isinstance(reviews, dict):
        reviews = {}
    for name in ("material_mix", "visual", "editor_ready"):
        review = reviews.get(name, {})
        if not isinstance(review, dict) or review.get("status") != "passed" or not nonempty(review.get("evidence")):
            issue("review.incomplete", f"{name}: 採用内容を確認した結果・修正反映の記録が必要です。")
    heavy = sum(member(o.get("kind"), {"diagram", "chart", "text_card"}) for o in chosen)
    if len(chosen) >= 5 and heavy / len(chosen) >= .8:
        mix = reviews.get("material_mix", {})
        if not isinstance(mix, dict) or not nonempty(mix.get("diagram_heavy_reason")):
            issue("review.diagram_heavy", "図解・文字カードに偏っています。生活・感情・動きの場面を再検討し、妥当な場合だけ理由を記録してください。")
    hosts = quality.get("host_checks", {})
    if not isinstance(hosts, dict):
        hosts = {}
    inline_requested = case.get("preview", {}).get("inline_requested", False)
    for host in ("hosted", "browser", "chat_preview"):
        optional_inline = host == "chat_preview" and not inline_requested
        default = {"status": "not_applicable", "evidence": "会話内表示は明示依頼時だけ行います。"} if optional_inline else {"status": "not_run", "evidence": "未確認"}
        item = hosts.get(host, default)
        allowed = {"passed", "not_run", "failed"} | ({"not_applicable"} if optional_inline else set())
        if not isinstance(item, dict) or not member(item.get("status"), allowed) or not nonempty(item.get("evidence")):
            issue("host.invalid", f"{host}: 表示・再生確認の状態が不正です。")
            item = {"status": "not_run", "evidence": "有効な確認記録なし"}
        item = dict(item)
        if host == "hosted":
            # Metadata can record verified publication, but this builder does
            # not perform it. Never infer private access from an unlisted URL.
            visibility = item.get("visibility")
            if visibility is not None and visibility != "private":
                issue("host.private_required", "hosted: 確認ページはprivateが必要です。一般公開・URLを知る人向け公開へ切り替えられません。")
                item["status"] = "failed"
            elif item["status"] == "passed" and visibility != "private":
                issue("host.private_unverified", "hosted: 限定アクセスが未確認のため、配信確認済みにはできません。")
                item["status"] = "not_run"
            if item["status"] == "passed":
                try:
                    value = item.get("url", "")
                    url = urlsplit(value if isinstance(value, str) else "")
                    valid_url = url.scheme == "https" and bool(url.hostname) and not url.username and not url.password and not any(c.isspace() for c in value)
                except (TypeError, ValueError):
                    valid_url = False
                if not valid_url:
                    issue("host.url_missing", "hosted: 配信された確認ページのHTTPS URLが必要です。")
                    item["status"] = "not_run"
        if item["status"] == "failed":
            issue("host.failed", f"{host}: 表示・再生テストの失敗が未解消です。")
        report["host_checks"][host] = item
    report["status"] = "passed" if not blockers else "needs_review"
    report["verified_scope"] = "素材構成・制作記録・原本参照・目視確認記録・ファイル構造"
    return report

