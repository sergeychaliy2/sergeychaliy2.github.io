# -*- coding: utf-8 -*-
"""UI-кит для макетов мобильных приложений: карточки, иконки, панели,
графики. Поверх примитивов из make_screens."""

import math

from make_screens import (T, RR, C, star, poly, sparkle, lgrad, lgrad3, rgrad, fade, W, H)

F = "Segoe UI, Arial, sans-serif"          # основной шрифт интерфейса
INK = "#1d2335"                            # основной текст
MUTE = "#8b93a7"                           # вторичный текст
LINE = "#e6e9f2"                           # разделители
BG = "#f3f5fa"                             # фон экрана


def txt(x, y, s, size=32, c=INK, w=600, anchor="start", op=1, ls=0, extra=""):
    return T(x, y, s, size, fill=c, w=w, anchor=anchor, fam=F, op=op, ls=ls, extra=extra)


def card(x, y, w, h, r=32, fill="#ffffff", stroke=None, sw=2, shadow=True, op=1):
    o = []
    if shadow:
        o.append(RR(x, y + 8, w, h, r, "#1d233514"))
        o.append(RR(x + 4, y + 14, w - 8, h, r, "#1d23350e"))
    st = f'stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o.append(RR(x, y, w, h, r, fill, st + f' opacity="{op}"'))
    return "".join(o)


def pill_btn(x, y, w, h, label, c1, c2, size=32, c="#ffffff", r=None, icon=None, iw=0):
    r = r if r is not None else h / 2
    o = [RR(x, y + 8, w, h, r, "#1d233520"),
         RR(x, y, w, h, r, lgrad(c1, c2)),
         RR(x + 10, y + 6, w - 20, h * 0.34, r * 0.6, "#ffffff", 'opacity="0.18"')]
    o.append(txt(x + w / 2 + iw / 2, y + h / 2 + size * 0.36, label, size, c, 700, "middle"))
    return "".join(o)


def ghost_btn(x, y, w, h, label, accent, size=30, r=None, fill="#ffffff"):
    r = r if r is not None else h / 2
    return (RR(x, y, w, h, r, fill, f'stroke="{accent}" stroke-width="3"') +
            txt(x + w / 2, y + h / 2 + size * 0.36, label, size, accent, 700, "middle"))


def chip(x, y, w, h, label, active=False, accent="#2b6ad6", size=28):
    if active:
        return (RR(x, y, w, h, h / 2, lgrad(accent, accent)) +
                txt(x + w / 2, y + h / 2 + size * 0.36, label, size, "#ffffff", 700, "middle"))
    return (RR(x, y, w, h, h / 2, "#ffffff", f'stroke="{LINE}" stroke-width="2"') +
            txt(x + w / 2, y + h / 2 + size * 0.36, label, size, MUTE, 600, "middle"))


def field(x, y, w, h, placeholder, icon_name="search", accent=MUTE, r=None, fill="#ffffff",
          stroke=LINE, value=None):
    r = r if r is not None else h / 2
    o = [RR(x, y, w, h, r, fill, f'stroke="{stroke}" stroke-width="2"')]
    if icon_name:
        o.append(ic(icon_name, x + 44, y + h / 2, 0.9, accent))
        tx = x + 84
    else:
        tx = x + 32
    o.append(txt(tx, y + h / 2 + 11, value or placeholder, 30,
                 INK if value else MUTE, 600 if value else 500))
    return "".join(o)


def toggle(x, y, on=True, accent="#2fa84f", w=96, h=52):
    knob = x + w - h / 2 - 4 if on else x + h / 2 + 4
    return (RR(x, y, w, h, h / 2, lgrad(accent, accent) if on else "#d7dced") +
            C(knob, y + h / 2, h / 2 - 6, "#ffffff", 'filter="url(#shs)"'))


def divider(x, y, w):
    return RR(x, y, w, 2, 1, LINE)


def avatar(cx, cy, r, c1="#9bb8ff", c2="#3f6fd8"):
    return (C(cx, cy, r, lgrad(c1, c2)) +
            C(cx, cy - r * 0.22, r * 0.34, "#ffffff", 'opacity="0.95"') +
            f'<path d="M {cx-r*0.58} {cy+r*0.72} a {r*0.58} {r*0.52} 0 0 1 {r*1.16} 0 Z" '
            f'fill="#ffffff" opacity="0.95"/>')


