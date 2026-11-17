# -*- coding: utf-8 -*-
"""Генератор макетов игровых экранов (1080x1920) -> HTML c inline SVG.
Рендер в PNG делается отдельно через headless Edge (render.ps1)."""

import os, math, random

W, H = 1080, 1920
ROOT = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(ROOT, "html")

F = "Segoe UI, Arial, sans-serif"
FB = "Arial Black, Segoe UI Black, Segoe UI, Arial, sans-serif"

DEFS = []
CNT = [0]


def uid(p="x"):
    CNT[0] += 1
    return "%s%d" % (p, CNT[0])


def lgrad(c1, c2, d="v"):
    i = uid("lg")
    x1, y1, x2, y2 = {"v": ("0", "0", "0", "1"),
                      "h": ("0", "0", "1", "0"),
                      "d": ("0", "0", "1", "1")}[d]
    DEFS.append('<linearGradient id="%s" x1="%s" y1="%s" x2="%s" y2="%s">'
                '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/>'
                '</linearGradient>' % (i, x1, y1, x2, y2, c1, c2))
    return "url(#%s)" % i


def lgrad3(c1, c2, c3, d="v"):
    i = uid("lg")
    x1, y1, x2, y2 = {"v": ("0", "0", "0", "1"), "h": ("0", "0", "1", "0"),
                      "d": ("0", "0", "1", "1")}[d]
    DEFS.append('<linearGradient id="%s" x1="%s" y1="%s" x2="%s" y2="%s">'
                '<stop offset="0" stop-color="%s"/><stop offset="0.5" stop-color="%s"/>'
                '<stop offset="1" stop-color="%s"/></linearGradient>' % (i, x1, y1, x2, y2, c1, c2, c3))
    return "url(#%s)" % i


def rgrad(c1, c2, cx="34%", cy="28%", r="76%"):
    i = uid("rg")
    DEFS.append('<radialGradient id="%s" cx="%s" cy="%s" r="%s">'
                '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/>'
                '</radialGradient>' % (i, cx, cy, r, c1, c2))
    return "url(#%s)" % i


def fade(c, o1=0.5, o2=0.0):
    i = uid("fd")
    DEFS.append('<radialGradient id="%s"><stop offset="0" stop-color="%s" stop-opacity="%s"/>'
                '<stop offset="1" stop-color="%s" stop-opacity="%s"/></radialGradient>' % (i, c, o1, c, o2))
    return "url(#%s)" % i


FILTERS = (
    '<filter id="sh" x="-60%" y="-60%" width="220%" height="220%">'
    '<feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#120a24" flood-opacity="0.45"/></filter>'
    '<filter id="shs" x="-60%" y="-60%" width="220%" height="220%">'
    '<feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#120a24" flood-opacity="0.35"/></filter>'
    '<filter id="glow" x="-80%" y="-80%" width="260%" height="260%">'
    '<feGaussianBlur stdDeviation="16" result="b"/><feMerge>'
    '<feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
    '<filter id="blur" x="-50%" y="-50%" width="200%" height="200%">'
    '<feGaussianBlur stdDeviation="26"/></filter>'
)


def T(x, y, s, size, fill="#fff", w=900, anchor="middle", fam=FB,
      stroke=None, sw=10, op=1, ls=0, extra=""):
    st = ""
    if stroke:
        st = ' stroke="%s" stroke-width="%s" paint-order="stroke" stroke-linejoin="round"' % (stroke, sw)
    return ('<text x="%s" y="%s" font-family="%s" font-size="%s" font-weight="%s" '
            'text-anchor="%s" fill="%s" opacity="%s" letter-spacing="%s"%s %s>%s</text>'
            % (x, y, fam, size, w, anchor, fill, op, ls, st, extra, s))


def RR(x, y, w, h, r, fill, extra=""):
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" %s/>' % (x, y, w, h, r, fill, extra)


def C(cx, cy, r, fill, extra=""):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s" %s/>' % (cx, cy, r, fill, extra)


def gloss(x, y, w, h, r, op=0.30):
    """блик на верхней половине кнопки"""
    return RR(x + w * 0.06, y + h * 0.10, w * 0.88, h * 0.36, r * 0.6, "#ffffff", 'opacity="%s"' % op)


def btn(x, y, w, h, r, c1, c2, label="", size=40, txt="#ffffff",
        lip="#00000040", outline="#ffffff55", tstroke=None, fam=FB):
    o = []
    o.append(RR(x, y + 10, w, h, r, lip))
    o.append(RR(x, y, w, h, r, lgrad(c1, c2), 'stroke="%s" stroke-width="4"' % outline))
    o.append(gloss(x, y, w, h, r))
    if label:
        o.append(T(x + w / 2.0, y + h / 2.0 + size * 0.36, label, size, fill=txt,
                   stroke=tstroke, sw=8, fam=fam))
    return "".join(o)


def pill(x, y, w, h, c1, c2, outline="#ffffff44"):
    return (RR(x, y + 6, w, h, h / 2.0, "#00000035") +
            RR(x, y, w, h, h / 2.0, lgrad(c1, c2), 'stroke="%s" stroke-width="3"' % outline) +
            RR(x + 10, y + 6, w - 20, h * 0.34, h * 0.2, "#ffffff", 'opacity="0.22"'))


def coin(cx, cy, r, c1="#ffe08a", c2="#f0a500", rim="#b96d00", sym="$"):
    o = [C(cx, cy, r, rgrad(c1, c2), 'stroke="%s" stroke-width="%s"' % (rim, max(2, r * 0.12))),
         C(cx, cy, r * 0.68, "none", 'stroke="#ffffff" stroke-opacity="0.45" stroke-width="%s"' % (r * 0.1)),
         '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff" opacity="0.6" transform="rotate(-30 %s %s)"/>'
         % (cx - r * 0.3, cy - r * 0.35, r * 0.28, r * 0.16, cx - r * 0.3, cy - r * 0.35)]
    if sym:
        o.append(T(cx, cy + r * 0.34, sym, r * 1.0, fill="#b96d00", fam=FB))
    return "".join(o)


def gemicon(cx, cy, r, c1="#8ef1ff", c2="#2196f3"):
    p = "M %s %s L %s %s L %s %s L %s %s L %s %s L %s %s Z" % (
        cx, cy - r, cx + r * 0.88, cy - r * 0.35, cx + r * 0.72, cy + r * 0.8,
        cx - r * 0.72, cy + r * 0.8, cx - r * 0.88, cy - r * 0.35, cx, cy - r)
    return ('<path d="%s" fill="%s" stroke="#0b5aa8" stroke-width="%s" stroke-linejoin="round"/>'
            '<path d="M %s %s L %s %s L %s %s Z" fill="#ffffff" opacity="0.45"/>'
            % (p, lgrad(c1, c2), max(2, r * 0.12), cx, cy - r, cx - r * 0.88, cy - r * 0.35,
               cx - r * 0.1, cy + r * 0.1))


def heart(cx, cy, r, c1="#ff7d93", c2="#e01e46"):
    d = ("M %s %s C %s %s %s %s %s %s C %s %s %s %s %s %s "
         "C %s %s %s %s %s %s C %s %s %s %s %s %s Z" % (
        cx, cy + r * 0.85,
        cx - r * 1.05, cy + r * 0.05, cx - r * 0.95, cy - r * 0.75, cx - r * 0.45, cy - r * 0.75,
        cx - r * 0.18, cy - r * 0.75, cx - r * 0.02, cy - r * 0.5, cx, cy - r * 0.38,
        cx + r * 0.02, cy - r * 0.5, cx + r * 0.18, cy - r * 0.75, cx + r * 0.45, cy - r * 0.75,
        cx + r * 0.95, cy - r * 0.75, cx + r * 1.05, cy + r * 0.05, cx, cy + r * 0.85))
    return ('<path d="%s" fill="%s" stroke="#9c0f30" stroke-width="%s" stroke-linejoin="round"/>'
            '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff" opacity="0.5" transform="rotate(-25 %s %s)"/>'
            % (d, rgrad(c1, c2), max(2, r * 0.12), cx - r * 0.38, cy - r * 0.32, r * 0.22, r * 0.13,
               cx - r * 0.38, cy - r * 0.32))


