#!/usr/bin/env python3
"""Geo experiment toolkit: profile a panel, design a test, size it, read it.

Dependencies: numpy, pandas, scipy. matplotlib is optional (charts only).

Input is a long-format panel, one row per geo and period:

    date,geo,kpi[,spend][,value]

Commands
    profile   Check a panel and say what it supports.
    quick     Size a test from summary numbers when there is no panel.
    design    Search treatment groups, estimate MDE, cost and duration.
    readout   Estimate the effect of a test that has run.

Every command prints a JSON document to stdout and, with --out, writes it
plus a Markdown summary (and charts for readout) next to it.

Methods
    TBR  Time-based regression (Kerman, Wang, Vaver 2017): the treated
         aggregate is regressed on the control aggregate in the pre-period.
    SC   Synthetic control with an intercept and non-negative weights
         (Abadie et al. 2010; demeaned variant as in Doudchenko and Imbens
         2016), ridge-penalised, penalty chosen by rolling-origin validation.
    Inference
         In-time placebos: the same estimator run on pseudo-test windows of
         the same length inside the pre-period. Their cumulative errors give
         an empirical null distribution (in the spirit of Chernozhukov,
         Wuthrich and Zhu 2021). This is the primary interval because it
         absorbs autocorrelation and model misfit that the parametric TBR
         interval ignores.
         In-space placebos: control geos reassigned as fake treated groups
         under the same assignment rule (as in Abadie et al. 2010 and
         Meridian GeoX). Reported as a permutation p-value.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import nnls

VERSION = "1.0.0"

DATE_ALIASES = ["date", "day", "ds", "week", "period", "fecha"]
GEO_ALIASES = ["geo", "location", "region", "dma", "market", "province",
               "state", "city", "country", "zip", "postcode", "area", "provincia"]
KPI_ALIASES = ["kpi", "conversions", "orders", "leads", "signups", "sales",
               "purchases", "transactions", "y", "outcome", "conversiones"]
SPEND_ALIASES = ["spend", "cost", "media_spend", "ad_spend", "coste", "gasto"]
VALUE_ALIASES = ["value", "revenue", "conversion_value", "gmv", "ingresos"]


# --------------------------------------------------------------------------
# Loading and validation
# --------------------------------------------------------------------------

def _pick(columns, explicit, aliases, required, label):
    if explicit:
        if explicit not in columns:
            raise SystemExit(f"Column '{explicit}' for {label} not found. Columns: {list(columns)}")
        return explicit
    lower = {c.lower().strip(): c for c in columns}
    for a in aliases:
        if a in lower:
            return lower[a]
    if required:
        raise SystemExit(
            f"Could not find a {label} column. Pass --{label}-col. Columns: {list(columns)}")
    return None


@dataclass
class Panel:
    kpi: pd.DataFrame            # index=date, columns=geo
    spend: pd.DataFrame | None
    value: pd.DataFrame | None
    freq: str                    # "D" or "W"
    notes: list = field(default_factory=list)

    @property
    def geos(self):
        return list(self.kpi.columns)

    @property
    def dates(self):
        return self.kpi.index


def load_panel(path, date_col=None, geo_col=None, kpi_col=None,
               spend_col=None, value_col=None, exclude=None) -> Panel:
    df = pd.read_csv(path)
    if df.empty:
        raise SystemExit("The file is empty.")
    d = _pick(df.columns, date_col, DATE_ALIASES, True, "date")
    g = _pick(df.columns, geo_col, GEO_ALIASES, True, "geo")
    k = _pick(df.columns, kpi_col, KPI_ALIASES, True, "kpi")
    s = _pick(df.columns, spend_col, SPEND_ALIASES, False, "spend")
    v = _pick(df.columns, value_col, VALUE_ALIASES, False, "value")
    notes = []
    df = df.copy()
    df[d] = pd.to_datetime(df[d], errors="coerce")
    bad = int(df[d].isna().sum())
    if bad:
        notes.append(f"{bad} rows with unparseable dates were dropped.")
        df = df[df[d].notna()]
    df[g] = df[g].astype(str).str.strip()
    if exclude:
        df = df[~df[g].isin(exclude)]
    for c in [k, s, v]:
        if c:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    dup = int(df.duplicated([d, g]).sum())
    if dup:
        notes.append(f"{dup} duplicated date-geo rows were summed.")

    def pivot(col):
        if not col:
            return None
        p = df.pivot_table(index=d, columns=g, values=col, aggfunc="sum")
        return p.sort_index()

    kp = pivot(k)
    freq = _infer_freq(kp.index)
    full = pd.date_range(kp.index.min(), kp.index.max(),
                         freq="D" if freq == "D" else "7D")
    missing = len(full) - len(kp.index)
    if missing > 0:
        notes.append(f"{missing} periods had no rows for any geo and were filled with 0.")
    kp = kp.reindex(full)
    n_nan = int(kp.isna().sum().sum())
    if n_nan:
        notes.append(f"{n_nan} geo-period cells were missing and were filled with 0.")
    kp = kp.fillna(0.0)
    sp = pivot(s)
    vp = pivot(v)
    if sp is not None:
        sp = sp.reindex(full).fillna(0.0)[kp.columns]
    if vp is not None:
        vp = vp.reindex(full).fillna(0.0)[kp.columns]
    neg = int((kp < 0).sum().sum())
    if neg:
        notes.append(f"{neg} negative KPI values found. Check refunds or corrections.")
    return Panel(kpi=kp, spend=sp, value=vp, freq=freq, notes=notes)


def _infer_freq(idx) -> str:
    if len(idx) < 3:
        return "D"
    step = pd.Series(idx).diff().dropna().dt.days.median()
    return "W" if step >= 6 else "D"


def _period_label(freq):
    return "days" if freq == "D" else "weeks"


def _to_periods(n_days, freq):
    return int(n_days) if freq == "D" else max(1, int(round(n_days / 7)))


# --------------------------------------------------------------------------
# Estimators
# --------------------------------------------------------------------------

def tbr_fit(y, x):
    """OLS of y on [1, x] with b >= 0. Returns (a, b, sigma, T, xbar, sxx)."""
    T = len(y)
    xbar = float(np.mean(x))
    sxx = float(np.sum((x - xbar) ** 2))
    if sxx <= 0:
        b = 0.0
    else:
        b = float(np.sum((x - xbar) * (y - np.mean(y))) / sxx)
    b = max(b, 0.0)  # treated and control move together; as in Meridian GeoX
    a = float(np.mean(y) - b * xbar)
    resid = y - (a + b * x)
    sigma = float(np.sqrt(np.sum(resid ** 2) / max(T - 2, 1)))
    return a, b, sigma, T, xbar, sxx


def tbr_predict(fit, x_new):
    a, b, *_ = fit
    return a + b * np.asarray(x_new)


def tbr_cum_se(fit, x_new):
    """SE of the cumulative prediction error over the test window
    (Kerman et al. 2017, eq. for the cumulative effect, iid errors)."""
    a, b, sigma, T, xbar, sxx = fit
    n = len(x_new)
    xt = float(np.mean(x_new))
    var_mean = (1.0 / T) + ((xt - xbar) ** 2 / sxx if sxx > 0 else 0.0)
    var = sigma ** 2 * (n + n ** 2 * var_mean)
    return float(np.sqrt(var)), T - 2


def _nnls_ridge(X, y, lam):
    """min ||y - Xw||^2 + lam ||w||^2, w >= 0. X, y already centred."""
    K = X.shape[1]
    Xa = np.vstack([X, math.sqrt(lam) * np.eye(K)])
    ya = np.concatenate([y, np.zeros(K)])
    w, _ = nnls(Xa, ya)
    return w


class SyntheticControl:
    """Intercept + non-negative weights, ridge, columns scaled to unit RMS."""

    LAMBDAS = [1e-3, 1e-2, 1e-1, 1.0, 10.0]

    def __init__(self, lam=None):
        self.lam = lam

    def fit(self, y, X):
        y = np.asarray(y, float)
        X = np.asarray(X, float)
        self.scale = np.sqrt(np.mean(X ** 2, axis=0))
        self.scale[self.scale == 0] = 1.0
        Xs = X / self.scale
        if self.lam is None:
            self.lam = self._choose_lambda(y, Xs)
        self._fit_scaled(y, Xs, self.lam)
        return self

    def _fit_scaled(self, y, Xs, lam):
        self.xm = Xs.mean(axis=0)
        self.ym = y.mean()
        T = len(y)
        self.ws = _nnls_ridge(Xs - self.xm, y - self.ym, lam * T)
        self.intercept = self.ym - self.xm @ self.ws
        self.weights = self.ws / self.scale

    def _choose_lambda(self, y, Xs):
        T = len(y)
        h = max(7, T // 6)
        origins = [T - h * i for i in range(1, 4) if T - h * i >= max(14, T // 2)]
        if not origins:
            return 0.1
        best, best_err = 0.1, np.inf
        for lam in self.LAMBDAS:
            err = 0.0
            for o in origins:
                self._fit_scaled(y[:o], Xs[:o], lam)
                pred = self.intercept + Xs[o:o + h] @ self.ws
                err += (np.sum(y[o:o + h] - pred)) ** 2
            if err < best_err:
                best, best_err = lam, err
        return best

    def predict(self, X):
        return self.intercept + np.asarray(X, float) @ self.weights


def _aggregate(panel_df, geos):
    return panel_df[geos].sum(axis=1).to_numpy(float)


MAX_SC_DONORS = 50


def _screen_donors(y, X, controls, k=MAX_SC_DONORS):
    """Keep the k donors most correlated with the treated series in the
    pre-period. Large donor pools slow the fit and add little."""
    if len(controls) <= k:
        return controls, X
    yc = y - y.mean()
    Xc = X - X.mean(axis=0)
    den = np.sqrt((Xc ** 2).sum(axis=0) * (yc ** 2).sum())
    corr = np.where(den > 0, (Xc * yc[:, None]).sum(axis=0) / np.where(den > 0, den, 1), -1)
    keep = np.argsort(-corr)[:k]
    return [controls[i] for i in keep], keep


def counterfactual(method, kpi, treated, controls, pre_mask, post_mask, lam=None):
    """Fit on pre, return (y_post, yhat_post, yhat_pre, y_pre, extra)."""
    y = _aggregate(kpi, treated)
    if method == "tbr":
        x = _aggregate(kpi, controls)
        fit = tbr_fit(y[pre_mask], x[pre_mask])
        return (y[post_mask], tbr_predict(fit, x[post_mask]),
                tbr_predict(fit, x[pre_mask]), y[pre_mask],
                {"fit": fit, "x_post": x[post_mask]})
    if method == "sc":
        X = kpi[controls].to_numpy(float)
        if len(controls) > MAX_SC_DONORS:
            controls, keep = _screen_donors(y[pre_mask], X[pre_mask], controls)
            X = X[:, keep]
        sc = SyntheticControl(lam=lam).fit(y[pre_mask], X[pre_mask])
        weights = {g: float(w) for g, w in zip(controls, sc.weights) if w > 1e-9}
        return (y[post_mask], sc.predict(X[post_mask]), sc.predict(X[pre_mask]),
                y[pre_mask], {"weights": weights, "lambda": sc.lam})
    raise ValueError(method)


def fit_quality(y, yhat):
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    mape = float(np.mean(np.abs(y - yhat)) / max(np.mean(np.abs(y)), 1e-9))
    return {"r2": r2, "wape": mape}


# --------------------------------------------------------------------------
# In-time placebos
# --------------------------------------------------------------------------

def in_time_placebos(method, kpi, treated, controls, pre_len, n, min_train=None,
                     step=None, lam=None):
    """Cumulative relative errors of the estimator on pseudo-test windows of
    length n inside the first pre_len periods. Returns list of dicts."""
    if min_train is None:
        min_train = max(2 * n, 28 if n >= 7 else 8)
    if step is None:
        step = max(1, n // 3)
    out = []
    idx = np.arange(len(kpi))
    start = min_train
    while start + n <= pre_len:
        pre_mask = idx < start
        post_mask = (idx >= start) & (idx < start + n)
        y_post, yhat_post, *_ = counterfactual(method, kpi, treated, controls,
                                                pre_mask, post_mask, lam=lam)
        base = float(np.sum(yhat_post))
        err = float(np.sum(y_post) - base)
        out.append({"start": int(start), "err": err,
                    "rel": err / base if base > 0 else float("nan")})
        start += step
    return out


def ar1_cum_se(resid, n, extra_var=0.0):
    """SE of a sum of n future errors when residuals follow AR(1). Used when
    the pre-period is too short for in-time placebos. extra_var adds the
    parameter uncertainty of the fitted counterfactual."""
    r = np.asarray(resid, float)
    if len(r) < 8:
        return None, None
    sigma = float(np.std(r, ddof=1))
    phi = float(np.corrcoef(r[:-1], r[1:])[0, 1]) if np.std(r[:-1]) > 0 else 0.0
    phi = min(max(phi, 0.0), 0.95)
    # exact variance of the sum of n AR(1) terms with stationary variance sigma^2
    k = np.arange(1, n)
    var = sigma ** 2 * (n + 2 * np.sum((n - k) * phi ** k))
    return float(np.sqrt(var + extra_var)), phi


def empirical_interval(rels, conf):
    """Interval for the relative error, from placebo windows. Uses the
    t-distribution on the RMS when there are few windows, else quantiles."""
    r = np.asarray([v for v in rels if np.isfinite(v)])
    if len(r) < 4:
        return None
    rms = float(np.sqrt(np.mean(r ** 2)))
    bias = float(np.mean(r))
    alpha = 1 - conf
    if len(r) >= 40:
        lo, hi = np.quantile(r, [alpha / 2, 1 - alpha / 2])
        return {"lo": float(lo), "hi": float(hi), "rms": rms, "bias": bias,
                "n": int(len(r)), "kind": "quantile"}
    t = stats.t.ppf(1 - alpha / 2, df=len(r) - 1)
    return {"lo": -t * rms, "hi": t * rms, "rms": rms, "bias": bias,
            "n": int(len(r)), "kind": "t_rms"}


# --------------------------------------------------------------------------
# Assignment
# --------------------------------------------------------------------------

def stratified_draw(geos_sorted, n_treat, rng):
    """Sort-and-stratify: split geos ordered by volume into n_treat strata of
    near-equal size and draw one geo at random from each stratum."""
    strata = np.array_split(np.array(geos_sorted, dtype=object), n_treat)
    return [str(rng.choice(s)) for s in strata if len(s)]


def _volume_order(kpi, pre_mask, geos):
    tot = kpi.loc[pre_mask, geos].sum().sort_values(ascending=False)
    return list(tot.index)


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------

def cmd_profile(a):
    p = load_panel(a.data, a.date_col, a.geo_col, a.kpi_col, a.spend_col,
                   a.value_col, a.exclude)
    kpi = p.kpi
    T = len(kpi)
    per = _period_label(p.freq)
    tot = kpi.sum().sort_values(ascending=False)
    share = (tot / tot.sum()).round(4)
    daily_mean = kpi.mean()
    cv = (kpi.std() / kpi.mean().replace(0, np.nan)).round(3)
    zero_share = (kpi == 0).mean().round(3)
    agg = kpi.sum(axis=1)
    warnings = list(p.notes)
    if p.freq == "D" and T < 56:
        warnings.append(f"Only {T} days of history. Aim for at least 8 weeks before the test, ideally a full year to cover seasonality.")
    if p.freq == "W" and T < 26:
        warnings.append(f"Only {T} weeks of history. Weekly panels need at least 26 weeks; daily data gives far better power.")
    if len(p.geos) < 10:
        warnings.append(f"Only {len(p.geos)} geos. Fewer than 10 geos makes in-space placebo inference weak; consider finer geos (cities, postcodes, DMAs).")
    top = share.iloc[0]
    if top > 0.35:
        warnings.append(f"'{share.index[0]}' holds {top:.0%} of the KPI. A geo that large is hard to treat or to replace with controls.")
    sparse = list(zero_share[zero_share > 0.3].index)
    if sparse:
        warnings.append(f"{len(sparse)} geos have zero KPI in more than 30% of {per}: {', '.join(map(str, sparse[:10]))}{'...' if len(sparse) > 10 else ''}. Consider merging them into larger units.")
    weekly = None
    if p.freq == "D" and T >= 28:
        dow = agg.groupby(agg.index.dayofweek).mean()
        weekly = float((dow.max() - dow.min()) / dow.mean()) if dow.mean() > 0 else None
    # Structural breaks: the largest jump in the 7-period rolling mean of the aggregate
    roll = agg.rolling(7 if p.freq == "D" else 4).mean()
    jumps = roll.pct_change(7 if p.freq == "D" else 4).abs()
    big = jumps[jumps > 0.4]
    if len(big):
        warnings.append(f"The total KPI moves more than 40% within a week around {big.index[0].date()}. Check for tracking changes, promotions or outages before using that period.")
    if p.spend is None:
        warnings.append("No spend column. The design cannot estimate the cost of the test and the readout cannot compute iCPA or iROAS.")
    out = {
        "command": "profile", "version": VERSION,
        "frequency": p.freq, "periods": T,
        "start": str(kpi.index.min().date()), "end": str(kpi.index.max().date()),
        "geos": len(p.geos), "kpi_total": float(tot.sum()),
        "kpi_per_period": float(agg.mean()),
        "has_spend": p.spend is not None, "has_value": p.value is not None,
        "weekly_pattern_amplitude": weekly,
        "geo_table": [
            {"geo": g, "share": float(share[g]), "mean_per_period": float(daily_mean[g]),
             "cv": None if pd.isna(cv[g]) else float(cv[g]),
             "zero_share": float(zero_share[g])}
            for g in tot.index],
        "warnings": warnings,
    }
    return out


def cmd_quick(a):
    """Closed-form sizing from summary numbers. Daily noise on the treated
    aggregate after the model is approximated by cv * baseline; AR(1)
    autocorrelation phi inflates the variance of the window sum."""
    z = stats.norm.ppf(1 - a.alpha / 2) + stats.norm.ppf(a.power)
    base = a.baseline_per_day
    sd = a.residual_cv * base
    rows = []
    for n in a.days:
        phi = a.autocorrelation
        infl = (1 + phi) / (1 - phi) if phi < 1 else float("inf")
        se_sum = sd * math.sqrt(n * infl)
        mde = z * se_sum / (base * n)
        rows.append({"days": n, "mde_pct": round(100 * mde, 2),
                     "baseline_in_window": round(base * n, 1)})
    return {"command": "quick", "version": VERSION, "alpha": a.alpha, "power": a.power,
            "inputs": {"baseline_per_day": base, "residual_cv": a.residual_cv,
                       "autocorrelation": a.autocorrelation},
            "rows": rows,
            "note": ("Rough sizing. residual_cv is the day-to-day noise of the treated group "
                     "after the control explains what it can; typical values are 0.05 to 0.15 for "
                     "large aggregates and 0.2 to 0.4 for small ones. Use the design command on "
                     "real data before committing budget.")}


def _design_eval(kpi, treated, controls, pre_len, n, method, alpha, z):
    """MDE for one treated group using in-time placebos. Windows are split:
    the older two thirds select, the most recent third validates."""
    pl = in_time_placebos(method, kpi, treated, controls, pre_len, n)
    rels = [w["rel"] for w in pl if np.isfinite(w["rel"])]
    if len(rels) < 6:
        return None
    k = max(2, len(rels) // 3)
    sel, val = rels[:-k], rels[-k:]
    rms_sel = float(np.sqrt(np.mean(np.square(sel))))
    rms_val = float(np.sqrt(np.mean(np.square(val))))
    rms_all = float(np.sqrt(np.mean(np.square(rels))))
    # Mirror the readout: its interval uses a t quantile on the placebo count,
    # and the chosen group's validation RMS is itself a noisy estimate. Plan on
    # the larger of validation and all-window RMS.
    z_eff = z - stats.norm.ppf(1 - alpha / 2) + stats.t.ppf(1 - alpha / 2, df=max(len(rels) - 1, 1))
    rms_plan = max(rms_val, rms_all)
    return {"rms_sel": rms_sel, "rms_val": rms_val, "rms_all": rms_all,
            "bias": float(np.mean(rels)), "windows": len(rels),
            "mde_sel": z_eff * rms_sel, "mde_val": z_eff * rms_plan, "mde": z_eff * rms_all}


def cmd_design(a):
    p = load_panel(a.data, a.date_col, a.geo_col, a.kpi_col, a.spend_col,
                   a.value_col, a.exclude)
    kpi = p.kpi
    T = len(kpi)
    n = _to_periods(a.test_days, p.freq)
    z = stats.norm.ppf(1 - a.alpha / 2) + stats.norm.ppf(a.power)
    geos = p.geos
    pre_mask = np.ones(T, bool)
    order = _volume_order(kpi, pre_mask, geos)
    total = float(kpi.sum().sum())
    rng = np.random.default_rng(a.seed)
    must = [g for g in (a.must_treat or []) if g in geos]
    never = set(a.never_treat or [])
    warnings = list(p.notes)
    if a.treated:
        candidates = [[g for g in a.treated if g in geos]]
        missing = set(a.treated) - set(geos)
        if missing:
            warnings.append(f"Treated geos not found in the data: {sorted(missing)}")
        mode = "fixed"
    else:
        mode = "stratified_random_search"
        n_treat = max(1, int(round(a.treated_share * len(geos))))
        pool = [g for g in order if g not in never and g not in must]
        candidates, seen = [], set()
        tries = 0
        while len(candidates) < a.draws and tries < a.draws * 20:
            tries += 1
            k = max(1, n_treat - len(must))
            draw = sorted(set(must + stratified_draw(pool, k, rng)))
            key = tuple(draw)
            if key in seen:
                continue
            seen.add(key)
            share = float(kpi[draw].sum().sum()) / total
            if not (a.treated_share * 0.6 <= share <= a.treated_share * 1.5):
                continue
            candidates.append(draw)
        if not candidates:
            raise SystemExit("No treated group met the share constraint. Lower --treated-share or relax --never-treat.")
    min_needed = max(3 * n, 28 if p.freq == "D" else 8) + 6 * max(1, n // 3) + n
    if T < min_needed:
        warnings.append(
            f"The panel has {T} {_period_label(p.freq)}; a {n}-{_period_label(p.freq)[:-1]} test needs about {min_needed} for a reliable MDE estimate. Results below rest on few placebo windows.")
    results = []
    for cand in candidates:
        controls = [g for g in geos if g not in cand]
        if not controls:
            continue
        ev = _design_eval(kpi, cand, controls, T, n, a.method, a.alpha, z)
        if ev is None:
            continue
        share = float(kpi[cand].sum().sum()) / total
        results.append({"treated": cand, "kpi_share": share, **ev})
    if not results:
        raise SystemExit("Not enough history to evaluate any design. Shorten --test-days or add history.")
    results.sort(key=lambda r: r["mde_sel"])
    best = results[0]
    # Duration curve for the chosen group
    controls = [g for g in geos if g not in best["treated"]]
    curve = []
    for d in a.curve_days:
        nn = _to_periods(d, p.freq)
        ev = _design_eval(kpi, best["treated"], controls, T, nn, a.method, a.alpha, z)
        if ev:
            curve.append({"test_days": d, "mde_pct": round(100 * ev["mde"], 2),
                          "windows": ev["windows"]})
    # Fit of the chosen group over the full pre-period
    idx = np.arange(T)
    fit_mask = idx < T
    y_post, yhat_post, yhat_pre, y_pre, extra = counterfactual(
        a.method, kpi, best["treated"], controls, fit_mask, fit_mask)
    quality = fit_quality(y_pre, yhat_pre)
    # Cost
    recent = kpi.iloc[-max(n, 28 if p.freq == "D" else 4):]
    base_per = float(recent[best["treated"]].sum(axis=1).mean())
    base_window = base_per * n
    cost = {"treated_kpi_per_period": round(base_per, 2),
            "treated_kpi_in_window": round(base_window, 1)}
    if p.spend is not None:
        sp_recent = p.spend.iloc[-max(n, 28 if p.freq == "D" else 4):]
        sp_per = float(sp_recent[best["treated"]].sum(axis=1).mean())
        tot_sp = float(sp_recent.sum(axis=1).mean())
        cost["treated_spend_per_period"] = round(sp_per, 2)
        cost["treated_spend_share"] = round(sp_per / tot_sp, 4) if tot_sp else None
        if a.type == "go_dark":
            cost["spend_withheld_in_window"] = round(sp_per * n, 2)
        elif a.type == "holdback":
            cost["spend_withheld_in_window"] = round(sp_per * n * a.intensity, 2)
        elif a.type == "heavy_up":
            cost["extra_spend_in_window"] = round(sp_per * n * a.intensity, 2)
    mde_v = best["mde_val"]
    scen = []
    for lift in a.scenarios:
        scen.append({"true_effect_pct": round(100 * lift, 1),
                     "kpi_change_in_window": round(lift * base_window, 1),
                     "detectable": lift >= mde_v})
    cost["scenarios"] = scen
    mdes = np.array([r["mde_val"] for r in results])
    out = {
        "command": "design", "version": VERSION, "mode": mode, "seed": a.seed,
        "method": a.method, "type": a.type, "frequency": p.freq,
        "test_periods": n, "alpha": a.alpha, "power": a.power,
        "geos": len(geos), "candidates_evaluated": len(results),
        "recommended": {
            "treated": best["treated"], "n_treated": len(best["treated"]),
            "kpi_share": round(best["kpi_share"], 4),
            "mde_pct_validation": round(100 * best["mde_val"], 2),
            "mde_pct_selection": round(100 * best["mde_sel"], 2),
            "mde_pct_all_windows": round(100 * best["mde"], 2),
            "placebo_windows": best["windows"],
            "placebo_bias_pct": round(100 * best["bias"], 2),
            "pre_fit": quality,
            "sc_weights": extra.get("weights"),
        },
        "alternatives": [
            {"treated": r["treated"], "kpi_share": round(r["kpi_share"], 4),
             "mde_pct_validation": round(100 * r["mde_val"], 2)}
            for r in results[1:6]],
        "mde_distribution_pct": {
            "p10": round(100 * float(np.quantile(mdes, 0.1)), 2),
            "median": round(100 * float(np.median(mdes)), 2),
            "p90": round(100 * float(np.quantile(mdes, 0.9)), 2)},
        "duration_curve": curve,
        "cost": cost,
        "warnings": warnings,
        "notes": [
            "MDE is the smallest true effect, as a share of the treated group's KPI over the window, that the test detects with the stated power.",
            "The recommended group is chosen on older placebo windows; mde_pct_validation is measured on the most recent windows it was not chosen on. Plan on that number.",
            "The group is chosen by search over stratified random draws. The readout's in-space p-value treats the group as one random draw; the in-time interval does not depend on that assumption.",
        ],
    }
    if best["mde_val"] > 1.5 * best["mde_sel"]:
        warnings.append("Validation MDE is much worse than selection MDE: the group fits old data better than recent data. Recheck recent tracking or business changes, or prefer a larger treated share.")
    if quality["r2"] < 0.6:
        warnings.append(f"Pre-period fit R2 is {quality['r2']:.2f}. The controls explain little of the treated series; expect wide intervals.")
    return out


def _resolve_window(kpi, start, end):
    idx = kpi.index
    s = pd.Timestamp(start)
    e = pd.Timestamp(end) if end else idx.max()
    if s <= idx.min():
        raise SystemExit("The test start is at or before the first date: there is no pre-period.")
    pre = idx < s
    post = (idx >= s) & (idx <= e)
    if post.sum() == 0:
        raise SystemExit("No data inside the test window.")
    return pre, post


def _in_space_placebos(method, kpi, treated, controls, pre, post, rng, draws, order,
                       lam=None):
    """Fake treated groups drawn from controls with the same size, using the
    same sort-and-stratify rule. Returns relative effects."""
    k = len(treated)
    if len(controls) - k < 2:
        return []
    ordered = [g for g in order if g in controls]
    rels, seen = [], set()
    n_possible = math.comb(len(controls), k)
    target = min(draws, n_possible)
    tries = 0
    while len(rels) < target and tries < target * 10:
        tries += 1
        fake = tuple(sorted(stratified_draw(ordered, k, rng)))
        if fake in seen:
            continue
        seen.add(fake)
        donors = [g for g in controls if g not in fake]
        y_post, yhat_post, *_ = counterfactual(method, kpi, list(fake), donors, pre, post,
                                               lam=lam)
        b = float(np.sum(yhat_post))
        if b > 0:
            rels.append((float(np.sum(y_post)) - b) / b)
    return rels


def cmd_readout(a):
    p = load_panel(a.data, a.date_col, a.geo_col, a.kpi_col, a.spend_col,
                   a.value_col, a.exclude)
    kpi = p.kpi
    treated = [g for g in a.treated if g in kpi.columns]
    missing = sorted(set(a.treated) - set(treated))
    if not treated:
        raise SystemExit("None of the treated geos are in the data.")
    exclude_ctrl = set(a.exclude_controls or [])
    controls = [g for g in kpi.columns if g not in treated and g not in exclude_ctrl]
    pre, post = _resolve_window(kpi, a.start, a.end)
    n = int(post.sum())
    pre_len = int(pre.sum())
    warnings = list(p.notes)
    if missing:
        warnings.append(f"Treated geos not found in the data: {missing}")
    # Cooldown periods (between end of treatment and end of measurement) are part
    # of the window when the user passes --end beyond the treatment end.
    conf = a.conf
    rng = np.random.default_rng(a.seed)
    order = _volume_order(kpi, pre, list(kpi.columns))
    results = {}
    for method in ["tbr", "sc"]:
        y_post, yhat_post, yhat_pre, y_pre, extra = counterfactual(
            method, kpi, treated, controls, pre, post)
        cf = float(np.sum(yhat_post))
        obs = float(np.sum(y_post))
        eff = obs - cf
        rel = eff / cf if cf > 0 else float("nan")
        lam = extra.get("lambda")
        pl = in_time_placebos(method, kpi, treated, controls, pre_len, n, lam=lam)
        emp = empirical_interval([w["rel"] for w in pl], conf)
        r = {"observed": obs, "counterfactual": cf, "effect": eff, "lift": rel,
             "pre_fit": fit_quality(y_pre, yhat_pre), "placebo_windows": len(pl)}
        if emp:
            # Effect interval: observed minus counterfactual*(1 + placebo error)
            lo_rel = (obs / (cf * (1 + emp["hi"]))) - 1
            hi_rel = (obs / (cf * (1 + emp["lo"]))) - 1
            r["interval_lift"] = [lo_rel, hi_rel]
            r["interval_effect"] = [obs - cf * (1 + emp["hi"]), obs - cf * (1 + emp["lo"])]
            r["placebo_rms_pct"] = 100 * emp["rms"]
            r["placebo_bias_pct"] = 100 * emp["bias"]
            r["interval_kind"] = emp["kind"]
            errs = np.array([w["rel"] for w in pl if np.isfinite(w["rel"])])
            r["p_in_time"] = float((1 + np.sum(np.abs(errs) >= abs(rel))) / (1 + len(errs)))
        # AR(1)-corrected parametric interval: reported always, primary when
        # there are too few placebo windows.
        extra_var = 0.0
        if method == "tbr":
            se_iid, _ = tbr_cum_se(extra["fit"], extra["x_post"])
            sig = extra["fit"][2]
            extra_var = max(se_iid ** 2 - sig ** 2 * n, 0.0)
        resid = y_pre - yhat_pre
        if method == "sc":
            # In-sample SC residuals understate noise: correct for the number of
            # active donors (degrees of freedom used by the fit).
            k_act = len(extra["weights"]) + 1
            resid = resid * math.sqrt(len(resid) / max(len(resid) - k_act, 1))
        se_ar, phi = ar1_cum_se(resid, n, extra_var)
        if se_ar:
            zc = stats.norm.ppf(1 - (1 - conf) / 2)
            r["ar1_interval_effect"] = [eff - zc * se_ar, eff + zc * se_ar]
            r["residual_autocorrelation"] = phi
            if not emp or emp["n"] < 10:
                # Short history: few placebo windows and in-sample residuals both
                # understate noise. Take the wider of the two intervals.
                half_ar = zc * se_ar
                half_emp = 0.0
                if emp:
                    half_emp = cf * max(abs(emp["lo"]), abs(emp["hi"]))
                half = max(half_ar, half_emp)
                r["interval_effect"] = [eff - half, eff + half]
                r["interval_lift"] = [v / cf for v in r["interval_effect"]] if cf > 0 else None
                r["interval_kind"] = "short_history_conservative"
                r["p_ar1"] = float(2 * (1 - stats.norm.cdf(abs(eff) / se_ar)))
        if method == "tbr":
            se, df = tbr_cum_se(extra["fit"], extra["x_post"])
            t = stats.t.ppf(1 - (1 - conf) / 2, df)
            r["parametric_interval_effect"] = [eff - t * se, eff + t * se]
            r["parametric_p"] = float(2 * (1 - stats.t.cdf(abs(eff) / se, df))) if se > 0 else None
        else:
            r["weights"] = extra["weights"]
        if a.in_space_draws > 0:
            draws = a.in_space_draws if method == "tbr" else min(a.in_space_draws, 100)
            sp = _in_space_placebos(method, kpi, treated, controls, pre, post, rng,
                                    draws, order, lam=lam)
            if len(sp) >= 10:
                sp = np.array(sp)
                r["p_in_space"] = float((1 + np.sum(np.abs(sp) >= abs(rel))) / (1 + len(sp)))
                r["in_space_placebos"] = int(len(sp))
            else:
                r["p_in_space"] = None
                r["in_space_placebos"] = int(len(sp))
        r["series"] = {"dates": [str(d.date()) for d in kpi.index[post]],
                       "observed": [float(v) for v in y_post],
                       "counterfactual": [float(v) for v in yhat_post]}
        r["pre_series"] = {"dates": [str(d.date()) for d in kpi.index[pre]],
                           "observed": [float(v) for v in y_pre],
                           "fitted": [float(v) for v in yhat_pre]}
        results[method] = r
    prim = results[a.method]
    # Spend and value
    money = {}
    if p.spend is not None:
        sp_t = p.spend[treated].sum(axis=1).to_numpy(float)
        sp_c = p.spend[controls].sum(axis=1).to_numpy(float)
        fit = tbr_fit(sp_t[pre], sp_c[pre])
        sp_cf = float(np.sum(tbr_predict(fit, sp_c[post])))
        sp_obs = float(np.sum(sp_t[post]))
        d_sp = sp_obs - sp_cf
        money["spend_observed"] = sp_obs
        money["spend_counterfactual"] = sp_cf
        money["spend_delta"] = d_sp
        if abs(d_sp) > 0 and prim["effect"] != 0:
            money["icpa"] = d_sp / prim["effect"]
            if "interval_effect" in prim:
                lo, hi = prim["interval_effect"]
                if lo * hi > 0:
                    money["icpa_interval"] = sorted([d_sp / lo, d_sp / hi])
                else:
                    money["icpa_interval"] = None
        pre_sp_share = float(sp_t[pre].sum() / max(sp_t[pre].sum() + sp_c[pre].sum(), 1e-9))
        if a.type in ("go_dark",) and sp_obs > 0.1 * max(sp_cf, 1e-9):
            warnings.append(f"Spend in treated geos during the test is {sp_obs:,.0f}, {sp_obs / max(sp_cf, 1e-9):.0%} of expected. A go-dark should be near zero: check geo targeting (Presence only) and other campaigns.")
        money["treated_spend_share_pre"] = pre_sp_share
    if p.value is not None:
        v_t = p.value[treated].sum(axis=1).to_numpy(float)
        v_c = p.value[controls].sum(axis=1).to_numpy(float)
        fit = tbr_fit(v_t[pre], v_c[pre])
        v_cf = float(np.sum(tbr_predict(fit, v_c[post])))
        v_obs = float(np.sum(v_t[post]))
        money["value_effect"] = v_obs - v_cf
        if "spend_delta" in money and money["spend_delta"] != 0:
            money["iroas"] = (v_obs - v_cf) / money["spend_delta"]
    # Checks
    checks = []
    q = prim["pre_fit"]
    checks.append({"check": "pre_period_fit_r2", "value": round(q["r2"], 3),
                   "pass": q["r2"] >= 0.6})
    if "placebo_bias_pct" in prim:
        checks.append({"check": "placebo_bias_pct", "value": round(prim["placebo_bias_pct"], 2),
                       "pass": abs(prim["placebo_bias_pct"]) < 0.5 * max(prim["placebo_rms_pct"], 1e-9)})
    checks.append({"check": "placebo_windows", "value": prim["placebo_windows"],
                   "pass": prim["placebo_windows"] >= 10})
    t_l, s_l = results["tbr"]["lift"], results["sc"]["lift"]
    agree = (np.sign(t_l) == np.sign(s_l)) and abs(t_l - s_l) <= max(
        0.5 * max(abs(t_l), abs(s_l)), 0.02)
    checks.append({"check": "tbr_sc_agree", "value": [round(100 * t_l, 2), round(100 * s_l, 2)],
                   "pass": bool(agree)})
    ctrl_pre = kpi.loc[pre, controls].sum(axis=1)
    ctrl_post = kpi.loc[post, controls].sum(axis=1)
    lvl = float(ctrl_post.mean() / ctrl_pre.iloc[-max(n, 7):].mean() - 1) if ctrl_pre.iloc[-max(n, 7):].mean() > 0 else 0.0
    checks.append({"check": "control_level_shift_pct", "value": round(100 * lvl, 1),
                   "pass": abs(lvl) < 0.3})
    if pre_len < 3 * n:
        warnings.append(f"Pre-period ({pre_len}) is shorter than three times the test window ({n}). Intervals rest on few placebo windows.")
    sig = None
    if "interval_lift" in prim:
        lo, hi = prim["interval_lift"]
        sig = bool(lo > 0 or hi < 0)
    out = {
        "command": "readout", "version": VERSION, "primary_method": a.method,
        "type": a.type, "frequency": p.freq, "confidence": conf,
        "treated": treated, "n_controls": len(controls),
        "window": {"start": str(kpi.index[post].min().date()),
                   "end": str(kpi.index[post].max().date()), "periods": n,
                   "pre_periods": pre_len},
        "primary": {k: v for k, v in prim.items() if k not in ("series", "pre_series")},
        "secondary": {k: v for k, v in results["sc" if a.method == "tbr" else "tbr"].items()
                      if k not in ("series", "pre_series")},
        "significant": sig,
        "money": money, "checks": checks, "warnings": warnings,
    }
    out["_series"] = {m: {"post": results[m]["series"], "pre": results[m]["pre_series"]}
                      for m in results}
    return out


# --------------------------------------------------------------------------
# Directional methods: one series, no geo split
# --------------------------------------------------------------------------

def load_series(path, date_col=None, kpi_col=None, control_col=None,
                spend_col=None, geo_col=None):
    """Daily single series. If a geo column exists, geos are summed."""
    df = pd.read_csv(path)
    d = _pick(df.columns, date_col, DATE_ALIASES, True, "date")
    k = _pick(df.columns, kpi_col, KPI_ALIASES, True, "kpi")
    c = control_col if control_col else None
    if c and c not in df.columns:
        raise SystemExit(f"Control column '{c}' not found. Columns: {list(df.columns)}")
    s = _pick(df.columns, spend_col, SPEND_ALIASES, False, "spend")
    if s and s == c:
        s = None
    df[d] = pd.to_datetime(df[d], errors="coerce")
    df = df[df[d].notna()]
    cols = [x for x in [k, c, s] if x]
    for x in cols:
        df[x] = pd.to_numeric(df[x], errors="coerce")
    g = df.groupby(d)[cols].sum().sort_index()
    if _infer_freq(g.index) != "D":
        raise SystemExit("Directional methods need daily data.")
    g = g.reindex(pd.date_range(g.index.min(), g.index.max(), freq="D")).fillna(0.0)
    ren = {k: "kpi"}
    if c:
        ren[c] = "control"
    if s:
        ren[s] = "spend"
    return g.rename(columns=ren)


def _baseline_prior_weeks(y, s, n, weeks):
    """Same weekday average over the previous `weeks` weeks, per test day."""
    vals = []
    for i in range(n):
        t = s + i
        m0 = i // 7 + 1          # first week back that falls before the window
        past = [t - 7 * (m0 + j) for j in range(weeks)]
        if past[-1] < 0:
            return None
        vals.append(np.mean(y[past]))
    return float(np.sum(vals))


def _baseline_control(y, c, s, n, pre_len):
    lo = max(0, s - pre_len)
    cy, cc = y[lo:s].sum(), c[lo:s].sum()
    if cc <= 0:
        return None
    return float(cy / cc * c[s:s + n].sum())


def _baseline_yoy(y, s, n, ref):
    """Last year's same window (364 days back, weekday-aligned), scaled by the
    growth of the `ref` days before the window against the same days a year
    earlier."""
    if s - 364 - ref < 0:
        return None
    ly = y[s - 364:s - 364 + n].sum()
    g_now = y[s - ref:s].sum()
    g_ly = y[s - 364 - ref:s - 364].sum()
    if g_ly <= 0:
        return None
    return float(ly * g_now / g_ly)


def cmd_prepost(a):
    df = load_series(a.data, a.date_col, a.kpi_col, a.control_col, a.spend_col)
    idx = df.index
    s = int(np.searchsorted(idx, pd.Timestamp(a.start)))
    e = int(np.searchsorted(idx, pd.Timestamp(a.end), side="right")) if a.end else len(idx)
    n = e - s
    if s <= 0 or n <= 0:
        raise SystemExit("The window must start after the first date and contain data.")
    y = df["kpi"].to_numpy(float)
    c = df["control"].to_numpy(float) if "control" in df else None
    comps = {
        "prior_weeks": lambda st: _baseline_prior_weeks(y, st, n, a.weeks),
        "yoy": lambda st: _baseline_yoy(y, st, n, a.yoy_ref_days),
    }
    if c is not None:
        comps["control_ratio"] = lambda st: _baseline_control(y, c, st, n, a.control_pre_days)
    obs = float(y[s:e].sum())
    rows = []
    excl = set()
    for w in (a.exclude_windows or []):
        ws, we = w.split(":")
        excl.update(range(int(np.searchsorted(idx, pd.Timestamp(ws))),
                          int(np.searchsorted(idx, pd.Timestamp(we), side="right"))))
    for name, fn in comps.items():
        base = fn(s)
        if base is None or base <= 0:
            continue
        # Noise: the same comparator on historical windows of the same length
        errs = []
        for st in range(0, s - n + 1):
            if any(t in excl for t in range(st, st + n)):
                continue
            b = fn(st)
            if b and b > 0:
                errs.append(float(y[st:st + n].sum()) / b - 1)
        errs = np.array(errs)
        if len(errs) >= 4:
            # windows overlap; thin to every n-th start for a fairer count
            thin = errs[::max(1, n // 2)]
            rms = float(np.sqrt(np.mean(errs ** 2)))
            band = float(np.quantile(np.abs(errs), 0.9)) if len(errs) >= 20 else 1.645 * rms
        else:
            thin, rms, band = errs, None, None
        rel = obs / base - 1
        rows.append({
            "comparator": name, "baseline": base, "observed": obs, "change": obs - base,
            "change_pct": rel, "historical_windows": int(len(errs)),
            "independent_windows": int(len(thin)),
            "noise_rms_pct": None if rms is None else rms,
            "noise_band_90_pct": band,
            "share_of_history_with_bigger_move": None if len(errs) < 4 else
                float(np.mean(np.abs(errs) >= abs(rel))),
            "outside_noise": None if band is None else bool(abs(rel) > band),
        })
    if not rows:
        raise SystemExit("No comparator could be built. Add history (4+ weeks before the window, a year for YoY) or a control column.")
    signs = {np.sign(r["change_pct"]) for r in rows}
    outside = [r for r in rows if r["outside_noise"]]
    if len(signs) > 1:
        verdict = "inconclusive: comparators disagree on the direction"
    elif len(outside) == len(rows):
        verdict = "directional signal: every comparator moves the same way and outside its normal range"
    elif outside:
        verdict = "weak signal: same direction, but only some comparators are outside their normal range"
    else:
        verdict = "no signal: the change is within the normal movement of comparable windows"
    money = {}
    if "spend" in df:
        sp = df["spend"].to_numpy(float)
        sp_obs = float(sp[s:e].sum())
        sp_base = _baseline_prior_weeks(sp, s, n, a.weeks)
        if sp_base is not None:
            money = {"spend_observed": sp_obs, "spend_baseline": sp_base,
                     "spend_change": sp_obs - sp_base}
            pw = next((r for r in rows if r["comparator"] == "prior_weeks"), None)
            if pw and pw["change"] != 0 and sp_obs != sp_base:
                money["directional_icpa"] = (sp_obs - sp_base) / pw["change"]
    return {"command": "prepost", "version": VERSION, "rigor": "directional",
            "window": {"start": str(idx[s].date()), "end": str(idx[e - 1].date()), "days": n},
            "comparators": rows, "verdict": verdict, "money": money,
            "caveats": [
                "Directional, not causal: anything else that changed in the window (promotions, competitors, seasonality, tracking, other channels) is inside the estimate.",
                "noise_band_90_pct is how much the same comparison moves in 90% of past windows with no test. A change inside that band is indistinguishable from a normal week.",
            ]}


def cmd_switchback(a):
    """Alternating on/off periods in one market. Regression of the KPI on an
    off indicator plus weekday effects and a linear trend, with a block
    permutation test over the on/off labels."""
    df = load_series(a.data, a.date_col, a.kpi_col, None, a.spend_col)
    idx = df.index
    off = np.zeros(len(idx), bool)
    blocks = []
    for w in a.off_periods:
        ws, we = w.split(":")
        m = (idx >= pd.Timestamp(ws)) & (idx <= pd.Timestamp(we))
        off |= m
    s = idx >= pd.Timestamp(a.start) if a.start else np.ones(len(idx), bool)
    e = idx <= pd.Timestamp(a.end) if a.end else np.ones(len(idx), bool)
    win = s & e
    # Build blocks of consecutive equal state inside the window
    state = off.astype(int)
    cur, start_i = None, None
    for i in np.where(win)[0]:
        if cur is None or state[i] != cur or (start_i is not None and i != prev + 1):
            if cur is not None:
                blocks.append((start_i, prev, cur))
            cur, start_i = state[i], i
        prev = i
    blocks.append((start_i, prev, cur))
    if len(blocks) < 4:
        raise SystemExit("A switchback needs at least 4 alternating blocks (for example on-off-on-off).")
    keep = np.zeros(len(idx), bool)
    for b0, b1, _ in blocks:
        keep[b0 + a.washout_days:b1 + 1] = True
    y = df["kpi"].to_numpy(float)
    dow = idx.dayofweek

    def design_matrix(offv):
        X = [np.ones(len(idx)), np.arange(len(idx)) / 365.0, offv.astype(float)]
        for d_ in range(1, 7):
            X.append((dow == d_).astype(float))
        return np.column_stack(X)

    def coef(offv):
        X = design_matrix(offv)[keep]
        beta, *_ = np.linalg.lstsq(X, y[keep], rcond=None)
        return beta

    beta = coef(off)
    on_mean = float(np.mean(y[keep & ~off]))
    eff = float(beta[2])
    rel = eff / on_mean if on_mean > 0 else float("nan")
    # Block permutation: reshuffle which blocks are off, same count
    rng = np.random.default_rng(a.seed)
    labels = np.array([b[2] for b in blocks])
    perm = []
    import itertools
    k_off = int(labels.sum())
    combos = list(itertools.combinations(range(len(blocks)), k_off))
    if len(combos) <= a.permutations:
        choices = combos
    else:
        choices = [tuple(sorted(rng.choice(len(blocks), k_off, replace=False)))
                   for _ in range(a.permutations)]
    for comb in choices:
        fake = np.zeros(len(idx), bool)
        for j in comb:
            b0, b1, _ = blocks[j]
            fake[b0:b1 + 1] = True
        perm.append(coef(fake)[2])
    perm = np.array(perm)
    p = float(np.mean(np.abs(perm) >= abs(eff) - 1e-12))
    out = {"command": "switchback", "version": VERSION, "rigor": "directional_plus",
           "blocks": [{"start": str(idx[b0].date()), "end": str(idx[b1].date()),
                       "state": "off" if st else "on"} for b0, b1, st in blocks],
           "washout_days": a.washout_days,
           "effect_per_day_when_off": eff, "on_mean_per_day": on_mean,
           "effect_pct_when_off": rel,
           "permutation_p": p, "permutations": int(len(perm)),
           "min_possible_p": float(1 / len(combos)) if combos else None,
           "caveats": [
               "Valid only if the effect switches off within the washout. Upper-funnel media with long carryover breaks this design.",
               "With few blocks the smallest attainable p-value is large; min_possible_p shows it.",
           ]}
    if "spend" in df:
        sp = df["spend"].to_numpy(float)
        d_sp = float(np.mean(sp[keep & off]) - np.mean(sp[keep & ~off]))
        out["spend_change_per_day_when_off"] = d_sp
        if eff != 0 and d_sp != 0:
            out["directional_icpa"] = d_sp / eff
    return out


def _md_prepost(o):
    lines = ["# Pre/post comparison (directional)", "",
             f"- Window: {o['window']['start']} to {o['window']['end']} ({o['window']['days']} days)",
             f"- Verdict: {o['verdict']}", "",
             "| Comparator | Baseline | Observed | Change | Normal range (90%) | Past windows with a bigger move |",
             "|---|---:|---:|---:|---:|---:|"]
    for r in o["comparators"]:
        lines.append(f"| {r['comparator']} | {r['baseline']:,.0f} | {r['observed']:,.0f} | {_fmt_pct(r['change_pct'])} | ±{_fmt_pct(r['noise_band_90_pct'])} | {_fmt_pct(r['share_of_history_with_bigger_move'], 0)} |")
    lines += ["", "## Caveats", ""] + [f"- {c}" for c in o["caveats"]]
    return "\n".join(lines) + "\n"


def _md_switchback(o):
    lines = ["# Switchback (directional)", "",
             f"- Effect when off: {o['effect_per_day_when_off']:,.1f} per day ({_fmt_pct(o['effect_pct_when_off'])})",
             f"- Permutation p: {o['permutation_p']:.3f} over {o['permutations']} relabelings (minimum possible {o['min_possible_p']:.3f})",
             f"- Washout dropped at the start of each block: {o['washout_days']} days", "",
             "| Block | Start | End | State |", "|---:|---|---|---|"]
    for i, b in enumerate(o["blocks"], 1):
        lines.append(f"| {i} | {b['start']} | {b['end']} | {b['state']} |")
    lines += ["", "## Caveats", ""] + [f"- {c}" for c in o["caveats"]]
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------

def _fmt_pct(x, d=1):
    return "n/a" if x is None or (isinstance(x, float) and not np.isfinite(x)) else f"{100 * x:.{d}f}%"


def _md_profile(o):
    lines = [f"# Panel profile", "",
             f"- Frequency: {o['frequency']}, {o['periods']} periods, {o['start']} to {o['end']}",
             f"- Geos: {o['geos']}",
             f"- KPI per period (all geos): {o['kpi_per_period']:,.1f}",
             f"- Spend column: {'yes' if o['has_spend'] else 'no'}; value column: {'yes' if o['has_value'] else 'no'}",
             "", "| Geo | Share | Mean/period | CV | Zero share |", "|---|---:|---:|---:|---:|"]
    for r in o["geo_table"][:30]:
        lines.append(f"| {r['geo']} | {_fmt_pct(r['share'])} | {r['mean_per_period']:,.1f} | {r['cv'] if r['cv'] is not None else 'n/a'} | {_fmt_pct(r['zero_share'], 0)} |")
    if len(o["geo_table"]) > 30:
        lines.append(f"| ... {len(o['geo_table']) - 30} more | | | | |")
    if o["warnings"]:
        lines += ["", "## Warnings", ""] + [f"- {w}" for w in o["warnings"]]
    return "\n".join(lines) + "\n"


def _md_design(o):
    r = o["recommended"]
    lines = ["# Test design", "",
             f"- Type: {o['type']}; method: {o['method'].upper()}; alpha {o['alpha']}, power {o['power']}",
             f"- Test length: {o['test_periods']} {'days' if o['frequency'] == 'D' else 'weeks'}",
             f"- Treated geos ({r['n_treated']}): {', '.join(r['treated'])}",
             f"- Treated share of KPI: {_fmt_pct(r['kpi_share'])}",
             f"- MDE (validation windows): {r['mde_pct_validation']}%",
             f"- MDE (selection windows): {r['mde_pct_selection']}%",
             f"- Pre-period fit: R2 {r['pre_fit']['r2']:.3f}, WAPE {_fmt_pct(r['pre_fit']['wape'])}",
             f"- Seed: {o['seed']}; candidates evaluated: {o['candidates_evaluated']}",
             "", "## Duration", "", "| Test days | MDE |", "|---:|---:|"]
    for c in o["duration_curve"]:
        lines.append(f"| {c['test_days']} | {c['mde_pct']}% |")
    c = o["cost"]
    lines += ["", "## Cost", ""]
    for k, v in c.items():
        if k != "scenarios":
            lines.append(f"- {k}: {v}")
    lines += ["", "| True effect | KPI change in window | Detectable |", "|---:|---:|---|"]
    for s in c["scenarios"]:
        lines.append(f"| {s['true_effect_pct']}% | {s['kpi_change_in_window']:,.1f} | {'yes' if s['detectable'] else 'no'} |")
    if o["warnings"]:
        lines += ["", "## Warnings", ""] + [f"- {w}" for w in o["warnings"]]
    return "\n".join(lines) + "\n"


def _md_readout(o):
    p = o["primary"]
    s = o["secondary"]
    il = p.get("interval_lift")
    lines = ["# Test readout", "",
             f"- Window: {o['window']['start']} to {o['window']['end']} ({o['window']['periods']} periods, {o['window']['pre_periods']} pre-periods)",
             f"- Treated: {', '.join(o['treated'])}; controls: {o['n_controls']}",
             f"- Observed KPI: {p['observed']:,.1f}; counterfactual: {p['counterfactual']:,.1f}",
             f"- Effect: {p['effect']:,.1f} ({_fmt_pct(p['lift'])})",
             f"- {int(100 * o['confidence'])}% interval for lift: {_fmt_pct(il[0]) + ' to ' + _fmt_pct(il[1]) if il else 'n/a'}",
             f"- In-time placebo p: {p.get('p_in_time', 'n/a')}; in-space placebo p: {p.get('p_in_space', 'n/a')}",
             f"- Secondary method lift: {_fmt_pct(s['lift'])}",
             ""]
    m = o["money"]
    if m:
        lines += ["## Spend and value", ""]
        for k, v in m.items():
            lines.append(f"- {k}: {v}")
        lines.append("")
    lines += ["## Checks", "", "| Check | Value | Pass |", "|---|---|---|"]
    for c in o["checks"]:
        lines.append(f"| {c['check']} | {c['value']} | {'yes' if c['pass'] else 'no'} |")
    if o["warnings"]:
        lines += ["", "## Warnings", ""] + [f"- {w}" for w in o["warnings"]]
    return "\n".join(lines) + "\n"


def _chart_readout(o, path):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return None
    ser = o["_series"][o["primary_method"]]
    pre_d = pd.to_datetime(ser["pre"]["dates"])
    post_d = pd.to_datetime(ser["post"]["dates"])
    k = min(len(pre_d), max(4 * len(post_d), 56))
    fig, ax = plt.subplots(2, 1, figsize=(10, 6.5), sharex=False,
                           gridspec_kw={"height_ratios": [3, 2]})
    ax[0].plot(pre_d[-k:], ser["pre"]["observed"][-k:], color="#1f2937", lw=1.2, label="Treated, observed")
    ax[0].plot(pre_d[-k:], ser["pre"]["fitted"][-k:], color="#6b7280", lw=1.0, ls="--", label="Counterfactual")
    ax[0].plot(post_d, ser["post"]["observed"], color="#1f2937", lw=1.2)
    ax[0].plot(post_d, ser["post"]["counterfactual"], color="#6b7280", lw=1.0, ls="--")
    ax[0].axvline(post_d.min(), color="#b45309", lw=1)
    ax[0].set_title("Treated geos: observed vs counterfactual")
    ax[0].legend(frameon=False, loc="upper left")
    cum = np.cumsum(np.array(ser["post"]["observed"]) - np.array(ser["post"]["counterfactual"]))
    ax[1].plot(post_d, cum, color="#b45309", lw=1.5)
    il = o["primary"].get("interval_effect")
    if il:
        ax[1].axhspan(il[0], il[1], color="#b45309", alpha=0.12,
                      label=f"{int(100 * o['confidence'])}% interval, full window")
        ax[1].legend(frameon=False, loc="upper left")
    ax[1].axhline(0, color="#9ca3af", lw=0.8)
    ax[1].set_title("Cumulative effect")
    for a_ in ax:
        a_.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return str(path)


def _write(o, out, md_fn):
    if not out:
        return
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    clean = {k: v for k, v in o.items() if not k.startswith("_")}
    out.with_suffix(".json").write_text(json.dumps(clean, indent=2, default=float))
    out.with_suffix(".md").write_text(md_fn(o))
    if o.get("command") == "readout":
        _chart_readout(o, out.with_suffix(".png"))
        ser = o["_series"][o["primary_method"]]["post"]
        pd.DataFrame({"date": ser["dates"], "observed": ser["observed"],
                      "counterfactual": ser["counterfactual"]}).assign(
            effect=lambda d: d.observed - d.counterfactual,
            cumulative_effect=lambda d: (d.observed - d.counterfactual).cumsum()
        ).to_csv(out.with_name(out.stem + "_daily.csv"), index=False)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def _common(sp):
    sp.add_argument("--data", required=True, help="CSV in long format")
    sp.add_argument("--date-col")
    sp.add_argument("--geo-col")
    sp.add_argument("--kpi-col")
    sp.add_argument("--spend-col")
    sp.add_argument("--value-col")
    sp.add_argument("--exclude", nargs="*", default=[], help="Geos to drop entirely")
    sp.add_argument("--out", help="Output path stem; writes .json and .md")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("profile")
    _common(sp)

    sp = sub.add_parser("quick")
    sp.add_argument("--baseline-per-day", type=float, required=True)
    sp.add_argument("--residual-cv", type=float, default=0.15)
    sp.add_argument("--autocorrelation", type=float, default=0.3)
    sp.add_argument("--days", type=int, nargs="*", default=[14, 21, 28, 42, 56])
    sp.add_argument("--alpha", type=float, default=0.10)
    sp.add_argument("--power", type=float, default=0.80)
    sp.add_argument("--out")

    sp = sub.add_parser("design")
    _common(sp)
    sp.add_argument("--test-days", type=int, required=True)
    sp.add_argument("--type", choices=["go_dark", "holdback", "heavy_up"], default="go_dark")
    sp.add_argument("--intensity", type=float, default=0.5,
                    help="Holdback: share of spend removed. Heavy-up: share of spend added.")
    sp.add_argument("--treated-share", type=float, default=0.2,
                    help="Target share of geos in the treated group")
    sp.add_argument("--treated", nargs="*", help="Evaluate this fixed group instead of searching")
    sp.add_argument("--must-treat", nargs="*")
    sp.add_argument("--never-treat", nargs="*")
    sp.add_argument("--draws", type=int, default=150)
    sp.add_argument("--method", choices=["tbr", "sc"], default="tbr")
    sp.add_argument("--alpha", type=float, default=0.10)
    sp.add_argument("--power", type=float, default=0.80)
    sp.add_argument("--seed", type=int, default=20261002)
    sp.add_argument("--curve-days", type=int, nargs="*", default=[14, 21, 28, 42, 56])
    sp.add_argument("--scenarios", type=float, nargs="*", default=[0.02, 0.05, 0.10, 0.20])

    sp = sub.add_parser("readout")
    _common(sp)
    sp.add_argument("--treated", nargs="+", required=True)
    sp.add_argument("--start", required=True, help="First day of the test")
    sp.add_argument("--end", help="Last day measured (include the cooldown)")
    sp.add_argument("--type", choices=["go_dark", "holdback", "heavy_up"], default="go_dark")
    sp.add_argument("--method", choices=["tbr", "sc"], default="tbr")
    sp.add_argument("--exclude-controls", nargs="*",
                    help="Geos kept out of the control pool (spillover risk)")
    sp.add_argument("--conf", type=float, default=0.90)
    sp.add_argument("--in-space-draws", type=int, default=200)
    sp.add_argument("--seed", type=int, default=20261002)

    sp = sub.add_parser("prepost", help="Directional: one series, before vs during")
    sp.add_argument("--data", required=True)
    sp.add_argument("--date-col")
    sp.add_argument("--kpi-col")
    sp.add_argument("--control-col", help="A series the change did not touch (another country, organic, a product without ads)")
    sp.add_argument("--spend-col")
    sp.add_argument("--start", required=True)
    sp.add_argument("--end")
    sp.add_argument("--weeks", type=int, default=4)
    sp.add_argument("--yoy-ref-days", type=int, default=28)
    sp.add_argument("--control-pre-days", type=int, default=56)
    sp.add_argument("--exclude-windows", nargs="*", help="start:end periods to skip when measuring noise (other tests, outages)")
    sp.add_argument("--out")

    sp = sub.add_parser("switchback", help="Directional+: alternating on/off blocks")
    sp.add_argument("--data", required=True)
    sp.add_argument("--date-col")
    sp.add_argument("--kpi-col")
    sp.add_argument("--spend-col")
    sp.add_argument("--off-periods", nargs="+", required=True, help="start:end for each off block")
    sp.add_argument("--start")
    sp.add_argument("--end")
    sp.add_argument("--washout-days", type=int, default=2)
    sp.add_argument("--permutations", type=int, default=2000)
    sp.add_argument("--seed", type=int, default=20261002)
    sp.add_argument("--out")

    a = ap.parse_args(argv)
    if a.cmd == "prepost":
        o = cmd_prepost(a); _write(o, a.out, _md_prepost)
    elif a.cmd == "switchback":
        o = cmd_switchback(a); _write(o, a.out, _md_switchback)
    elif a.cmd == "profile":
        o = cmd_profile(a); _write(o, a.out, _md_profile)
    elif a.cmd == "quick":
        o = cmd_quick(a)
        if a.out:
            Path(a.out).with_suffix(".json").write_text(json.dumps(o, indent=2))
    elif a.cmd == "design":
        o = cmd_design(a); _write(o, a.out, _md_design)
    else:
        o = cmd_readout(a); _write(o, a.out, _md_readout)
    printable = {k: v for k, v in o.items() if not k.startswith("_")}
    json.dump(printable, sys.stdout, indent=2, default=float)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