def ring(cx, cy, r, frac, c1, c2, width=26, bg="#eceff7", rot=-90):
    circ = 2 * math.pi * r
    return (C(cx, cy, r, "none", f'stroke="{bg}" stroke-width="{width}"') +
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{lgrad(c1, c2)}" '
            f'stroke-width="{width}" stroke-linecap="round" stroke-dasharray="{circ*frac:.1f} {circ:.1f}" '
            f'transform="rotate({rot} {cx} {cy})"/>')


def donut(cx, cy, r, segments, width=44, bg="#eceff7"):
    """segments: [(доля, цвет), ...]"""
    circ = 2 * math.pi * r
    o = [C(cx, cy, r, "none", f'stroke="{bg}" stroke-width="{width}"')]
    off = 0.0
    for (frac, col) in segments:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" '
                 f'stroke-width="{width}" stroke-dasharray="{circ*frac-6:.1f} {circ:.1f}" '
                 f'stroke-dashoffset="{-circ*off:.1f}" stroke-linecap="butt" '
                 f'transform="rotate(-90 {cx} {cy})"/>')
        off += frac
    return "".join(o)


def bars(x, y, w, h, values, labels, c1, c2, hi=None, vmax=None, lab_c=MUTE, val_fmt=None,
         track="#eef1f8", inac="#bfd2f5", val_c=INK):
    n = len(values)
    vmax = vmax or max(values) * 1.15
    bw = w / (n * 1.8)
    gap = (w - bw * n) / (n - 1) if n > 1 else 0
    o = []
    for i, v in enumerate(values):
        bx = x + i * (bw + gap)
        bh = max(10, h * v / vmax)
        active = (hi == i)
        o.append(RR(bx, y, bw, h, bw / 2, track))
        o.append(RR(bx, y + h - bh, bw, bh, bw / 2, lgrad(c1, c2) if active or hi is None else inac))
        o.append(txt(bx + bw / 2, y + h + 36, labels[i], 24, lab_c, 600, "middle"))
        if val_fmt and active:
            o.append(txt(bx + bw / 2, y + h - bh - 18, val_fmt % v, 24, val_c, 700, "middle"))
    return "".join(o)


def line_chart(x, y, w, h, values, accent, fill_op=0.18, dots=True, vmin=None, vmax=None):
    vmin = vmin if vmin is not None else min(values) * 0.9
    vmax = vmax if vmax is not None else max(values) * 1.05
    n = len(values)
    pts = []
    for i, v in enumerate(values):
        px = x + w * i / (n - 1)
        py = y + h - h * (v - vmin) / max(0.001, (vmax - vmin))
        pts.append((px, py))
    d = " ".join(("M" if i == 0 else "L") + f" {px:.1f} {py:.1f}" for i, (px, py) in enumerate(pts))
    o = [f'<path d="{d} L {x+w} {y+h} L {x} {y+h} Z" fill="{accent}" opacity="{fill_op}"/>',
         f'<path d="{d}" fill="none" stroke="{accent}" stroke-width="7" stroke-linecap="round" '
         f'stroke-linejoin="round"/>']
    if dots:
        for (px, py) in pts:
            o.append(C(px, py, 9, "#ffffff", f'stroke="{accent}" stroke-width="5"'))
    return "".join(o)


def tabbar(items, active, accent, y=1710, h=210, bg="#ffffff"):
    """items: [(подпись, имя иконки), ...]"""
    o = [RR(0, y, W, h + 40, 46, "#1d233512"), RR(0, y, W, h + 40, 46, bg)]
    n = len(items)
    for i, (label, icon_name) in enumerate(items):
        cx = W * (i + 0.5) / n
        col = accent if i == active else "#a7aec2"
        if i == active:
            o.append(RR(cx - 46, y + 34, 92, 68, 26, accent, 'opacity="0.12"'))
        o.append(ic(icon_name, cx, y + 68, 1.05, col))
        o.append(txt(cx, y + 136, label, 24, col, 700 if i == active else 600, "middle"))
    o.append(RR(W / 2 - 120, y + 174, 240, 10, 5, "#d7dced"))
    return "".join(o)


def status_free_top():
    return ""