def star(cx, cy, r, fill, stroke="#b06a00", sw=4, rot=-90, inner=0.46, op=1):
    pts = []
    for i in range(10):
        a = math.radians(rot + i * 36)
        rr = r if i % 2 == 0 else r * inner
        pts.append("%.1f,%.1f" % (cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return '<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round" opacity="%s"/>' % (
        " ".join(pts), fill, stroke, sw, op)


def poly(cx, cy, r, n, rot, fill, stroke="#00000030", sw=4):
    pts = []
    for i in range(n):
        a = math.radians(rot + i * 360.0 / n)
        pts.append("%.1f,%.1f" % (cx + r * math.cos(a), cy + r * math.sin(a)))
    return '<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (
        " ".join(pts), fill, stroke, sw)


def sparkle(cx, cy, r, c="#ffffff", op=0.9):
    d = ("M %s %s Q %s %s %s %s Q %s %s %s %s Q %s %s %s %s Q %s %s %s %s Z" % (
        cx, cy - r, cx + r * 0.16, cy - r * 0.16, cx + r, cy,
        cx + r * 0.16, cy + r * 0.16, cx, cy + r,
        cx - r * 0.16, cy + r * 0.16, cx - r, cy,
        cx - r * 0.16, cy - r * 0.16, cx, cy - r))
    return '<path d="%s" fill="%s" opacity="%s"/>' % (d, c, op)


# строка состояния телефона; NO_STATUSBAR=1 убирает её (чистые кадры для стора)
SHOW_STATUSBAR = os.environ.get("NO_STATUSBAR") != "1"


def statusbar(color="#ffffff", op=0.92):
    if not SHOW_STATUSBAR:
        return ""
    o = [T(58, 64, "9:41", 36, fill=color, w=700, anchor="start", fam=F, op=op)]
    x = W - 248
    for i in range(4):
        hh = 12 + i * 9
        o.append('<rect x="%s" y="%s" width="10" height="%s" rx="3" fill="%s" opacity="%s"/>'
                 % (x + i * 16, 62 - hh, hh, color, op if i < 3 else 0.45))
    cx, cy = W - 160, 60
    for rr in (13, 24, 35):
        o.append('<path d="M %s %s A %s %s 0 0 1 %s %s" fill="none" stroke="%s" stroke-width="6" '
                 'stroke-linecap="round" opacity="%s"/>' % (cx - rr * 0.78, cy - rr * 0.55, rr, rr,
                                                            cx + rr * 0.78, cy - rr * 0.55, color, op))
    o.append(C(cx, cy - 2, 5, color, 'opacity="%s"' % op))
    o.append('<rect x="%s" y="36" width="66" height="30" rx="10" fill="none" stroke="%s" stroke-width="4" opacity="%s"/>'
             % (W - 116, color, op))
    o.append('<rect x="%s" y="42" width="46" height="18" rx="6" fill="%s" opacity="%s"/>' % (W - 110, color, op))
    o.append('<rect x="%s" y="44" width="8" height="14" rx="3" fill="%s" opacity="%s"/>' % (W - 44, color, op))
    return "".join(o)


def bg_blobs(colors, seed=1, n=6, rmin=180, rmax=420, op=0.5):
    random.seed(seed)
    o = []
    for i in range(n):
        c = colors[i % len(colors)]
        cx = random.randint(-100, W + 100)
        cy = random.randint(100, H)
        r = random.randint(rmin, rmax)
        o.append(C(cx, cy, r, fade(c, op, 0.0)))
    return "".join(o)


def confetti(seed=3, n=60, colors=("#ffffff",), op=0.35):
    random.seed(seed)
    o = []
    for _ in range(n):
        x = random.randint(0, W)
        y = random.randint(90, H - 60)
        r = random.choice([3, 4, 5, 6, 7])
        c = random.choice(colors)
        if random.random() < 0.35:
            o.append(star(x, y, r * 1.8, c, stroke="none", sw=0, op=op))
        else:
            o.append(C(x, y, r, c, 'opacity="%s"' % op))
    return "".join(o)


def page(svg_body, title):
    return ('<!doctype html><html><head><meta charset="utf-8"><title>%s</title>'
            '<style>html,body{margin:0;padding:0;background:#000;overflow:hidden}svg{display:block}</style>'
            '</head><body><svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 %d %d"><defs>%s%s</defs>%s</svg></body></html>'
            % (title, W, H, W, H, FILTERS, "".join(DEFS), svg_body))


def write(name, body, title):
    if not os.path.isdir(HTML_DIR):
        os.makedirs(HTML_DIR)
    with open(os.path.join(HTML_DIR, name + ".html"), "w", encoding="utf-8") as f:
        f.write(page(body, title))
    print("ok", name)


# ----------------------------------------------------------------------------
# 1. MATCH-3
# ----------------------------------------------------------------------------
CANDY = [("#ff6b8a", "#d11149", "#8c0a2e"),    # 0 круг  розовый
         ("#6fd3ff", "#1273de", "#0a4a8f"),    # 1 квадрат синий
         ("#ffd95e", "#f49200", "#a85c00"),    # 2 звезда жёлтая
         ("#9bf07a", "#2fa84f", "#176b31"),    # 3 капля зелёная
         ("#d59bff", "#7b2cbf", "#4a1480"),    # 4 шестиугольник фиолет
         ("#ffa45c", "#e2560f", "#8f3203")]    # 5 сердце оранж


def candy(cx, cy, r, k, special=None):
    c1, c2, cd = CANDY[k]
    g = rgrad(c1, c2)
    o = []
    cid = uid("cl")
    if k == 0:
        shape = C(cx, cy, r, g, 'stroke="%s" stroke-width="5"' % cd)
        clip = '<circle cx="%s" cy="%s" r="%s"/>' % (cx, cy, r)
    elif k == 1:
        shape = RR(cx - r * 0.9, cy - r * 0.9, r * 1.8, r * 1.8, r * 0.42, g,
                   'stroke="%s" stroke-width="5"' % cd)
        clip = '<rect x="%s" y="%s" width="%s" height="%s" rx="%s"/>' % (
            cx - r * 0.9, cy - r * 0.9, r * 1.8, r * 1.8, r * 0.42)
    elif k == 2:
        shape = star(cx, cy, r * 1.08, g, stroke=cd, sw=5)
        clip = '<circle cx="%s" cy="%s" r="%s"/>' % (cx, cy, r)
    elif k == 3:
        d = ("M %s %s C %s %s %s %s %s %s C %s %s %s %s %s %s Z" % (
            cx, cy - r * 1.05,
            cx + r * 0.72, cy - r * 0.35, cx + r, cy + r * 0.28, cx, cy + r,
            cx - r, cy + r * 0.28, cx - r * 0.72, cy - r * 0.35, cx, cy - r * 1.05))
        shape = '<path d="%s" fill="%s" stroke="%s" stroke-width="5" stroke-linejoin="round"/>' % (d, g, cd)
        clip = '<circle cx="%s" cy="%s" r="%s"/>' % (cx, cy, r * 0.95)
    elif k == 4:
        shape = poly(cx, cy, r * 1.02, 6, 90, g, cd, 5)
        clip = '<circle cx="%s" cy="%s" r="%s"/>' % (cx, cy, r)
    else:
        shape = heart(cx, cy, r * 0.95, c1, c2)
        clip = '<circle cx="%s" cy="%s" r="%s"/>' % (cx, cy, r * 0.9)
    o.append(shape)
    o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff" opacity="0.55" '
             'transform="rotate(-28 %s %s)"/>' % (cx - r * 0.32, cy - r * 0.38, r * 0.3, r * 0.17,
                                                  cx - r * 0.32, cy - r * 0.38))
    if special == "stripe":
        DEFS.append('<clipPath id="%s">%s</clipPath>' % (cid, clip))
        s = ['<g clip-path="url(#%s)">' % cid]
        for i in (-1, 0, 1):
            s.append(RR(cx - r, cy + i * r * 0.46 - r * 0.11, r * 2, r * 0.22, r * 0.1, "#ffffff",
                        'opacity="0.85"'))
        s.append("</g>")
        o.append("".join(s))
    elif special == "bomb":
        o.append(C(cx, cy, r * 1.26, "none", 'stroke="#ffffff" stroke-width="6" stroke-opacity="0.9" '
                                             'stroke-dasharray="14 12"'))
        for a in (20, 140, 260):
            ax = cx + r * 1.5 * math.cos(math.radians(a))
            ay = cy + r * 1.5 * math.sin(math.radians(a))
            o.append(sparkle(ax, ay, r * 0.4, "#fff6b0", 0.95))
    elif special == "rainbow":
        o = [C(cx, cy, r, "#2b1b4a", 'stroke="#ffffff" stroke-width="5"')]
        for i, (a1, a2) in enumerate([(0, 60), (60, 120), (120, 180), (180, 240), (240, 300), (300, 360)]):
            x1 = cx + r * math.cos(math.radians(a1))
            y1 = cy + r * math.sin(math.radians(a1))
            x2 = cx + r * math.cos(math.radians(a2))
            y2 = cy + r * math.sin(math.radians(a2))
            o.append('<path d="M %s %s L %.1f %.1f A %s %s 0 0 1 %.1f %.1f Z" fill="%s" opacity="0.95"/>'
                     % (cx, cy, x1, y1, r, r, x2, y2, CANDY[i][0]))
        o.append(C(cx, cy, r * 0.3, "#ffffff", 'opacity="0.9"'))
        o.append(C(cx, cy, r, "none", 'stroke="#ffffff" stroke-width="5"'))
        for a in (30, 150, 270):
            o.append(sparkle(cx + r * 1.45 * math.cos(math.radians(a)),
                             cy + r * 1.45 * math.sin(math.radians(a)), r * 0.38, "#ffffff", 0.95))
    return "".join(o)


