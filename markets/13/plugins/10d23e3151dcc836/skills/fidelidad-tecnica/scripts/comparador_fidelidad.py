#!/usr/bin/env python3
"""Comparador local de fidelidad prompt/informe. Python 3.10+, solo biblioteca estándar.

No calcula cartas, no usa red ni importa código de Astroanamnesis. Los valores
del prompt son declaraciones literales, incluso cuando parecen inusuales.
Los resultados no certifican cobertura completa del lenguaje natural.
"""
from __future__ import annotations

import argparse
import bisect
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

VERSION = "1.0.0"
SCHEMA = "astroanamnesis.prompt-report-fidelity/1"
MAX_BYTES = 1_000_000
MAX_JSON_BYTES = 32_000_000
MAPS = ("tropical", "memoria", "sideral")
BODIES = {
    "sol": "Sun", "luna": "Moon", "mercurio": "Mercury", "venus": "Venus",
    "marte": "Mars", "jupiter": "Jupiter", "saturno": "Saturn", "urano": "Uranus",
    "neptuno": "Neptune", "pluton": "Pluto", "tierra": "tierra",
    "nodo norte": "true Node", "nodo sur": "south Node", "lilith": "Lilith",
    "quiron": "Chiron", "ceres": "Ceres", "palas": "Pallas", "juno": "Juno",
    "vesta": "Vesta", "chariklo": "Chariklo", "eros": "Eros", "eris": "Eris",
    "icaro": "Icarus", "nessus": "Nessus", "pholus": "Pholus", "psique": "Psyche",
    "punto medio sol-luna": "midpoint", "parte de la fortuna": "Part of Fortune",
    "parte del infortunio": "Part of Misfortune", "ascendente": "Ascendant",
    "descendente": "Descendant", "medio cielo": "Midheaven",
    "fondo del cielo": "ImumCoeli", "vertex": "Vertex",
}
SIGNS = "aries tauro geminis cancer leo virgo libra escorpio sagitario capricornio acuario piscis".split()
ASPECTS = "conjuncion semisextil semicuadratura sextil quintil cuadratura trigono sesquicuadratura biquintil quincuncio oposicion".split()
WORDS = {}
for _name in ASPECTS:
    WORDS[_name] = _name
    WORDS[_name[:-3] + "ciones" if _name.endswith("cion") else _name + ("es" if _name.endswith("il") else "s")] = _name


def alternatives(values):
    return "|".join(re.escape(x) for x in sorted(values, key=len, reverse=True))


P, A, S = alternatives(BODIES), alternatives(WORDS), alternatives(SIGNS)
ART = r"(?:(?:el|la|los|las)\s+)?"
MAP = r"(?:\s+(?:sideral|sidereo|tropical|de\s+(?:la\s+)?memoria(?:\s+inconsciente)?))?"
H = r"(?:xii|xi|ix|viii|vii|vi|iv|iii|ii|x|v|i|\d+)"
NUM = r"\d+(?:[.,]\d+)?"
ROMAN = dict(zip("i ii iii iv v vi vii viii ix x xi xii".split(), map(str, range(1, 13))))
TECHNICAL = rf"\b(?:{A}|{S}|decanatos?|dodecatemorias?|regentes?|regencias?|grados?|minutos?|segundos?|casas?|cuspides?|orbes?|retrograd\w*|domicilio|exaltacion|detrimento|caida|dispositor\w*)\b|[º°]"


def digest(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode("utf-8")).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def revision():
    return digest(Path(__file__).read_bytes())


def check_text(text, label):
    if not isinstance(text, str) or not text.strip() or "\0" in text:
        raise ValueError(f"{label}: falta un texto no vacío y sin caracteres NUL.")
    if len(text.encode("utf-8")) > MAX_BYTES:
        raise ValueError(f"{label}: supera {MAX_BYTES} bytes UTF-8; no fracciones el informe para simular cobertura total.")


def normalize(text):
    value = "".join(c for c in unicodedata.normalize("NFD", text) if not unicodedata.category(c).startswith("M"))
    return value.lower().translate(str.maketrans({"–": "-", "—": "-", "−": "-", "\xa0": " ", "\ufeff": " "}))


def mapped(original):
    value, offsets = [], []
    for i, char in enumerate(original):
        replacement = " " if char in "*_`" else normalize(char)
        value.append(replacement)
        offsets.extend([i] * len(replacement))
    offsets.append(len(original))
    return "".join(value), offsets


