#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import html as html_lib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Any


STRUCTURAL_TAG_RE = re.compile(
    r"""(?is)<\s*(?P<close>/?)\s*(?P<name>html|body|main|section|div|table|thead|tbody|tfoot|tr|td)\b(?:(?:"[^"]*"|'[^']*'|[^"'>])*>|[^>]*>)"""
)
STRUCTURAL_OR_IMAGE_TAG_RE = re.compile(
    r"""(?is)<\s*(?P<close>/?)\s*(?P<name>html|body|main|section|div|table|thead|tbody|tfoot|tr|td|img)\b(?:(?:"[^"]*"|'[^']*'|[^"'>])*>|[^>]*>)"""
)
SPAN_OPEN_TAG_RE = re.compile(r"""(?is)<span\b(?:(?:"[^"]*"|'[^']*'|[^"'>])*>|[^>]*>)""")
BODY_OPEN_TAG_RE = re.compile(r"""(?is)<body\b(?:(?:"[^"]*"|'[^']*'|[^"'>])*>|[^>]*>)""")
BODY_CLOSE_TAG_RE = re.compile(r"(?is)</body\s*>")
WHITESPACE_RUN_RE = re.compile(r"\s+")
# The `[if ...]>` head and `<![endif]` tail of a conditional comment tokenize as text once
# the `<!--`/`-->` wrapper is stripped. They are structure, not copy, so the inventory
# listing drops them; the sweep counts still see them, exactly as the write path does.
CONDITIONAL_COMMENT_GUARD_RE = re.compile(r"(?is)^(?:\[if[^\]]*\]>|<!\[endif\])$")
CLASS_ATTR_RE = re.compile(r"""(?is)\bclass\s*=\s*(["'])(.*?)\1""")
IMAGE_ATTRIBUTE_RE = re.compile(
    r"""(?is)(?P<prefix>(?<![\w:-])(?P<name>alt|title)\s*=\s*)(?P<quote>["'])(?P<value>.*?)(?P=quote)"""
)
HTML_TOKEN_RE = re.compile(
    # A tag may carry a raw ">" inside a quoted attribute value, so quoted runs are
    # consumed whole before looking for the closing ">" — the same reading html.parser
    # gives, which continues a quoted value across ">". The trailing alternative only
    # takes over when the quoted branch cannot reach a ">" at all (a quote left open to
    # end of input), where it restores the historical first-">" behaviour.
    r"""(?is)(<!--.*?-->|<(?:"[^"]*"|'[^']*'|[^"'>])+>|<[^>]+>)"""
)
# Exactly the skip set of RetenoTextExtractor in verify_reteno_email_translation.py, so this
# write surface and that verify surface agree on which text counts as visible.
NON_VISIBLE_TEXT_TAGS = frozenset({"head", "script", "style", "noscript"})
NON_VISIBLE_TAG_LIST = "/".join(sorted(NON_VISIBLE_TEXT_TAGS))
NON_VISIBLE_TAG_RE = re.compile(
    rf"""(?is)^<\s*(?P<close>/?)\s*(?P<name>{"|".join(sorted(NON_VISIBLE_TEXT_TAGS))})\b"""
)
# --- shared merge-token grammar; keep byte-identical with verify_reteno_email_translation.py ---
# Velocity/merge tokens as they appear in Reteno builder exports: $name, $!name, ${name},
# $!{name} with optional .member chains and (...) call syntax, plus VTL directives.
MERGE_TOKEN_RE = re.compile(
    r"""(?x)
    \$!?\{[^{}]*\}
    | \$!?[A-Za-z_][A-Za-z0-9_-]*(?:\([^()]*\))?(?:\.[A-Za-z_][A-Za-z0-9_-]*(?:\([^()]*\))?)*
    | \#(?:set|foreach|if|elseif|else|end|macro|parse|include|stop|break)\b
    """
)
# A directive that carries no arguments is indistinguishable from prose ("#end of season
# sale"), so it counts as a token only in a document that also opens a real VTL block.
BARE_VELOCITY_DIRECTIVES = frozenset({"#end", "#else", "#stop", "#break"})
VELOCITY_OPENER_RE = re.compile(r"#(?:if|foreach|macro)\s*\(")


def _merge_token_counts(html: str) -> Counter[str]:
    has_opener = VELOCITY_OPENER_RE.search(html) is not None
    return Counter(
        token
        for token in (match.group(0) for match in MERGE_TOKEN_RE.finditer(html))
        if has_opener or token not in BARE_VELOCITY_DIRECTIVES
    )
# --- end shared merge-token grammar ---
REPLACEMENT_BLOCK_TYPES = {"text", "button", "menu", "image", "hidden_preheader", "document"}
BLOCK_CENSUS_TYPES = ("text", "button", "menu", "image", "hidden_preheader")
MATCH_MODES = {"auto", "single", "responsive_pair", "all"}
INLINE_TAGS = frozenset({"a", "b", "em", "i", "s", "small", "span", "strong", "sub", "sup", "u"})
DESKTOP_HIDDEN_CLASS = "es-desk-hidden"
MOBILE_HIDDEN_CLASS = "es-mobile-hidden"
RESPONSIVE_PAIR_VISIBILITIES = frozenset({"desktop-only", "mobile-only"})
INVENTORY_CONTEXT_RADIUS = 48
INVENTORY_MAX_MATCHES = 20


class EditError(Exception):
    pass