def screen_match3():
    o = []
    o.append(RR(0, 0, W, H, 0, lgrad3("#5b2a9e", "#3a1b73", "#1d0d45")))
    o.append(bg_blobs(["#ff6ec7", "#4cc9f0", "#b388ff"], seed=5, n=7, op=0.45))
    o.append(confetti(seed=11, n=50, colors=("#ffffff", "#ffe08a", "#8ef1ff"), op=0.3))
    o.append(statusbar())

    # --- верхняя строка ресурсов
    o.append(pill(48, 104, 220, 76, "#ff8fa8", "#d6234f"))
    o.append(heart(92, 142, 30))
    o.append(T(196, 158, "5", 46, stroke="#8c0a2e", sw=8))
    o.append(pill(296, 104, 268, 76, "#ffd979", "#e8870b"))
    o.append(coin(338, 142, 30))
    o.append(T(452, 158, "12 480", 38, stroke="#8a4b00", sw=8))
    o.append(pill(592, 104, 236, 76, "#7fd9ff", "#1273de"))
    o.append(gemicon(634, 142, 30))
    o.append(T(736, 158, "356", 42, stroke="#0a4a8f", sw=8))
    o.append(btn(856, 100, 84, 84, 26, "#8c6bd6", "#5a36a8", "", 0))
    o.append(RR(884, 124, 12, 36, 5, "#ffffff"))
    o.append(RR(906, 124, 12, 36, 5, "#ffffff"))
    o.append(btn(956, 100, 84, 84, 26, "#8c6bd6", "#5a36a8", "", 0))
    o.append(T(998, 160, "⚙", 48, fill="#ffffff", fam=F))

    # --- панель цели
    o.append(RR(60, 212, 960, 196, 44, "#00000040"))
    o.append(RR(60, 212, 960, 196, 44, lgrad("#43218f", "#2a1263"),
                'stroke="#b388ff" stroke-width="5"'))
    o.append(RR(80, 226, 920, 60, 30, "#ffffff", 'opacity="0.10"'))
    o.append(pill(380, 186, 320, 68, "#ffd979", "#e8870b"))
    o.append(T(540, 236, "УРОВЕНЬ 24", 38, stroke="#8a4b00", sw=8))

    goals = [(0, "12", False), (2, "8", False), (4, "5", True)]
    gx = 230
    for i, (k, num, done) in enumerate(goals):
        x = gx + i * 230
        o.append(C(x, 332, 62, "#00000035"))
        o.append(candy(x, 328, 48, k))
        o.append(RR(x + 18, 352, 92, 54, 24, "#1d0d45", 'stroke="#b388ff" stroke-width="4"'))
        if done:
            o.append('<path d="M %s %s l 16 18 l 30 -36" fill="none" stroke="#6ef08a" stroke-width="10" '
                     'stroke-linecap="round" stroke-linejoin="round"/>' % (x + 42, 378))
        else:
            o.append(T(x + 64, 395, num, 40, stroke="#000000", sw=0))

    # --- прогресс-бар со звёздами
    o.append(RR(120, 440, 840, 42, 21, "#1d0d45", 'stroke="#000000" stroke-opacity="0.35" stroke-width="3"'))
    o.append(RR(124, 444, 560, 34, 17, lgrad("#8ef1ff", "#2196f3")))
    o.append(RR(136, 450, 530, 12, 6, "#ffffff", 'opacity="0.35"'))
    for i, sx in enumerate((400, 680, 930)):
        filled = i == 0
        o.append(star(sx, 461, 40, lgrad("#ffe9a8", "#f5a800") if filled else "#2b1b4a",
                      stroke="#b06a00" if filled else "#5a36a8", sw=5))

    # --- игровое поле
    bx, by, cols, rows, cell = 70, 520, 8, 9, 118
    bw, bh = cols * cell, rows * cell
    o.append(RR(bx - 18, by - 18, bw + 36, bh + 44, 48, "#00000050"))
    o.append(RR(bx - 18, by - 18, bw + 36, bh + 36, 48, lgrad("#2e1566", "#1a0b40"),
                'stroke="#7b4bd6" stroke-width="6"'))
    random.seed(42)
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            opts = list(range(6))
            if c >= 2 and row[c - 1] == row[c - 2] and row[c - 1] in opts:
                opts.remove(row[c - 1])
            if r >= 2 and grid[r - 1][c] == grid[r - 2][c] and grid[r - 1][c] in opts:
                opts.remove(grid[r - 1][c])
            row.append(random.choice(opts))
        grid.append(row)
    specials = {(2, 3): "stripe", (5, 6): "bomb", (7, 1): "rainbow", (4, 2): "stripe"}
    for r in range(rows):
        for c in range(cols):
            cx = bx + c * cell + cell / 2.0
            cy = by + r * cell + cell / 2.0
            o.append(RR(cx - cell / 2 + 6, cy - cell / 2 + 6, cell - 12, cell - 12, 24,
                        "#ffffff", 'opacity="%s"' % (0.07 if (r + c) % 2 == 0 else 0.03)))
            o.append('<g filter="url(#shs)">%s</g>' % candy(cx, cy, 44, grid[r][c], specials.get((r, c))))
    # подсветка выбранной фишки
    o.append(RR(bx + 3 * cell + 4, by + 2 * cell + 4, cell - 8, cell - 8, 26, "none",
                'stroke="#ffffff" stroke-width="6" stroke-dasharray="18 14" opacity="0.95"'))

    # --- бустеры
    labels = [("⚒", "5", "#ff9e6b", "#e2560f"), ("✦", "2", "#7fd9ff", "#1273de"),
              ("↻", "3", "#9bf07a", "#2fa84f")]
    for i, (ic, n, c1, c2) in enumerate(labels):
        x = 148 + i * 300
        o.append(btn(x, 1660, 160, 150, 44, c1, c2))
        o.append(T(x + 80, 1760, ic, 86, fill="#ffffff", fam=F, stroke="#00000030", sw=4))
        o.append(C(x + 150, 1670, 32, lgrad("#ff6b8a", "#d11149"), 'stroke="#ffffff" stroke-width="4"'))
        o.append(T(x + 150, 1684, n, 34, stroke=None))
    o.append(T(540, 1872, "НАЙДИ ХОД  •  ОСТАЛОСЬ 23", 34, fill="#ffffff", op=0.75, fam=F, w=700, ls=2))
    return "".join(o)


# ----------------------------------------------------------------------------
# 2. MERGE
# ----------------------------------------------------------------------------
FRUIT = [("#ff7a7a", "#d62828", "#8c0a0a"), ("#ffc46b", "#f3722c", "#a63d00"),
         ("#ffe066", "#fcbf49", "#a87800"), ("#b8f07a", "#55a630", "#2b6b16"),
         ("#8ef1d6", "#13a383", "#0a6b56"), ("#9bb8ff", "#3f6fd8", "#1d3f91"),
         ("#d9a6ff", "#8338ec", "#4a1480")]


def fruit(cx, cy, r, lvl):
    c1, c2, cd = FRUIT[lvl % len(FRUIT)]
    o = [C(cx, cy + r * 0.12, r * 0.95, "#00000030"),
         C(cx, cy, r, rgrad(c1, c2), 'stroke="%s" stroke-width="5"' % cd)]
    o.append('<path d="M %s %s q %s %s %s %s q %s %s %s %s Z" fill="#4fae3e" stroke="#2b6b16" stroke-width="4"/>'
             % (cx + r * 0.1, cy - r * 0.92, r * 0.5, -r * 0.42, r * 0.78, -r * 0.1,
                -r * 0.3, r * 0.38, -r * 0.78, r * 0.1))
    o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff" opacity="0.6" '
             'transform="rotate(-30 %s %s)"/>' % (cx - r * 0.34, cy - r * 0.36, r * 0.26, r * 0.15,
                                                  cx - r * 0.34, cy - r * 0.36))
    o.append(RR(cx - r * 0.52, cy + r * 0.44, r * 1.04, r * 0.44, r * 0.22, "#00000055"))
    o.append(T(cx, cy + r * 0.78, str(lvl + 1), r * 0.44, fill="#ffffff", fam=FB))
    return "".join(o)