def number(text):
    if not re.fullmatch(NUM, text):
        return None
    whole, _, fraction = text.replace(",", ".").partition(".")
    whole, fraction = whole.lstrip("0") or "0", fraction.rstrip("0")
    return whole + ("." + fraction if fraction else "")


def house(text):
    return ROMAN.get(text, number(text))


def markers(text):
    return set("sideral" if x == "sidereo" else x for x in re.findall(r"\b(tropical|memoria|sideral|sidereo)\b", text))


def unique(items):
    return list({canonical(item): item for item in items}.values())


def assertions(text):
    found = []

    def save(p, q, word, start, end):
        found.append(dict(a=BODIES[p], b=BODIES[q], name=WORDS[word], start=start, end=end))

    patterns = [
        (rf"\b({P}){MAP}\s+(?:en\s+|(?:forma|hace|presenta|mantiene|tiene)\s+(?:(?:un|una|unos|unas)\s+)?)?({A})\s+(?:(?:a|con|de|del)\s+)?{ART}({P})\b", (1, 3, 2)),
        (rf"\b({P}){MAP}\s+(?:esta|estan|se\s+encuentra|se\s+encuentran)\s+en\s+(?:(?:un|una|unos|unas)\s+)?({A})\s+(?:con|a)\s+{ART}({P})\b", (1, 3, 2)),
        (rf"\b({P})\s+(?:y|con)\s+{ART}({P})\s+(?:forman|tienen|mantienen)\s+(?:(?:un|una|unos|unas)\s+)?({A})\b", (1, 2, 3)),
    ]
    for pattern, (p, q, word) in patterns:
        for m in re.finditer(pattern, text):
            save(m[p], m[q], m[word], m.start(), m.end())
    for m in re.finditer(rf"\b({A}){MAP}\s+(?:(?:de|del|entre)\s+)?{ART}({P})\s*(?:-|/|y|con|a)\s*{ART}({P})\b", text):
        if any(a["start"] < m.start() < a["end"] for a in found):
            continue
        if re.match(rf"\s+con\s+{ART}(?:{P})\b", text[m.end():]):
            continue
        save(m[2], m[3], m[1], m.start(), m.end())
    for m in re.finditer(rf"\b({A})\s+de\s+{ART}({P})\s+y\s+{ART}({P})\s+con\s+{ART}({P})\b", text):
        for p in (m[2], m[3]):
            save(p, m[4], m[1], m.start(), m.end())
    groups = [
        (rf"\b({A}){MAP}\s+(?:de|del)\s+{ART}({P}){MAP}\s+(?:con|a)\s+", (2, 1)),
        (rf"\b({P}){MAP}\s+(?:forma|hace|presenta|mantiene|tiene|esta\s+en)\s+(?:(?:un|una|unos|unas)\s+)?({A})\s+(?:con|a)\s+", (1, 2)),
        (rf"\b({P}){MAP}\s+(?:en\s+)?({A})\s+(?:(?:con|a)\s+)?", (1, 2)),
    ]
    for pattern, (subject, aspect) in groups:
        for m in re.finditer(pattern, text):
            rest, used, items = text[m.end():], 0, []
            while rest:
                item = re.match(rf"{ART}({P})\b", rest)
                if not item:
                    break
                if items and re.match(rf"\s+(?:{A}|forma|hace|presenta|mantiene|tiene|esta|en)\b", rest[item.end():]):
                    break
                items.append(item[1])
                used += item.end()
                rest = rest[item.end():]
                separator = re.match(r"\s*(?:,\s*(?:y\s+)?|y\s+)(?:con\s+)?", rest)
                if not separator:
                    break
                used += separator.end()
                rest = rest[separator.end():]
            for body in items:
                save(m[subject], body, m[aspect], m.start(), m.end() + used)
    # Prefer the complete enumeration span over an overlapping short match.
    return list({(a["a"], a["b"], a["name"], a["start"]): a for a in found}.values())