# ----------------------------------------------------------------------------
# иконки
# ----------------------------------------------------------------------------
def ic(name, cx, cy, s=1.0, c=INK, sw=None):
    k = 24 * s
    sw = sw if sw is not None else 5 * s
    P = lambda d, extra="": (f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{sw}" '
                             f'stroke-linecap="round" stroke-linejoin="round" {extra}/>')
    if name == "home":
        return (P(f"M {cx-k} {cy} L {cx} {cy-k} L {cx+k} {cy} V {cy+k} H {cx-k} Z"))
    if name == "search":
        return (C(cx - k * 0.18, cy - k * 0.18, k * 0.66, "none", f'stroke="{c}" stroke-width="{sw}"') +
                P(f"M {cx+k*0.34} {cy+k*0.34} L {cx+k*0.86} {cy+k*0.86}"))
    if name == "heart":
        return (f'<path d="M {cx} {cy+k*0.78} C {cx-k*1.3} {cy-k*0.1} {cx-k*0.86} {cy-k*0.96} '
                f'{cx} {cy-k*0.34} C {cx+k*0.86} {cy-k*0.96} {cx+k*1.3} {cy-k*0.1} {cx} {cy+k*0.78} Z" '
                f'fill="{c}"/>')
    if name == "cart":
        return (P(f"M {cx-k} {cy-k*0.7} h {k*0.4} l {k*0.42} {k*1.3} h {k*1.1}") +
                P(f"M {cx-k*0.4} {cy-k*0.3} h {k*1.7} l {-k*0.3} {k*0.9} h {-k*1.1}") +
                C(cx - k * 0.1, cy + k * 0.82, k * 0.17, c) + C(cx + k * 0.62, cy + k * 0.82, k * 0.17, c))
    if name == "user":
        return (C(cx, cy - k * 0.34, k * 0.44, "none", f'stroke="{c}" stroke-width="{sw}"') +
                P(f"M {cx-k*0.78} {cy+k*0.92} a {k*0.78} {k*0.68} 0 0 1 {k*1.56} 0"))
    if name == "bell":
        return (P(f"M {cx-k*0.74} {cy+k*0.42} h {k*1.48} l {-k*0.2} {-k*0.4} v {-k*0.5} "
                  f"a {k*0.54} {k*0.54} 0 0 0 {-k*1.08} 0 v {k*0.5} Z") +
                P(f"M {cx-k*0.26} {cy+k*0.66} a {k*0.26} {k*0.26} 0 0 0 {k*0.52} 0"))
    if name == "plus":
        return P(f"M {cx-k*0.7} {cy} h {k*1.4} M {cx} {cy-k*0.7} v {k*1.4}")
    if name == "minus":
        return P(f"M {cx-k*0.7} {cy} h {k*1.4}")
    if name == "check":
        return P(f"M {cx-k*0.6} {cy} l {k*0.42} {k*0.46} l {k*0.82} {-k*0.92}")
    if name == "chev_r":
        return P(f"M {cx-k*0.26} {cy-k*0.6} l {k*0.56} {k*0.6} l {-k*0.56} {k*0.6}")
    if name == "chev_d":
        return P(f"M {cx-k*0.6} {cy-k*0.26} l {k*0.6} {k*0.56} l {k*0.6} {-k*0.56}")
    if name == "pin":
        return (P(f"M {cx} {cy+k} c {k*0.9} {-k*0.9} {k*0.74} {-k*1.42} {k*0.74} {-k*1.72} "
                  f"a {k*0.74} {k*0.74} 0 1 0 {-k*1.48} 0 c 0 {k*0.3} {-k*0.16} {k*0.82} {k*0.74} {k*1.72} Z") +
                C(cx, cy - k * 0.42, k * 0.26, c))
    if name == "clock":
        return (C(cx, cy, k * 0.86, "none", f'stroke="{c}" stroke-width="{sw}"') +
                P(f"M {cx} {cy-k*0.48} V {cy} l {k*0.42} {k*0.26}"))
    if name == "calendar":
        return (RR(cx - k * 0.86, cy - k * 0.74, k * 1.72, k * 1.56, k * 0.26, "none",
                   f'stroke="{c}" stroke-width="{sw}"') +
                P(f"M {cx-k*0.86} {cy-k*0.18} h {k*1.72} M {cx-k*0.42} {cy-k*1.02} v {k*0.44} "
                  f"M {cx+k*0.42} {cy-k*1.02} v {k*0.44}"))
    if name == "card":
        return (RR(cx - k, cy - k * 0.68, k * 2, k * 1.36, k * 0.26, "none",
                   f'stroke="{c}" stroke-width="{sw}"') +
                P(f"M {cx-k} {cy-k*0.16} h {k*2}"))
    if name == "wallet":
        return (RR(cx - k * 0.94, cy - k * 0.74, k * 1.88, k * 1.5, k * 0.3, "none",
                   f'stroke="{c}" stroke-width="{sw}"') +
                C(cx + k * 0.48, cy + k * 0.06, k * 0.2, c))
    if name == "chart":
        return P(f"M {cx-k*0.86} {cy+k*0.7} V {cy-k*0.1} M {cx} {cy+k*0.7} V {cy-k*0.74} "
                 f"M {cx+k*0.86} {cy+k*0.7} V {cy+k*0.1}")
    if name == "chat":
        return (P(f"M {cx-k*0.92} {cy-k*0.76} h {k*1.84} v {k*1.2} h {-k*1.1} l {-k*0.74} {k*0.62} "
                  f"v {-k*0.62} h 0 Z"))
    if name == "doc":
        return (P(f"M {cx-k*0.7} {cy-k*0.94} h {k*0.96} l {k*0.44} {k*0.44} v {k*1.44} h {-k*1.4} Z") +
                P(f"M {cx-k*0.38} {cy+k*0.1} h {k*0.76} M {cx-k*0.38} {cy+k*0.48} h {k*0.76}"))
    if name == "gear":
        o = [C(cx, cy, k * 0.4, "none", f'stroke="{c}" stroke-width="{sw}"')]
        for a in range(0, 360, 45):
            rad = math.radians(a)
            o.append(f'<rect x="{cx-k*0.1+k*0.78*math.cos(rad):.1f}" '
                     f'y="{cy-k*0.1+k*0.78*math.sin(rad):.1f}" width="{k*0.2}" height="{k*0.2}" '
                     f'rx="{k*0.06}" fill="{c}"/>')
        return "".join(o)
    if name == "flame":
        return (f'<path d="M {cx} {cy-k*1.05} C {cx+k*0.9} {cy-k*0.1} {cx+k*0.66} {cy+k} {cx} {cy+k} '
                f'C {cx-k*0.66} {cy+k} {cx-k*0.9} {cy-k*0.1} {cx} {cy-k*1.05} Z" fill="{c}"/>'
                f'<path d="M {cx} {cy-k*0.18} C {cx+k*0.42} {cy+k*0.2} {cx+k*0.3} {cy+k*0.72} {cx} {cy+k*0.72} '
                f'C {cx-k*0.3} {cy+k*0.72} {cx-k*0.42} {cy+k*0.2} {cx} {cy-k*0.18} Z" '
                f'fill="#ffffff" opacity="0.35"/>')
    if name == "drop":
        return (f'<path d="M {cx} {cy-k} c {k*0.86} {k*0.9} {k*0.86} {k*1.0} {k*0.86} {k*1.3} '
                f'a {k*0.86} {k*0.86} 0 0 1 {-k*1.72} 0 c 0 {-k*0.3} 0 {-k*0.4} {k*0.86} {-k*1.3} Z" fill="{c}"/>')
    if name == "bolt":
        return f'<path d="M {cx+k*0.3} {cy-k} L {cx-k*0.6} {cy+k*0.14} h {k*0.6} L {cx-k*0.2} {cy+k} L {cx+k*0.7} {cy-k*0.2} h {-k*0.62} Z" fill="{c}"/>'
    if name == "sun":
        o = [C(cx, cy, k * 0.52, c)]
        for a in range(0, 360, 45):
            rad = math.radians(a)
            o.append(f'<line x1="{cx+k*0.78*math.cos(rad):.1f}" y1="{cy+k*0.78*math.sin(rad):.1f}" '
                     f'x2="{cx+k*1.06*math.cos(rad):.1f}" y2="{cy+k*1.06*math.sin(rad):.1f}" '
                     f'stroke="{c}" stroke-width="{sw}" stroke-linecap="round"/>')
        return "".join(o)
    if name == "moon":
        return (f'<path d="M {cx+k*0.22} {cy-k*0.88} a {k*0.9} {k*0.9} 0 1 0 {k*0.02} {k*1.76} '
                f'a {k*0.72} {k*0.72} 0 1 1 {-k*0.04} {-k*1.76} Z" fill="{c}"/>')
    if name == "cloud":
        return (f'<path d="M {cx-k*0.82} {cy+k*0.44} a {k*0.5} {k*0.5} 0 0 1 {k*0.1} {-k*0.98} '
                f'a {k*0.66} {k*0.66} 0 0 1 {k*1.26} {-k*0.1} a {k*0.5} {k*0.5} 0 0 1 {k*0.2} {k*1.08} Z" '
                f'fill="{c}"/>')
    if name == "cloudsun":
        return (C(cx + k * 0.42, cy - k * 0.52, k * 0.4, "#ffd166") +
                f'<path d="M {cx-k*0.86} {cy+k*0.5} a {k*0.48} {k*0.48} 0 0 1 {k*0.1} {-k*0.94} '
                f'a {k*0.62} {k*0.62} 0 0 1 {k*1.2} {-k*0.1} a {k*0.48} {k*0.48} 0 0 1 {k*0.18} {k*1.04} Z" '
                f'fill="{c}"/>')
    if name == "rain":
        return (f'<path d="M {cx-k*0.82} {cy+k*0.1} a {k*0.48} {k*0.48} 0 0 1 {k*0.1} {-k*0.94} '
                f'a {k*0.62} {k*0.62} 0 0 1 {k*1.2} {-k*0.1} a {k*0.48} {k*0.48} 0 0 1 {k*0.18} {k*1.04} Z" '
                f'fill="{c}"/>' +
                P(f"M {cx-k*0.4} {cy+k*0.46} l {-k*0.14} {k*0.4} M {cx} {cy+k*0.46} l {-k*0.14} {k*0.4} "
                  f"M {cx+k*0.4} {cy+k*0.46} l {-k*0.14} {k*0.4}"))
    if name == "wind":
        return P(f"M {cx-k*0.9} {cy-k*0.3} h {k*1.1} a {k*0.34} {k*0.34} 0 1 0 {-k*0.34} {-k*0.34} "
                 f"M {cx-k*0.9} {cy+k*0.3} h {k*1.4} a {k*0.34} {k*0.34} 0 1 1 {-k*0.34} {k*0.34}")
    if name == "car":
        return (P(f"M {cx-k*0.96} {cy+k*0.3} v {-k*0.4} l {k*0.34} {-k*0.6} h {k*1.24} l {k*0.34} {k*0.6} "
                  f"v {k*0.4} Z") +
                C(cx - k * 0.52, cy + k * 0.34, k * 0.2, c) + C(cx + k * 0.52, cy + k * 0.34, k * 0.2, c))
    if name == "steps":
        return (f'<ellipse cx="{cx-k*0.4}" cy="{cy-k*0.2}" rx="{k*0.32}" ry="{k*0.5}" fill="{c}" '
                f'transform="rotate(-12 {cx-k*0.4} {cy-k*0.2})"/>'
                f'<ellipse cx="{cx+k*0.42}" cy="{cy+k*0.3}" rx="{k*0.32}" ry="{k*0.5}" fill="{c}" '
                f'transform="rotate(10 {cx+k*0.42} {cy+k*0.3})"/>')
    if name == "pulse":
        return P(f"M {cx-k} {cy} h {k*0.5} l {k*0.26} {-k*0.6} l {k*0.42} {k*1.2} l {k*0.3} {-k*0.6} h {k*0.52}")
    if name == "bulb":
        return (P(f"M {cx} {cy-k*0.92} a {k*0.68} {k*0.68} 0 0 1 {k*0.38} {k*1.24} v {k*0.24} h {-k*0.76} "
                  f"v {-k*0.24} a {k*0.68} {k*0.68} 0 0 1 {k*0.38} {-k*1.24} Z") +
                P(f"M {cx-k*0.3} {cy+k*0.76} h {k*0.6}"))
    if name == "ac":
        return (RR(cx - k * 0.98, cy - k * 0.72, k * 1.96, k * 0.86, k * 0.22, "none",
                   f'stroke="{c}" stroke-width="{sw}"') +
                P(f"M {cx-k*0.5} {cy+k*0.4} v {k*0.5} M {cx} {cy+k*0.4} v {k*0.64} M {cx+k*0.5} {cy+k*0.4} v {k*0.5}"))
    if name == "curtain":
        return (P(f"M {cx-k} {cy-k*0.8} h {k*2}") +
                P(f"M {cx-k*0.7} {cy-k*0.8} v {k*1.6} q {k*0.34} {-k*0.4} 0 {-k*0.8}") +
                P(f"M {cx+k*0.7} {cy-k*0.8} v {k*1.6} q {-k*0.34} {-k*0.4} 0 {-k*0.8}"))
    if name == "cam":
        return (RR(cx - k * 0.96, cy - k * 0.52, k * 1.5, k * 1.04, k * 0.22, "none",
                   f'stroke="{c}" stroke-width="{sw}"') +
                P(f"M {cx+k*0.56} {cy} l {k*0.46} {-k*0.36} v {k*0.72} Z"))
    if name == "kettle":
        return (P(f"M {cx-k*0.7} {cy-k*0.3} h {k*1.4} l {-k*0.18} {k*1.1} h {-k*1.04} Z") +
                P(f"M {cx+k*0.7} {cy-k*0.1} q {k*0.4} {k*0.2} 0 {k*0.5}") +
                P(f"M {cx-k*0.3} {cy-k*0.3} v {-k*0.4} h {k*0.6} v {k*0.4}"))
    if name == "socket":
        return (C(cx, cy, k * 0.86, "none", f'stroke="{c}" stroke-width="{sw}"') +
                C(cx - k * 0.3, cy - k * 0.1, k * 0.13, c) + C(cx + k * 0.3, cy - k * 0.1, k * 0.13, c))
    if name == "filter":
        return P(f"M {cx-k*0.9} {cy-k*0.6} h {k*1.8} l {-k*0.68} {k*0.78} v {k*0.72} l {-k*0.44} {k*0.3} "
                 f"v {-k*1.02} Z")
    if name == "percent":
        return (C(cx - k * 0.42, cy - k * 0.42, k * 0.26, "none", f'stroke="{c}" stroke-width="{sw}"') +
                C(cx + k * 0.42, cy + k * 0.42, k * 0.26, "none", f'stroke="{c}" stroke-width="{sw}"') +
                P(f"M {cx-k*0.72} {cy+k*0.72} L {cx+k*0.72} {cy-k*0.72}"))
    if name == "arrow_up":
        return P(f"M {cx} {cy+k*0.8} V {cy-k*0.8} M {cx-k*0.5} {cy-k*0.3} L {cx} {cy-k*0.8} L {cx+k*0.5} {cy-k*0.3}")
    if name == "arrow_dl":
        return P(f"M {cx} {cy-k*0.8} V {cy+k*0.8} M {cx-k*0.5} {cy+k*0.3} L {cx} {cy+k*0.8} L {cx+k*0.5} {cy+k*0.3}")
    if name == "swap":
        return P(f"M {cx-k*0.8} {cy-k*0.3} h {k*1.6} l {-k*0.5} {-k*0.5} M {cx+k*0.8} {cy+k*0.3} "
                 f"h {-k*1.6} l {k*0.5} {k*0.5}")
    if name == "list":
        return (P(f"M {cx-k*0.5} {cy-k*0.6} h {k*1.4} M {cx-k*0.5} {cy} h {k*1.4} "
                  f"M {cx-k*0.5} {cy+k*0.6} h {k*1.4}") +
                C(cx - k * 0.86, cy - k * 0.6, k * 0.12, c) + C(cx - k * 0.86, cy, k * 0.12, c) +
                C(cx - k * 0.86, cy + k * 0.6, k * 0.12, c))
    if name == "fire":
        return ic("flame", cx, cy, s, c, sw)
    if name == "star":
        return star(cx, cy, k * 0.95, c, stroke="none", sw=0)
    if name == "gas":
        return (C(cx, cy + k * 0.2, k * 0.7, "none", f'stroke="{c}" stroke-width="{sw}"') +
                P(f"M {cx} {cy-k*0.5} v {-k*0.5} M {cx-k*0.34} {cy-k*0.74} h {k*0.68}") +
                P(f"M {cx-k*0.26} {cy+k*0.2} a {k*0.26} {k*0.26} 0 1 0 {k*0.52} 0 "
                  f"a {k*0.26} {k*0.26} 0 1 0 {-k*0.52} 0"))
    if name == "meter":
        return (C(cx, cy, k * 0.9, "none", f'stroke="{c}" stroke-width="{sw}"') +
                P(f"M {cx} {cy} L {cx+k*0.5} {cy-k*0.42}") +
                C(cx, cy, k * 0.12, c))
    if name == "leafapp":
        return (f'<path d="M {cx-k*0.8} {cy+k*0.7} c 0 {-k*1.1} {k*0.8} {-k*1.6} {k*1.6} {-k*1.6} '
                f'c 0 {k*1.1} {-k*0.7} {k*1.6} {-k*1.6} {k*1.6} Z" fill="{c}"/>')
    return C(cx, cy, k * 0.7, c)