def screen_merge():
    o = []
    o.append(RR(0, 0, W, H, 0, lgrad3("#7fd4ff", "#b7ebc0", "#5aa84f")))
    # холмы
    o.append('<path d="M 0 760 Q 270 620 540 730 Q 810 840 1080 700 L 1080 1920 L 0 1920 Z" fill="%s"/>'
             % lgrad("#86d46a", "#3f8f3a"))
    o.append('<path d="M 0 900 Q 300 800 620 900 Q 860 970 1080 880 L 1080 1920 L 0 1920 Z" fill="%s"/>'
             % lgrad("#6fc258", "#2f7a2f"))
    o.append(C(880, 300, 150, fade("#fff6b0", 0.7, 0.0)))
    o.append(C(880, 300, 76, "#fff3a0", 'opacity="0.95"'))
    for cx, cy, s in ((200, 330, 1.0), (640, 250, 0.7), (960, 520, 0.55)):
        o.append('<g opacity="0.85"><ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff"/>'
                 '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff"/>'
                 '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff"/></g>'
                 % (cx, cy, 90 * s, 54 * s, cx - 70 * s, cy + 16 * s, 60 * s, 38 * s,
                    cx + 72 * s, cy + 18 * s, 54 * s, 34 * s))
    o.append(statusbar("#143d2b", 0.8))

    # HUD
    o.append(pill(48, 104, 280, 78, "#ffd979", "#e8870b"))
    o.append(coin(92, 143, 32))
    o.append(T(220, 160, "48 920", 38, stroke="#8a4b00", sw=8))
    o.append(C(314, 143, 30, lgrad("#9bf07a", "#2fa84f"), 'stroke="#ffffff" stroke-width="4"'))
    o.append(T(314, 157, "+", 42, stroke=None))
    o.append(pill(356, 104, 250, 78, "#c9a3ff", "#6a2fd0"))
    o.append(gemicon(398, 143, 30, "#f5c6ff", "#c454f0"))
    o.append(T(512, 160, "128", 38, stroke="#3c0a66", sw=8))
    o.append(C(592, 143, 30, lgrad("#9bf07a", "#2fa84f"), 'stroke="#ffffff" stroke-width="4"'))
    o.append(T(592, 157, "+", 42, stroke=None))
    o.append(pill(634, 104, 320, 78, "#ffe98a", "#f49200"))
    o.append(T(686, 160, "⚡", 46, fill="#fff6b0", fam=F, stroke="#a85c00", sw=6))
    o.append(RR(716, 120, 184, 46, 23, "#5a3000"))
    o.append(RR(720, 124, 128, 38, 19, lgrad("#ffe066", "#f3a000")))
    o.append(T(808, 155, "47/50", 30, stroke="#5a3000", sw=6))
    o.append(btn(968, 100, 84, 86, 26, "#8ce1ff", "#2b8fd6"))
    o.append(T(1010, 162, "☰", 44, fill="#ffffff", fam=F))

    # квест-карточка
    o.append(RR(48, 214, 560, 150, 40, "#00000030"))
    o.append(RR(48, 214, 560, 150, 40, lgrad("#fff6e2", "#ffd9a0"), 'stroke="#b96d00" stroke-width="5"'))
    o.append(T(80, 272, "ЗАКАЗ", 32, fill="#a85c00", anchor="start", ls=3))
    o.append(RR(76, 288, 92, 62, 20, "#ffffff", 'stroke="#d8a257" stroke-width="4"'))
    o.append(fruit(122, 318, 26, 3))
    o.append(T(196, 342, "× 3", 44, fill="#5a3000", anchor="start"))
    o.append(RR(300, 292, 180, 56, 28, "#e8c99a"))
    o.append(RR(304, 296, 112, 48, 24, lgrad("#9bf07a", "#2fa84f")))
    o.append(T(390, 332, "2/3", 32, fill="#ffffff", stroke="#176b31", sw=6))
    o.append(btn(498, 286, 92, 68, 26, "#ffd979", "#e8870b"))
    o.append(coin(544, 320, 24))
    o.append(RR(640, 214, 180, 150, 40, lgrad("#ffb3c9", "#e5407a"), 'stroke="#ffffff" stroke-width="5"'))
    o.append(T(730, 288, "★", 54, fill="#fff6b0", fam=F, stroke="#9c0f30", sw=6))
    o.append(T(730, 340, "СОБЫТИЕ", 24, fill="#ffffff", ls=1))
    o.append(RR(852, 214, 180, 150, 40, lgrad("#8ce1ff", "#2b8fd6"), 'stroke="#ffffff" stroke-width="5"'))
    o.append(T(942, 292, "⚑", 58, fill="#ffffff", fam=F, stroke="#0a4a8f", sw=6))
    o.append(T(942, 340, "СЕЗОН", 24, fill="#ffffff", ls=1))

    # поле мержа
    bx, by, cols, rows, cell = 86, 440, 5, 7, 182
    bw, bh = cols * cell, rows * cell
    o.append(RR(bx - 22, by - 22, bw + 44, bh + 52, 54, "#00000040"))
    o.append(RR(bx - 22, by - 22, bw + 44, bh + 44, 54, lgrad("#a9703f", "#6d4220"),
                'stroke="#4a2a10" stroke-width="6"'))
    random.seed(9)
    board = [[None] * cols for _ in range(rows)]
    placed = [(0, 0, 2), (0, 2, 0), (0, 4, 1), (1, 1, 3), (1, 3, 2), (2, 0, 4), (2, 2, 1),
              (2, 4, 0), (3, 1, 5), (3, 2, 5), (3, 4, 3), (4, 0, 2), (4, 3, 1), (5, 1, 0),
              (5, 2, 4), (5, 4, 6), (6, 0, 1), (6, 2, 3)]
    for (r, c, lv) in placed:
        board[r][c] = lv
    for r in range(rows):
        for c in range(cols):
            cx = bx + c * cell + cell / 2.0
            cy = by + r * cell + cell / 2.0
            o.append(RR(cx - cell / 2 + 10, cy - cell / 2 + 10, cell - 20, cell - 20, 32,
                        lgrad("#c08a52", "#8a5a2c"), 'stroke="#5c3515" stroke-width="4"'))
            o.append(RR(cx - cell / 2 + 18, cy - cell / 2 + 18, cell - 36, cell * 0.26, 20,
                        "#ffffff", 'opacity="0.14"'))
            if board[r][c] is not None:
                o.append('<g filter="url(#shs)">%s</g>' % fruit(cx, cy, 64, board[r][c]))
    # генератор
    gcx = bx + 3 * cell + cell / 2.0
    gcy = by + 5 * cell + cell / 2.0
    o.append(RR(gcx - 62, gcy - 46, 124, 92, 24, lgrad("#ffd979", "#c47700"),
                'stroke="#6d4220" stroke-width="6"'))
    o.append(RR(gcx - 62, gcy - 58, 124, 36, 16, lgrad("#ffe9a8", "#e8870b"),
                'stroke="#6d4220" stroke-width="6"'))
    o.append(C(gcx, gcy - 6, 18, "#6d4220"))
    o.append(C(gcx + 54, gcy - 68, 34, lgrad("#9bf07a", "#2fa84f"), 'stroke="#ffffff" stroke-width="5"'))
    o.append(T(gcx + 54, gcy - 52, "+", 46, stroke=None))
    # подсветка слияния
    mx = bx + 1 * cell + cell / 2.0
    my = by + 3 * cell + cell / 2.0
    o.append(RR(mx - cell / 2 + 6, my - cell / 2 + 6, cell * 2 - 12, cell - 12, 34, "none",
                'stroke="#fff6b0" stroke-width="7" stroke-dasharray="22 16" filter="url(#glow)"'))
    o.append(T(mx + cell / 2, my - cell / 2 - 16, "СЛИЯНИЕ!", 36, fill="#fff6b0", stroke="#7a4a00", sw=8))

    # нижняя панель
    o.append(RR(0, 1730, W, 190, 0, "#00000030"))
    o.append(RR(-20, 1736, W + 40, 200, 50, lgrad("#2f7a2f", "#1b4d1f"),
                'stroke="#9bf07a" stroke-width="5"'))
    tabs = [("⌂", "ДОМ", False), ("☘", "САД", False), ("☰", "ЗАКАЗЫ", True),
            ("⚑", "ЛИГА", False), ("⚲", "МАГАЗИН", False)]
    for i, (ic, lb, act) in enumerate(tabs):
        x = 56 + i * 196
        if act:
            o.append(btn(x - 8, 1756, 172, 140, 40, "#ffd979", "#e8870b"))
            o.append(T(x + 78, 1836, ic, 60, fill="#5a3000", fam=F))
            o.append(T(x + 78, 1876, lb, 26, fill="#5a3000", ls=1))
            o.append(C(x + 148, 1762, 28, lgrad("#ff6b8a", "#d11149"), 'stroke="#ffffff" stroke-width="4"'))
            o.append(T(x + 148, 1774, "3", 30, stroke=None))
        else:
            o.append(T(x + 78, 1836, ic, 58, fill="#ffffff", fam=F, op=0.92))
            o.append(T(x + 78, 1876, lb, 26, fill="#ffffff", op=0.8, ls=1))
    return "".join(o)


# ----------------------------------------------------------------------------
# 3. BUBBLE SHOOTER
# ----------------------------------------------------------------------------
BUB = [("#ff8aa0", "#e01e46", "#8c0a2e"), ("#8ad6ff", "#1273de", "#0a4a8f"),
       ("#ffe066", "#f49200", "#a85c00"), ("#9bf07a", "#2fa84f", "#176b31"),
       ("#d9a6ff", "#7b2cbf", "#4a1480"), ("#ffffff", "#c3d3e0", "#6a7f91")]


def bubble(cx, cy, r, k, special=None):
    c1, c2, cd = BUB[k]
    o = [C(cx, cy, r, rgrad(c1, c2), 'stroke="%s" stroke-width="4"' % cd),
         '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff" opacity="0.65" '
         'transform="rotate(-30 %s %s)"/>' % (cx - r * 0.33, cy - r * 0.36, r * 0.3, r * 0.18,
                                              cx - r * 0.33, cy - r * 0.36)]
    if special == "star":
        o.append(star(cx, cy, r * 0.62, lgrad("#fff3a0", "#f5a800"), stroke="#a85c00", sw=4))
    elif special == "bomb":
        o.append(C(cx, cy, r * 0.56, "#2a2a3a", 'stroke="#ffffff" stroke-width="4"'))
        o.append('<path d="M %s %s q 14 -22 30 -10" fill="none" stroke="#ffd166" stroke-width="7" '
                 'stroke-linecap="round"/>' % (cx + r * 0.22, cy - r * 0.46))
    elif special == "ice":
        o.append(C(cx, cy, r * 0.92, "#bfe9ff", 'opacity="0.55"'))
        for a in (0, 60, 120):
            o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#ffffff" stroke-width="6" '
                     'stroke-linecap="round" opacity="0.9"/>'
                     % (cx - r * 0.6 * math.cos(math.radians(a)), cy - r * 0.6 * math.sin(math.radians(a)),
                        cx + r * 0.6 * math.cos(math.radians(a)), cy + r * 0.6 * math.sin(math.radians(a))))
    return "".join(o)


