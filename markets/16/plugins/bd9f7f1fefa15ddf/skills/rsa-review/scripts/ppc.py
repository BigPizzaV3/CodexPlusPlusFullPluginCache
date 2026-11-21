#!/usr/bin/env python3
"""Read Google Ads report exports and answer two questions with arithmetic,
not opinion.

Commands
    inspect   Detect the report type, columns, date range and segments.
    triage    Why did CPA / ROAS / conversions move between two periods?
              Decomposes the change along the chain
              eligible impressions -> impression share -> CTR -> CPC / CVR,
              per segment (brand, non-brand, PMax, ...), and splits the
              account-level change into within-segment change and mix shift.
    ngrams    Search terms report -> n-grams with spend, conversions and CPA,
              negative-keyword candidates and terms to protect.

Input is a CSV or XLSX exported from the Google Ads UI or Editor, in English
or Spanish (other languages via --map). Preamble lines, totals rows,
thousands separators, currency symbols, percentages and "--" are handled.

Dependencies: pandas, numpy. Prints JSON; with --out also writes .json and .md.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

VERSION = "1.0.0"

# Canonical field -> accepted header names (lowercased, accents stripped).
ALIASES = {
    "date": ["day", "date", "dia", "fecha"],
    "week": ["week", "semana"],
    "month": ["month", "mes"],
    "campaign": ["campaign", "campana", "campaign name"],
    "campaign_type": ["campaign type", "tipo de campana", "advertising channel type"],
    "ad_group": ["ad group", "grupo de anuncios", "ad group name"],
    "search_term": ["search term", "termino de busqueda", "search terms", "terminos de busqueda", "query"],
    "match_type": ["match type", "tipo de concordancia", "search term match type",
                   "tipo de concordancia del termino de busqueda"],
    "keyword": ["keyword", "palabra clave", "search keyword"],
    "impressions": ["impr.", "impressions", "impr", "impresiones"],
    "clicks": ["clicks", "clics", "interactions", "interacciones"],
    "cost": ["cost", "coste", "costo", "spend"],
    "conversions": ["conversions", "conversiones", "conv."],
    "conv_value": ["conv. value", "conversion value", "valor de conv.", "valor de conversion",
                   "conversion value (by conv. time)", "all conv. value"],
    "search_is": ["search impr. share", "cuota de impresiones de busqueda", "search impression share",
                  "cuota de impr. de busqueda", "impr. share", "cuota de impresiones"],
    "lost_is_rank": ["search lost is (rank)", "cuota de impr. de busqueda perdida (ranking)",
                     "search lost impression share (rank)", "cuota de impresiones perdidas de la red de busqueda (ranking)"],
    "lost_is_budget": ["search lost is (budget)", "cuota de impr. de busqueda perdida (presupuesto)",
                       "search lost impression share (budget)", "cuota de impresiones perdidas de la red de busqueda (presupuesto)"],
    "currency": ["currency code", "currency", "codigo de moneda", "moneda"],
}

BRAND_DEFAULT = r"\bbrand\b|\bmarca\b|\bbrnd\b"
NONBRAND_GUARD = r"non[-_ ]?brand|nonbrand|generic|no[-_ ]?marca|competitor|competencia"


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", s.strip().lower())


# --------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------

def _read_raw(path):
    p = Path(path)
    if p.suffix.lower() in (".xlsx", ".xls"):
        return pd.read_excel(p, header=None, dtype=str)
    raw = p.read_bytes()
    for enc in ("utf-8-sig", "utf-16", "latin-1"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    lines = text.splitlines()
    sample = "\n".join(lines[:50])
    seps = {",": sample.count(","), "\t": sample.count("\t"), ";": sample.count(";")}
    sep = max(seps, key=seps.get)
    import csv
    from io import StringIO
    rows = list(csv.reader(StringIO(text), delimiter=sep))
    width = max((len(r) for r in rows), default=0)
    rows = [r + [None] * (width - len(r)) for r in rows]
    return pd.DataFrame(rows, dtype=object)


def _find_header(raw, extra_map):
    known = {a for v in ALIASES.values() for a in v} | set(extra_map)
    best, best_i = 0, None
    for i in range(min(len(raw), 30)):
        row = [_norm(x) for x in raw.iloc[i].tolist() if isinstance(x, str)]
        hits = sum(1 for x in row if x in known)
        if hits > best:
            best, best_i = hits, i
    if best_i is None or best < 2:
        raise SystemExit("Could not find a header row with Google Ads columns (e.g. Campaign, Clicks, Cost).")
    return best_i


def _to_num(series, decimal):
    s = series.astype(str).str.strip()
    s = s.replace({"--": np.nan, "": np.nan, "nan": np.nan, "None": np.nan, " --": np.nan})
    pct = s.str.endswith("%", na=False)
    lt = s.str.startswith("<", na=False)   # "< 10%" in impression share
    gt = s.str.startswith(">", na=False)   # "> 90%"
    s = s.str.replace(r"[<>%\s ]", "", regex=True)
    s = s.str.replace(r"[^\d,.\-]", "", regex=True)
    if decimal == ",":
        s = s.str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
    else:
        s = s.str.replace(",", "", regex=False)
    out = pd.to_numeric(s, errors="coerce")
    out = np.where(pct, out / 100.0, out)
    out = pd.Series(out, index=series.index)
    # "< 10%" -> 0.10 is an upper bound; keep the bound and flag it upstream
    return out, bool(lt.any() or gt.any())


def _detect_decimal(df, cols):
    commas = dots = 0
    for c in cols:
        for v in df[c].dropna().astype(str).head(200):
            v = v.strip().rstrip("%")
            if re.search(r"\d,\d{1,2}$", v):
                commas += 1
            elif re.search(r"\d\.\d{1,2}$", v):
                dots += 1
    return "," if commas > dots else "."


def load_report(path, mapping=None):
    extra = {_norm(k): v for k, v in (mapping or {}).items()}
    raw = _read_raw(path)
    h = _find_header(raw, extra)
    header = [str(x) if isinstance(x, str) else "" for x in raw.iloc[h].tolist()]
    df = raw.iloc[h + 1:].copy()
    df.columns = header
    df = df.dropna(how="all")
    rename, notes = {}, []
    for col in df.columns:
        n = _norm(col)
        if n in extra:
            rename[col] = extra[n]
            continue
        for field, al in ALIASES.items():
            if n in al and field not in rename.values():
                rename[col] = field
                break
    df = df.rename(columns=rename)
    allowed = set(ALIASES) | set(extra.values())
    df = df.loc[:, [c for c in df.columns if c in allowed]]
    df = df.loc[:, ~df.columns.duplicated()]
    # Drop totals rows: first text column starting with "Total"
    text_cols = [c for c in df.columns if c in ("campaign", "search_term", "ad_group", "keyword",
                                                 "date", "week", "month", "campaign_type")
                 or str(c).startswith(("auction_domain", "ch_time"))]
    mask = pd.Series(False, index=df.index)
    for c in text_cols:
        mask |= df[c].astype(str).str.strip().str.lower().str.match(r"^(total|totales|totale|gesamt)\b")
    if mask.any():
        notes.append(f"{int(mask.sum())} totals rows removed.")
    df = df[~mask]
    num_cols = [c for c in ["impressions", "clicks", "cost", "conversions", "conv_value",
                            "search_is", "lost_is_rank", "lost_is_budget"] if c in df.columns]
    dec = _detect_decimal(df, num_cols)
    for c in num_cols:
        df[c], bounded = _to_num(df[c], dec)
        if bounded and c.startswith(("search_is", "lost")):
            notes.append(f"'{c}' has values shown as '< 10%' or '> 90%'; the bound was used.")
    for c in ["date", "week", "month"]:
        if c in df.columns:
            df[c] = pd.to_datetime(df[c], errors="coerce", dayfirst=(dec == ","))
    return df.reset_index(drop=True), {"decimal": dec, "notes": notes,
                                       "columns": list(df.columns)}


# --------------------------------------------------------------------------
# Segments
# --------------------------------------------------------------------------

def segment_of(row, brand_re, pmax_re):
    name = str(row.get("campaign", "")).lower()
    ctype = _norm(row.get("campaign_type", ""))
    if "performance max" in ctype or re.search(pmax_re, name):
        return "pmax"
    if ctype and ctype not in ("search", "busqueda", "red de busqueda"):
        if ctype.startswith("app") or "multi" in ctype or "aplicacion" in ctype:
            return "app"
        if "shopping" in ctype or "compras" in ctype:
            return "shopping"
        if "demand" in ctype or "video" in ctype or "display" in ctype or "discovery" in ctype:
            return "upper_funnel"
        return ctype.replace(" ", "_")
    if re.search(brand_re, name) and not re.search(NONBRAND_GUARD, name):
        return "brand"
    return "non_brand"


# --------------------------------------------------------------------------
# Triage
# --------------------------------------------------------------------------

def _agg(d):
    s = {k: float(d[k].sum()) for k in ["impressions", "clicks", "cost", "conversions", "conv_value"]
         if k in d.columns}
    if "search_is" in d.columns and "impressions" in d.columns:
        ok = d["search_is"].notna() & (d["search_is"] > 0) & d["impressions"].notna()
        if ok.any():
            # Eligible impressions are additive; IS is not. Sum eligible, then divide.
            elig = float((d.loc[ok, "impressions"] / d.loc[ok, "search_is"]).sum())
            s["eligible_impressions"] = elig
            s["search_is"] = float(d.loc[ok, "impressions"].sum()) / elig if elig else np.nan
            for k in ("lost_is_rank", "lost_is_budget"):
                if k in d.columns:
                    w = d.loc[ok, k].fillna(0) * (d.loc[ok, "impressions"] / d.loc[ok, "search_is"])
                    s[k] = float(w.sum()) / elig if elig else np.nan
    return s


def _ratios(s):
    r = dict(s)
    div = lambda a, b: (a / b) if b else np.nan  # noqa: E731
    r["ctr"] = div(s.get("clicks", 0), s.get("impressions", 0))
    r["cpc"] = div(s.get("cost", 0), s.get("clicks", 0))
    r["cvr"] = div(s.get("conversions", 0), s.get("clicks", 0))
    r["cpa"] = div(s.get("cost", 0), s.get("conversions", 0))
    if "conv_value" in s:
        r["roas"] = div(s["conv_value"], s.get("cost", 0))
        r["value_per_conv"] = div(s["conv_value"], s.get("conversions", 0))
    return r


def _chg(a, b):
    if a is None or b is None or not np.isfinite(a) or not np.isfinite(b) or a == 0:
        return None
    return b / a - 1


def _log_share(parts):
    """Share of a multiplicative change explained by each factor (log
    decomposition). parts: {name: (before, after)}."""
    logs = {}
    for k, (x, y) in parts.items():
        if x and y and x > 0 and y > 0:
            logs[k] = math.log(y / x)
    tot = sum(logs.values())
    if not logs or abs(tot) < 1e-12:
        return {k: None for k in parts}, logs
    return {k: v / tot for k, v in logs.items()}, logs


def _verdict(ra, rb, sa, sb, min_conv, vol_logs=None, days=(1, 1)):
    lines = []
    conv_a, conv_b = sa.get("conversions", 0), sb.get("conversions", 0)
    if min(conv_a, conv_b) < min_conv:
        lines.append(f"Few conversions ({conv_a:.0f} vs {conv_b:.0f}). Ratio changes on this base are mostly noise.")
    cpa_c, cpc_c, cvr_c = _chg(ra["cpa"], rb["cpa"]), _chg(ra["cpc"], rb["cpc"]), _chg(ra["cvr"], rb["cvr"])
    if cpa_c is not None and cpc_c is not None and cvr_c is not None:
        if abs(cpa_c) >= 0.05:
            if abs(math.log1p(cpc_c)) > 2 * abs(math.log1p(cvr_c)):
                lines.append("CPA moved because of CPC (auction price), not conversion rate. Look at the auction: position, competitors, targets, budget.")
            elif abs(math.log1p(cvr_c)) > 2 * abs(math.log1p(cpc_c)):
                lines.append("CPA moved because of conversion rate. Look at traffic quality (search terms, geo, device), the landing page and tracking.")
            else:
                lines.append("CPA moved with both CPC and conversion rate. Check both.")
    conv_c = _chg(conv_a / days[0], conv_b / days[1])  # per day, like the factors below
    if conv_c is not None and abs(conv_c) >= 0.05 and vol_logs:
        labels = {"eligible_impressions(demand)": "eligible impressions (market demand or targeting reach)",
                  "impression_share": "impression share", "impressions": "impressions",
                  "clicks_per_impression(ctr)": "CTR", "cvr": "conversion rate"}
        same = {k: v for k, v in vol_logs.items() if v * math.log1p(conv_c) > 0}
        against = {k: v for k, v in vol_logs.items() if v * math.log1p(conv_c) < 0}
        if same:
            top = max(same, key=lambda k: abs(same[k]))
            msg = f"Conversions per day {'rose' if conv_c > 0 else 'fell'} {abs(conv_c):.0%}, mainly through {labels[top]} ({math.expm1(same[top]):+.0%})."
            against = {k: v for k, v in against.items() if abs(math.expm1(v)) >= 0.02}
            if against:
                msg += " Offset by " + ", ".join(f"{labels[k]} ({math.expm1(v):+.0%})" for k, v in against.items()) + "."
            lines.append(msg)
        if "impression_share" in vol_logs and vol_logs["impression_share"] < math.log(0.95):
            rk, bd = sb.get("lost_is_rank"), sb.get("lost_is_budget")
            if rk is not None and bd is not None:
                lines.append(f"Impression share lost after the change: {rk:.0%} to rank, {bd:.0%} to budget. "
                             + ("Budget will not recover it; bids, targets or quality will." if rk >= bd else "More budget would recover part of it."))
    return lines


def _break_date(d, tcol, b0, b1, a0):
    """Day where daily CPA (or conversions when CPA is undefined) shifts most:
    the split that maximises the difference in means, with at least 5 days on
    each side, searched over the two periods."""
    g = d[(d[tcol] >= a0) & (d[tcol] <= b1)].groupby(tcol)[["cost", "conversions"]].sum()
    if len(g) < 12:
        return None
    cpa = (g["cost"] / g["conversions"].replace(0, np.nan)).ffill().bfill()
    y = np.log(cpa.to_numpy()) if np.isfinite(cpa).all() and (cpa > 0).all() else g["conversions"].to_numpy(float)
    best, best_i = 0.0, None
    for i in range(7, len(y) - 7):
        x1, x2 = y[:i], y[i:]
        se = math.sqrt(x1.var(ddof=1) / len(x1) + x2.var(ddof=1) / len(x2)) + 1e-12
        t = abs(x2.mean() - x1.mean()) / se   # Welch t; high bar because every split is tried
        if t > best:
            best, best_i = t, i
    if best_i is None or best < 4:
        return None
    return str(pd.Timestamp(g.index[best_i]).date())


def cmd_triage(a):
    df, meta = load_report(a.data, json.loads(a.map) if a.map else None)
    tcol = next((c for c in ["date", "week", "month"] if c in df.columns), None)
    if tcol is None:
        raise SystemExit("The report needs a Day, Week or Month column. Export it with a time segment.")
    for c in ["clicks", "cost", "conversions", "impressions"]:
        if c not in df.columns:
            raise SystemExit(f"Missing column '{c}'. Export Impr., Clicks, Cost and Conversions.")
    a0, a1 = [pd.Timestamp(x) for x in a.a.split(":")]
    b0, b1 = [pd.Timestamp(x) for x in a.b.split(":")]
    A = df[(df[tcol] >= a0) & (df[tcol] <= a1)]
    B = df[(df[tcol] >= b0) & (df[tcol] <= b1)]
    if A.empty or B.empty:
        raise SystemExit(f"One of the periods has no rows. Data covers {df[tcol].min().date()} to {df[tcol].max().date()}.")
    days_a = (a1 - a0).days + 1
    days_b = (b1 - b0).days + 1
    if "campaign" in df.columns:
        df["segment"] = df.apply(segment_of, axis=1, args=(a.brand_regex, a.pmax_regex))
        A = A.assign(segment=df.loc[A.index, "segment"])
        B = B.assign(segment=df.loc[B.index, "segment"])
    else:
        A = A.assign(segment="all")
        B = B.assign(segment="all")
    out_segments = []
    sa_tot, sb_tot = _agg(A), _agg(B)
    for seg in sorted(set(A["segment"]) | set(B["segment"])):
        sa, sb = _agg(A[A.segment == seg]), _agg(B[B.segment == seg])
        ra, rb = _ratios(sa), _ratios(sb)
        row = {"segment": seg, "before": ra, "after": rb,
               "change": {k: _chg(ra.get(k), rb.get(k)) for k in rb if isinstance(rb.get(k), (int, float))}}
        # volume metrics are compared per day, so periods of different length compare
        for k in ["impressions", "clicks", "cost", "conversions", "conv_value", "eligible_impressions"]:
            if k in sa and k in sb:
                row["change"][k] = _chg(sa[k] / days_a, sb[k] / days_b)
        cpa_parts, _ = _log_share({"cpc": (ra["cpc"], rb["cpc"]), "cvr_inverse": (
            1 / ra["cvr"] if ra["cvr"] else None, 1 / rb["cvr"] if rb["cvr"] else None)})
        row["cpa_explained_by"] = cpa_parts
        vol = {"clicks_per_impression(ctr)": (ra["ctr"], rb["ctr"]),
               "cvr": (ra["cvr"], rb["cvr"])}
        if "eligible_impressions" in sa and "eligible_impressions" in sb:
            vol["eligible_impressions(demand)"] = (sa["eligible_impressions"] / days_a, sb["eligible_impressions"] / days_b)
            vol["impression_share"] = (sa["search_is"], sb["search_is"])
        else:
            vol["impressions"] = (sa["impressions"] / days_a, sb["impressions"] / days_b)
        row["conversions_explained_by"], vol_logs = _log_share(vol)
        row["verdict"] = _verdict(ra, rb, sa, sb, a.min_conv, vol_logs, (days_a, days_b))
        row["break_date"] = _break_date(df[df.get("segment", "all") == seg] if "segment" in df.columns else df, tcol, b0, b1, a0)
        row["share_of_cost_after"] = sb.get("cost", 0) / sb_tot["cost"] if sb_tot.get("cost") else None
        out_segments.append(row)
    # Mix: account CPA change = within-segment CPA change + shift in conversion mix
    ra_t, rb_t = _ratios(sa_tot), _ratios(sb_tot)
    mix = None
    if len(out_segments) > 1 and ra_t["cpa"] and rb_t["cpa"]:
        # Counterfactual: after-period segment CPAs with before-period conversion mix
        conv_a = {s["segment"]: s["before"]["conversions"] for s in out_segments}
        tot_a = sum(conv_a.values())
        cf = 0.0
        ok = True
        for s in out_segments:
            w = conv_a[s["segment"]] / tot_a if tot_a else 0
            cpa_b = s["after"]["cpa"]
            if w > 0 and (cpa_b is None or not np.isfinite(cpa_b)):
                ok = False
            elif w > 0:
                cf += w * cpa_b
        if ok and cf > 0:
            # account CPA is conv-weighted harmonic-ish; use cost/conv identity via weights on CPA
            within = cf / ra_t["cpa"] - 1
            total = rb_t["cpa"] / ra_t["cpa"] - 1
            mix = {"account_cpa_change": total, "within_segments": within,
                   "mix_shift": (1 + total) / (1 + within) - 1}
    warnings = list(meta["notes"])
    segs = {s["segment"] for s in out_segments}
    if "brand" in segs and len(segs) > 1:
        warnings.append("Brand is reported separately. Do not read the account CPA without it: brand captures existing demand at a much lower CPA.")
    if "campaign" in df.columns and not ({"brand"} & segs):
        warnings.append("No campaign matched the brand pattern. If brand campaigns are named differently, pass --brand-regex.")
    if segs & {"app", "upper_funnel"} and len(segs) > 1:
        warnings.append("App and upper-funnel campaigns usually optimize to different conversion actions (installs, view-through). The account CPA mixes unlike conversions: read segments, not the total.")
    if days_a != days_b:
        warnings.append(f"Periods differ in length ({days_a} vs {days_b} days).")
    warnings.append("Volume changes (impressions, clicks, cost, conversions) are per day; ratios (CPA, CPC, CVR, CTR, impression share) are over the whole period.")
    imp_a = {s["segment"]: s["before"].get("impressions", 0) for s in out_segments}
    imp_b = {s["segment"]: s["after"].get("impressions", 0) for s in out_segments}
    ta, tb = sum(imp_a.values()) or 1, sum(imp_b.values()) or 1
    shift = max(abs(imp_b[k] / tb - imp_a[k] / ta) for k in imp_a) if imp_a else 0
    if shift > 0.1:
        warnings.append(f"The impression mix between segments shifted by up to {shift:.0%}. Account-level CTR, CPC and CVR changes partly reflect that mix; read them per segment.")
    late = [s_["segment"] for s_ in out_segments if s_.get("break_date") and pd.Timestamp(s_["break_date"]) >= b1 - pd.Timedelta(days=10)]
    if late:
        warnings.append(f"Shift found in the last 10 days for {', '.join(late)}: if conversions arrive late (leads to sales, trials to paid), this can be conversion lag, not a real change.")
    if "search_is" not in df.columns:
        warnings.append("No Search impr. share column: demand and share cannot be separated. Add Search impr. share, Search lost IS (rank) and (budget) to the export.")
    return {"command": "triage", "version": VERSION,
            "periods": {"before": [str(a0.date()), str(a1.date())], "after": [str(b0.date()), str(b1.date())]},
            "account": {"before": ra_t, "after": rb_t,
                        "change": {k: (_chg(ra_t.get(k) / days_a, rb_t.get(k) / days_b)
                                       if k in ("impressions", "clicks", "cost", "conversions", "conv_value", "eligible_impressions")
                                       else _chg(ra_t.get(k), rb_t.get(k)))
                                   for k in rb_t if isinstance(rb_t.get(k), (int, float))}},
            "days": {"before": days_a, "after": days_b},
            "mix": mix, "segments": out_segments, "warnings": warnings,
            "columns_found": meta["columns"]}


# --------------------------------------------------------------------------
# N-grams
# --------------------------------------------------------------------------

STOP = set("""a an and or the of for to in on with at by from de del la las el los y o en
con para por un una unos unas al lo que se su sus mi tu no is are be my your how what why
do does can i me it this that as vs""".split())

INTENT_HINTS = [
    ("jobs", r"\b(jobs?|careers?|hiring|vacanc\w*|salar\w*|internships?|resume|cv|empleo|trabajo|sueldo|salario|oferta de empleo)\b"),
    ("free", r"\b(free|gratis|gratuit\w*|crack\w*|torrent|pirat\w*|mod apk)\b"),
    ("informational", r"\b(how to|what is|what are|meaning|definition|tutorial|examples?|que es|como)\b"),
    ("navigational", r"\b(login|log in|sign in|account|contact|phone number|customer service|iniciar sesion)\b"),
    ("diy_or_learning", r"\b(course|courses|class|certification|degree|curso|pdf|book)\b"),
]


def intent_hint(text):
    t = _norm(text)
    hits = [name for name, pat in INTENT_HINTS if re.search(pat, t)]
    return ",".join(hits) or None


def _tokens(s):
    s = _norm(s)
    return [t for t in re.findall(r"[a-z0-9]+(?:['\-][a-z0-9]+)*", s)]


def conflicts(candidate, protected):
    """A phrase or broad negative on `candidate` blocks every search term that
    contains its tokens. It conflicts when a converting n-gram contains it.
    The reverse (candidate longer than the converting n-gram) is safe."""
    c = f" {candidate} "
    return any(c in f" {p} " for p in protected)


def cmd_ngrams(a):
    df, meta = load_report(a.data, json.loads(a.map) if a.map else None)
    if "search_term" not in df.columns:
        raise SystemExit("No search term column. Export the Search terms report (Insights and reports > Search terms).")
    for c in ["cost", "clicks"]:
        if c not in df.columns:
            raise SystemExit(f"Missing column '{c}'.")
    if "conversions" not in df.columns:
        df["conversions"] = 0.0
    df = df[df["search_term"].notna()]
    if "campaign" in df.columns:
        df["segment"] = df.apply(segment_of, axis=1, args=(a.brand_regex, a.pmax_regex))
        if not a.include_brand:
            df = df[df.segment != "brand"]
    tot_cost = float(df["cost"].sum())
    tot_conv = float(df["conversions"].sum())
    acct_cpa = tot_cost / tot_conv if tot_conv else None
    target = a.target_cpa or acct_cpa
    rows = []
    for n in a.n:
        acc = {}
        for _, r in df.iterrows():
            toks = _tokens(r["search_term"])
            grams = set(" ".join(toks[i:i + n]) for i in range(len(toks) - n + 1))
            for g in grams:
                parts = g.split()
                if parts[0] in STOP or parts[-1] in STOP:
                    continue
                d = acc.setdefault(g, {"terms": 0, "impressions": 0.0, "clicks": 0.0, "cost": 0.0,
                                       "conversions": 0.0, "conv_value": 0.0, "campaigns": set(),
                                       "ids": set()})
                d["terms"] += 1
                d["ids"].add(r.name)
                for k in ["impressions", "clicks", "cost", "conversions", "conv_value"]:
                    if k in r and pd.notna(r[k]):
                        d[k] += float(r[k])
                if "campaign" in r:
                    d["campaigns"].add(str(r["campaign"]))
        for g, d in acc.items():
            if d["cost"] <= 0 and d["conversions"] <= 0:
                continue
            cpa = d["cost"] / d["conversions"] if d["conversions"] else None
            rows.append({"ngram": g, "n": n, "terms": d["terms"], "ids": frozenset(d["ids"]),
                         "intent_hint": intent_hint(g), "impressions": d["impressions"],
                         "clicks": d["clicks"], "cost": d["cost"], "conversions": d["conversions"],
                         "cpa": cpa, "cost_share": d["cost"] / tot_cost if tot_cost else None,
                         "campaigns": len(d["campaigns"]),
                         "cpa_vs_target": (cpa / target) if (cpa and target) else None})
    res = pd.DataFrame(rows)
    if res.empty:
        raise SystemExit("No n-grams with cost found.")
    # Candidates: spend at least `waste_multiple` x target CPA with zero conversions,
    # or CPA above `bad_ratio` x target with enough clicks to judge.
    thr = (a.waste_multiple * target) if target else res["cost"].quantile(0.95)
    zero = res[(res.conversions == 0) & (res.cost >= thr) & (res.clicks >= a.min_clicks)]
    # One candidate per set of search terms: keep the shortest n-gram that covers them
    zero = zero.sort_values(["n", "cost"], ascending=[True, False]).drop_duplicates("ids")
    poor = res[(res.conversions > 0) & (res.cpa_vs_target >= a.bad_ratio) & (res.clicks >= 3 * a.min_clicks)]
    # Protection: n-grams that carry conversions at or below target
    protect = res[(res.conversions >= a.protect_conv) & ((res.cpa_vs_target.isna()) | (res.cpa_vs_target <= 1.0))]
    protect_set = set(protect.ngram)
    coverage = None
    if a.negatives:
        negs = [" ".join(_tokens(x)) for x in a.negatives]
        hit = df["search_term"].map(lambda t: any(f" {n} " in f" {' '.join(_tokens(t))} " for n in negs))
        zc = df["conversions"] == 0
        coverage = {"negatives": negs,
                    "zero_conv_cost_total": float(df.loc[zc, "cost"].sum()),
                    "zero_conv_cost_blocked": float(df.loc[zc & hit, "cost"].sum()),
                    "converting_terms_blocked": int((hit & ~zc).sum()),
                    "conversions_blocked": float(df.loc[hit, "conversions"].sum()),
                    "cost_blocked_total": float(df.loc[hit, "cost"].sum()),
                    "blocked_converting_examples": df.loc[hit & ~zc, "search_term"].head(10).tolist()}
        zt = coverage["zero_conv_cost_total"]
        coverage["share_of_zero_conv_cost_covered"] = coverage["zero_conv_cost_blocked"] / zt if zt else None

    zero = zero.assign(conflicts_with_converting=zero.ngram.map(lambda g: conflicts(g, protect_set)))
    poor = poor.assign(conflicts_with_converting=poor.ngram.map(lambda g: conflicts(g, protect_set)))
    cols = ["ngram", "n", "terms", "clicks", "cost", "conversions", "cpa", "cost_share", "campaigns", "intent_hint"]
    fmt = lambda d, k: d.sort_values("cost", ascending=False).head(k)  # noqa: E731
    out = {"command": "ngrams", "version": VERSION,
           "rows": int(len(df)), "cost_total": tot_cost, "conversions_total": tot_conv,
           "account_cpa": acct_cpa, "target_cpa_used": target,
           "thresholds": {"zero_conv_min_cost": thr, "min_clicks": a.min_clicks,
                          "poor_cpa_ratio": a.bad_ratio},
           "negative_candidates_zero_conv": fmt(zero, a.top)[cols + ["conflicts_with_converting"]].to_dict("records"),
           "high_cpa_ngrams": fmt(poor, a.top)[cols + ["cpa_vs_target", "conflicts_with_converting"]].to_dict("records"),
           "protect": protect.sort_values("conversions", ascending=False).head(a.top)[cols].to_dict("records"),
           "top_by_cost": fmt(res, a.top)[cols].to_dict("records"),
           "negatives_coverage": coverage,
           "wasted_cost_share_zero_conv_terms": float(df.loc[df.conversions == 0, "cost"].sum() / tot_cost) if tot_cost else None,
           "warnings": list(meta["notes"]),
           "notes": [
               "N-grams overlap: one search term counts in every n-gram it contains, so n-gram costs do not add up to the total.",
               "A candidate is a starting point, not a negative to add blindly: check the keyword, ad group and campaign that matched it, and whether another campaign should get that traffic.",
               "conflicts_with_converting = a converting n-gram contains this one. A phrase or broad negative on it would block that converting traffic; use exact, or negate a longer phrase.",
           ]}
    if "campaign" in df.columns and not a.include_brand:
        out["notes"].append("Brand campaigns were excluded. Pass --include-brand to keep them.")
    return out


# --------------------------------------------------------------------------
# Auction insights
# --------------------------------------------------------------------------

AUCTION_ALIASES = {
    "domain": ["display url domain", "dominio de la url visible", "domain"],
    "is": ["search impr. share (auction insights)", "impr. share", "search impr. share",
           "cuota de impresiones de busqueda (informe de subasta)", "cuota de impresiones"],
    "overlap": ["search overlap rate", "overlap rate", "porcentaje de coincidencias", "tasa de solapamiento"],
    "position_above": ["search position above rate", "position above rate", "porcentaje de posicion superior"],
    "top": ["top of page rate", "search top of page rate", "porcentaje de parte superior de la pagina"],
    "abs_top": ["abs. top of page rate", "search abs. top of page rate",
                "porcentaje de parte superior absoluta de la pagina"],
    "outranking": ["search outranking share", "outranking share", "cuota de superacion"],
}


def cmd_auction(a):
    m = {}
    for field, al in AUCTION_ALIASES.items():
        for x in al:
            m[x] = "auction_" + field
    df, meta = load_report(a.data, {**m, **(json.loads(a.map) if a.map else {})})
    df.columns = [c.replace("auction_", "") for c in df.columns]
    if "domain" not in df.columns:
        raise SystemExit("No 'Display URL domain' column. Export Auction insights from the Campaigns or Keywords view.")
    dec = meta["decimal"]
    for c in ["is", "overlap", "position_above", "top", "abs_top", "outranking"]:
        if c in df.columns and df[c].dtype == object:
            below = df[c].astype(str).str.strip().str.startswith("<")
            df[c], _ = _to_num(df[c], dec)
            # "< 10%" is a bound, not a value: keep it out of averages
            df.loc[below, c] = np.nan
    tcol = next((c for c in ["week", "month", "date"] if c in df.columns), None)
    if a.campaign and "campaign" in df.columns:
        df = df[df["campaign"].astype(str).str.contains(a.campaign, case=False, regex=False)]
    you = df["domain"].astype(str).str.strip().str.lower().isin(["you", "tu", "tú", "usted", "vous", "sie"])
    df["domain"] = np.where(you, "YOU", df["domain"].astype(str).str.strip().str.lower())
    metrics = [c for c in ["is", "overlap", "position_above", "top", "abs_top", "outranking"] if c in df.columns]
    notes = list(meta["notes"])
    if "campaign" in df.columns and df["campaign"].nunique() > 1:
        notes.append("Several campaigns are averaged with equal weight; the export has no impressions to weight by. Filter with --campaign or export at account level for exact shares.")
    out = {"command": "auction", "version": VERSION, "metrics": metrics, "notes": notes}
    if tcol:
        periods = sorted(df[tcol].dropna().unique())
        if len(periods) < 2:
            tcol = None
    if tcol:
        n = max(1, a.window)
        recent = periods[-n:]
        before = periods[-2 * n:-n] if len(periods) >= 2 * n else periods[:-n]
        R = df[df[tcol].isin(recent)].groupby("domain")[metrics].mean()
        B = df[df[tcol].isin(before)].groupby("domain")[metrics].mean()
        present_r = set(df[df[tcol].isin(recent)]["domain"])
        present_b = set(df[df[tcol].isin(before)]["domain"])
        rows = []
        for d in sorted(set(R.index) | set(B.index)):
            r = {"domain": d}
            for c in metrics:
                rv = R.at[d, c] if d in R.index else np.nan
                bv = B.at[d, c] if d in B.index else np.nan
                r[f"{c}_now"] = rv
                r[f"{c}_before"] = bv
                r[f"{c}_change_pts"] = (rv - bv) if np.isfinite(rv) and np.isfinite(bv) else None
            r["status"] = ("new" if d not in present_b else "gone" if d not in present_r else "present")
            if "is" in metrics and not np.isfinite(r["is_now"]) and d in present_r:
                r["is_now_label"] = "<10%"
            rows.append(r)
        res = pd.DataFrame(rows)
        key = "is_now" if "is_now" in res.columns else res.columns[1]
        res = res.sort_values(key, ascending=False, na_position="last")
        out["periods"] = {"recent": [str(pd.Timestamp(x).date()) for x in recent],
                          "before": [str(pd.Timestamp(x).date()) for x in before]}
        out["competitors"] = res.head(a.top).to_dict("records")
        out["new_entrants"] = res[(res.status == "new") & (res.get("is_now", pd.Series(dtype=float)).fillna(0) >= 0.1)]["domain"].tolist()
        out["new_below_10pct"] = res[(res.status == "new") & res.get("is_now", pd.Series(dtype=float)).isna()]["domain"].tolist()
        if "is_change_pts" in res.columns:
            mv = res[res.domain != "YOU"].dropna(subset=["is_change_pts"])
            out["rising"] = mv.sort_values("is_change_pts", ascending=False).head(5)[["domain", "is_now", "is_change_pts"]].to_dict("records")
            out["falling"] = mv.sort_values("is_change_pts").head(5)[["domain", "is_now", "is_change_pts"]].to_dict("records")
        if "YOU" in res.domain.values:
            out["you"] = res[res.domain == "YOU"].iloc[0].to_dict()
    else:
        res = df.groupby("domain")[metrics].mean().sort_values(metrics[0], ascending=False)
        out["competitors"] = res.head(a.top).reset_index().to_dict("records")
    out["how_to_read"] = [
        "Impression share: how often the competitor showed when you were eligible. Values shown as '< 10%' are bounds; they are left out of averages and shown as <10%.",
        "Overlap rate: how often their ad showed when yours did. High overlap plus rising share means they are buying your queries.",
        "Outranking share (on your row of each competitor): how often you ranked above them or they did not show.",
        "Position above rate: how often they ranked above you when both showed. Rising position above with flat share often means higher bids or targets.",
    ]
    return out


def md_auction(o):
    L = ["# Auction insights", ""]
    if "periods" in o:
        L += [f"- Recent: {o['periods']['recent'][0]} to {o['periods']['recent'][-1]}; before: {o['periods']['before'][0] if o['periods']['before'] else 'n/a'} to {o['periods']['before'][-1] if o['periods']['before'] else 'n/a'}"]
        if o.get("new_entrants"):
            L.append(f"- New with at least 10% share: {', '.join(o['new_entrants'])}")
        L += ["", "| Domain | Impr. share | Change (pts) | Overlap | Position above | Outranking |", "|---|---:|---:|---:|---:|---:|"]
        for r in o["competitors"]:
            f = lambda k: "n/a" if r.get(k) is None or (isinstance(r.get(k), float) and not np.isfinite(r.get(k))) else f"{100 * r[k]:.1f}%"  # noqa: E731
            ch = r.get("is_change_pts")
            L.append(f"| {_c(r['domain'])} | {r.get('is_now_label') or f('is_now')} | {'n/a' if ch is None else f'{100 * ch:+.1f}'} | {f('overlap_now')} | {f('position_above_now')} | {f('outranking_now')} |")
    L += ["", "## Notes", ""] + [f"- {x}" for x in o["notes"] + o["how_to_read"]]
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------
# Change history
# --------------------------------------------------------------------------

CH_ALIASES = {"date & time": "ch_time", "fecha y hora": "ch_time", "date and time": "ch_time",
              "user": "ch_user", "usuario": "ch_user", "changes": "ch_changes", "cambios": "ch_changes",
              "campaign": "campaign", "campana": "campaign", "ad group": "ad_group",
              "grupo de anuncios": "ad_group", "tool": "ch_tool", "herramienta": "ch_tool"}

CH_PATTERNS = [
    ("target_cpa", r"target cpa (?:increased|decreased|changed) from ([^\s]+) to ([^\s/]+)"),
    ("target_roas", r"target roas (?:increased|decreased|changed) from ([^\s]+) to ([^\s/]+)"),
    ("budget", r"budget amount (?:increased|decreased|changed)?\s*(?:changed )?from ([^\s]+) to ([^\s/]+)"),
    ("bid_strategy", r"bid strategy (?:type )?changed from (.+?) to (.+?)(?: /|$)"),
    ("status", r"status changed from (\w+) to (\w+)"),
    ("location", r"location|geo target|location target"),
    ("keyword", r"keyword"),
    ("negative", r"negative"),
    ("ad", r"\bad\b|responsive search ad|headline|description"),
    ("asset", r"asset|sitelink|callout|snippet|extension"),
    ("audience", r"audience"),
    ("conversion", r"conversion goal|conversion action"),
    ("network", r"network|search partners|display network"),
]


def _money(s):
    v, _ = _to_num(pd.Series([s]), "," if re.search(r"\d,\d{2}$", s) else ".")
    return float(v.iloc[0]) if pd.notna(v.iloc[0]) else None


def _parse_dt(series):
    s = series.astype(str).str.replace("\u202f", " ", regex=False)
    try:
        return pd.to_datetime(s, errors="coerce", format="mixed")
    except (TypeError, ValueError):  # pandas < 2.0
        return pd.to_datetime(s, errors="coerce")


def cmd_changes(a):
    df2, meta = load_report(a.data, CH_ALIASES)
    if "ch_changes" not in df2.columns:
        raise SystemExit("No 'Changes' column. Export Change history from Tools > Change history > Download.")
    df2["when"] = _parse_dt(df2["ch_time"]) if "ch_time" in df2.columns else pd.NaT
    rows = []
    for _, r in df2.iterrows():
        txt = re.sub(r"\s*\n\s*", "; ", str(r.get("ch_changes", ""))).strip("; ")
        low = txt.lower()
        kinds, values = [], {}
        for kind, pat in CH_PATTERNS:
            mt = re.search(pat, low)
            if mt:
                kinds.append(kind)
                if mt.groups() and kind in ("target_cpa", "target_roas", "budget"):
                    o = re.search(pat, txt, flags=re.I)
                    a0, a1 = _money(o.group(1)), _money(o.group(2))
                    if a0 and a1:
                        values[kind] = (a0, a1)
                elif mt.groups():
                    values[kind] = mt.groups()
                if kind in ("target_cpa", "target_roas", "budget", "bid_strategy", "status"):
                    break
        user = str(r.get("ch_user", ""))
        auto = bool(re.search(r"recommendation|auto[- ]?appl|automated", user.lower()))
        rows.append({"when": r["when"], "user": user, "campaign": r.get("campaign"), "ad_group": r.get("ad_group"),
                     "kind": kinds[0] if kinds else "other", "values": values, "auto": auto, "text": txt[:200]})
    ch = pd.DataFrame(rows)
    flags = []
    # Target and budget changes: size and frequency
    for kind in ("target_cpa", "target_roas", "budget"):
        sub = ch[ch.kind == kind].sort_values("when")
        for camp, g in sub.groupby("campaign"):
            seq = []
            for _, r in g.iterrows():
                v = r["values"].get(kind)
                if v:
                    pct = v[1] / v[0] - 1
                    seq.append((r["when"], v[0], v[1], pct))
                    if abs(pct) > a.big_change:
                        high = abs(pct) > 2 * a.big_change
                        flags.append({"severity": "high" if high else "medium",
                                      "campaign": camp, "when": str(r["when"]), "what": f"{kind} {v[0]:g} -> {v[1]:g} ({pct:+.0%})",
                                      "why": f"Step above {2 * a.big_change:.0%} (high) or {a.big_change:.0%} (medium) at once. Large steps reset calibration and make the effect hard to read."
                                             + (" A factor of 10 or more often means a typo." if abs(pct) >= 9 or (v[1] and v[0] / v[1] >= 10) else "")})
            for i in range(1, len(seq)):
                gap = (seq[i][0] - seq[i - 1][0]).days if pd.notna(seq[i][0]) and pd.notna(seq[i - 1][0]) else None
                if kind != "budget" and gap is not None and gap < a.learning_days:
                    flags.append({"severity": "high", "campaign": camp, "when": str(seq[i][0]),
                                  "what": f"{kind} changed again after {gap} days",
                                  "why": f"Target changed inside the calibration window ({a.learning_days} days). Results in between cannot be attributed to either target."})
    net = []
    for kind in ("target_cpa", "target_roas", "budget"):
        sub = ch[ch.kind == kind].dropna(subset=["when"]).sort_values("when")
        for camp, g in sub.groupby("campaign"):
            vals = [r["values"][kind] for _, r in g.iterrows() if kind in r["values"]]
            if len(vals) >= 2:
                first, last = vals[0][0], vals[-1][1]
                net.append({"campaign": camp, "kind": kind, "changes": len(vals), "from": first, "to": last,
                            "net_change": last / first - 1 if first else None,
                            "from_date": str(g["when"].iloc[0]), "to_date": str(g["when"].iloc[-1])})
    for _, r in ch[ch.kind == "bid_strategy"].iterrows():
        flags.append({"severity": "high", "campaign": r["campaign"], "when": str(r["when"]),
                      "what": "bid strategy changed", "why": "Resets calibration; compare results only after 1 to 2 conversion cycles."})
    for _, r in ch[ch.auto].iterrows():
        flags.append({"severity": "medium", "campaign": r["campaign"], "when": str(r["when"]),
                      "what": "auto-applied or system change: " + r["text"][:80],
                      "why": "Changes made by recommendations auto-apply are easy to miss. Check they match the account goals."})
    for _, r in ch[ch.kind.isin(["conversion", "network", "location"])].iterrows():
        flags.append({"severity": "medium", "campaign": r["campaign"], "when": str(r["when"]),
                      "what": f"{r['kind']} change: " + r["text"][:80],
                      "why": "Changes to conversion goals, networks or locations alter what the campaign buys or counts."})
    sev = {"high": 0, "medium": 1}
    flags.sort(key=lambda f: (sev[f["severity"]], f["when"]))
    by_kind = ch["kind"].value_counts().to_dict()
    by_user = ch["user"].value_counts().head(10).to_dict()
    by_day = ch.dropna(subset=["when"]).groupby(ch["when"].dt.date).size()
    busiest = by_day.sort_values(ascending=False).head(5)
    return {"command": "changes", "version": VERSION, "rows": int(len(ch)),
            "range": [str(ch["when"].min()), str(ch["when"].max())],
            "by_kind": by_kind, "by_user": by_user,
            "busiest_days": {str(k): int(v) for k, v in busiest.items()},
            "net_changes": net,
            "flags": flags[: a.top * 2],
            "timeline_targets_budgets": ch[ch.kind.isin(["target_cpa", "target_roas", "budget", "bid_strategy", "status"])]
                .sort_values("when")[["when", "campaign", "kind", "text"]].astype(str).tail(60).to_dict("records"),
            "notes": meta["notes"] + [
                "Match the dates of flagged changes with the performance timeline before naming a cause.",
                "Change history does not include every change (for example some shared library edits). Absence here is not proof nothing changed.",
            ]}


def md_changes(o):
    L = ["# Change history", "", f"- Changes: {o['rows']} from {o['range'][0]} to {o['range'][1]}",
         "- By type: " + ", ".join(f"{k} {v}" for k, v in o["by_kind"].items()),
         "- By user: " + ", ".join(f"{k} {v}" for k, v in o["by_user"].items()), "",
         "## Net change over the period", "", "| Campaign | Setting | Changes | From | To | Net |", "|---|---|---:|---:|---:|---:|"]
    for n_ in o.get("net_changes", []):
        L.append(f"| {_c(str(n_['campaign'])[:40])} | {n_['kind']} | {n_['changes']} | {n_['from']:g} | {n_['to']:g} | {_p(n_['net_change'], 0)} |")
    L += ["", "## Flags", "", "| Severity | When | Campaign | What | Why |", "|---|---|---|---|---|"]
    for f in o["flags"]:
        L.append(f"| {f['severity']} | {f['when'][:16]} | {_c(str(f['campaign'])[:40])} | {_c(f['what'])} | {_c(f['why'])} |")
    L += ["", "## Notes", ""] + [f"- {x}" for x in o["notes"]]
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------
# Quality Score
# --------------------------------------------------------------------------

QS_ALIASES = {"quality score": "qs", "nivel de calidad": "qs", "qual. score": "qs",
              "exp. ctr": "qs_ctr", "expected ctr": "qs_ctr", "ctr esperado": "qs_ctr",
              "ad relevance": "qs_rel", "relevancia del anuncio": "qs_rel",
              "landing page exp.": "qs_lp", "landing page experience": "qs_lp",
              "experiencia en la pagina de destino": "qs_lp", "exp. de pagina de destino": "qs_lp"}


def _rating(v):
    s = _norm(v)
    if s.startswith(("above", "superior", "por encima")):
        return 1
    if s.startswith(("below", "inferior", "por debajo")):
        return -1
    if s.startswith(("average", "media", "promedio")):
        return 0
    return np.nan


def cmd_qs(a):
    df2, meta2 = load_report(a.data, QS_ALIASES)
    if "qs" not in df2.columns:
        raise SystemExit("No Quality Score column. In Keywords, add Quality Score, Exp. CTR, Ad relevance and Landing page exp.")
    d = df2.copy()
    d["qs"] = pd.to_numeric(d["qs"], errors="coerce")
    w = "cost" if "cost" in d.columns else "impressions" if "impressions" in d.columns else None
    if w is None:
        raise SystemExit("Add Cost or Impr. to weight Quality Score.")
    d = d[d[w].fillna(0) > 0]
    has = d["qs"].notna()
    cov = float(d.loc[has, w].sum() / d[w].sum()) if d[w].sum() else 0
    wqs = float((d.loc[has, "qs"] * d.loc[has, w]).sum() / d.loc[has, w].sum()) if has.any() else None
    comp = {}
    for c, name in [("qs_ctr", "expected_ctr"), ("qs_rel", "ad_relevance"), ("qs_lp", "landing_page")]:
        if c in d.columns:
            r = d[c].map(_rating)
            tot = d.loc[r.notna(), w].sum()
            comp[name] = {k: float(d.loc[r == v, w].sum() / tot) if tot else None
                          for k, v in [("above", 1), ("average", 0), ("below", -1)]}
    worst = max(comp, key=lambda k: comp[k]["below"] or 0) if comp else None
    cols = [c for c in ["campaign", "ad_group", "keyword", "qs", "qs_ctr", "qs_rel", "qs_lp", "cost", "conversions"] if c in d.columns]
    low = d[has & (d["qs"] <= a.low)].sort_values(w, ascending=False).head(a.top)[cols]
    dist = d.loc[has].groupby("qs")[w].sum()
    dist = (dist / dist.sum()).round(4).to_dict() if dist.sum() else {}
    return {"command": "qs", "version": VERSION, "weighted_by": w,
            "weighted_quality_score": wqs, "coverage_share": cov,
            "distribution_by_score": {int(k): v for k, v in dist.items()},
            "components": comp, "main_drag": worst,
            "low_qs_top_spend": low.astype(object).where(low.notna(), None).to_dict("records"),
            "notes": meta2["notes"] + [
                "Quality Score is a diagnostic, not a KPI. A keyword with a low score and a good CPA is fine.",
                "Expected CTR below average: ad copy and keyword-to-query fit. Ad relevance below average: ad group too broad for its ads. Landing page below average: page match and experience; it is measured per keyword, not per page.",
            ]}


def md_qs(o):
    L = ["# Quality Score", "",
         f"- Quality Score weighted by {o['weighted_by']}: {_n(o['weighted_quality_score'], 1)} (covers {_n(100 * o['coverage_share'], 0)}% of {o['weighted_by']})",
         f"- Component most often below average: {o['main_drag']}", "",
         "| Component | Above | Average | Below |", "|---|---:|---:|---:|"]
    for k, v in o["components"].items():
        L.append(f"| {k} | {_n(100 * (v['above'] or 0), 0)}% | {_n(100 * (v['average'] or 0), 0)}% | {_n(100 * (v['below'] or 0), 0)}% |")
    L += ["", "## Low Quality Score, highest spend", ""]
    for r in o["low_qs_top_spend"]:
        L.append("- " + ", ".join(f"{k}: {v}" for k, v in r.items()))
    L += ["", "## Notes", ""] + [f"- {x}" for x in o["notes"]]
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------
# Budget pacing
# --------------------------------------------------------------------------

def cmd_pacing(a):
    df, meta = load_report(a.data, json.loads(a.map) if a.map else None)
    tcol = "date" if "date" in df.columns else None
    if tcol is None or "cost" not in df.columns:
        raise SystemExit("Pacing needs a report by Day with Cost.")
    today = pd.Timestamp(a.today) if a.today else pd.Timestamp.today().normalize()
    m0 = today.replace(day=1)
    m_end = (m0 + pd.offsets.MonthEnd(0))
    if a.campaign and "campaign" in df.columns:
        df = df[df["campaign"].astype(str).str.contains(a.campaign, case=False, regex=False)]
    daily = df.groupby(tcol)["cost"].sum()
    mtd = daily[(daily.index >= m0) & (daily.index < today)]   # today is partial: excluded
    days_done = (today - m0).days
    days_left = (m_end - today).days + 1
    spent = float(mtd.sum()) * (1 + a.surcharge)
    budget = a.budget
    rr_all = spent / days_done if days_done else 0
    last7 = daily[(daily.index >= today - pd.Timedelta(days=7)) & (daily.index < today)]
    rr_7 = float(last7.sum()) * (1 + a.surcharge) / max(len(last7), 1) if len(last7) else rr_all
    fc_all = spent + rr_all * days_left
    fc_7 = spent + rr_7 * days_left
    need = max(budget - spent, 0) / days_left if days_left else 0
    over = spent - budget if spent > budget else 0.0
    return {"over_budget_already": over,"command": "pacing", "version": VERSION,
            "month": str(m0.date())[:7], "as_of": str(today.date()),
            "days_done": days_done, "days_left_including_today": days_left,
            "spent_mtd": spent, "budget": budget, "surcharge_applied": a.surcharge,
            "run_rate_mtd": rr_all, "run_rate_last7": rr_7,
            "forecast_eom_mtd_rate": fc_all, "forecast_eom_last7_rate": fc_7,
            "forecast_vs_budget_last7": fc_7 / budget - 1 if budget else None,
            "daily_needed_to_land": need,
            "daily_needed_vs_last7": need / rr_7 - 1 if rr_7 else None,
            "notes": meta["notes"] + [
                "Today is excluded: its spend is partial.",
                "Google can spend up to twice the average daily budget on a given day, and is held to the monthly limit of about 30.4 times the daily budget per campaign.",
                "Under Smart Bidding, raising the daily budget does not raise spend if the campaign is limited by its target, not its budget.",
            ]}


def md_pacing(o):
    L = [f"# Budget pacing, {o['month']} (as of {o['as_of']})", "",
         f"- Spent month to date: {_n(o['spent_mtd'])} of {_n(o['budget'])} ({o['days_done']} days done, {o['days_left_including_today']} left including today)",
         f"- Run rate: {_n(o['run_rate_mtd'])}/day month to date, {_n(o['run_rate_last7'])}/day last 7 days",
         f"- Forecast at last-7-day rate: {_n(o['forecast_eom_last7_rate'])} ({_p(o['forecast_vs_budget_last7'])} vs budget)",
         (f"- Budget already exceeded by {_n(o['over_budget_already'])}. Pause or cut now to limit the overrun." if o.get("over_budget_already") else
          f"- Daily spend needed to land on budget: {_n(o['daily_needed_to_land'])} ({_p(o['daily_needed_vs_last7'])} vs last 7 days)"),
         "", "## Notes", ""] + [f"- {x}" for x in o["notes"]]
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------
# Unit economics -> targets
# --------------------------------------------------------------------------

def cmd_targets(a):
    """Break-even and target CPA / ROAS from unit economics. Works for
    e-commerce (order value, margin) and lead generation (funnel rates)."""
    value = None
    steps = []
    if a.order_value is not None:
        value = a.order_value * a.margin * a.ltv_multiple
        steps.append(f"Value per conversion = order value {a.order_value:g} x gross margin {a.margin:.0%} x LTV multiple {a.ltv_multiple:g} = {value:,.2f}")
    elif a.deal_value is not None:
        rate = a.lead_to_opp * a.opp_to_win
        value = a.deal_value * a.margin * a.ltv_multiple * rate
        steps.append(f"Value per lead = deal value {a.deal_value:g} x margin {a.margin:.0%} x LTV multiple {a.ltv_multiple:g} x lead-to-opportunity {a.lead_to_opp:.0%} x win rate {a.opp_to_win:.0%} = {value:,.2f}")
    else:
        raise SystemExit("Give --order-value (e-commerce) or --deal-value with --lead-to-opp and --opp-to-win (lead generation).")
    breakeven_cpa = value
    target_cpa = value * (1 - a.profit_share)
    steps.append(f"Break-even CPA = value per conversion = {breakeven_cpa:,.2f}")
    steps.append(f"Target CPA keeping {a.profit_share:.0%} of the value as profit = {target_cpa:,.2f}")
    inc = a.incrementality
    if inc < 1:
        steps.append(f"Only {inc:.0%} of reported conversions are incremental: platform target CPA = {target_cpa:,.2f} x {inc:.0%} = {target_cpa * inc:,.2f}")
    out = {"command": "targets", "version": VERSION, "value_per_conversion": value,
           "breakeven_cpa": breakeven_cpa, "target_cpa": target_cpa,
           "platform_target_cpa": target_cpa * inc, "steps": steps}
    if a.order_value is not None:
        # ROAS on revenue: break-even when revenue x margin x LTV = cost
        be_roas = 1 / (a.margin * a.ltv_multiple)
        t_roas = be_roas / (1 - a.profit_share)
        out.update({"breakeven_roas": be_roas, "target_roas": t_roas, "platform_target_roas": t_roas / inc})
        steps.append(f"Break-even ROAS on revenue = 1 / (margin x LTV multiple) = {be_roas:.2f} ({be_roas:.0%})")
        steps.append(f"Target ROAS = {t_roas:.2f} ({t_roas:.0%}); with incrementality {inc:.0%}: {t_roas / inc:.2f} ({t_roas / inc:.0%})")
    out["notes"] = [
        "These are ceilings for the marginal conversion. The average CPA will be lower than the marginal one; set the target from the economics, then watch volume.",
        "If conversion values in Google Ads already include margin or LTV, do not apply them twice.",
        "Incrementality below 100% is common for brand and retargeting; measure it rather than guess (Fiera Incrementality plugin).",
    ]
    return out


def md_targets(o):
    L = ["# Targets from unit economics", ""] + [f"- {s}" for s in o["steps"]]
    L += ["", "## Notes", ""] + [f"- {x}" for x in o["notes"]]
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------
# RSA check
# --------------------------------------------------------------------------

LIMITS = {"headline": 30, "description": 90, "path": 15}
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF\U00002700-\U000027BF\U0001F000-\U0001F2FF☀-⛿]")


def _display_len(s):
    """Google counts most characters as 1 and double-width (CJK, full-width) as 2."""
    return sum(2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1 for ch in s)


def _dki_render_len(s):
    # {KeyWord:default text} counts as the default text
    return _display_len(re.sub(r"\{(?:keyword|KeyWord|Keyword|KEYWORD|KEYword|KeyWORD):([^}]*)\}", r"\1", s))


def cmd_rsa(a):
    items = []
    if a.data:
        df = pd.read_csv(a.data) if a.data.endswith(".csv") else pd.read_excel(a.data)
        cols = {_norm(c): c for c in df.columns}
        tcol = cols.get("type") or cols.get("asset type") or cols.get("tipo")
        xcol = cols.get("text") or cols.get("asset") or cols.get("texto")
        pcol = cols.get("pin") or cols.get("pinned") or cols.get("position")
        if not (tcol and xcol):
            raise SystemExit("CSV needs columns 'type' (headline, description, path) and 'text', optional 'pin'.")
        for _, r in df.iterrows():
            items.append({"type": _norm(r[tcol]).rstrip("s"), "text": str(r[xcol]),
                          "pin": None if not pcol or pd.isna(r[pcol]) else str(r[pcol])})
    for h in a.headline or []:
        items.append({"type": "headline", "text": h, "pin": None})
    for d in a.description or []:
        items.append({"type": "description", "text": d, "pin": None})
    for p in a.path or []:
        items.append({"type": "path", "text": p, "pin": None})
    comp = [c.lower() for c in (a.competitors or [])]
    allowed_caps = set(a.allow_caps or [])
    page = None
    if a.landing:
        page = _norm(Path(a.landing).read_text(errors="ignore"))
        page_nums = set(re.findall(r"\d+(?:[.,]\d+)?", page.replace(",", "")))
    issues, rows = [], []
    for i, it in enumerate(items):
        t, kind = it["text"].strip(), it["type"]
        lim = LIMITS.get(kind)
        ln = _dki_render_len(t)
        row = {"type": kind, "text": t, "length": ln, "limit": lim, "pin": it["pin"]}
        rows.append(row)
        if lim and ln > lim:
            issues.append({"severity": "error", "text": t, "issue": f"{ln} characters, limit {lim}"})
        if lim and kind != "path" and ln < 0.6 * lim:
            issues.append({"severity": "info", "text": t, "issue": f"Uses {ln} of {lim} characters; room for a benefit, number or call to action"})
        if re.search(r"([!?.,])\1", t):
            issues.append({"severity": "error", "text": t, "issue": "Repeated punctuation is not allowed by Google's editorial policy"})
        if EMOJI_RE.search(t):
            issues.append({"severity": "error", "text": t, "issue": "Emoji are not allowed in ad text"})
        if kind == "headline" and "!" in t:
            issues.append({"severity": "warning", "text": t, "issue": "Exclamation marks in headlines are often disapproved; keep them for descriptions"})
        if re.search(r"\b[a-z]*[@$0-9][a-z]+[@$][a-z]*\b", t.lower()) or re.search(r"\b(?:[A-Za-z]\.){3,}", t):
            issues.append({"severity": "error", "text": t, "issue": "Symbols or dots inside words read as distorted text"})
        caps = [w for w in re.findall(r"\b[A-ZÁÉÍÓÚÑ]{4,}\b", t) if w not in allowed_caps]
        if caps:
            issues.append({"severity": "warning", "text": t, "issue": f"Words in capitals ({', '.join(caps)}) can be disapproved as excessive capitalization unless they are brand names or acronyms"})
        if re.search(r"(\+?\d[\d\s().-]{7,}\d)", t) and kind != "path":
            issues.append({"severity": "warning", "text": t, "issue": "Phone numbers belong in a call asset, not in ad text"})
        if page is not None and kind != "path":
            nums = [x for x in re.findall(r"\d+(?:[.,]\d+)?", t.replace(",", "")) if x not in page_nums]
            if nums:
                issues.append({"severity": "error", "text": t, "issue": f"Number(s) {', '.join(nums)} not found on the landing page: possible invented claim"})
        for c in comp:
            if c and re.search(rf"\b{re.escape(c)}\b", t.lower()):
                issues.append({"severity": "error", "text": t, "issue": f"Mentions competitor '{c}'"})
        if re.search(r"\{(?!keyword:|KeyWord:|Keyword:|KEYWORD:|KEYword:|KeyWORD:)[^}]*\}", t):
            issues.append({"severity": "error", "text": t, "issue": "Malformed insertion syntax; use {KeyWord:default text}"})
    heads = [r for r in rows if r["type"] == "headline"]
    descs = [r for r in rows if r["type"] == "description"]
    paths = [r for r in rows if r["type"] == "path"]
    if heads and not 3 <= len(heads) <= 15:
        issues.append({"severity": "error", "text": "", "issue": f"{len(heads)} headlines; RSAs take 3 to 15"})
    if descs and not 2 <= len(descs) <= 4:
        issues.append({"severity": "error", "text": "", "issue": f"{len(descs)} descriptions; RSAs take 2 to 4"})
    if len(paths) > 2:
        issues.append({"severity": "error", "text": "", "issue": "More than 2 paths"})
    # duplicates and near-duplicates
    def stem(w):
        for suf in ("ing", "es", "s"):
            if len(w) > 4 and w.endswith(suf):
                return w[: -len(suf)]
        return w

    def toks(s):
        return {stem(w) for w in _tokens(s)} - STOP
    for group in (heads, descs):
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                x, y = group[i]["text"], group[j]["text"]
                if _norm(x) == _norm(y):
                    issues.append({"severity": "error", "text": y, "issue": f"Duplicate of '{x}'"})
                    continue
                tx, ty = toks(x), toks(y)
                if tx and ty and len(tx & ty) / len(tx | ty) >= 0.75:
                    issues.append({"severity": "warning", "text": y, "issue": f"Near-duplicate of '{x}': adds no new angle"})
    # capitalization consistency among headlines
    def style(s):
        ws = [w for w in re.findall(r"[A-Za-zÀ-ÿ]+", s) if len(w) > 3]
        if not ws:
            return None
        tc = sum(w[0].isupper() for w in ws) / len(ws)
        return "title" if tc > 0.7 else "sentence" if tc < 0.4 else "mixed"
    styles = [style(h["text"]) for h in heads if style(h["text"])]
    if len(set(styles)) > 1:
        issues.append({"severity": "info", "text": "", "issue": f"Headline capitalization is mixed ({', '.join(sorted(set(styles)))}). Pick one style for the ad"})
    pinned = [r for r in rows if r["pin"]]
    if pinned:
        issues.append({"severity": "info", "text": "", "issue": f"{len(pinned)} pinned assets. Pinning reduces the combinations tested; keep it for text that must appear for legal reasons"})
    sev = {"error": 0, "warning": 1, "info": 2}
    issues.sort(key=lambda x: sev[x["severity"]])
    return {"command": "rsa", "version": VERSION, "assets": rows,
            "counts": {"headlines": len(heads), "descriptions": len(descs), "paths": len(paths)},
            "issues": issues,
            "ok": not any(i["severity"] == "error" for i in issues),
            "notes": ["Lengths count {KeyWord:default} as its default text and double-width characters as 2.",
                      "Editorial checks catch common disapprovals; final approval is Google's policy review."]}


def md_rsa(o):
    L = ["# RSA check", "", f"- Headlines {o['counts']['headlines']}, descriptions {o['counts']['descriptions']}, paths {o['counts']['paths']}",
         f"- Result: {'no errors' if o['ok'] else 'errors to fix'}", "",
         "| Type | Length | Text |", "|---|---:|---|"]
    for r in o["assets"]:
        L.append(f"| {r['type']} | {r['length']}/{r['limit']} | {_c(r['text'])} |")
    L += ["", "## Issues", ""] + [f"- **{i['severity']}**: {i['issue']}" + (f" ({i['text']})" if i["text"] else "") for i in o["issues"]]
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------
# Inspect
# --------------------------------------------------------------------------

def cmd_inspect(a):
    df, meta = load_report(a.data, json.loads(a.map) if a.map else None)
    cols = set(df.columns)
    kind = ("search_terms" if "search_term" in cols else
            "keywords" if "keyword" in cols else
            "ad_groups" if "ad_group" in cols else
            "campaigns" if "campaign" in cols else "account")
    tcol = next((c for c in ["date", "week", "month"] if c in cols), None)
    out = {"command": "inspect", "version": VERSION, "report": kind, "rows": int(len(df)),
           "columns": meta["columns"], "decimal_separator": meta["decimal"],
           "time_column": tcol, "notes": meta["notes"]}
    if tcol:
        out["date_range"] = [str(df[tcol].min().date()), str(df[tcol].max().date())]
    if "campaign" in cols:
        seg = df.apply(segment_of, axis=1, args=(a.brand_regex, a.pmax_regex))
        out["segments"] = seg.value_counts().to_dict()
        out["campaigns_by_segment"] = {s: sorted(df.loc[seg == s, "campaign"].astype(str).unique().tolist())[:15]
                                       for s in seg.unique()}
    for c in ["cost", "conversions", "clicks", "impressions", "conv_value"]:
        if c in cols:
            out[f"total_{c}"] = float(df[c].sum())
    missing = [c for c in ["impressions", "clicks", "cost", "conversions"] if c not in cols]
    if missing:
        out["missing_core_columns"] = missing
    return out


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------

def _c(x):
    """Cell text safe for a markdown table."""
    return str(x).replace("|", "\\|").replace("\n", " ")


def _p(x, d=1):
    return "n/a" if x is None or (isinstance(x, float) and not np.isfinite(x)) else f"{100 * x:+.{d}f}%"


def _n(x, d=2):
    return "n/a" if x is None or (isinstance(x, float) and not np.isfinite(x)) else f"{x:,.{d}f}"


def md_triage(o):
    L = [f"# Performance change: {o['periods']['before'][0]} to {o['periods']['before'][1]} vs {o['periods']['after'][0]} to {o['periods']['after'][1]}", ""]
    if o["mix"]:
        m = o["mix"]
        L += [f"- Account CPA change: {_p(m['account_cpa_change'])}",
              f"- From CPA changes inside segments: {_p(m['within_segments'])}",
              f"- From the mix of conversions between segments: {_p(m['mix_shift'])}", ""]
    L += ["## Values", "", "| Segment | Period | Cost/day | Conv./day | CPA | CPC | CVR | CTR | Impr. share |",
          "|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    da, db = o["days"]["before"], o["days"]["after"]
    for s_ in o["segments"]:
        for lab, r, dd in (("before", s_["before"], da), ("after", s_["after"], db)):
            L.append(f"| {_c(s_['segment'])} | {lab} | {_n(r.get('cost', 0) / dd)} | {_n(r.get('conversions', 0) / dd, 1)} | {_n(r.get('cpa'))} | {_n(r.get('cpc'))} | {_n(100 * r['cvr'] if r.get('cvr') is not None else None, 2)}% | {_n(100 * r['ctr'] if r.get('ctr') is not None else None, 2)}% | {_n(100 * r['search_is'] if r.get('search_is') is not None else None, 1)}% |")
    L += ["", "## Changes", ""]
    L += ["| Segment | Cost share | Conv./day | CPA | CPC | CVR | CTR | Eligible impr./day | Impr. share | Shift starts |",
          "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    for s in o["segments"]:
        c = s["change"]
        L.append(f"| {_c(s['segment'])} | {_n(100 * s['share_of_cost_after'] if s['share_of_cost_after'] is not None else None, 0)}% | {_p(c.get('conversions'))} | {_p(c.get('cpa'))} | {_p(c.get('cpc'))} | {_p(c.get('cvr'))} | {_p(c.get('ctr'))} | {_p(c.get('eligible_impressions'))} | {_p(c.get('search_is'))} | {s.get('break_date') or 'none found'} |")
    L.append("")
    for s in o["segments"]:
        if s["verdict"]:
            L += [f"## {s['segment']}", ""] + [f"- {v}" for v in s["verdict"]] + [""]
    if o["warnings"]:
        L += ["## Warnings", ""] + [f"- {w}" for w in o["warnings"]]
    return "\n".join(L) + "\n"


def md_ngrams(o):
    L = ["# Search terms n-grams", "",
         f"- Rows: {o['rows']}; cost {_n(o['cost_total'])}; conversions {_n(o['conversions_total'], 1)}; CPA {_n(o['account_cpa'])}",
         f"- Cost on search terms with zero conversions: {_n(100 * o['wasted_cost_share_zero_conv_terms'] if o['wasted_cost_share_zero_conv_terms'] is not None else None, 1)}%",
         "", "## Negative candidates (no conversions)", "",
         "| N-gram | Terms | Clicks | Cost | Intent hint | Conflicts with converting |", "|---|---:|---:|---:|---|---|"]
    for r in o["negative_candidates_zero_conv"]:
        L.append(f"| {_c(r['ngram'])} | {r['terms']} | {r['clicks']:.0f} | {_n(r['cost'])} | {_c(r.get('intent_hint') or '')} | {'yes' if r['conflicts_with_converting'] else 'no'} |")
    L += ["", "## High CPA n-grams", "", "| N-gram | Conv. | CPA | x target | Conflicts |", "|---|---:|---:|---:|---|"]
    for r in o["high_cpa_ngrams"]:
        L.append(f"| {r['ngram']} | {r['conversions']:.1f} | {_n(r['cpa'])} | {_n(r['cpa_vs_target'], 1)} | {'yes' if r['conflicts_with_converting'] else 'no'} |")
    L += ["", "## Protect (converting at or below target)", "", "| N-gram | Conv. | CPA |", "|---|---:|---:|"]
    for r in o["protect"]:
        L.append(f"| {r['ngram']} | {r['conversions']:.1f} | {_n(r['cpa'])} |")
    cv = o.get("negatives_coverage")
    if cv:
        L += ["", "## Proposed negatives (phrase match)", "",
              f"- Negatives: {', '.join(cv['negatives'])}",
              f"- Zero-conversion cost blocked: {_n(cv['zero_conv_cost_blocked'])} of {_n(cv['zero_conv_cost_total'])} ({_n(100 * (cv['share_of_zero_conv_cost_covered'] or 0), 0)}%)",
              f"- Converting search terms blocked: {cv['converting_terms_blocked']} ({_n(cv['conversions_blocked'], 1)} conversions)"]
        if cv["blocked_converting_examples"]:
            L.append(f"- Examples: {', '.join(cv['blocked_converting_examples'])}")
    L += ["", "## Notes", ""] + [f"- {x}" for x in o["notes"] + o["warnings"]]
    return "\n".join(L) + "\n"


def _write(o, out, md):
    if not out:
        return
    p = Path(out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.with_suffix(".json").write_text(json.dumps(o, indent=2, default=lambda x: None if isinstance(x, float) and not np.isfinite(x) else float(x)))
    if md:
        p.with_suffix(".md").write_text(md(o))


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return o


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("--data", required=True)
        sp.add_argument("--map", help='JSON of extra header -> field, e.g. {"Kosten": "cost"}')
        sp.add_argument("--brand-regex", default=BRAND_DEFAULT,
                        help="Regex on campaign name for brand campaigns")
        sp.add_argument("--pmax-regex", default=r"\bpmax\b|performance max")
        sp.add_argument("--out")

    sp = sub.add_parser("inspect"); common(sp)
    sp = sub.add_parser("triage"); common(sp)
    sp.add_argument("--a", required=True, help="Before period start:end")
    sp.add_argument("--b", required=True, help="After period start:end")
    sp.add_argument("--min-conv", type=float, default=30)
    sp = sub.add_parser("ngrams"); common(sp)
    sp.add_argument("--n", type=int, nargs="*", default=[1, 2, 3])
    sp.add_argument("--target-cpa", type=float)
    sp.add_argument("--waste-multiple", type=float, default=1.0,
                    help="Zero-conversion n-grams need at least this x target CPA in cost")
    sp.add_argument("--bad-ratio", type=float, default=2.0)
    sp.add_argument("--min-clicks", type=int, default=10)
    sp.add_argument("--protect-conv", type=float, default=2)
    sp.add_argument("--top", type=int, default=25)
    sp.add_argument("--include-brand", action="store_true")
    sp.add_argument("--negatives", nargs="*", help="Proposed negatives (phrase match) to measure coverage and collateral")

    sp = sub.add_parser("auction"); common(sp)
    sp.add_argument("--campaign", help="Substring of the campaign name to keep")
    sp.add_argument("--window", type=int, default=4, help="Periods in 'recent' and 'before'")
    sp.add_argument("--top", type=int, default=15)
    sp = sub.add_parser("changes"); common(sp)
    sp.add_argument("--big-change", type=float, default=0.2)
    sp.add_argument("--learning-days", type=int, default=14)
    sp.add_argument("--top", type=int, default=25)
    sp = sub.add_parser("qs"); common(sp)
    sp.add_argument("--low", type=int, default=5)
    sp.add_argument("--top", type=int, default=20)
    sp = sub.add_parser("pacing"); common(sp)
    sp.add_argument("--budget", type=float, required=True, help="Monthly budget")
    sp.add_argument("--surcharge", type=float, default=0.0, help="Regulatory surcharge rate, e.g. 0.03")
    sp.add_argument("--today", help="YYYY-MM-DD; default today")
    sp.add_argument("--campaign")
    sp = sub.add_parser("targets")
    sp.add_argument("--order-value", type=float)
    sp.add_argument("--deal-value", type=float)
    sp.add_argument("--lead-to-opp", type=float, default=1.0)
    sp.add_argument("--opp-to-win", type=float, default=1.0)
    sp.add_argument("--margin", type=float, required=True, help="Gross margin as a share, e.g. 0.4")
    sp.add_argument("--ltv-multiple", type=float, default=1.0, help="Lifetime value / first order value")
    sp.add_argument("--profit-share", type=float, default=0.3, help="Share of value kept as profit")
    sp.add_argument("--incrementality", type=float, default=1.0, help="Share of reported conversions that are incremental")
    sp.add_argument("--out")
    sp = sub.add_parser("rsa")
    sp.add_argument("--data", help="CSV with type,text[,pin]")
    sp.add_argument("--headline", nargs="*")
    sp.add_argument("--description", nargs="*")
    sp.add_argument("--path", nargs="*")
    sp.add_argument("--competitors", nargs="*")
    sp.add_argument("--landing", help="Text file with the landing page copy, to check numbers in the ads")
    sp.add_argument("--allow-caps", nargs="*", help="Words allowed in capitals (brand names, acronyms)")
    sp.add_argument("--out")

    a = ap.parse_args(argv)
    fn = {"inspect": (cmd_inspect, None), "triage": (cmd_triage, md_triage),
          "ngrams": (cmd_ngrams, md_ngrams), "auction": (cmd_auction, md_auction),
          "changes": (cmd_changes, md_changes), "qs": (cmd_qs, md_qs),
          "pacing": (cmd_pacing, md_pacing), "targets": (cmd_targets, md_targets),
          "rsa": (cmd_rsa, md_rsa)}[a.cmd]
    o = _clean(fn[0](a))
    _write(o, a.out, fn[1])
    json.dump(o, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
