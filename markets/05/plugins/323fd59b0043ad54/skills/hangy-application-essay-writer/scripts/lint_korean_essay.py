#!/usr/bin/env python3
"""Lightweight Korean application-essay linter.

This script reports length, repeated phrasing, long sentences, and common
generic or over-polished phrases. It never rewrites the draft and its warnings
are review prompts rather than automatic rejection rules.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


SUBJECTS = ("저는", "제가", "저의", "제게", "저에게")
CONNECTORS = (
    "또한",
    "이를 통해",
    "이러한 경험을 바탕으로",
    "이 경험을 바탕으로",
    "따라서",
    "그러나",
)
ABSTRACT_WORDS = (
    "따뜻",
    "진심",
    "다정",
    "책임감",
    "사명감",
    "공감",
    "소통",
    "성장",
    "열정",
)
AI_LIKE_PHRASES = (
    "깊이 공감",
    "큰 울림",
    "맞닿아 있",
    "단순히",
    "을 넘어",
    "를 넘어",
    "뜻깊은 활동",
    "선도적인",
    "한 단계 성장",
    "역량을 키웠",
    "기여하고자",
    "기여하겠습니다",
)
VAGUE_ABSOLUTES = (
    "누구보다",
    "항상",
    "반드시",
    "최고의",
    "완벽한",
    "믿어 의심치",
    "최선을 다하겠습니다",
    "열심히 하겠습니다",
)
HEDGES = (
    "것 같습니다",
    "일지도 모릅니다",
    "생각됩니다",
    "느껴집니다",
    "하는 편이 좋",
)
CONTRAST_PHRASES = (
    "에서 그치지 않고",
    "에 그치지 않고",
    "멈추지 않고",
    "것이 아니라",
    "것보다",
)
COMMON_ENDINGS = (
    "했습니다.",
    "하겠습니다.",
    "생각합니다.",
    "배웠습니다.",
    "되었습니다.",
    "느꼈습니다.",
)


def read_file(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "cp949"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("essay", data, 0, len(data), "UTF-8 또는 CP949로 읽을 수 없습니다")


def split_sentences(text: str) -> list[str]:
    normalized = re.sub(r"[ \t]+", " ", text.strip())
    parts = re.split(r"(?<=[.!?])\s+|\n+", normalized)
    return [part.strip() for part in parts if part.strip()]


def count_terms(text: str, terms: tuple[str, ...]) -> dict[str, int]:
    return {term: text.count(term) for term in terms if text.count(term)}


def add_issue(issues: list[dict[str, Any]], severity: str, code: str, message: str) -> None:
    issues.append({"severity": severity, "code": code, "message": message})


def lint(text: str, min_chars: int | None, max_chars: int | None, count_mode: str) -> dict[str, Any]:
    stripped = text.strip()
    chars_with_spaces = len(stripped)
    chars_without_spaces = len(re.sub(r"\s", "", stripped))
    counted_chars = chars_with_spaces if count_mode == "spaces" else chars_without_spaces
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n+", stripped) if p.strip()]
    sentences = split_sentences(stripped)
    sentence_lengths = [len(sentence) for sentence in sentences]
    issues: list[dict[str, Any]] = []

    if "\ufffd" in stripped:
        add_issue(issues, "error", "replacement-character", "한글 대체문자(�)가 있습니다. 인코딩이나 복사 오류를 확인하세요.")
    if min_chars is not None and counted_chars < min_chars:
        add_issue(issues, "error", "below-minimum", f"기준 글자 수가 {counted_chars}자로 최소 {min_chars}자보다 짧습니다.")
    if max_chars is not None and counted_chars > max_chars:
        add_issue(issues, "error", "above-maximum", f"기준 글자 수가 {counted_chars}자로 최대 {max_chars}자를 초과합니다.")

    subject_counts = count_terms(stripped, SUBJECTS)
    subject_total = sum(subject_counts.values())
    if subject_total >= 4 and subject_total > max(3, len(sentences) * 0.35):
        add_issue(
            issues,
            "warning",
            "subject-repetition",
            f"1인칭 주어가 {subject_total}회 반복됩니다: {subject_counts}. 문맥상 분명한 주어는 덜어 내세요.",
        )

    connector_counts = count_terms(stripped, CONNECTORS)
    repeated_connectors = {term: count for term, count in connector_counts.items() if count >= 2}
    if sum(connector_counts.values()) >= 4 or repeated_connectors:
        add_issue(
            issues,
            "warning",
            "connector-repetition",
            f"연결 표현이 반복됩니다: {connector_counts}. 문단 기능과 행동 동사로 흐름을 만드세요.",
        )

    abstract_counts = count_terms(stripped, ABSTRACT_WORDS)
    repeated_abstracts = {term: count for term, count in abstract_counts.items() if count >= 3}
    if sum(abstract_counts.values()) >= 6 or repeated_abstracts:
        add_issue(
            issues,
            "warning",
            "abstract-word-density",
            f"추상 가치어가 많습니다: {abstract_counts}. 각 가치어를 실제 행동과 외부 근거로 바꾸세요.",
        )

    ai_like_counts = count_terms(stripped, AI_LIKE_PHRASES)
    if ai_like_counts:
        add_issue(
            issues,
            "warning",
            "generic-polish",
            f"상투적이거나 지나치게 매끈한 표현이 있습니다: {ai_like_counts}. 기관 사실과 개인 행동으로 다시 쓰세요.",
        )

    absolute_counts = count_terms(stripped, VAGUE_ABSOLUTES)
    if absolute_counts:
        add_issue(
            issues,
            "warning",
            "vague-absolute",
            f"입증하기 어려운 절대·다짐 표현이 있습니다: {absolute_counts}. 범위를 낮추거나 근거를 붙이세요.",
        )

    hedge_counts = count_terms(stripped, HEDGES)
    if hedge_counts:
        add_issue(
            issues,
            "info",
            "hedging",
            f"추측·회피형 표현을 확인하세요: {hedge_counts}. 근거가 있으면 정확히 쓰고, 없으면 범위를 낮추세요.",
        )

    contrast_counts = count_terms(stripped, CONTRAST_PHRASES)
    only_frame_count = len(re.findall(r"(?:으)?로만 여기지 않", stripped))
    if only_frame_count:
        contrast_counts["(으)로만 여기지 않"] = only_frame_count
    than_count = stripped.count("보다")
    if than_count >= 3 or sum(contrast_counts.values()) >= 2:
        add_issue(
            issues,
            "warning",
            "template-contrast-density",
            f"대비형 전개가 반복됩니다: '보다' {than_count}회, 세부 표현 {contrast_counts}. "
            "핵심 대비 한 번만 남기고 고유한 장면과 행동으로 바꾸세요.",
        )

    long_sentences = [
        {"index": index + 1, "characters": len(sentence), "preview": sentence[:90]}
        for index, sentence in enumerate(sentences)
        if len(sentence) > 110
    ]
    if long_sentences:
        add_issue(
            issues,
            "warning",
            "long-sentence",
            f"110자를 넘는 문장이 {len(long_sentences)}개 있습니다. 주장과 근거를 나누어 보세요.",
        )

    long_paragraphs = [
        {"index": index + 1, "characters": len(paragraph)}
        for index, paragraph in enumerate(paragraphs)
        if len(paragraph) > 650
    ]
    if long_paragraphs:
        add_issue(
            issues,
            "warning",
            "long-paragraph",
            f"650자를 넘는 문단이 있습니다: {long_paragraphs}. 한 문단에 한 선발 이유만 남기세요.",
        )

    ending_counts = {ending: stripped.count(ending) for ending in COMMON_ENDINGS if stripped.count(ending)}
    repeated_endings = {ending: count for ending, count in ending_counts.items() if count >= 4}
    if repeated_endings:
        add_issue(
            issues,
            "info",
            "ending-repetition",
            f"같은 종결 표현이 연속될 가능성이 있습니다: {repeated_endings}. 낭독하며 문장 리듬을 확인하세요.",
        )

    # Put longer units first so that values such as "6개월" are not
    # truncated to "6개".  These are only fact-check prompts; the linter
    # does not treat a detected number as verified evidence.
    number_units = (
        "퍼센트|개월|학년|학기|시간|만원|천원|백만원|"
        "%|명|회|건|개|년|월|주|일|시|분|초|원|점|등|위|쪽|장|곳"
    )
    numbers = re.findall(
        rf"(?<![A-Za-z가-힣])\d+(?:[.,]\d+)?(?:{number_units})?",
        stripped,
    )
    return {
        "stats": {
            "characters_with_spaces": chars_with_spaces,
            "characters_without_spaces": chars_without_spaces,
            "count_mode": count_mode,
            "counted_characters": counted_chars,
            "paragraphs": len(paragraphs),
            "sentences": len(sentences),
            "average_sentence_characters": round(sum(sentence_lengths) / len(sentence_lengths), 1) if sentence_lengths else 0,
            "longest_sentence_characters": max(sentence_lengths, default=0),
            "numbers_found": numbers,
        },
        "counts": {
            "subjects": subject_counts,
            "connectors": connector_counts,
            "abstract_words": abstract_counts,
            "generic_polish": ai_like_counts,
            "vague_absolutes": absolute_counts,
            "hedges": hedge_counts,
            "contrast_phrases": contrast_counts,
            "than_count": than_count,
            "sentence_endings": ending_counts,
        },
        "details": {
            "long_sentences": long_sentences,
            "long_paragraphs": long_paragraphs,
        },
        "issues": issues,
    }


def print_human(result: dict[str, Any]) -> None:
    stats = result["stats"]
    print("자소서 문장 점검")
    print(f"- 공백 포함: {stats['characters_with_spaces']}자")
    print(f"- 공백 제외: {stats['characters_without_spaces']}자")
    print(f"- 문단/문장: {stats['paragraphs']}개 / {stats['sentences']}개")
    print(f"- 평균/최장 문장: {stats['average_sentence_characters']}자 / {stats['longest_sentence_characters']}자")
    if stats["numbers_found"]:
        print(f"- 발견한 수치: {', '.join(stats['numbers_found'])}")
    if not result["issues"]:
        print("- 자동 점검에서 특이사항을 찾지 못했습니다. 사실·기관 적합성·면접 방어 가능성은 별도로 검토하세요.")
        return
    print("\n검토할 항목")
    for issue in result["issues"]:
        print(f"- [{issue['severity'].upper()}] {issue['message']}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="한국어 자소서의 길이와 반복·상투 표현을 점검합니다.")
    parser.add_argument("file", nargs="?", help="UTF-8 또는 CP949 텍스트 파일")
    parser.add_argument("--text", help="명령행에서 직접 전달할 본문")
    parser.add_argument("--stdin", action="store_true", help="표준 입력에서 UTF-8 본문 읽기")
    parser.add_argument("--min-chars", type=int, help="최소 글자 수")
    parser.add_argument("--max-chars", type=int, help="최대 글자 수")
    parser.add_argument("--count-mode", choices=("spaces", "no-spaces"), default="spaces", help="제한 계산 방식")
    parser.add_argument("--json", action="store_true", help="JSON으로 출력")
    args = parser.parse_args()
    selected = sum(bool(value) for value in (args.file, args.text, args.stdin))
    if selected != 1:
        parser.error("file, --text, --stdin 중 하나만 지정하세요.")
    if args.min_chars is not None and args.max_chars is not None and args.min_chars > args.max_chars:
        parser.error("--min-chars는 --max-chars보다 클 수 없습니다.")
    return args


def main() -> int:
    args = parse_args()
    try:
        if args.file:
            text = read_file(Path(args.file))
        elif args.text is not None:
            text = args.text
        else:
            if hasattr(sys.stdin, "reconfigure"):
                sys.stdin.reconfigure(encoding="utf-8")
            text = sys.stdin.read()
    except (OSError, UnicodeError) as exc:
        print(f"입력 오류: {exc}", file=sys.stderr)
        return 2

    result = lint(text, args.min_chars, args.max_chars, args.count_mode)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_human(result)
    return 1 if any(issue["severity"] == "error" for issue in result["issues"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