def screen_bubble():
    o = []
    o.append(RR(0, 0, W, H, 0, lgrad3("#3ec1f3", "#8fe3ff", "#0f6fb8")))
    for cx, cy, s, op in ((190, 420, 1.0, 0.75), (820, 330, 0.75, 0.6), (560, 1180, 1.2, 0.3),
                          (120, 1450, 0.9, 0.28)):
        o.append('<g opacity="%s"><ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff"/>'
                 '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff"/>'
                 '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff"/></g>'
                 % (op, cx, cy, 110 * s, 62 * s, cx - 86 * s, cy + 18 * s, 70 * s, 44 * s,
                    cx + 88 * s, cy + 20 * s, 62 * s, 38 * s))
    o.append(statusbar())

    # HUD
    o.append(btn(48, 100, 92, 92, 28, "#ffd979", "#e8870b"))
    o.append(RR(76, 126, 14, 40, 6, "#8a4b00"))
    o.append(RR(100, 126, 14, 40, 6, "#8a4b00"))
    o.append(pill(190, 104, 330, 84, "#7b4bd6", "#3a1b73"))
    o.append(star(238, 146, 32, lgrad("#fff3a0", "#f5a800")))
    o.append(T(300, 162, "28 450", 40, anchor="start", stroke="#1d0d45", sw=8))
    o.append(pill(560, 104, 240, 84, "#ff8fa8", "#d6234f"))
    o.append(T(680, 162, "УР. 86", 40, stroke="#8c0a2e", sw=8))
    o.append(btn(832, 100, 92, 92, 28, "#8ce1ff", "#1273de"))
    o.append(T(878, 166, "♫", 50, fill="#ffffff", fam=F))
    o.append(btn(940, 100, 92, 92, 28, "#8ce1ff", "#1273de"))
    o.append(T(986, 168, "⚙", 50, fill="#ffffff", fam=F))

    # цель
    o.append(RR(300, 212, 480, 86, 43, "#00000030"))
    o.append(RR(300, 212, 480, 86, 43, lgrad("#ffffff", "#d9ecff"), 'stroke="#1273de" stroke-width="5"'))
    o.append(T(348, 270, "ЦЕЛЬ:", 34, fill="#0a4a8f", anchor="start", fam=F, w=800))
    o.append(bubble(500, 255, 26, 0))
    o.append(T(556, 270, "× 14", 36, fill="#0a4a8f", anchor="start"))
    o.append(RR(652, 232, 104, 46, 23, "#0f6fb8"))
    o.append(T(704, 268, "↓ 8", 32, fill="#ffffff"))

    # потолок и кластер шаров
    o.append(RR(-10, 300, W + 20, 46, 20, lgrad("#6a4a2a", "#3d2a16"), 'stroke="#2a1b0d" stroke-width="4"'))
    random.seed(17)
    r = 52
    top = 390
    specials = {(0, 4): "bomb", (2, 2): "star", (3, 7): "ice", (1, 8): "star"}
    for row in range(7):
        cols = 10 if row % 2 == 0 else 9
        off = r if row % 2 else 0
        n = cols
        if row >= 5:
            n = cols - 2
        for c in range(n):
            if row >= 4 and random.random() < 0.18:
                continue
            cx = 50 + off + c * (2 * r) + r
            cy = top + row * int(2 * r * 0.88)
            if cx > W - 20:
                continue
            k = random.randint(0, 4)
            o.append('<g filter="url(#shs)">%s</g>' % bubble(cx, cy, r - 3, k, specials.get((row, c))))
    # прицел с отскоком
    sx, sy = 540, 1690
    p1 = (96, 1180)
    p2 = (335, 905)
    o.append('<path d="M %s %s L %s %s L %s %s" fill="none" stroke="#ffffff" stroke-width="10" '
             'stroke-linecap="round" stroke-dasharray="4 32" opacity="0.92"/>'
             % (sx, sy, p1[0], p1[1], p2[0], p2[1]))
    o.append(C(p2[0], p2[1], 58, "none", 'stroke="#ffffff" stroke-width="7" opacity="0.92"'))
    o.append(C(p1[0], p1[1], 18, "#ffffff", 'opacity="0.9"'))

    # пушка
    barrel = (RR(sx - 58, sy - 300, 116, 320, 54, lgrad("#e8f6ff", "#5d7f96"),
                 'stroke="#2d4a5c" stroke-width="7"') +
              RR(sx - 36, sy - 282, 30, 250, 15, "#ffffff", 'opacity="0.45"') +
              RR(sx - 66, sy - 306, 132, 54, 26, lgrad("#ffd979", "#e8870b"),
                 'stroke="#8a4b00" stroke-width="6"'))
    o.append('<g transform="rotate(-41 %s %s)">%s</g>' % (sx, sy, barrel))
    o.append(C(sx, sy, 110, lgrad("#8ad6ff", "#1273de"), 'stroke="#0a4a8f" stroke-width="7"'))
    o.append(C(sx, sy, 86, lgrad("#e8f6ff", "#9fc5db"), 'stroke="#2d4a5c" stroke-width="5"'))
    o.append('<g filter="url(#shs)">%s</g>' % bubble(sx, sy, 56, 0))
    o.append(C(sx - 180, sy + 30, 70, "#00000030"))
    o.append(C(sx - 180, sy + 24, 62, lgrad("#e8f6ff", "#9fc5db"), 'stroke="#2d4a5c" stroke-width="5"'))
    o.append(bubble(sx - 180, sy + 24, 42, 3))
    o.append(T(sx - 180, sy + 130, "ДАЛЕЕ", 26, fill="#ffffff", op=0.9, ls=2))
    # бустеры справа
    o.append(btn(sx + 120, sy - 46, 120, 120, 36, "#ffd979", "#e8870b"))
    o.append(T(sx + 180, sy + 34, "⚑", 62, fill="#ffffff", fam=F, stroke="#8a4b00", sw=5))
    o.append(btn(sx + 270, sy - 46, 120, 120, 36, "#ff9e6b", "#e2560f"))
    o.append(T(sx + 330, sy + 32, "✦", 62, fill="#ffffff", fam=F, stroke="#8f3203", sw=5))
    return "".join(o)


# ----------------------------------------------------------------------------
# 4. RUNNER
# ----------------------------------------------------------------------------
HZ = 820


def proj(p, lane):
    """p: 0 - горизонт, 1 - низ экрана"""
    y = HZ + (H - HZ + 120) * (p ** 1.75)
    half = 60 + 620 * (p ** 1.55)
    x = W / 2.0 + lane * half * 0.62
    sc = 0.1 + 1.05 * (p ** 1.6)
    return x, y, half, sc