def claims_in_sentence(text):
    claims, pending, covered = [], [], []

    def add(kind, subject, field, value, start, end):
        claims.append(dict(kind=kind, subject=subject, field=field, value=value, start=start, end=end))
        covered.append((start, end))

    for c in assertions(text):
        subject = "|".join(sorted((c["a"], c["b"])))
        add("aspect", subject, "aspect", c["name"], c["start"], c["end"])
        detail = re.match(rf"\s*\(\s*({NUM})\s*[º°](?:\s*,\s*orbe\s*({NUM})\s*[º°])?\s*\)", text[c["end"]:])
        if detail:
            add("aspect", subject, "angle", number(detail[1]), c["end"], c["end"] + detail.end())
            if detail[2] is not None:
                add("aspect", subject, "orb", number(detail[2]), c["end"], c["end"] + detail.end())
    anchor = rf"\b({P}){MAP}\s*(?:\([^)]*\)\s*)?(?::\s*)?(?:(?:y\s+)?(?:esta|se encuentra|se situa|situado|ubicado)\s+)?(?:(?:en\s+(?:(?:el\s+)?signo\s+(?:de\s+)?)?({S})\b)|(?=(?:tiene\s+|con\s+|en\s+)?(?:decanato|dodecatemoria|(?:la\s+)?casa|grado)\b))"
    cusp = rf"\b(?:cuspide\s+(?:de\s+)?(?:la\s+)?casa|casa)\s+({H})\s*(?:\([^)]*\)\s*)?(?:(?:se encuentra|esta)\s+)?en\s+({S})\b"
    subjects = [(m, BODIES[m[1]], m[2]) for m in re.finditer(anchor, text)]
    subjects += [(m, "cusp:" + house(m[1]), m[2]) for m in re.finditer(cusp, text)]
    subjects.sort(key=lambda item: item[0].start())
    attrs = [
        ("decanate", rf"\bdecanato\s+(?:de\s+|en\s+)?({S})\b", str),
        ("dodecatemoria", rf"\bdodecatemoria\s+(?:de\s+|en\s+)?({S})\b", str),
        ("house", rf"\b(?:en\s+)?(?:la\s+)?casa\s+({H})\b", house),
        ("degree", rf"\bgrados?\s+({NUM})\s*[º°]?", number),
        ("minute", rf"\bminutos?\s+({NUM})", number),
        ("second", rf"\bsegundos?\s+({NUM})", number),
    ]
    for i, (m, subject, sign) in enumerate(subjects):
        end = subjects[i + 1][0].start() if i + 1 < len(subjects) else len(text)
        if sign:
            add("position", subject, "sign", sign, m.start(), m.end())
        tail = text[m.end():end]
        dms = re.match(rf"\s*(?:a\s+)?({NUM})\s*[º°](?:\s*({NUM})\s*['′])?(?:\s*({NUM})\s*[\"″])?", tail)
        if dms:
            for j, field in enumerate(("degree", "minute", "second"), 1):
                if dms[j] is not None:
                    add("position", subject, field, number(dms[j]), m.start(), m.end() + dms.end())
        consumed = dms.end() if dms else 0
        while consumed < len(tail):
            for field, pattern, convert in attrs:
                a = re.match(rf"\s*(?:,\s*|y\s+)?{pattern}", tail[consumed:])
                if a:
                    consumed += a.end()
                    add("position", subject, field, convert(a[1]), m.start(), m.end() + consumed)
                    break
            else:
                break
    reverse = rf"\b(decanato|dodecatemoria|grado|minuto|segundo|casa)\s+(?:de\s+|del\s+){ART}({P}){MAP}\s+(?:es|esta en)\s+({S}|{NUM}|{H})\b"
    fields = dict(decanato="decanate", dodecatemoria="dodecatemoria", grado="degree", minuto="minute", segundo="second", casa="house")
    for m in re.finditer(reverse, text):
        field = fields[m[1]]
        value = (m[3] if m[3] in SIGNS else None) if field in ("decanate", "dodecatemoria") else house(m[3]) if field == "house" else number(m[3])
        if value is not None:
            add("position", BODIES[m[2]], field, value, m.start(), m.end())
    ruler = rf"\b(?:planeta\s+)?regente\s+(?:(?:del|de)\s+)?(?:(?:el\s+)?signo\s+)?(solar|lunar|{S})\s+(?:es|:)\s+{ART}({P})\b"
    for m in re.finditer(ruler, text):
        add("rulership", m[1], "ruler", BODIES[m[2]], m.start(), m.end())
    for m in re.finditer(rf"\b({P})\s+es\s+(?:el\s+)?regente\s+(?:de|del)\s+(?:signo\s+)?({S})\b", text):
        add("rulership", m[2], "ruler", BODIES[m[1]], m.start(), m.end())
    for m in re.finditer(rf"\bregente\s+de\s+la\s+casa\s+({H})\s+(?:es|:)\s+{ART}({P})\b", text):
        add("rulership", "cusp:" + house(m[1]), "ruler", BODIES[m[2]], m.start(), m.end())
    for m in re.finditer(rf"\b({P})\s+no\s+tiene\s+aspectos\b", text):
        add("absence", BODIES[m[1]], "aspects", "none", m.start(), m.end())
    # Parenthetical content must not disappear inside a positional anchor.
    # The DMS/aspect-detail grammar above consumes only the explicit numerical form.
    for m in re.finditer(r"\([^)]*\)", text):
        numeric_detail = re.fullmatch(rf"\(\s*{NUM}\s*[º°](?:\s*,\s*orbe\s*{NUM}\s*[º°])?\s*\)", m[0])
        chart_label = re.fullmatch(r"\(\s*(?:sideral|tropical|memoria(?: inconsciente)?)\s*\)", m[0])
        native_label = re.fullmatch(r"\(\s*(?:la casa del sol|cuspide casa 1)\s*\)", m[0])
        if re.search(TECHNICAL, m[0]) and not (numeric_detail or chart_label or native_label):
            pending.append(dict(code="UNPARSED_PARENTHETICAL", start=m.start(), end=m.end()))
    modality = re.search(r"\b(no|ni|quiza|quizas|podria|si|supongamos|en vez de|en lugar de)\b", text)
    absence_only = re.fullmatch(rf"\s*(?:los aspectos .+? son:\s*)?(?:{P}) no tiene aspectos(?:\s*\(sideral\))?\s*", text)
    if modality and not absence_only and claims:
        pending.append(dict(code="AMBIGUOUS_POLARITY", start=modality.start(), end=modality.end()))
    for token in re.finditer(TECHNICAL, text):
        if not any(start <= token.start() and end >= token.end() for start, end in covered):
            pending.append(dict(code="UNPARSED_TECHNICAL_EXPRESSION", start=token.start(), end=token.end()))
    label = re.match(r"\s*los aspectos .+? son:\s*", text)
    for body in re.finditer(rf"\b(?:{P})\b", text):
        if body.start() >= (label.end() if label else 0) and not any(start <= body.start() < end for start, end in covered):
            pending.append(dict(code="UNRESOLVED_SUBJECT", start=body.start(), end=body.end()))
    return claims, pending