# ----------------------------------------------------------------------------
# предметные иллюстрации
# ----------------------------------------------------------------------------
def flower_head(cx, cy, r, c1, c2, core="#ffd166", n=8):
    o = []
    for i in range(n):
        a = math.radians(i * 360.0 / n)
        px, py = cx + r * 0.6 * math.cos(a), cy + r * 0.6 * math.sin(a)
        o.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{r*0.44}" ry="{r*0.3}" '
                 f'fill="{lgrad(c1, c2)}" transform="rotate({i*360.0/n} {px:.1f} {py:.1f})"/>')
    o.append(C(cx, cy, r * 0.42, rgrad("#fff3a0", core)))
    return "".join(o)


def bouquet(cx, cy, s, palette, wrap=("#f6e6f2", "#e7c9dd"), heads=7):
    """cy — низ букета (точка обвязки)"""
    o = []
    random_seed = int(abs(cx) + abs(cy)) % 7
    spots = [(-1.0, -1.5), (0.0, -1.85), (1.0, -1.5), (-0.6, -1.0), (0.62, -1.02),
             (0.0, -1.18), (-1.3, -0.9), (1.3, -0.92)]
    for i in range(min(heads, len(spots))):
        dx, dy = spots[i]
        o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+dx*48*s:.1f}" y2="{cy+dy*48*s:.1f}" '
                 f'stroke="#4e9440" stroke-width="{8*s}" stroke-linecap="round"/>')
    for i in range(min(heads, len(spots))):
        dx, dy = spots[i]
        c1, c2 = palette[(i + random_seed) % len(palette)]
        o.append(flower_head(cx + dx * 48 * s, cy + dy * 48 * s, 36 * s, c1, c2))
    o.append(f'<path d="M {cx-62*s} {cy-30*s} L {cx+62*s} {cy-30*s} L {cx+40*s} {cy+76*s} '
             f'L {cx-40*s} {cy+76*s} Z" fill="{lgrad(wrap[0], wrap[1])}" stroke="#d9bdd0" '
             f'stroke-width="{3*s}"/>')
    o.append(RR(cx - 66 * s, cy - 18 * s, 132 * s, 22 * s, 11 * s, lgrad("#ff9bb8", "#e2548a")))
    return "".join(o)