@dataclass(frozen=True)
class ReplacementSpec:
    block_type: str
    old: str
    new: str
    match_mode: str = "auto"
    expected_blocks: int | None = None
    expected_matches: int | None = None
    text_mode: str = "text"


@dataclass(frozen=True)
class EditableBlock:
    block_type: str
    inner_start: int
    inner_end: int
    effective_visibility: str = "both"
    visibility_classes: tuple[str, ...] = ()


@dataclass(frozen=True)
class EditableImage:
    tag_start: int
    tag_end: int
    effective_visibility: str = "both"
    visibility_classes: tuple[str, ...] = ()


@dataclass(frozen=True)
class StructuralElement:
    tag_name: str
    inner_start: int
    block_type: str | None
    hidden_on: frozenset[str]
    visibility_classes: tuple[str, ...]


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Apply validated text and image alt/title replacements inside Reteno exported HTML."
        ),
    )
    parser.add_argument("--html", type=Path, required=True, help="Path to the exported Reteno HTML file to edit in place.")
    parser.add_argument(
        "--replacements",
        type=Path,
        default=None,
        help="Path to a JSON file containing a replacement list or an object with a replacements array.",
    )
    parser.add_argument(
        "--allow-document-sweep",
        action="store_true",
        help=(
            "Authorize block_type 'document' replacements, which sweep the whole rendered "
            "body instead of one editable block. Full localization only."
        ),
    )
    subparsers = parser.add_subparsers(dest="command")
    inventory = subparsers.add_parser(
        "inventory",
        help="Print a JSON census of editable blocks, uncovered visible text, and replacement occurrences.",
    )
    # SUPPRESS, not None: a subparser default would otherwise overwrite the top-level
    # --replacements value in the shared namespace.
    inventory.add_argument(
        "--replacements",
        type=Path,
        default=argparse.SUPPRESS,
        help="Optional replacement JSON to audit occurrence counts against.",
    )

    args = parser.parse_args()
    if args.command is None and args.replacements is None:
        parser.error("the following arguments are required: --replacements")
    return args