def scan_document(original):
    text, offsets = mapped(original)
    claims, pending = [], []
    context, buffer_start, buffer_end, line_start = None, None, 0, 0
    byte_offsets = [0]
    line_breaks = [i for i, char in enumerate(original) if char == "\n"]
    for char in original:
        byte_offsets.append(byte_offsets[-1] + len(char.encode("utf-8")))

    def locate(start, end):
        a, b = offsets[start], offsets[end]
        return dict(start=a, end=b, byteStart=byte_offsets[a], byteEnd=byte_offsets[b],
                    line=bisect.bisect_left(line_breaks, a) + 1, quote=original[a:b])

    def flush():
        nonlocal buffer_start
        if buffer_start is None:
            return
        chunk, cursor = text[buffer_start:buffer_end], 0
        boundaries = [(m.start(), m.end()) for m in re.finditer(r"[;!?]|(?<!\d)\.|\.(?!\d)", chunk)]
        for end, next_cursor in boundaries + [(len(chunk), len(chunk))]:
            sentence, base = chunk[cursor:end], buffer_start + cursor
            found = markers(re.sub(r"\bmemoria\b(?!\s+inconsciente)", "recuerdo", sentence))
            literal = original[offsets[base]:offsets[base + len(sentence)]]
            if re.search(r"\b(?:Memoria|MEMORIA)\b", literal) or re.search(r"\b(?:carta|mapa)\s+(?:de\s+(?:la\s+)?)?memoria\b", sentence):
                found.add("memoria")
            chart = next(iter(found)) if len(found) == 1 else None if found else context
            extracted, unresolved = claims_in_sentence(sentence)
            uncertain = any(p["code"] == "AMBIGUOUS_POLARITY" for p in unresolved)
            for c in extracted:
                ref = locate(base + c["start"], base + c["end"])
                if not chart or uncertain:
                    pending.append(dict(code="AMBIGUOUS_POLARITY" if chart else "AMBIGUOUS_MAP", map=chart, reference=ref))
                else:
                    claims.append(dict(map=chart, **{k: c[k] for k in ("kind", "subject", "field", "value")}, reference=ref))
            for p in unresolved:
                pending.append(dict(code=p["code"], map=chart,
                                    reference=locate(base + p["start"], base + p["end"]),
                                    context=locate(base + max(0, p["start"] - 100),
                                                   base + min(len(sentence), p["end"] + 140))))
            cursor = next_cursor
        buffer_start = None

    for line in text.split("\n"):
        names = markers(line)
        markdown = re.match(r"\s*#{1,6}\s", line)
        heading = re.fullmatch(r"\s*(?:[abc][).]\s*)?(?:carta\s+(?:de\s+)?)?(?:tropical|memoria(?: inconsciente)?|sideral)\s*:?\s*", line)
        native = re.match(r"\s*(?:planetas y (?:sus )?aspectos|comparativa de)\b", line)
        if markdown or heading or native:
            flush()
            if names:
                context = next(iter(names)) if len(names) == 1 else None
            elif markdown and not re.match(r"\s*#{3,6}\s", line):
                context = None
            if markdown and not heading and re.search(TECHNICAL, line):
                buffer_start, buffer_end = line_start, line_start + len(line)
                flush()
        elif not line.strip():
            flush()
        else:
            if buffer_start is None:
                buffer_start = line_start
            buffer_end = line_start + len(line)
        line_start += len(line) + 1
    flush()
    return unique(claims), unique(pending)


