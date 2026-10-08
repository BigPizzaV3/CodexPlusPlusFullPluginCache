#!/usr/bin/env python3
"""Find the separate subjects on a transparent sheet.

A sheet whose subjects float in transparent gaps does not need slicing on
a grid: each subject is its own island of alpha, so it can be found and
cut on its own bounds. That is what makes the cut tolerant of a grid that
drifted, a canvas that came back non-square, or gaps of uneven width.

Grid slicing stays as the fallback for opaque sheets and for sheets whose
subjects touch. No scipy here — labelling is a two-pass union-find over a
downsampled mask, which is plenty for one sheet.
"""
import numpy as np
from PIL import Image, ImageFilter


class _Union:
    def __init__(self):
        self.parent = {}

    def find(self, a):
        p = self.parent.setdefault(a, a)
        while p != a:
            a, p = p, self.parent.setdefault(p, p)
        return a

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[max(ra, rb)] = min(ra, rb)


def _label(mask):
    """Two-pass 8-connected labelling. Returns an int array, 0 = background."""
    h, w = mask.shape
    lab = np.zeros((h, w), dtype=np.int32)
    uf = _Union()
    nxt = 1
    for y in range(h):
        row, prev = mask[y], lab[y - 1] if y else None
        for x in range(w):
            if not row[x]:
                continue
            n = []
            if x and lab[y][x - 1]:
                n.append(lab[y][x - 1])
            if prev is not None:
                for dx in (-1, 0, 1):
                    xx = x + dx
                    if 0 <= xx < w and prev[xx]:
                        n.append(prev[xx])
            if n:
                m = min(n)
                lab[y][x] = m
                for o in n:
                    uf.union(m, o)
            else:
                lab[y][x] = nxt
                uf.union(nxt, nxt)
                nxt += 1
    if nxt == 1:
        return lab
    flat = lab.ravel()
    nz = flat > 0
    flat[nz] = np.array([uf.find(v) for v in flat[nz]], dtype=np.int32)
    return flat.reshape(h, w)


def find_subjects(img, alpha_threshold=16, min_area_frac=0.0015, merge_px=6, scale_to=256):
    """Bounding boxes of each subject island, in reading order.

    Returns [] when the image has no usable alpha. Boxes are in the
    coordinates of `img`.
    """
    if img.mode not in ("RGBA", "LA"):
        return []
    a = np.array(img.convert("RGBA"))[..., 3]
    if (a < alpha_threshold).mean() < 0.02:          # effectively opaque
        return []

    H, W = a.shape
    k = max(1, int(round(max(W, H) / scale_to)))
    small = Image.fromarray((a >= alpha_threshold).astype(np.uint8) * 255).resize(
        (max(1, W // k), max(1, H // k)), Image.NEAREST)
    # Dilate so one subject's detached bits — a sparkle, a dot, a loose limb —
    # join up instead of each becoming its own "subject".
    if merge_px > 1:
        r = max(1, merge_px // k)
        small = small.filter(ImageFilter.MaxFilter(r * 2 + 1))
    mask = np.array(small) > 127

    lab = _label(mask)
    out = []
    total = mask.size
    for v in np.unique(lab):
        if v == 0:
            continue
        ys, xs = np.where(lab == v)
        if len(ys) / total < min_area_frac:
            continue
        out.append((int(xs.min() * k), int(ys.min() * k),
                    int((xs.max() + 1) * k), int((ys.max() + 1) * k)))
    if not out:
        return []

    # Clip the dilation back off, then re-tighten to the real alpha inside.
    pad = merge_px
    tight = []
    for (x0, y0, x1, y1) in out:
        x0, y0 = max(0, x0 + pad), max(0, y0 + pad)
        x1, y1 = min(W, x1 - pad), min(H, y1 - pad)
        if x1 - x0 < 8 or y1 - y0 < 8:
            continue
        sub = a[y0:y1, x0:x1] >= alpha_threshold
        if not sub.any():
            continue
        ys, xs = np.where(sub)
        tight.append((x0 + int(xs.min()), y0 + int(ys.min()),
                      x0 + int(xs.max()) + 1, y0 + int(ys.max()) + 1))

    # Reading order: cluster into rows by vertical overlap, then left to right.
    tight.sort(key=lambda b: (b[1] + b[3]) / 2)
    rows, cur = [], []
    for b in tight:
        if cur and (b[1] + b[3]) / 2 - (cur[0][1] + cur[0][3]) / 2 > (cur[0][3] - cur[0][1]) * 0.6:
            rows.append(cur); cur = []
        cur.append(b)
    if cur:
        rows.append(cur)
    ordered = []
    for r in rows:
        ordered.extend(sorted(r, key=lambda b: (b[0] + b[2]) / 2))
    return ordered