def _load_replacements(path: Path, *, require_document_counts: bool = True) -> list[ReplacementSpec]:
    try:
        raw_value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise EditError(f"replacements file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise EditError(f"replacements file is not valid JSON: {path}: {exc}") from exc

    if isinstance(raw_value, dict):
        raw_value = raw_value.get("replacements")
    if not isinstance(raw_value, list):
        raise EditError("replacements JSON must be a list or an object with a 'replacements' list")

    replacements: list[ReplacementSpec] = []
    for index, item in enumerate(raw_value):
        if not isinstance(item, dict):
            raise EditError(f"replacement[{index}] must be an object")
        block_type = str(item.get("block_type") or "").strip().lower()
        old = item.get("old")
        new = item.get("new")
        match_mode = str(item.get("match_mode") or "auto").strip().lower()
        expected_blocks = item.get("expected_blocks")
        expected_matches = item.get("expected_matches")
        text_mode = item.get("text_mode", "text")
        if text_mode not in {"text", "inline"}:
            raise EditError(f"replacement[{index}] text_mode must be 'text' or 'inline'")
        if text_mode == "inline" and block_type not in {"text", "button", "menu", "document"}:
            raise EditError(f"replacement[{index}] inline mode requires a visible text block")
        if block_type not in REPLACEMENT_BLOCK_TYPES:
            allowed = "', '".join(sorted(REPLACEMENT_BLOCK_TYPES))
            raise EditError(f"replacement[{index}] block_type must be one of '{allowed}'")
        if not isinstance(old, str) or not old:
            raise EditError(f"replacement[{index}] old must be a non-empty string")
        if not isinstance(new, str):
            raise EditError(f"replacement[{index}] new must be a string")
        if match_mode not in MATCH_MODES:
            raise EditError(
                f"replacement[{index}] match_mode must be 'auto', 'single', 'responsive_pair', or 'all'"
            )
        if expected_blocks is not None and (
            not isinstance(expected_blocks, int) or isinstance(expected_blocks, bool) or expected_blocks < 1
        ):
            raise EditError(f"replacement[{index}] expected_blocks must be a positive integer")
        if expected_matches is not None and (
            not isinstance(expected_matches, int) or isinstance(expected_matches, bool) or expected_matches < 1
        ):
            raise EditError(f"replacement[{index}] expected_matches must be a positive integer")
        if match_mode == "all" and expected_blocks is None:
            raise EditError(f"replacement[{index}] match_mode 'all' requires expected_blocks")
        # A document sweep has no block partition to disambiguate it, so the occurrence
        # count is the only bound left; without it the sweep is unbounded by construction.
        if block_type == "document" and require_document_counts and expected_matches is None:
            raise EditError(
                f"replacement[{index}] block_type 'document' requires expected_matches"
            )
        if text_mode == "inline" and require_document_counts and expected_matches is None:
            raise EditError(f"replacement[{index}] inline mode requires expected_matches")
        replacements.append(
            ReplacementSpec(
                block_type=block_type,
                old=old,
                new=new,
                match_mode=match_mode,
                expected_blocks=expected_blocks,
                expected_matches=expected_matches,
                text_mode=text_mode,
            )
        )
    return replacements


def _extract_block_type(tag_text: str) -> str | None:
    classes = _tag_classes(tag_text)
    if "esd-block-button" in classes:
        return "button"
    if "esd-block-text" in classes:
        return "text"
    if "esd-block-menu" in classes:
        return "menu"
    return None


def _tag_classes(tag_text: str) -> frozenset[str]:
    match = CLASS_ATTR_RE.search(tag_text)
    if match is None:
        return frozenset()
    return frozenset(value.casefold() for value in match.group(2).split())


def _tag_has_class(tag_text: str, class_name: str) -> bool:
    return class_name.casefold() in _tag_classes(tag_text)


def _visibility_classes(tag_text: str) -> tuple[str, ...]:
    classes: list[str] = []
    if _tag_has_class(tag_text, DESKTOP_HIDDEN_CLASS):
        classes.append(DESKTOP_HIDDEN_CLASS)
    if _tag_has_class(tag_text, MOBILE_HIDDEN_CLASS):
        classes.append(MOBILE_HIDDEN_CLASS)
    return tuple(classes)


def _hidden_devices(classes: tuple[str, ...]) -> frozenset[str]:
    hidden: set[str] = set()
    if DESKTOP_HIDDEN_CLASS in classes:
        hidden.add("desktop")
    if MOBILE_HIDDEN_CLASS in classes:
        hidden.add("mobile")
    return frozenset(hidden)


def _effective_visibility(hidden_on: frozenset[str]) -> str:
    if hidden_on == {"desktop", "mobile"}:
        return "neither"
    if hidden_on == {"desktop"}:
        return "mobile-only"
    if hidden_on == {"mobile"}:
        return "desktop-only"
    return "both"


def _find_editable_blocks(html: str) -> list[EditableBlock]:
    stack: list[StructuralElement] = []
    blocks: list[EditableBlock] = []

    for match in STRUCTURAL_TAG_RE.finditer(html):
        tag_text = match.group(0)
        tag_name = match.group("name").lower()
        is_close = bool(match.group("close"))
        if not is_close:
            own_classes = _visibility_classes(tag_text)
            inherited_hidden = stack[-1].hidden_on if stack else frozenset()
            inherited_classes = stack[-1].visibility_classes if stack else ()
            stack.append(
                StructuralElement(
                    tag_name=tag_name,
                    inner_start=match.end(),
                    block_type=_extract_block_type(tag_text) if tag_name == "td" else None,
                    hidden_on=inherited_hidden | _hidden_devices(own_classes),
                    visibility_classes=tuple(dict.fromkeys((*inherited_classes, *own_classes))),
                )
            )
            continue
        if not stack:
            raise EditError(f"Reteno HTML is malformed: unmatched </{tag_name}> tag")
        element = stack.pop()
        if element.tag_name != tag_name:
            raise EditError(
                "Reteno HTML is malformed: "
                f"expected </{element.tag_name}> before </{tag_name}>"
            )
        if element.block_type is not None:
            blocks.append(
                EditableBlock(
                    block_type=element.block_type,
                    inner_start=element.inner_start,
                    inner_end=match.start(),
                    effective_visibility=_effective_visibility(element.hidden_on),
                    visibility_classes=element.visibility_classes,
                )
            )

    if stack:
        raise EditError(f"Reteno HTML is malformed: unmatched <{stack[-1].tag_name}> tag")
    blocks.sort(key=lambda block: block.inner_start)
    return blocks


def _find_hidden_preheader_blocks(html: str) -> list[EditableBlock]:
    blocks: list[EditableBlock] = []
    for match in SPAN_OPEN_TAG_RE.finditer(html):
        if not _tag_has_class(match.group(0), "esd-hidden-preheader"):
            continue
        close_match = re.search(r"(?is)</span\s*>", html[match.end() :])
        if close_match is None:
            raise EditError("Reteno HTML is malformed: hidden preheader span is missing </span>")
        inner_end = match.end() + close_match.start()
        blocks.append(
            EditableBlock(
                block_type="hidden_preheader",
                inner_start=match.end(),
                inner_end=inner_end,
                effective_visibility="neither",
            )
        )
    return blocks


def _document_sweep_span(html: str) -> tuple[int, int]:
    open_match = BODY_OPEN_TAG_RE.search(html)
    close_match = None
    for close_match in BODY_CLOSE_TAG_RE.finditer(html):
        pass
    if open_match is None or close_match is None or close_match.start() < open_match.end():
        return 0, len(html)
    return open_match.end(), close_match.start()


def _find_document_blocks(html: str) -> list[EditableBlock]:
    """The whole rendered body as editable regions, with every preheader span carved out.

    Text still travels through ``_replace_visible_text``, so markup, attributes, hrefs and
    plain comments stay untouchable by construction; only the SCOPE widens. Hidden
    preheader spans are excluded because they carry their own ``hidden_preheader`` block
    type: a sweep aimed at body copy must not silently rewrite variant metadata.
    """
    start, end = _document_sweep_span(html)
    blocks: list[EditableBlock] = []
    cursor = start
    for preheader in sorted(
        _find_hidden_preheader_blocks(html), key=lambda block: block.inner_start
    ):
        if preheader.inner_end <= cursor or preheader.inner_start >= end:
            continue
        if preheader.inner_start > cursor:
            blocks.append(
                EditableBlock(
                    block_type="document",
                    inner_start=cursor,
                    inner_end=preheader.inner_start,
                )
            )
        cursor = max(cursor, preheader.inner_end)
    if cursor < end:
        blocks.append(
            EditableBlock(block_type="document", inner_start=cursor, inner_end=end)
        )
    return blocks


def _visible_text_runs(fragment: str, *, base: int = 0, depth: int = 0) -> list[tuple[int, str]]:
    """Absolute-offset text runs that ``_replace_visible_text`` would rewrite.

    Same tokenizer, same skip depth, same descent into conditional comments, so an
    inventory count and the count a sweep enforces cannot disagree.
    """
    runs: list[tuple[int, str]] = []
    cursor = 0
    for match in HTML_TOKEN_RE.finditer(fragment):
        if match.start() > cursor and not depth:
            runs.append((base + cursor, fragment[cursor : match.start()]))
        token = match.group(0)
        if token.startswith("<!--") and _is_conditional_comment(token):
            runs.extend(
                _visible_text_runs(token[4:-3], base=base + match.start() + 4, depth=depth)
            )
        else:
            depth = _non_visible_depth_after(token, depth)
        cursor = match.end()
    if cursor < len(fragment) and not depth:
        runs.append((base + cursor, fragment[cursor:]))
    return runs


def _find_editable_images(html: str) -> list[EditableImage]:
    stack: list[StructuralElement] = []
    images: list[EditableImage] = []

    for match in STRUCTURAL_OR_IMAGE_TAG_RE.finditer(html):
        tag_text = match.group(0)
        tag_name = match.group("name").lower()
        is_close = bool(match.group("close"))
        if tag_name == "img":
            if is_close:
                raise EditError("Reteno HTML is malformed: unexpected </img> tag")
            own_classes = _visibility_classes(tag_text)
            inherited_hidden = stack[-1].hidden_on if stack else frozenset()
            inherited_classes = stack[-1].visibility_classes if stack else ()
            images.append(
                EditableImage(
                    tag_start=match.start(),
                    tag_end=match.end(),
                    effective_visibility=_effective_visibility(
                        inherited_hidden | _hidden_devices(own_classes)
                    ),
                    visibility_classes=tuple(
                        dict.fromkeys((*inherited_classes, *own_classes))
                    ),
                )
            )
            continue
        if not is_close:
            own_classes = _visibility_classes(tag_text)
            inherited_hidden = stack[-1].hidden_on if stack else frozenset()
            inherited_classes = stack[-1].visibility_classes if stack else ()
            stack.append(
                StructuralElement(
                    tag_name=tag_name,
                    inner_start=match.end(),
                    block_type=None,
                    hidden_on=inherited_hidden | _hidden_devices(own_classes),
                    visibility_classes=tuple(
                        dict.fromkeys((*inherited_classes, *own_classes))
                    ),
                )
            )
            continue
        if not stack:
            raise EditError(f"Reteno HTML is malformed: unmatched </{tag_name}> tag")
        element = stack.pop()
        if element.tag_name != tag_name:
            raise EditError(
                "Reteno HTML is malformed: "
                f"expected </{element.tag_name}> before </{tag_name}>"
            )

    if stack:
        raise EditError(f"Reteno HTML is malformed: unmatched <{stack[-1].tag_name}> tag")
    return images


def _is_conditional_comment(token: str) -> bool:
    lowered = token.lower()
    return lowered.startswith("<!--") and "[if " in lowered and lowered.endswith("-->")


def _non_visible_depth_after(tag_text: str, depth: int) -> int:
    match = NON_VISIBLE_TAG_RE.match(tag_text)
    if match is None:
        return depth
    if match.group("close"):
        return max(depth - 1, 0)
    return depth + 1


def _skip_depths_at(html: str, positions: list[int]) -> list[int]:
    """Document-global skip depth at each position, in one pass.

    A block's own fragment starts at depth 0, so a skip element opened OUTSIDE the block
    is invisible to the per-fragment walk: the block's text would be edited even though
    the verifier and every renderer treat it as stylesheet or script content.
    """
    wanted = sorted(set(positions))
    depths: dict[int, int] = {}
    depth = 0
    index = 0
    for match in HTML_TOKEN_RE.finditer(html):
        while index < len(wanted) and wanted[index] <= match.start():
            depths[wanted[index]] = depth
            index += 1
        depth = _non_visible_depth_after(match.group(0), depth)
    while index < len(wanted):
        depths[wanted[index]] = depth
        index += 1
    return [depths[position] for position in positions]


def _replace_visible_text(
    fragment: str, old: str, new: str, *, span: tuple[int, int] | None = None
) -> tuple[str, int]:
    replaced, matches, depth = _replace_text_tokens(fragment, old, new, depth=0)
    if depth:
        where = f" at offsets {span[0]}-{span[1]}" if span else ""
        # A skip tag cannot legally straddle the end of an editable block, so an
        # unbalanced one means the rest of this block was treated as non-visible and
        # silently left untranslated. Refuse instead of shipping a partial edit.
        raise EditError(
            f"Reteno HTML is malformed: editable block{where} leaves "
            f"{NON_VISIBLE_TAG_LIST} markup unbalanced (depth 0 in, {depth} out)"
        )
    return replaced, matches


def _inline_signature(fragment: str) -> tuple[list[str], Counter]:
    """Keep markup bytes and each merge token's original formatting/link context."""
    tags: list[str] = []
    stack: list[tuple[str, int]] = []
    bindings: Counter = Counter()
    for token in HTML_TOKEN_RE.split(fragment):
        if not token:
            continue
        if HTML_TOKEN_RE.fullmatch(token):
            match = re.match(r"(?is)<\s*(/?)\s*([a-z]+)\b", token)
            if match is None or match[2].lower() not in INLINE_TAGS:
                raise EditError("inline replacements allow only balanced inline formatting/link tags")
            name = match[2].lower()
            if match[1]:
                if not stack or stack[-1][0] != name:
                    raise EditError("inline replacement markup is unbalanced")
                stack.pop()
            else:
                if token.rstrip().endswith("/>"):
                    raise EditError("inline replacement markup must use paired tags")
                stack.append((name, len(tags)))
            tags.append(token)
        else:
            if "<" in token or ">" in token:
                raise EditError("inline text must escape literal angle brackets")
            for merge in MERGE_TOKEN_RE.finditer(token):
                if merge[0].startswith("#"):
                    raise EditError("inline replacements cannot move Velocity directives")
                bindings[(merge[0], tuple(stack))] += 1
    if stack:
        raise EditError("inline replacement markup is unbalanced")
    return tags, bindings


def _replace_inline_text(fragment: str, old: str, new: str) -> tuple[str, int]:
    old_tags, old_bindings = _inline_signature(old)
    new_tags, new_bindings = _inline_signature(new)
    if not old_tags or old_tags != new_tags:
        raise EditError("inline replacements must preserve every tag and attribute byte-for-byte in order")
    if old_bindings != new_bindings:
        raise EditError("inline replacements must preserve merge tokens in their original formatting/link context")
    markup = list(HTML_TOKEN_RE.finditer(fragment))
    positions: list[int] = []
    cursor = 0
    while (start := fragment.find(old, cursor)) != -1:
        end = start + len(old)
        # Never match inside an attribute, a comment, or non-visible content.
        overlaps = [m for m in markup if m.start() < end and m.end() > start]
        if not _skip_depths_at(fragment, [start])[0] and all(
            start <= m.start() and m.end() <= end and not m[0].startswith("<!--")
            for m in overlaps
        ):
            positions.append(start)
        cursor = end
    for start in reversed(positions):
        fragment = fragment[:start] + new + fragment[start + len(old):]
    return fragment, len(positions)


def _replace_copy(fragment: str, replacement: ReplacementSpec, *, span: tuple[int, int]) -> tuple[str, int]:
    if replacement.text_mode == "inline":
        _replace_visible_text(fragment, replacement.old, replacement.new, span=span)
        return _replace_inline_text(fragment, replacement.old, replacement.new)
    return _replace_visible_text(
        fragment, replacement.old, html_lib.escape(replacement.new, quote=False), span=span
    )


def _replace_text_tokens(fragment: str, old: str, new: str, *, depth: int) -> tuple[str, int, int]:
    output: list[str] = []
    matches = 0

    for token in HTML_TOKEN_RE.split(fragment):
        if token == "":
            continue
        if HTML_TOKEN_RE.fullmatch(token):
            if token.startswith("<!--") and _is_conditional_comment(token):
                inner = token[4:-3]
                replaced_inner, nested_matches, inner_depth = _replace_text_tokens(
                    inner, old, new, depth=depth
                )
                if inner_depth != depth:
                    raise EditError(
                        "Reteno HTML is malformed: conditional comment leaves "
                        f"{NON_VISIBLE_TAG_LIST} markup unbalanced "
                        f"(depth {depth} in, {inner_depth} out)"
                    )
                matches += nested_matches
                output.append(f"<!--{replaced_inner}-->")
            else:
                output.append(token)
                depth = _non_visible_depth_after(token, depth)
            continue
        if depth:
            output.append(token)
            continue
        matches += token.count(old)
        output.append(token.replace(old, new))

    return "".join(output), matches, depth


def _replace_image_attributes(
    tag_text: str,
    old: str,
    new: str,
) -> tuple[str, int, tuple[str, ...]]:
    output: list[str] = []
    cursor = 0
    matches = 0
    attributes: list[str] = []
    escaped_new = html_lib.escape(new, quote=True)

    for match in IMAGE_ATTRIBUTE_RE.finditer(tag_text):
        if html_lib.unescape(match.group("value")) != old:
            continue
        output.append(tag_text[cursor : match.start("value")])
        output.append(escaped_new)
        cursor = match.end("value")
        matches += 1
        attributes.append(match.group("name").lower())

    if not matches:
        return tag_text, 0, ()
    output.append(tag_text[cursor:])
    return "".join(output), matches, tuple(attributes)


def _target_name(block_type: str) -> str:
    if block_type == "image":
        return "images"
    if block_type == "document":
        return "document sweep regions"
    return f"{block_type} blocks"


def _assert_document_sweep_authorized(
    replacements: list[ReplacementSpec], *, allow_document_sweep: bool
) -> None:
    if allow_document_sweep:
        return
    for index, replacement in enumerate(replacements):
        if replacement.block_type == "document":
            raise EditError(
                f"replacement[{index}] block_type 'document' requires --allow-document-sweep; "
                "a document sweep is authorized only for full translation/localization of a "
                "language variant, never for a bounded copy edit"
            )


def _assert_document_olds_disjoint(replacements: list[ReplacementSpec]) -> None:
    """Reject a document `old` set where one phrase contains another.

    Inside a 200-byte block a collision like ``old:"Order"`` also hitting "Order summary"
    is rare; over a 75KB body it is routine, and whichever phrase runs first silently
    changes the other's occurrence count.
    """
    entries = [
        (index, replacement.old)
        for index, replacement in enumerate(replacements)
        if replacement.block_type == "document"
    ]
    for position, (first_index, first_old) in enumerate(entries):
        for second_index, second_old in entries[position + 1 :]:
            if first_old not in second_old and second_old not in first_old:
                continue
            shorter, longer = (
                (first_index, second_index)
                if len(first_old) <= len(second_old)
                else (second_index, first_index)
            )
            raise EditError(
                f"replacement[{shorter}] old text is contained in replacement[{longer}] "
                "old text; document sweep replacements must not overlap"
            )


def _document_application_order(replacements: list[ReplacementSpec]) -> list[int]:
    """Indices in application order: document replacements longest-``old`` first.

    Only the document entries are permuted, and only among the slots they already occupy,
    so a mixed list still applies its block-scoped entries in the order they were written.
    """
    slots = [
        index
        for index, replacement in enumerate(replacements)
        if replacement.block_type == "document"
    ]
    ranked = sorted(slots, key=lambda index: (-len(replacements[index].old), index))
    order = list(range(len(replacements)))
    for slot, index in zip(slots, ranked):
        order[slot] = index
    return order


def _assert_disjoint_blocks(
    *,
    index: int,
    replacement: ReplacementSpec,
    matching_blocks: list[tuple[EditableBlock, int]],
) -> None:
    """Reject overlapping selections before any splice happens.

    Replacements are spliced in descending ``inner_start`` order so that an earlier
    splice cannot invalidate the offsets of a later one. That only holds for disjoint
    ranges: when one editable block is nested inside another, replacing the inner
    block both shifts the outer block's cached ``inner_end`` and leaves the outer
    replacement re-scanning text the inner replacement already rewrote.
    """
    ordered = sorted(
        matching_blocks,
        key=lambda item: (item[0].inner_start, item[0].inner_end),
    )
    for (outer, _), (inner, _) in zip(ordered, ordered[1:]):
        if inner.inner_start < outer.inner_end:
            raise EditError(
                f"replacement[{index}] selected nested "
                f"{_target_name(replacement.block_type)}: offsets "
                f"{outer.inner_start}-{outer.inner_end} contain "
                f"{inner.inner_start}-{inner.inner_end}; nested editable blocks "
                "cannot be edited safely"
            )


def _selection_details(
    *,
    index: int,
    replacement: ReplacementSpec,
    matching_blocks: list[tuple[EditableBlock | EditableImage, int]],
) -> bool:
    target_name = _target_name(replacement.block_type)
    if replacement.expected_blocks is not None and len(matching_blocks) != replacement.expected_blocks:
        raise EditError(
            f"replacement[{index}] expected {replacement.expected_blocks} matching "
            f"{target_name}, found {len(matching_blocks)}"
        )
    occurrence_name = (
        "alt/title values"
        if replacement.block_type == "image"
        else "visible text occurrences"
    )
    visibilities = frozenset(block.effective_visibility for block, _ in matching_blocks)
    is_responsive_pair = (
        len(matching_blocks) == 2 and visibilities == RESPONSIVE_PAIR_VISIBILITIES
    )
    if replacement.match_mode == "single" and len(matching_blocks) != 1:
        raise EditError(
            f"replacement[{index}] match_mode 'single' found {len(matching_blocks)} "
            f"{target_name}"
        )
    if replacement.match_mode == "responsive_pair" and not is_responsive_pair:
        raise EditError(
            f"replacement[{index}] match_mode 'responsive_pair' requires exactly one desktop-only "
            f"and one mobile-only {target_name}; found {sorted(visibilities)}"
        )
    if replacement.expected_matches is not None:
        total_matches = sum(matches for _, matches in matching_blocks)
        if total_matches != replacement.expected_matches:
            raise EditError(
                f"replacement[{index}] expected {replacement.expected_matches} matching "
                f"{occurrence_name} across {target_name}, found {total_matches}"
            )

    # A document sweep's regions are one region split around the preheader spans, not a
    # partition of rival candidates, so there is nothing to disambiguate between them;
    # expected_matches above is the bound.
    if (
        len(matching_blocks) > 1
        and replacement.block_type != "document"
        and replacement.match_mode not in {"all", "responsive_pair"}
        and not is_responsive_pair
    ):
        visibility_summary = ", ".join(
            block.effective_visibility for block, _ in matching_blocks
        )
        raise EditError(
            f"replacement[{index}] old text is ambiguous across {len(matching_blocks)} "
            f"{target_name} (visibility: {visibility_summary})"
        )
    return is_responsive_pair


def _assert_merge_tokens_unchanged(index: int, before: Counter[str], after: Counter[str]) -> None:
    if before == after:
        return
    added = sorted((after - before).elements())
    removed = sorted((before - after).elements())
    raise EditError(
        f"replacement[{index}] changed Velocity/merge tokens: added {added}, removed {removed}"
    )


def _apply_image_replacement(
    html: str,
    *,
    index: int,
    replacement: ReplacementSpec,
) -> tuple[str, dict[str, Any]]:
    # Image spans come from one finditer pass over non-overlapping <img> tags, so unlike
    # editable blocks they can never nest and need no disjointness check.
    matching_images: list[tuple[EditableImage, int]] = []
    for image in _find_editable_images(html):
        tag_text = html[image.tag_start : image.tag_end]
        _, attribute_matches, _ = _replace_image_attributes(
            tag_text,
            replacement.old,
            replacement.new,
        )
        if attribute_matches:
            matching_images.append((image, attribute_matches))

    if not matching_images:
        if replacement.old in html:
            raise EditError(
                f"replacement[{index}] old text appears only outside exact image alt/title attributes"
            )
        raise EditError(f"replacement[{index}] old text not found")

    is_responsive_pair = _selection_details(
        index=index,
        replacement=replacement,
        matching_blocks=matching_images,
    )
    current_html = html
    changed_images: list[dict[str, Any]] = []
    for image, attribute_matches in sorted(
        matching_images,
        key=lambda item: item[0].tag_start,
        reverse=True,
    ):
        original_tag = current_html[image.tag_start : image.tag_end]
        replaced_tag, _, attributes = _replace_image_attributes(
            original_tag,
            replacement.old,
            replacement.new,
        )
        current_html = (
            current_html[: image.tag_start]
            + replaced_tag
            + current_html[image.tag_end :]
        )
        changed_images.append(
            {
                "effective_visibility": image.effective_visibility,
                "visibility_classes": list(image.visibility_classes),
                "attribute_matches": attribute_matches,
                "attributes": list(attributes),
            }
        )
    changed_images.reverse()
    return current_html, {
        "replacement_index": index,
        "block_type": replacement.block_type,
        "match_mode": replacement.match_mode,
        "expected_matches": replacement.expected_matches,
        "matching_blocks": len(matching_images),
        "responsive_pair": is_responsive_pair,
        "attribute_matches": sum(matches for _, matches in matching_images),
        "blocks": changed_images,
    }


def _apply_replacements(
    html: str,
    replacements: list[ReplacementSpec],
    *,
    allow_document_sweep: bool = False,
) -> tuple[str, list[dict[str, Any]]]:
    _assert_document_sweep_authorized(
        replacements, allow_document_sweep=allow_document_sweep
    )
    _assert_document_olds_disjoint(replacements)
    current_html = html
    applied: list[dict[str, Any]] = []

    for index in _document_application_order(replacements):
        replacement = replacements[index]
        tokens_before = _merge_token_counts(current_html)
        if replacement.block_type == "image":
            current_html, detail = _apply_image_replacement(
                current_html,
                index=index,
                replacement=replacement,
            )
            _assert_merge_tokens_unchanged(index, tokens_before, _merge_token_counts(current_html))
            applied.append(detail)
            continue
        if replacement.block_type == "hidden_preheader":
            blocks = _find_hidden_preheader_blocks(current_html)
        elif replacement.block_type == "document":
            blocks = _find_document_blocks(current_html)
        else:
            blocks = _find_editable_blocks(current_html)
        matching_blocks: list[tuple[EditableBlock, int]] = []

        for block in blocks:
            if block.block_type != replacement.block_type:
                continue
            block_inner = current_html[block.inner_start : block.inner_end]
            _, visible_matches = _replace_copy(
                block_inner,
                replacement,
                span=(block.inner_start, block.inner_end),
            )
            if visible_matches:
                matching_blocks.append((block, visible_matches))

        total_matches = current_html.count(replacement.old)
        if not matching_blocks:
            if total_matches:
                raise EditError(
                    f"replacement[{index}] old text appears only outside allowed "
                    f"{_target_name(replacement.block_type)}, or inside "
                    f"{NON_VISIBLE_TAG_LIST} markup that is not editable visible text"
                )
            raise EditError(f"replacement[{index}] old text not found")

        entry_depths = _skip_depths_at(
            current_html, [block.inner_start for block, _ in matching_blocks]
        )
        for (block, _), entry_depth in zip(matching_blocks, entry_depths):
            if entry_depth:
                raise EditError(
                    f"replacement[{index}] editable block at offsets "
                    f"{block.inner_start}-{block.inner_end} begins inside "
                    f"{NON_VISIBLE_TAG_LIST} markup opened earlier in the document"
                )
        _assert_disjoint_blocks(
            index=index,
            replacement=replacement,
            matching_blocks=matching_blocks,
        )
        is_responsive_pair = _selection_details(
            index=index,
            replacement=replacement,
            matching_blocks=matching_blocks,
        )

        changed_blocks: list[dict[str, Any]] = []
        for block, visible_matches in sorted(
            matching_blocks,
            key=lambda item: item[0].inner_start,
            reverse=True,
        ):
            original_inner = current_html[block.inner_start : block.inner_end]
            replaced_inner, _ = _replace_copy(
                original_inner,
                replacement,
                span=(block.inner_start, block.inner_end),
            )
            current_html = current_html[: block.inner_start] + replaced_inner + current_html[block.inner_end :]
            changed_blocks.append(
                {
                    "effective_visibility": block.effective_visibility,
                    "visibility_classes": list(block.visibility_classes),
                    "visible_matches": visible_matches,
                }
            )
        changed_blocks.reverse()
        _assert_merge_tokens_unchanged(index, tokens_before, _merge_token_counts(current_html))
        applied.append(
            {
                "replacement_index": index,
                "block_type": replacement.block_type,
                "text_mode": replacement.text_mode,
                "match_mode": replacement.match_mode,
                "expected_matches": replacement.expected_matches,
                "matching_blocks": len(matching_blocks),
                "responsive_pair": is_responsive_pair,
                "visible_matches": sum(matches for _, matches in matching_blocks),
                "blocks": changed_blocks,
            }
        )

    applied.sort(key=lambda detail: detail["replacement_index"])
    return current_html, applied


def _excerpt(html: str, start: int, end: int) -> str:
    window_start = max(0, start - INVENTORY_CONTEXT_RADIUS)
    window_end = min(len(html), end + INVENTORY_CONTEXT_RADIUS)
    prefix = "…" if window_start > 0 else ""
    suffix = "…" if window_end < len(html) else ""
    return prefix + WHITESPACE_RUN_RE.sub(" ", html[window_start:window_end]).strip() + suffix


def _covering_block(blocks: list[EditableBlock], start: int, end: int) -> EditableBlock | None:
    for block in blocks:
        if block.inner_start <= start and end <= block.inner_end:
            return block
    return None


def _inventory_payload(html: str, *, replacements: list[ReplacementSpec]) -> dict[str, Any]:
    """Census, uncovered visible text, and per-`old` occurrence contexts.

    Tolerant on purpose: this is the tool you run BEFORE deciding how to edit, so a
    document the write path would refuse still has to produce a readable report.
    """
    census = dict.fromkeys(BLOCK_CENSUS_TYPES, 0)
    census_errors: list[str] = []
    covered_blocks: list[EditableBlock] = []
    for finder in (_find_editable_blocks, _find_hidden_preheader_blocks):
        try:
            covered_blocks.extend(finder(html))
        except EditError as exc:
            census_errors.append(str(exc))
    for block in covered_blocks:
        census[block.block_type] += 1
    try:
        census["image"] = len(_find_editable_images(html))
    except EditError as exc:
        census_errors.append(str(exc))
    try:
        sweep_blocks = _find_document_blocks(html)
    except EditError as exc:
        census_errors.append(str(exc))
        start, end = _document_sweep_span(html)
        sweep_blocks = [EditableBlock(block_type="document", inner_start=start, inner_end=end)]

    sweep_runs = [
        run
        for block in sweep_blocks
        for run in _visible_text_runs(
            html[block.inner_start : block.inner_end], base=block.inner_start
        )
    ]

    uncovered: list[dict[str, Any]] = []
    for start, text in _visible_text_runs(html):
        end = start + len(text)
        stripped = text.strip()
        if not stripped or CONDITIONAL_COMMENT_GUARD_RE.match(stripped):
            continue
        if _covering_block(covered_blocks, start, end) is not None:
            continue
        uncovered.append(
            {
                "offset": start,
                "text": WHITESPACE_RUN_RE.sub(" ", text).strip(),
                "context": _excerpt(html, start, end),
                "in_document_sweep": any(
                    run_start <= start and end <= run_start + len(run_text)
                    for run_start, run_text in sweep_runs
                ),
            }
        )

    checks: list[dict[str, Any]] = []
    for index, replacement in enumerate(replacements):
        sweep_matches = sum(text.count(replacement.old) for _, text in sweep_runs)
        if replacement.text_mode == "inline":
            try:
                sweep_matches = sum(
                    _replace_inline_text(
                        html[block.inner_start:block.inner_end], replacement.old, replacement.new
                    )[1]
                    for block in sweep_blocks
                )
            except EditError as exc:
                census_errors.append(str(exc))
        matches: list[dict[str, Any]] = []
        position = html.find(replacement.old)
        while position != -1:
            end = position + len(replacement.old)
            matches.append(
                {
                    "offset": position,
                    "context": _excerpt(html, position, end),
                    "in_document_sweep": any(
                        run_start <= position and end <= run_start + len(run_text)
                        for run_start, run_text in sweep_runs
                    ),
                }
            )
            position = html.find(replacement.old, end)
        checks.append(
            {
                "replacement_index": index,
                "block_type": replacement.block_type,
                "old": replacement.old,
                "expected_matches": replacement.expected_matches,
                "occurrences": len(matches),
                "document_sweep_matches": sweep_matches,
                "matches": matches[:INVENTORY_MAX_MATCHES],
                "matches_truncated": len(matches) > INVENTORY_MAX_MATCHES,
            }
        )

    return {
        "block_census": census,
        "census_errors": census_errors,
        "document_sweep_regions": [
            {"start": block.inner_start, "end": block.inner_end} for block in sweep_blocks
        ],
        "uncovered_text_run_count": len(uncovered),
        "uncovered_text_runs": uncovered,
        "replacement_checks": checks,
    }


def _write_atomic(path: Path, text: str) -> None:
    """Replace ``path`` via a same-directory temp file so a crash cannot truncate it."""
    handle, temp_name = tempfile.mkstemp(
        dir=path.parent, prefix=f".{path.name}.", suffix=".tmp"
    )
    temp_path = Path(temp_name)
    try:
        with open(handle, "w", encoding="utf-8", newline="") as stream:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        try:
            os.chmod(temp_path, os.stat(path).st_mode & 0o777)
        except OSError:
            pass
        os.replace(temp_path, path)
    except BaseException:
        temp_path.unlink(missing_ok=True)
        raise


def main() -> int:
    args = _parse_args()
    try:
        html_text = args.html.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"error: html file not found: {args.html}", file=sys.stderr)
        return 1
    except UnicodeDecodeError as exc:
        print(f"error: html file is not valid UTF-8: {args.html}: {exc}", file=sys.stderr)
        return 1

    try:
        if args.command == "inventory":
            # Lenient load: inventory is how expected_matches is DISCOVERED, so a draft
            # replacement file that has not filled the counts in yet must still report.
            audited = (
                _load_replacements(args.replacements, require_document_counts=False)
                if args.replacements is not None
                else []
            )
            payload = _inventory_payload(html_text, replacements=audited)
            print(
                json.dumps(
                    {"html": str(args.html), **payload}, ensure_ascii=False, sort_keys=True
                )
            )
            return 0

        replacements = _load_replacements(args.replacements)
        updated_html, applied = _apply_replacements(
            html_text, replacements, allow_document_sweep=args.allow_document_sweep
        )
    except EditError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if updated_html != html_text:
        _write_atomic(args.html, updated_html)

    print(
        json.dumps(
            {
                "html": str(args.html),
                "replacements_applied": len(applied),
                "details": applied,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