def fact_key(fact):
    return tuple(fact[k] for k in ("map", "kind", "subject", "field"))


def prepare_source(prompt):
    """Extrae un registro comprobable; nunca modifica el texto recibido."""
    check_text(prompt, "Prompt")
    claims, pending = scan_document(prompt)
    charts, indexed, by_field = {m: {"facts": []} for m in MAPS}, {}, {}
    for claim in claims:
        key = fact_key(claim) + (claim["value"],)
        if key not in indexed:
            indexed[key] = {k: claim[k] for k in ("map", "kind", "subject", "field", "value")}
            indexed[key]["references"] = []
            charts[claim["map"]]["facts"].append(indexed[key])
            by_field.setdefault(fact_key(claim), []).append(indexed[key])
        indexed[key]["references"].append(claim["reference"])
    for facts in by_field.values():
        if len(facts) > 1:
            pending.append(dict(code="AMBIGUOUS_SOURCE_FACT", map=facts[0]["map"], subject=facts[0]["subject"],
                                field=facts[0]["field"], values=[f["value"] for f in facts],
                                references=[r for f in facts for r in f["references"]]))
    record = dict(schema=SCHEMA, comparatorVersion=VERSION, comparatorSha256=revision(),
                  promptSha256=digest(prompt), charts=charts, pending=pending)
    counts = {m: len(charts[m]["facts"]) for m in MAPS}
    return dict(status="blocked" if not sum(counts.values()) else "requires_manual_review" if pending else "ready",
                sourceSha256=digest(canonical(record)), factsByChart=counts, record=record,
                notice="Referencia literal; no se comprueba astronomía ni coherencia entre cartas.")


def compare(prompt, report):
    """Compara exclusivamente las afirmaciones reconocidas; no autoriza entregar."""
    check_text(report, "Informe")
    source = prepare_source(prompt)
    record = source["record"]
    index = {}
    for chart in record["charts"].values():
        for fact in chart["facts"]:
            index.setdefault(fact_key(fact), []).append(fact)
    claims, pending = scan_document(report)
    issues = [dict(p, severity="pending") for p in pending]
    matched = []
    for claim in claims:
        facts = index.get(fact_key(claim), [])
        values = list(dict.fromkeys(f["value"] for f in facts))
        detail = {k: claim[k] for k in ("map", "kind", "subject", "field", "reference")}
        detail["actual"] = claim["value"]
        inventory = record["charts"][claim["map"]]["facts"]
        contrary = []
        if claim["kind"] == "aspect" and claim["field"] == "aspect":
            contrary = [f for f in inventory if f["kind"] == "absence" and f["subject"] in claim["subject"].split("|")]
        elif claim["kind"] == "absence":
            contrary = [f for f in inventory if f["kind"] == "aspect" and f["field"] == "aspect" and claim["subject"] in f["subject"].split("|")]
        if contrary:
            issues.append(dict(detail, code="AMBIGUOUS_SOURCE_FACT" if values else "CONTRADICTS_DECLARED_INVENTORY",
                               severity="pending" if values else "error", sourceReferences=[r for f in contrary for r in f["references"]]))
        elif not values:
            issues.append(dict(detail, code="FACT_NOT_PROVIDED", severity="pending"))
        elif len(values) > 1:
            issues.append(dict(detail, code="AMBIGUOUS_SOURCE_FACT", severity="pending", expected=values,
                               sourceReferences=[r for f in facts for r in f["references"]]))
        elif values[0] != claim["value"]:
            issues.append(dict(detail, code="INCORRECT_ASPECT" if claim["field"] == "aspect" else "FACT_MISMATCH",
                               severity="error", expected=values[0], sourceReferences=[r for f in facts for r in f["references"]]))
        else:
            matched.append(detail)
    errors = sum(i["severity"] == "error" for i in issues)
    needs_review = bool(pending or record["pending"] or len(matched) != len(claims) or not claims)
    result = dict(schema=SCHEMA, comparatorVersion=VERSION, comparatorSha256=revision(),
                  status="blocked" if errors or source["status"] == "blocked" else "requires_manual_review",
                  fidelityStatus="mismatch" if errors else "pending" if needs_review else "matched_supported_claims",
                  deliveryAllowed=False, promptSha256=record["promptSha256"], sourceSha256=source["sourceSha256"],
                  reportSha256=digest(report), checkedClaims=len(claims), matchedClaims=len(matched), issues=issues,
                  sourcePending=record["pending"], sourceStatus=source["status"],
                  coverage=dict(recognizedClaims=matched, manualReviewRequired=True,
                                reason="Gramática limitada: las elipsis, metáforas, comparaciones y expresiones no reconocidas requieren revisión humana."))
    result["auditSha256"] = digest(canonical(result))
    return result