def food_icon(kind, cx, cy, r):
    if kind == "pizza":
        return (f'<path d="M {cx} {cy-r} L {cx+r*0.86} {cy+r*0.74} L {cx-r*0.86} {cy+r*0.74} Z" '
                f'fill="{lgrad("#ffd166", "#f0920b")}" stroke="#c96a12" stroke-width="4" '
                f'stroke-linejoin="round"/>' +
                C(cx, cy + r * 0.1, r * 0.16, "#e2443c") + C(cx - r * 0.3, cy + r * 0.48, r * 0.13, "#e2443c") +
                C(cx + r * 0.32, cy + r * 0.44, r * 0.13, "#e2443c"))
    if kind == "sushi":
        return (f'<ellipse cx="{cx}" cy="{cy}" rx="{r*0.82}" ry="{r*0.72}" fill="#ffffff" '
                f'stroke="#d8dae6" stroke-width="4"/>' +
                f'<ellipse cx="{cx}" cy="{cy-r*0.16}" rx="{r*0.5}" ry="{r*0.34}" fill="#ff8a6b"/>' +
                RR(cx - r * 0.86, cy - r * 0.2, r * 0.2, r * 0.9, r * 0.08, "#2f6b4a") +
                RR(cx + r * 0.66, cy - r * 0.2, r * 0.2, r * 0.9, r * 0.08, "#2f6b4a"))
    if kind == "burger":
        return (f'<path d="M {cx-r*0.86} {cy-r*0.2} a {r*0.86} {r*0.7} 0 0 1 {r*1.72} 0 Z" '
                f'fill="{lgrad("#ffcd7a", "#e09a3c")}"/>' +
                RR(cx - r * 0.86, cy - r * 0.18, r * 1.72, r * 0.22, r * 0.1, "#7ec850") +
                RR(cx - r * 0.82, cy + r * 0.02, r * 1.64, r * 0.3, r * 0.1, "#9c5a28") +
                RR(cx - r * 0.86, cy + r * 0.34, r * 1.72, r * 0.34, r * 0.16, lgrad("#ffcd7a", "#d98e34")))
    if kind == "coffee":
        return (RR(cx - r * 0.6, cy - r * 0.6, r * 1.2, r * 1.3, r * 0.2, "#ffffff",
                   'stroke="#d8dae6" stroke-width="4"') +
                RR(cx - r * 0.6, cy - r * 0.6, r * 1.2, r * 0.42, r * 0.2, "#8a5a3a") +
                f'<path d="M {cx+r*0.62} {cy-r*0.2} a {r*0.3} {r*0.3} 0 0 1 0 {r*0.6}" fill="none" '
                f'stroke="#d8dae6" stroke-width="5"/>')
    if kind == "cake":
        return (RR(cx - r * 0.76, cy - r * 0.2, r * 1.52, r * 0.9, r * 0.14, lgrad("#ffd1e8", "#f093c0")) +
                RR(cx - r * 0.76, cy - r * 0.46, r * 1.52, r * 0.3, r * 0.14, lgrad("#fff6e2", "#f0dcb0")) +
                C(cx, cy - r * 0.58, r * 0.16, "#e2443c"))
    if kind == "salad":
        return (f'<path d="M {cx-r*0.8} {cy-r*0.1} a {r*0.8} {r*0.7} 0 0 0 {r*1.6} 0 Z" fill="#ffffff" '
                f'stroke="#d8dae6" stroke-width="4"/>' +
                C(cx - r * 0.3, cy - r * 0.24, r * 0.22, "#7ec850") + C(cx + r * 0.18, cy - r * 0.3, r * 0.2, "#e2443c") +
                C(cx + r * 0.44, cy - r * 0.16, r * 0.16, "#ffd166"))
    return C(cx, cy, r * 0.8, "#dfe4ee")