def screen_runner():
    o = []
    o.append(RR(0, 0, W, HZ + 10, 0, lgrad3("#2b1b6b", "#6a3fb5", "#ff9e6b")))
    o.append(C(540, 700, 300, fade("#ffd166", 0.9, 0.0)))
    o.append(C(540, 720, 150, "#ffdd8a", 'opacity="0.95"'))
    random.seed(4)
    for _ in range(40):
        o.append(C(random.randint(0, W), random.randint(90, 600), random.choice([2, 3, 4]),
                   "#ffffff", 'opacity="%s"' % round(random.uniform(0.3, 0.9), 2)))
    # силуэт города
    sil = []
    x = -20
    random.seed(8)
    while x < W + 40:
        bw = random.randint(70, 130)
        bh = random.randint(100, 280)
        sil.append((x, bh, bw))
        x += bw + random.randint(6, 18)
    pd = ["M -20 %s" % (HZ + 10)]
    for (bx_, bh, bw) in sil:
        pd.append("L %s %s L %s %s L %s %s" % (bx_, HZ + 10 - bh, bx_ + bw, HZ + 10 - bh, bx_ + bw, HZ + 10))
    pd.append("L %s %s Z" % (W + 40, HZ + 10))
    o.append('<path d="%s" fill="#2a1452" opacity="0.85"/>' % " ".join(pd))
    for (bx_, bh, bw) in sil:
        for wy in range(int(HZ - bh + 30), int(HZ - 10), 40):
            for wx in range(int(bx_ + 14), int(bx_ + bw - 18), 34):
                if random.random() < 0.45:
                    o.append(RR(wx, wy, 14, 20, 3, "#ffd166", 'opacity="0.55"'))

    # земля под горизонтом
    o.append(RR(0, HZ - 4, W, H - HZ + 4, 0, lgrad3("#52357f", "#33205c", "#160e2e")))
    o.append(RR(0, HZ - 60, W, 140, 0, fade("#ffb86b", 0.55, 0.0)))
    o.append(RR(0, HZ - 8, W, 16, 8, "#ffd9a8", 'opacity="0.55"'))

    # дорога
    lx, ly, lhalf, _ = proj(0.0, 0)
    bx, byy, bhalf, _ = proj(1.0, 0)
    o.append('<path d="M %s %s L %s %s L %s %s L %s %s Z" fill="%s"/>'
             % (lx - lhalf, HZ, lx + lhalf, HZ, bx + bhalf, H, bx - bhalf, H,
                lgrad("#4b3b7a", "#1c1333")))
    # обочины
    for s in (-1, 1):
        o.append('<path d="M %s %s L %s %s L %s %s L %s %s Z" fill="%s"/>'
                 % (lx + s * lhalf, HZ, lx + s * (lhalf + 26), HZ,
                    bx + s * (bhalf + 180), H, bx + s * bhalf, H, lgrad("#ff9e6b", "#c2410c")))
    # разметка полос
    for lane in (-0.33, 0.33):
        seg = 0.0
        i = 0
        while seg < 1.0:
            p1 = seg
            p2 = min(1.0, seg + 0.035 + seg * 0.05)
            x1, y1, h1, _ = proj(p1, 0)
            x2, y2, h2, _ = proj(p2, 0)
            wdt1 = max(1.5, h1 * 0.028)
            wdt2 = max(2.0, h2 * 0.028)
            cx1 = W / 2.0 + lane * h1 * 1.86
            cx2 = W / 2.0 + lane * h2 * 1.86
            o.append('<path d="M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z" fill="#ffffff" opacity="0.55"/>'
                     % (cx1 - wdt1, y1, cx1 + wdt1, y1, cx2 + wdt2, y2, cx2 - wdt2, y2))
            seg = p2 + 0.03 + seg * 0.06
            i += 1

    # фонари вдоль дороги
    for p in (0.07, 0.15, 0.27, 0.44, 0.68, 0.96):
        x_, y_, half_, sc_ = proj(p, 0)
        for s in (-1, 1):
            px = W / 2.0 + s * (half_ + 50 * sc_ + 24)
            o.append(RR(px - 10 * sc_, y_ - 330 * sc_, 20 * sc_, 330 * sc_, 10 * sc_,
                        lgrad("#9b7ae0", "#2e1a57")))
            o.append(C(px, y_ - 344 * sc_, 54 * sc_, fade("#8ef1ff", 0.85, 0.0)))
            o.append(C(px, y_ - 344 * sc_, 16 * sc_, "#e4fbff"))

    # ворота-множитель
    gx, gy, ghalf, gsc = proj(0.30, 0)
    o.append(RR(gx - ghalf * 0.95, gy - 230 * gsc, ghalf * 1.9, 24 * gsc + 14, 14,
                lgrad("#9bf07a", "#2fa84f"), 'stroke="#176b31" stroke-width="5"'))
    for s in (-1, 1):
        o.append(RR(gx + s * ghalf * 0.92 - 10, gy - 230 * gsc, 22, 230 * gsc, 10,
                    lgrad("#d8ffd0", "#2fa84f"), 'stroke="#176b31" stroke-width="4"'))
    o.append(RR(gx - ghalf * 0.92, gy - 215 * gsc, ghalf * 1.84, 200 * gsc, 16,
                "#9bf07a", 'opacity="0.28"'))
    o.append(T(gx, gy - 90 * gsc, "×2", 92 * gsc, fill="#ffffff", stroke="#176b31", sw=12))

    # монеты
    for i, p in enumerate((0.16, 0.235, 0.33, 0.44, 0.56)):
        cx, cy, half, sc = proj(p, 0)
        o.append(coin(cx, cy - 120 * sc, 46 * sc))
    # препятствия
    for lane, p in ((-1, 0.42), (1, 0.55)):
        cx, cy, half, sc = proj(p, lane)
        wdt, hgt = 230 * sc, 170 * sc
        o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#000000" opacity="0.3"/>'
                 % (cx, cy + 6, wdt * 0.55, hgt * 0.14))
        o.append(RR(cx - wdt / 2, cy - hgt, wdt, hgt, 18 * sc, lgrad("#ff6b6b", "#c01c1c"),
                    'stroke="#6d0a0a" stroke-width="%s"' % max(2, 5 * sc)))
        for i in range(3):
            o.append(RR(cx - wdt / 2 + 10 * sc + i * wdt * 0.3, cy - hgt + 12 * sc,
                        wdt * 0.16, hgt - 24 * sc, 8 * sc, "#ffffff", 'opacity="0.85"'))

    # персонаж
    cx, cy, half, sc = proj(0.88, 0)
    sc = min(sc, 1.05)
    o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#000000" opacity="0.4"/>'
             % (cx, cy + 10, 130 * sc, 32 * sc))
    for i, (dx, dy, rr_) in enumerate(((-150, -40, 26), (160, -70, 20), (-190, -120, 16),
                                       (200, -150, 13), (-120, -180, 11))):
        o.append(C(cx + dx * sc, cy + dy * sc, rr_ * sc, "#ffffff",
                   'opacity="%s"' % round(0.32 - i * 0.045, 2)))
    bodyc = lgrad("#4cc9f0", "#1273de")
    # ноги
    o.append(RR(cx - 48 * sc, cy - 160 * sc, 44 * sc, 150 * sc, 22 * sc, lgrad("#454b6b", "#22273f")))
    o.append(RR(cx + 6 * sc, cy - 180 * sc, 44 * sc, 170 * sc, 22 * sc, lgrad("#5a6185", "#2b3150")))
    o.append(RR(cx - 66 * sc, cy - 26 * sc, 74 * sc, 42 * sc, 20 * sc, lgrad("#fff0c0", "#e8870b"),
                'stroke="#8a4b00" stroke-width="%s"' % (4 * sc)))
    o.append(RR(cx + 2 * sc, cy - 44 * sc, 76 * sc, 42 * sc, 20 * sc, lgrad("#fff0c0", "#e8870b"),
                'stroke="#8a4b00" stroke-width="%s"' % (4 * sc)))
    # дальняя рука
    o.append('<g transform="rotate(-38 %s %s)">%s</g>'
             % (cx - 74 * sc, cy - 306 * sc,
                RR(cx - 136 * sc, cy - 322 * sc, 58 * sc, 164 * sc, 29 * sc,
                   lgrad("#3a9fd0", "#0d5ea8"), 'stroke="#0a4a8f" stroke-width="%s"' % (5 * sc))))
    # торс
    o.append(RR(cx - 80 * sc, cy - 336 * sc, 160 * sc, 206 * sc, 54 * sc, bodyc,
                'stroke="#0a4a8f" stroke-width="%s"' % (6 * sc)))
    o.append(RR(cx - 62 * sc, cy - 316 * sc, 52 * sc, 150 * sc, 26 * sc, "#ffffff", 'opacity="0.22"'))
    o.append(RR(cx - 80 * sc, cy - 208 * sc, 160 * sc, 30 * sc, 15 * sc, "#ffd166",
                'stroke="#0a4a8f" stroke-width="%s"' % (4 * sc)))
    # ближняя рука
    o.append('<g transform="rotate(32 %s %s)">%s</g>'
             % (cx + 74 * sc, cy - 306 * sc,
                RR(cx + 78 * sc, cy - 322 * sc, 58 * sc, 164 * sc, 29 * sc, bodyc,
                   'stroke="#0a4a8f" stroke-width="%s"' % (5 * sc)) +
                C(cx + 107 * sc, cy - 170 * sc, 30 * sc, lgrad("#ffe0bd", "#e8b48a"),
                  'stroke="#8a5a3a" stroke-width="%s"' % (4 * sc))))
    o.append(C(cx, cy - 400 * sc, 92 * sc, lgrad("#ffe0bd", "#e8b48a"),
               'stroke="#8a5a3a" stroke-width="%s"' % (6 * sc)))
    o.append('<path d="M %s %s a %s %s 0 0 1 %s 0 Z" fill="%s" stroke="#8f3203" stroke-width="%s"/>'
             % (cx - 96 * sc, cy - 410 * sc, 96 * sc, 96 * sc, 192 * sc,
                lgrad("#ff9e6b", "#e2560f"), 5 * sc))
    o.append(RR(cx - 96 * sc, cy - 424 * sc, 160 * sc, 26 * sc, 13 * sc, lgrad("#ff9e6b", "#e2560f"),
                'stroke="#8f3203" stroke-width="%s"' % (4 * sc)))
    o.append(C(cx - 32 * sc, cy - 390 * sc, 13 * sc, "#2a2338"))
    o.append(C(cx + 32 * sc, cy - 390 * sc, 13 * sc, "#2a2338"))
    o.append('<path d="M %s %s q %s %s %s 0" fill="none" stroke="#2a2338" stroke-width="%s" stroke-linecap="round"/>'
             % (cx - 26 * sc, cy - 348 * sc, 26 * sc, 28 * sc, 52 * sc, 7 * sc))
    # спид-линии
    for i in range(7):
        yy = 1180 + i * 96
        ln = 80 + i * 26
        side = -1 if i % 2 == 0 else 1
        o.append(RR(W / 2 + side * (300 + i * 36), yy, ln, 10, 5, "#ffffff", 'opacity="0.35"'))

    o.append(statusbar())
    # HUD
    o.append(btn(48, 100, 92, 92, 28, "#8c6bd6", "#4a2a8f"))
    o.append(RR(76, 126, 14, 40, 6, "#ffffff"))
    o.append(RR(100, 126, 14, 40, 6, "#ffffff"))
    o.append(T(540, 190, "12 480", 96, fill="#ffffff", stroke="#2b1b4a", sw=14))
    o.append(T(540, 238, "ОЧКИ", 32, fill="#ffffff", op=0.85, ls=6))
    o.append(pill(790, 104, 250, 84, "#ffd979", "#e8870b"))
    o.append(coin(836, 146, 32))
    o.append(T(956, 162, "1 284", 36, stroke="#8a4b00", sw=8))
    o.append(pill(790, 204, 250, 70, "#7b4bd6", "#3a1b73"))
    o.append(T(916, 254, "2 140 м", 34, stroke="#1d0d45", sw=7))

    # магнит-бустер с таймером
    o.append(btn(48, 1380, 130, 130, 40, "#ff8fa8", "#d6234f"))
    o.append(T(113, 1468, "★", 66, fill="#ffffff", fam=F, stroke="#8c0a2e", sw=5))
    o.append(RR(48, 1520, 130, 20, 10, "#00000055"))
    o.append(RR(52, 1524, 82, 12, 6, lgrad("#ffe066", "#f3a000")))
    o.append(btn(48, 1570, 130, 130, 40, "#8ce1ff", "#1273de"))
    o.append(T(113, 1660, "⚡", 62, fill="#ffffff", fam=F, stroke="#0a4a8f", sw=5))

    o.append(RR(300, 1760, 480, 96, 48, "#00000045"))
    o.append(T(540, 1824, "СВАЙП, ЧТОБЫ ПРЫГНУТЬ", 34, fill="#ffffff", ls=2, op=0.95))
    return "".join(o)