def check_receipt(prompt, report, receipt):
    """Vigencia local del contenido exacto y del programa; no es firma ni permiso."""
    fresh = compare(prompt, report)
    if fresh != receipt:
        raise ValueError("AUDIT_STALE: cambió el prompt, el informe, el comparador o el recibo. Ejecuta auditar de nuevo.")
    return dict(current=True, deliveryAllowed=False, fidelityStatus=fresh["fidelityStatus"],
                promptSha256=fresh["promptSha256"], reportSha256=fresh["reportSha256"], auditSha256=fresh["auditSha256"])


def read_text(path, limit=MAX_BYTES):
    # read_bytes avoids Python's universal-newline conversion (CRLF must survive).
    with Path(path).open("rb") as stream:
        data = stream.read(limit + 1)
    if len(data) > limit:
        raise ValueError(f"El archivo supera {limit} bytes.")
    return data.decode("utf-8", errors="strict")


def write_json(path, value):
    # Never overwrite input, previous audit, hard link or symlink target.
    with Path(path).open("xb") as stream:
        stream.write((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def exit_for(result):
    if result.get("status") == "blocked":
        return 2
    if result.get("fidelityStatus") == "pending" or result.get("status") == "requires_manual_review" and "fidelityStatus" not in result:
        return 3
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("preparar", "auditar", "comprobar"):
        command = sub.add_parser(name)
        command.add_argument("--prompt", required=True, help="Archivo original UTF-8; se lee sin modificarlo.")
        if name != "preparar":
            command.add_argument("--informe", required=True, help="Texto íntegro y definitivo UTF-8.")
        if name == "auditar":
            command.add_argument("--registro", help="Registro previo opcional, contrastado de nuevo con el original.")
        if name == "comprobar":
            command.add_argument("--recibo", required=True)
        else:
            command.add_argument("--salida", required=True, help="Archivo nuevo; no sobrescribe archivos existentes.")
    args = parser.parse_args(argv)
    try:
        prompt = read_text(args.prompt)
        if args.command == "preparar":
            result = prepare_source(prompt)
        elif args.command == "auditar":
            if args.registro and json.loads(read_text(args.registro, MAX_JSON_BYTES)) != prepare_source(prompt):
                raise ValueError("SOURCE_STALE: el registro no corresponde al prompt o comparador actual.")
            result = compare(prompt, read_text(args.informe))
        else:
            result = check_receipt(prompt, read_text(args.informe), json.loads(read_text(args.recibo, MAX_JSON_BYTES)))
        if args.command != "comprobar":
            write_json(args.salida, result)
            summary = {k: result[k] for k in ("status", "fidelityStatus", "deliveryAllowed", "sourceSha256", "reportSha256") if k in result}
            print(json.dumps(dict(summary, output=args.salida), ensure_ascii=True))
        else:
            print(json.dumps(result, ensure_ascii=True))
        return 0 if args.command == "comprobar" else exit_for(result)
    except (OSError, ValueError, UnicodeError) as error:
        print(json.dumps(dict(error=type(error).__name__, message=str(error), deliveryAllowed=False), ensure_ascii=True), file=sys.stderr)
        return 4


if __name__ == "__main__":
    sys.exit(main())