def map_bg(x, y, w, h, r=0):
    """стилизованная карта"""
    o = [RR(x, y, w, h, r, "#e9eef2")]
    import random as _r
    _r.seed(5)
    for i in range(26):
        bx = x + _r.randint(0, int(w) - 160)
        by = y + _r.randint(0, int(h) - 160)
        o.append(RR(bx, by, _r.randint(90, 190), _r.randint(80, 170), 14, "#dde4ea"))
    o.append(f'<path d="M {x} {y+h*0.26} h {w}" stroke="#ffffff" stroke-width="34"/>')
    o.append(f'<path d="M {x} {y+h*0.62} h {w}" stroke="#ffffff" stroke-width="40"/>')
    o.append(f'<path d="M {x+w*0.3} {y} v {h}" stroke="#ffffff" stroke-width="36"/>')
    o.append(f'<path d="M {x+w*0.74} {y} v {h}" stroke="#ffffff" stroke-width="30"/>')
    o.append(f'<path d="M {x} {y+h*0.9} L {x+w} {y+h*0.42}" stroke="#ffffff" stroke-width="26"/>')
    o.append(f'<path d="M {x+w*0.04} {y+h*0.08} q {w*0.2} {h*0.1} {w*0.16} {h*0.26} '
             f'q {-w*0.04} {h*0.12} {-w*0.2} {h*0.1} Z" fill="#cfe8c9"/>')
    o.append(f'<path d="M {x+w*0.62} {y+h*0.72} q {w*0.2} {-h*0.06} {w*0.4} {h*0.06} '
             f'l 0 {h*0.3} l {-w*0.4} 0 Z" fill="#cfe8c9"/>')
    o.append(f'<path d="M {x+w} {y+h*0.12} q {-w*0.34} {h*0.12} {-w*0.4} {h*0.34} '
             f'q {-w*0.04} {h*0.16} {-w*0.3} {h*0.22}" fill="none" stroke="#bfdcf0" stroke-width="46"/>')
    return "".join(o)


def map_pin(cx, cy, c="#2b6ad6", s=1.0, label=None):
    o = [f'<ellipse cx="{cx}" cy="{cy+6*s}" rx="{22*s}" ry="{8*s}" fill="#1d233530"/>',
         f'<path d="M {cx} {cy} c {34*s} {-34*s} {28*s} {-54*s} {28*s} {-64*s} '
         f'a {28*s} {28*s} 0 1 0 {-56*s} 0 c 0 {10*s} {-6*s} {30*s} {28*s} {64*s} Z" '
         f'fill="{c}" stroke="#ffffff" stroke-width="{5*s}"/>',
         C(cx, cy - 64 * s, 11 * s, "#ffffff")]
    if label:
        o.append(T(cx, cy - 54 * s, label, 30 * s, fill=c, w=800, fam=F))
        o[-2] = C(cx, cy - 64 * s, 18 * s, "#ffffff")
    return "".join(o)