# ----------------------------------------------------------------------------
# 5. IDLE TYCOON
# ----------------------------------------------------------------------------
def person(cx, cy, s, cbody1, cbody2, skin="#ffe0bd", hair="#3a2a20", hat=None):
    o = ['<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#000000" opacity="0.25"/>'
         % (cx, cy + 8 * s, 70 * s, 18 * s)]
    o.append(RR(cx - 62 * s, cy - 180 * s, 124 * s, 190 * s, 46 * s, lgrad(cbody1, cbody2),
               'stroke="#00000033" stroke-width="%s"' % (4 * s)))
    o.append(RR(cx - 46 * s, cy - 164 * s, 40 * s, 120 * s, 20 * s, "#ffffff", 'opacity="0.22"'))
    o.append(C(cx, cy - 248 * s, 76 * s, lgrad(skin, "#e8b48a"), 'stroke="#8a5a3a" stroke-width="%s"' % (4 * s)))
    if hat == "chef":
        o.append(RR(cx - 70 * s, cy - 330 * s, 140 * s, 40 * s, 14 * s, "#ffffff",
                    'stroke="#c9c9d6" stroke-width="%s"' % (4 * s)))
        o.append('<g>%s%s%s</g>' % (C(cx - 44 * s, cy - 356 * s, 40 * s, "#ffffff", 'stroke="#c9c9d6" stroke-width="3"'),
                                    C(cx + 44 * s, cy - 356 * s, 40 * s, "#ffffff", 'stroke="#c9c9d6" stroke-width="3"'),
                                    C(cx, cy - 376 * s, 48 * s, "#ffffff", 'stroke="#c9c9d6" stroke-width="3"')))
    elif hat == "cap":
        o.append('<path d="M %s %s a %s %s 0 0 1 %s 0 Z" fill="%s"/>'
                 % (cx - 78 * s, cy - 256 * s, 78 * s, 78 * s, 156 * s, lgrad("#ff6b8a", "#d11149")))
        o.append(RR(cx - 78 * s, cy - 268 * s, 130 * s, 22 * s, 11 * s, "#d11149"))
    else:
        o.append('<path d="M %s %s a %s %s 0 0 1 %s 0 Z" fill="%s"/>'
                 % (cx - 76 * s, cy - 252 * s, 76 * s, 76 * s, 152 * s, hair))
    o.append(C(cx - 26 * s, cy - 244 * s, 10 * s, "#2a2338"))
    o.append(C(cx + 26 * s, cy - 244 * s, 10 * s, "#2a2338"))
    o.append('<path d="M %s %s q %s %s %s 0" fill="none" stroke="#2a2338" stroke-width="%s" stroke-linecap="round"/>'
             % (cx - 22 * s, cy - 212 * s, 22 * s, 24 * s, 44 * s, 6 * s))
    return "".join(o)


def burger(cx, cy, s):
    o = ['<path d="M %s %s a %s %s 0 0 1 %s 0 Z" fill="%s" stroke="#a85c00" stroke-width="%s"/>'
         % (cx - 58 * s, cy - 18 * s, 58 * s, 58 * s, 116 * s, lgrad("#ffcd7a", "#e09a3c"), 3 * s)]
    for i in range(5):
        o.append(C(cx - 36 * s + i * 18 * s, cy - 40 * s - (6 if i % 2 else 0) * s, 4 * s, "#fff6e2"))
    o.append(RR(cx - 58 * s, cy - 16 * s, 116 * s, 16 * s, 8 * s, "#9bf07a", 'stroke="#2fa84f" stroke-width="%s"' % (2 * s)))
    o.append(RR(cx - 56 * s, cy - 2 * s, 112 * s, 22 * s, 8 * s, lgrad("#a0522d", "#5a2d0c")))
    o.append(RR(cx - 58 * s, cy + 18 * s, 116 * s, 14 * s, 7 * s, "#ffd166"))
    o.append(RR(cx - 56 * s, cy + 30 * s, 112 * s, 26 * s, 12 * s, lgrad("#ffcd7a", "#d98e34"),
                'stroke="#a85c00" stroke-width="%s"' % (3 * s)))
    return "".join(o)


def screen_idle():
    o = []
    o.append(RR(0, 0, W, H, 0, lgrad3("#ffd79a", "#ffb067", "#f07f3c")))
    o.append(RR(0, 0, W, 980, 0, lgrad("#5d3fa8", "#8a5fd0")))
    o.append(bg_blobs(["#ffd166", "#ff8fa8"], seed=21, n=5, op=0.35))
    # окно
    o.append(RR(120, 300, 380, 300, 40, lgrad("#8ad6ff", "#2b8fd6"), 'stroke="#2a1b4a" stroke-width="10"'))
    o.append(RR(140, 320, 150, 120, 20, "#ffffff", 'opacity="0.25"'))
    o.append(RR(580, 300, 380, 300, 40, lgrad("#ffd166", "#f49200"), 'stroke="#2a1b4a" stroke-width="10"'))
    o.append(burger(770, 440, 1.7))
    o.append(T(770, 560, "BURGER", 46, fill="#5a2d0c", stroke="#ffffff", sw=8))
    # лампы
    for lx in (250, 540, 830):
        o.append('<line x1="%s" y1="190" x2="%s" y2="252" stroke="#2a1b4a" stroke-width="8"/>' % (lx, lx))
        o.append('<path d="M %s 318 L %s 252 L %s 252 L %s 318 Z" fill="%s" stroke="#2a1b4a" '
                 'stroke-width="6" stroke-linejoin="round"/>'
                 % (lx - 78, lx - 16, lx + 16, lx + 78, lgrad("#ff8fa8", "#d6234f")))
        o.append('<path d="M %s 318 L %s 318 L %s 760 L %s 760 Z" fill="%s" opacity="0.45"/>'
                 % (lx - 76, lx + 76, lx + 190, lx - 190, fade("#fff3a0", 0.55, 0.0)))
        o.append('<ellipse cx="%s" cy="318" rx="74" ry="16" fill="#fff6c8"/>' % lx)
    # пол
    o.append(RR(0, 980, W, 940, 0, lgrad("#f8d8a8", "#d9a05b")))
    for i in range(10):
        o.append(RR(-40 + i * 130, 980, 70, 940, 0, "#ffffff", 'opacity="0.10"'))
    # повар за прилавком
    o.append(person(286, 1150, 0.9, "#ffffff", "#e3e8f2", hat="chef"))
    # прилавок
    o.append(RR(40, 1100, 1000, 250, 44, lgrad("#b06a35", "#7a4520"), 'stroke="#4a2a10" stroke-width="8"'))
    o.append(RR(40, 1100, 1000, 62, 31, lgrad("#f0d4a8", "#c08a52"), 'stroke="#4a2a10" stroke-width="6"'))
    for i in range(6):
        o.append(RR(100 + i * 160, 1190, 110, 130, 18, "#ffffff", 'opacity="0.08"'))
    o.append(RR(846, 962, 196, 138, 28, lgrad("#cfd9e8", "#8c9bb5"), 'stroke="#44506b" stroke-width="7"'))
    o.append(RR(868, 984, 152, 58, 14, "#2d3b55"))
    o.append(T(944, 1030, "$ $ $", 32, fill="#9bf07a"))
    o.append(burger(480, 1128, 0.6))
    o.append(burger(610, 1134, 0.5))
    # клиенты
    o.append(person(560, 1410, 0.76, "#8ce1ff", "#2b8fd6", hat="cap"))
    o.append(person(790, 1440, 0.7, "#ffb3c9", "#e5407a", hair="#5a2d0c"))
    # облачко заказа
    o.append(RR(560, 942, 300, 160, 46, "#ffffff", 'stroke="#2a1b4a" stroke-width="6"'))
    o.append('<path d="M 616 1090 L 572 1178 L 692 1096 Z" fill="#ffffff" stroke="#2a1b4a" stroke-width="6"/>')
    o.append(RR(600, 1072, 110, 24, 0, "#ffffff"))
    o.append(burger(646, 1020, 0.78))
    o.append(RR(738, 978, 86, 86, 43, "none", 'stroke="#e6e6ef" stroke-width="12"'))
    o.append('<path d="M 781 935 a 43 43 0 0 1 32 72" fill="none" stroke="#2fa84f" stroke-width="12" '
             'stroke-linecap="round"/>')
    o.append(T(781, 1036, "68%", 28, fill="#2a1b4a", fam=F, w=800))
    # всплывающие деньги
    o.append(T(452, 862, "+$2.4K", 58, fill="#9bf07a", stroke="#176b31", sw=10, op=0.95))
    o.append(T(726, 762, "+$860", 44, fill="#9bf07a", stroke="#176b31", sw=9, op=0.8))
    o.append(T(186, 700, "+$1.1K", 40, fill="#9bf07a", stroke="#176b31", sw=8, op=0.6))

    o.append(statusbar())
    # HUD
    o.append(RR(48, 100, 560, 110, 42, "#00000040"))
    o.append(RR(48, 100, 560, 110, 42, lgrad("#2a1b4a", "#140c2b"), 'stroke="#ffd166" stroke-width="5"'))
    o.append(coin(112, 155, 40))
    o.append(T(176, 178, "$ 1.24M", 56, anchor="start", stroke="#000000", sw=0))
    o.append(T(176, 126, "БАЛАНС", 24, fill="#ffd166", anchor="start", ls=3))
    o.append(pill(636, 108, 230, 94, "#c9a3ff", "#6a2fd0"))
    o.append(gemicon(686, 155, 32, "#f5c6ff", "#c454f0"))
    o.append(T(802, 172, "240", 38, stroke="#3c0a66", sw=8))
    o.append(btn(892, 104, 140, 102, 32, "#9bf07a", "#2fa84f"))
    o.append(T(962, 178, "✦", 56, fill="#ffffff", fam=F, stroke="#176b31", sw=5))
    # x3 буст
    o.append(btn(880, 700, 150, 150, 44, "#ffd979", "#e8870b"))
    o.append(T(955, 782, "▶", 54, fill="#ffffff", fam=F, stroke="#8a4b00", sw=5))
    o.append(T(955, 826, "×3", 34, fill="#ffffff", stroke="#8a4b00", sw=6))
    o.append(RR(880, 862, 150, 22, 11, "#00000055"))
    o.append(RR(884, 866, 96, 14, 7, lgrad("#ffe066", "#f3a000")))

    # карточки апгрейдов
    cards = [("Гриль Pro", "УР. 42", "+$320/с", "$18.4K", "#ff9e6b", "#e2560f"),
             ("Касса", "УР. 27", "+$180/с", "$9.2K", "#8ce1ff", "#2b8fd6")]
    for i, (nm, lv, inc, price, c1, c2) in enumerate(cards):
        y = 1486 + i * 156
        o.append(RR(48, y, 984, 142, 40, "#00000030"))
        o.append(RR(48, y, 984, 142, 40, lgrad("#fff6e2", "#ffdfb0"), 'stroke="#b96d00" stroke-width="5"'))
        o.append(RR(70, y + 16, 110, 110, 32, lgrad(c1, c2), 'stroke="#00000033" stroke-width="4"'))
        o.append(T(125, y + 92, "⚒" if i == 0 else "▤", 56, fill="#ffffff", fam=F))
        o.append(T(206, y + 58, nm, 42, fill="#5a3000", anchor="start"))
        o.append(RR(206, y + 78, 112, 42, 21, "#e8c99a"))
        o.append(T(262, y + 109, lv, 26, fill="#5a3000"))
        o.append(T(336, y + 109, inc, 30, fill="#2fa84f", anchor="start"))
        o.append(btn(726, y + 18, 284, 106, 34, "#9bf07a", "#2fa84f"))
        o.append(coin(776, y + 70, 26))
        o.append(T(892, y + 86, price, 38, anchor="middle", stroke="#176b31", sw=7))
    # нижние табы
    o.append(RR(-20, 1796, W + 40, 190, 48, lgrad("#2a1b4a", "#140c2b"), 'stroke="#ffd166" stroke-width="5"'))
    tabs = [("↑", "АПГРЕЙД", True), ("☺", "МЕНЕДЖЕРЫ", False),
            ("⚡", "БУСТЫ", False), ("⚑", "ФИЛИАЛЫ", False)]
    for i, (ic, lb, act) in enumerate(tabs):
        x = 60 + i * 248
        if act:
            o.append(RR(x - 10, 1810, 212, 118, 36, lgrad("#ffd979", "#e8870b"),
                        'stroke="#ffffff" stroke-width="4"'))
            col = "#5a3000"
        else:
            col = "#ffffff"
        o.append(T(x + 96, 1874, ic, 48, fill=col, fam=F))
        o.append(T(x + 96, 1910, lb, 23, fill=col, op=0.95, ls=1))
    return "".join(o)


# ----------------------------------------------------------------------------
# 6. BALL SORT
# ----------------------------------------------------------------------------
BALLC = [("#ff8aa0", "#e01e46", "#8c0a2e"), ("#8ad6ff", "#1273de", "#0a4a8f"),
         ("#ffe066", "#f49200", "#a85c00"), ("#9bf07a", "#2fa84f", "#176b31"),
         ("#d9a6ff", "#7b2cbf", "#4a1480"), ("#ffb08a", "#e2560f", "#8f3203"),
         ("#8ef1d6", "#13a383", "#0a6b56")]


def ball(cx, cy, r, k):
    c1, c2, cd = BALLC[k % len(BALLC)]
    return (C(cx, cy, r, rgrad(c1, c2), 'stroke="%s" stroke-width="4"' % cd) +
            '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff" opacity="0.6" '
            'transform="rotate(-28 %s %s)"/>' % (cx - r * 0.33, cy - r * 0.36, r * 0.28, r * 0.16,
                                                 cx - r * 0.33, cy - r * 0.36))


def tube(x, y, w, h, balls, r, done=False, lifted=None):
    o = []
    o.append(RR(x + 6, y + 10, w, h, w / 2.2, "#00000035"))
    o.append(RR(x, y, w, h, w / 2.2, "#ffffff", 'opacity="0.16"'))
    o.append(RR(x, y, w, h, w / 2.2, "none", 'stroke="#ffffff" stroke-opacity="0.65" stroke-width="5"'))
    cap = y + h - 18
    for i, k in enumerate(balls):
        cy = cap - r - i * (2 * r + 6)
        o.append(ball(x + w / 2.0, cy, r, k))
    o.append(RR(x + w * 0.16, y + 22, w * 0.17, h - 70, w * 0.09, "#ffffff", 'opacity="0.45"'))
    if done:
        o.append(RR(x - 8, y - 8, w + 16, h + 16, w / 2.0, "none",
                    'stroke="#9bf07a" stroke-width="7" filter="url(#glow)"'))
        o.append(C(x + w / 2.0, y - 34, 32, lgrad("#9bf07a", "#2fa84f"), 'stroke="#ffffff" stroke-width="4"'))
        o.append('<path d="M %s %s l 12 14 l 24 -28" fill="none" stroke="#ffffff" stroke-width="8" '
                 'stroke-linecap="round" stroke-linejoin="round"/>' % (x + w / 2.0 - 18, y - 34))
    if lifted is not None:
        o.append(ball(x + w / 2.0, y - 70, r, lifted))
        o.append('<path d="M %s %s l 18 26 l 18 -26" fill="none" stroke="#ffffff" stroke-width="7" '
                 'stroke-linecap="round" opacity="0.8"/>' % (x + w / 2.0 - 18, y - 16))
    return "".join(o)


def screen_ballsort():
    o = []
    o.append(RR(0, 0, W, H, 0, lgrad3("#2b2d6b", "#4a2a8f", "#16103a")))
    o.append(bg_blobs(["#7b5bff", "#ff6ec7", "#2bd9ff"], seed=31, n=6, op=0.4))
    o.append(confetti(seed=7, n=70, colors=("#ffffff", "#ffd166", "#8ef1ff", "#ff8aa0"), op=0.4))
    o.append(statusbar())

    o.append(btn(48, 104, 92, 92, 30, "#8c6bd6", "#4a2a8f"))
    o.append(T(94, 170, "←", 52, fill="#ffffff", fam=F))
    o.append(pill(360, 106, 360, 88, "#7b4bd6", "#3a1b73"))
    o.append(T(540, 168, "УРОВЕНЬ 137", 42, stroke="#1d0d45", sw=8))
    o.append(pill(760, 106, 272, 88, "#ffd979", "#e8870b"))
    o.append(coin(806, 150, 32))
    o.append(T(912, 166, "2 450", 38, stroke="#8a4b00", sw=8))

    # панель с кнопками-помощниками
    tools = [("↶", "ОТМЕНА", "#8ce1ff", "#2b8fd6", None),
             ("↻", "ЗАНОВО", "#ff9e6b", "#e2560f", None),
             ("✦", "ПОДСКАЗКА", "#ffd979", "#e8870b", "3"),
             ("+", "ПРОБИРКА", "#9bf07a", "#2fa84f", "▶")]
    for i, (ic, lb, c1, c2, badge) in enumerate(tools):
        x = 60 + i * 248
        o.append(btn(x, 232, 200, 130, 40, c1, c2))
        o.append(T(x + 100, 318, ic, 62, fill="#ffffff", fam=F, stroke="#00000030", sw=4))
        o.append(T(x + 100, 352, lb, 24, fill="#ffffff", ls=1))
        if badge:
            o.append(C(x + 186, 240, 28, lgrad("#ff6b8a", "#d11149"), 'stroke="#ffffff" stroke-width="4"'))
            o.append(T(x + 186, 252, badge, 28, stroke=None, fam=FB if badge != "▶" else F))

    # пробирки
    tw, th, r = 150, 470, 40
    rows = [(430, [(0, [0, 0, 1, 2]), (1, [3, 3, 3, 3], True), (2, [4, 1, 0, 5]),
                   (3, [2, 2, 5, 1]), (4, [6, 6, 4, 4])]),
            (1000, [(0, [1, 5, 2, 0]), (1, [5, 4, 6, 2]), (2, [], False, 3),
                    (3, [0, 6, 3], False), (4, [], False)])]
    for (ty, tubes) in rows:
        for t in tubes:
            idx, balls = t[0], t[1]
            done = t[2] if len(t) > 2 else False
            lifted = t[3] if len(t) > 3 else None
            x = 70 + idx * 190
            o.append(tube(x, ty, tw, th, balls, r, done=bool(done), lifted=lifted))

    # подпись-подсказка
    o.append(RR(240, 1570, 600, 90, 45, "#00000040"))
    o.append(T(540, 1630, "СОБЕРИ ШАРЫ ПО ЦВЕТАМ", 36, fill="#ffffff", ls=2, op=0.95))

    # нижние кнопки
    o.append(btn(90, 1700, 420, 150, 48, "#ffd979", "#e8870b"))
    o.append(T(300, 1790, "▶  +1 ХОД", 44, fill="#ffffff", stroke="#8a4b00", sw=8))
    o.append(btn(570, 1700, 420, 150, 48, "#9bf07a", "#2fa84f"))
    o.append(T(780, 1790, "ПЕРЕМЕШАТЬ", 40, fill="#ffffff", stroke="#176b31", sw=8))
    o.append(T(540, 1898, "● ● ●", 30, fill="#ffffff", op=0.4))
    return "".join(o)


SCREENS = [("Jelly_Crush_Party", screen_match3, "Jelly Crush Party"),
           ("Merge_Valley_Story", screen_merge, "Merge Valley Story"),
           ("Aqua_Pop_Blast", screen_bubble, "Aqua Pop Blast"),
           ("Neon_Dash", screen_runner, "Neon Dash"),
           ("Burger_Boss_Tycoon", screen_idle, "Burger Boss Tycoon"),
           ("Ball_Sort_Deluxe", screen_ballsort, "Ball Sort Deluxe")]

if __name__ == "__main__":
    for name, fn, title in SCREENS:
        DEFS[:] = []
        CNT[0] = 0
        write(name, fn(), title)
