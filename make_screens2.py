# -*- coding: utf-8 -*-
"""Вторая партия макетов (1080x1920): tower defense, ферма, слова,
пасьянс, блок-пазл, triple match. Общие хелперы берутся из make_screens."""

import math, random

from make_screens import (W, H, F, FB, DEFS, CNT, T, RR, C, btn, pill, coin, gemicon,
                          star, heart, poly, sparkle, statusbar, bg_blobs, confetti,
                          lgrad, lgrad3, rgrad, fade, write, person, burger, uid)


# ----------------------------------------------------------------------------
# 7. TOWER DEFENSE
# ----------------------------------------------------------------------------
TD_PATH = ("M -40 470 L 640 470 Q 800 470 800 610 L 800 800 Q 800 940 640 940 "
           "L 300 940 Q 150 940 150 1080 L 150 1280 Q 150 1420 310 1420 L 1120 1420")


def creep(cx, cy, s, c1, c2, hp=0.75, boss=False):
    o = ['<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#000000" opacity="0.28"/>'
         % (cx, cy + 46 * s, 46 * s, 14 * s)]
    o.append(RR(cx - 44 * s, cy - 36 * s, 88 * s, 86 * s, 36 * s, rgrad(c1, c2),
                'stroke="#00000044" stroke-width="%s"' % (4 * s)))
    o.append(C(cx - 17 * s, cy - 6 * s, 13 * s, "#ffffff"))
    o.append(C(cx + 17 * s, cy - 6 * s, 13 * s, "#ffffff"))
    o.append(C(cx - 15 * s, cy - 4 * s, 7 * s, "#2a2338"))
    o.append(C(cx + 19 * s, cy - 4 * s, 7 * s, "#2a2338"))
    o.append('<path d="M %s %s q %s %s %s 0" fill="none" stroke="#2a2338" stroke-width="%s" '
             'stroke-linecap="round"/>' % (cx - 16 * s, cy + 24 * s, 16 * s, 16 * s, 32 * s, 5 * s))
    if boss:
        o.append('<path d="M %s %s l %s %s l %s %s l %s %s l %s %s l %s %s l %s %s Z" fill="%s" '
                 'stroke="#a85c00" stroke-width="3"/>'
                 % (cx - 42 * s, cy - 42 * s, 14 * s, -26 * s, 14 * s, 16 * s, 14 * s, -26 * s,
                    14 * s, 26 * s, 14 * s, -16 * s, 14 * s, 26 * s, lgrad("#ffe066", "#f49200")))
    o.append(RR(cx - 44 * s, cy - 70 * s, 88 * s, 16 * s, 8 * s, "#1d0d45",
                'stroke="#000000" stroke-opacity="0.3" stroke-width="2"'))
    o.append(RR(cx - 41 * s, cy - 67 * s, 82 * s * hp, 10 * s, 5 * s,
                lgrad("#9bf07a", "#2fa84f") if hp > 0.4 else lgrad("#ff8fa8", "#d11149")))
    return "".join(o)


def tower(cx, cy, kind, lvl):
    c1, c2 = {"gun": ("#8ce1ff", "#2b8fd6"), "arrow": ("#9bf07a", "#2fa84f"),
              "mage": ("#d9a6ff", "#7b2cbf")}[kind]
    o = ['<ellipse cx="%s" cy="%s" rx="72" ry="22" fill="#000000" opacity="0.3"/>' % (cx, cy + 54)]
    o.append(RR(cx - 70, cy - 10, 140, 68, 26, lgrad("#cfd9e8", "#7c8aa8"),
                'stroke="#44506b" stroke-width="6"'))
    o.append(RR(cx - 56, cy - 78, 112, 84, 28, lgrad(c1, c2), 'stroke="#00000044" stroke-width="6"'))
    if kind == "gun":
        o.append(RR(cx - 19, cy - 168, 38, 104, 16, lgrad("#cfe6f5", "#5d7f96"),
                    'stroke="#2d4a5c" stroke-width="5"'))
        o.append(C(cx, cy - 168, 25, lgrad("#ffd979", "#e8870b"), 'stroke="#8a4b00" stroke-width="4"'))
    elif kind == "arrow":
        o.append('<path d="M %s %s L %s %s L %s %s Z" fill="%s" stroke="#176b31" stroke-width="5" '
                 'stroke-linejoin="round"/>' % (cx - 46, cy - 78, cx, cy - 164, cx + 46, cy - 78,
                                                lgrad("#d8ffd0", "#2fa84f")))
    else:
        o.append(C(cx, cy - 130, 38, lgrad("#ffffff", "#c9a3ff"), 'stroke="#4a1480" stroke-width="5"'))
        o.append(sparkle(cx, cy - 130, 24, "#ffffff", 0.9))
    o.append(RR(cx - 38, cy + 58, 76, 34, 17, "#1d0d45", 'stroke="#ffffff" stroke-opacity="0.5" stroke-width="3"'))
    o.append(T(cx, cy + 83, "ур.%d" % lvl, 24, fill="#ffffff", fam=F, w=800))
    return "".join(o)


def screen_td():
    o = []
    o.append(RR(0, 0, W, H, 0, lgrad3("#86d46a", "#5aa83c", "#36702a")))
    random.seed(12)
    for _ in range(90):
        x, y = random.randint(0, W), random.randint(300, 1560)
        o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#2f7a2f" opacity="0.18"/>'
                 % (x, y, random.randint(16, 46), random.randint(6, 16)))
    for (x, y, s) in ((80, 620, 1.0), (980, 520, 0.8), (920, 1180, 1.1), (70, 1560, 0.9)):
        o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#000000" opacity="0.22"/>'
                 % (x, y + 70 * s, 60 * s, 18 * s))
        o.append(RR(x - 16 * s, y - 40 * s, 32 * s, 116 * s, 14 * s, lgrad("#a9703f", "#6d4220")))
        o.append(C(x, y - 70 * s, 72 * s, rgrad("#9bf07a", "#1f6b2f"), 'stroke="#14501f" stroke-width="5"'))
        o.append(C(x - 34 * s, y - 24 * s, 46 * s, rgrad("#86d46a", "#246b28")))
        o.append(C(x + 36 * s, y - 28 * s, 42 * s, rgrad("#86d46a", "#246b28")))

    # дорога
    o.append('<path d="%s" fill="none" stroke="#6b4a24" stroke-width="172" stroke-linecap="round" '
             'stroke-linejoin="round"/>' % TD_PATH)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="146" stroke-linecap="round" '
             'stroke-linejoin="round"/>' % (TD_PATH, lgrad("#c79a60", "#a37742")))
    o.append('<path d="%s" fill="none" stroke="#fff0d0" stroke-width="8" stroke-linecap="round" '
             'stroke-dasharray="26 34" opacity="0.45"/>' % TD_PATH)
    # портал и база
    o.append('<ellipse cx="0" cy="470" rx="54" ry="108" fill="%s" stroke="#d9a6ff" stroke-width="7"/>'
             % lgrad("#7b2cbf", "#2b1055"))
    o.append(RR(948, 1300, 150, 240, 36, lgrad("#cfd9e8", "#7c8aa8"), 'stroke="#44506b" stroke-width="7"'))
    o.append('<path d="M 936 1300 L 1023 1222 L 1110 1300 Z" fill="%s" stroke="#8c0a2e" stroke-width="6" '
             'stroke-linejoin="round"/>' % lgrad("#ff8fa8", "#d11149"))
    o.append(heart(1023, 1400, 44))

    # башни
    o.append(C(330, 640, 230, "#ffffff", 'opacity="0.12"'))
    o.append(C(330, 640, 230, "none", 'stroke="#ffffff" stroke-width="5" stroke-dasharray="20 18" opacity="0.6"'))
    o.append(tower(330, 640, "gun", 3))
    o.append(tower(620, 1130, "arrow", 2))
    o.append(tower(930, 820, "mage", 4))
    o.append(C(430, 1230, 58, "#ffffff", 'opacity="0.18" stroke="#ffffff" stroke-width="5" stroke-dasharray="18 16"'))
    o.append(T(430, 1254, "+", 72, fill="#ffffff", op=0.85))

    # враги
    o.append(creep(150, 470, 1.0, "#9bf07a", "#2fa84f", 0.9))
    o.append(creep(330, 470, 1.0, "#9bf07a", "#2fa84f", 0.55))
    o.append(creep(520, 470, 1.0, "#ff9e6b", "#e2560f", 0.8))
    o.append(creep(800, 690, 1.0, "#9bf07a", "#2fa84f", 0.35))
    o.append(creep(690, 940, 1.15, "#d9a6ff", "#7b2cbf", 0.65, boss=True))
    o.append(creep(400, 940, 0.95, "#8ce1ff", "#2b8fd6", 1.0))
    o.append(creep(150, 1200, 0.95, "#8ce1ff", "#2b8fd6", 1.0))
    # выстрелы
    for (x1, y1, x2, y2) in ((330, 530, 332, 492), (930, 740, 820, 700)):
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#fff6b0" stroke-width="10" '
                 'stroke-linecap="round" opacity="0.8"/>' % (x1, y1, x2, y2))
    o.append(C(332, 492, 16, "#fff6b0", 'filter="url(#glow)"'))
    o.append(T(530, 408, "-24", 40, fill="#fff6b0", stroke="#8a4b00", sw=8))

    o.append(statusbar())
    # HUD
    o.append(pill(48, 104, 220, 80, "#ff8fa8", "#d6234f"))
    o.append(heart(92, 144, 30))
    o.append(T(190, 160, "20", 42, stroke="#8c0a2e", sw=8))
    o.append(pill(292, 104, 280, 80, "#ffd979", "#e8870b"))
    o.append(coin(336, 144, 32))
    o.append(T(450, 162, "1 250", 40, stroke="#8a4b00", sw=8))
    o.append(pill(596, 104, 300, 80, "#7b4bd6", "#3a1b73"))
    o.append(T(746, 162, "ВОЛНА 12/20", 36, stroke="#1d0d45", sw=8))
    o.append(btn(920, 100, 88, 88, 28, "#8c6bd6", "#4a2a8f"))
    o.append(T(964, 168, "»", 56, fill="#ffffff", fam=F))

    # панель постройки
    o.append(RR(-20, 1570, W + 40, 400, 54, lgrad("#2e1566", "#160b36"), 'stroke="#7b4bd6" stroke-width="6"'))
    o.append(T(80, 1648, "ПОСТРОЙКА", 34, fill="#c9a3ff", anchor="start", ls=3))
    shop = [("gun", "120", "#8ce1ff", "#2b8fd6"), ("arrow", "180", "#9bf07a", "#2fa84f"),
            ("mage", "320", "#d9a6ff", "#7b2cbf"), ("bomb", "450", "#ff9e6b", "#e2560f")]
    for i, (kind, price, c1, c2) in enumerate(shop):
        x = 60 + i * 190
        locked = i == 3
        o.append(btn(x, 1680, 164, 180, 40, c1 if not locked else "#5a5a6e",
                     c2 if not locked else "#32323f"))
        if kind == "gun":
            o.append(RR(x + 70, 1690, 24, 80, 12, "#ffffff",
                        'transform="rotate(24 %s 1766)"' % (x + 82)))
            o.append(C(x + 82, 1770, 34, "#ffffff"))
            o.append(C(x + 82, 1770, 15, c2))
        elif kind == "arrow":
            o.append('<path d="M %s 1792 L %s 1704 L %s 1792 Z" fill="#ffffff"/>' % (x + 44, x + 82, x + 120))
        elif kind == "mage":
            o.append(C(x + 82, 1742, 34, "#ffffff"))
            o.append(sparkle(x + 82, 1742, 22, "#d9a6ff", 0.95))
        else:
            o.append(C(x + 82, 1748, 34, "#20202c", 'stroke="#ffffff" stroke-width="4"'))
            o.append(T(x + 82, 1716, "⚠", 34, fill="#ffffff", fam=F))
        o.append(RR(x + 22, 1806, 120, 44, 22, "#00000055"))
        o.append(coin(x + 48, 1828, 18))
        o.append(T(x + 96, 1842, price, 30, fill="#ffd979"))
    o.append(btn(820, 1680, 212, 180, 44, "#9bf07a", "#2fa84f"))
    o.append(T(926, 1762, "▶", 60, fill="#ffffff", fam=F, stroke="#176b31", sw=6))
    o.append(T(926, 1822, "ВОЛНА", 30, fill="#ffffff", stroke="#176b31", sw=6))
    return "".join(o)


# ----------------------------------------------------------------------------
# 8. ФЕРМА
# ----------------------------------------------------------------------------
def crop(cx, cy, s, kind, stage=2):
    o = []
    if kind == "wheat":
        for dx in (-30, 0, 30):
            o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#4fae3e" stroke-width="%s" '
                     'stroke-linecap="round"/>' % (cx + dx * s, cy, cx + dx * s * 1.1, cy - 70 * s, 8 * s))
            if stage > 1:
                o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" stroke="#a85c00" '
                         'stroke-width="%s"/>' % (cx + dx * s * 1.1, cy - 82 * s, 15 * s, 28 * s,
                                                  lgrad("#ffe066", "#e8a000"), 3 * s))
    elif kind == "carrot":
        for dx in (-32, 2, 34):
            for a in (-26, 0, 26):
                o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#2fa84f" stroke-width="%s" '
                         'stroke-linecap="round"/>'
                         % (cx + dx * s, cy - 10 * s, cx + dx * s + a * s * 0.8, cy - 62 * s, 7 * s))
            if stage > 1:
                o.append('<path d="M %s %s L %s %s L %s %s Z" fill="%s" stroke="#a83800" '
                         'stroke-width="%s" stroke-linejoin="round"/>'
                         % (cx + dx * s - 16 * s, cy - 10 * s, cx + dx * s + 16 * s, cy - 10 * s,
                            cx + dx * s, cy + 24 * s, lgrad("#ffb08a", "#e2560f"), 3 * s))
    else:  # berry
        for dx in (-32, 2, 34):
            o.append(C(cx + dx * s, cy - 30 * s, 30 * s, rgrad("#9bf07a", "#2fa84f"),
                       'stroke="#176b31" stroke-width="%s"' % (3 * s)))
            if stage > 1:
                o.append(C(cx + dx * s - 10 * s, cy - 40 * s, 11 * s, "#e01e46"))
                o.append(C(cx + dx * s + 12 * s, cy - 24 * s, 10 * s, "#ff5470"))
    return "".join(o)


def plot(cx, cy, w, h, slant=46):
    pts = "%s,%s %s,%s %s,%s %s,%s" % (cx - w / 2, cy, cx - w / 2 + slant, cy - h,
                                       cx + w / 2 + slant, cy - h, cx + w / 2, cy)
    o = ['<polygon points="%s" fill="%s" stroke="#4a2a10" stroke-width="6" stroke-linejoin="round"/>'
         % (pts, lgrad("#a9703f", "#6d4220"))]
    for i in range(1, 4):
        y = cy - h * i / 4.0
        x0 = cx - w / 2 + slant * i / 4.0
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#5c3515" stroke-width="5" '
                 'opacity="0.55"/>' % (x0 + 12, y, x0 + w - 12, y))
    return "".join(o)


def screen_farm():
    o = []
    o.append(RR(0, 0, W, H, 0, lgrad3("#9fe3ff", "#d6f0a8", "#6cae46")))
    o.append(C(880, 250, 170, fade("#fff6b0", 0.8, 0.0)))
    o.append(C(880, 250, 82, "#fff3a0"))
    for cx, cy, s in ((230, 300, 0.9), (640, 220, 0.6)):
        o.append('<g opacity="0.9"><ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff"/>'
                 '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff"/></g>'
                 % (cx, cy, 96 * s, 56 * s, cx + 74 * s, cy + 16 * s, 62 * s, 40 * s))
    o.append('<path d="M 0 560 Q 280 470 560 540 Q 820 604 1080 520 L 1080 1920 L 0 1920 Z" fill="%s"/>'
             % lgrad("#86d46a", "#4e9440"))
    # амбар
    o.append(RR(690, 430, 320, 230, 24, lgrad("#ff8fa8", "#c01c3c"), 'stroke="#7d0c26" stroke-width="7"'))
    o.append('<path d="M 668 436 L 850 322 L 1032 436 Z" fill="%s" stroke="#7d0c26" stroke-width="7" '
             'stroke-linejoin="round"/>' % lgrad("#ffd979", "#e8870b"))
    o.append(RR(800, 520, 100, 140, 14, lgrad("#f8e3c0", "#c9a06a"), 'stroke="#7d0c26" stroke-width="6"'))
    o.append('<line x1="800" y1="590" x2="900" y2="590" stroke="#7d0c26" stroke-width="6"/>')
    # дерево и забор
    o.append(RR(150, 420, 40, 160, 18, lgrad("#a9703f", "#6d4220")))
    o.append(C(170, 400, 110, rgrad("#9bf07a", "#1f6b2f"), 'stroke="#14501f" stroke-width="6"'))
    o.append(C(96, 452, 66, rgrad("#86d46a", "#246b28")))
    o.append(C(246, 446, 60, rgrad("#86d46a", "#246b28")))
    for i in range(9):
        x = -20 + i * 130
        o.append(RR(x, 560, 26, 120, 10, lgrad("#f8e3c0", "#c9a06a"), 'stroke="#8a5a3a" stroke-width="4"'))
    o.append(RR(-20, 592, W + 40, 20, 8, lgrad("#f8e3c0", "#c9a06a"), 'stroke="#8a5a3a" stroke-width="4"'))
    # грядки
    beds = [(250, 940, "wheat", 2, "ready"), (600, 940, "carrot", 2, None), (950, 940, "berry", 1, "timer"),
            (250, 1160, "berry", 2, "ready"), (600, 1160, "wheat", 1, "timer"), (950, 1160, None, 0, "empty"),
            (250, 1380, "carrot", 2, "ready"), (600, 1380, None, 0, "empty"), (950, 1380, "wheat", 2, None)]
    for (cx, cy, kind, stage, mark) in beds:
        o.append(plot(cx, cy, 300, 140))
        if kind:
            o.append(crop(cx + 22, cy - 34, 0.9, kind, stage))
        ax = cx + (112 if cx < 700 else -112)
        if mark == "ready":
            o.append(C(ax, cy - 150, 40, lgrad("#9bf07a", "#2fa84f"), 'stroke="#ffffff" stroke-width="5"'))
            o.append('<path d="M %s %s l 14 16 l 26 -32" fill="none" stroke="#ffffff" stroke-width="9" '
                     'stroke-linecap="round" stroke-linejoin="round"/>' % (ax - 18, cy - 150))
        elif mark == "timer":
            o.append(RR(ax - 70, cy - 182, 140, 56, 28, "#1d0d45", 'stroke="#ffffff" stroke-width="4"'))
            o.append(T(ax, cy - 144, "2:40", 30, fill="#ffffff", fam=F, w=800))
        elif mark == "empty":
            o.append(C(ax, cy - 150, 40, lgrad("#ffd979", "#e8870b"), 'stroke="#ffffff" stroke-width="5"'))
            o.append(T(ax, cy - 134, "+", 48, stroke=None))
    # фермер и курица
    o.append(person(126, 1320, 0.62, "#8ce1ff", "#2b8fd6", hat="cap"))
    o.append('<ellipse cx="880" cy="1580" rx="44" ry="12" fill="#000000" opacity="0.22"/>')
    o.append(C(880, 1520, 54, rgrad("#ffffff", "#dfe4ee"), 'stroke="#b9bfd0" stroke-width="5"'))
    o.append(C(912, 1470, 32, rgrad("#ffffff", "#dfe4ee"), 'stroke="#b9bfd0" stroke-width="5"'))
    o.append('<path d="M 938 1468 L 972 1480 L 938 1492 Z" fill="#f49200"/>')
    o.append(C(922, 1462, 6, "#2a2338"))
    o.append(C(900, 1444, 14, "#e01e46"))

    o.append(statusbar("#143d2b", 0.8))
    # HUD
    o.append(pill(48, 104, 272, 78, "#ffd979", "#e8870b"))
    o.append(coin(92, 143, 31))
    o.append(T(216, 160, "26 410", 38, stroke="#8a4b00", sw=8))
    o.append(pill(344, 104, 236, 78, "#c9a3ff", "#6a2fd0"))
    o.append(gemicon(386, 143, 30, "#f5c6ff", "#c454f0"))
    o.append(T(490, 160, "86", 38, stroke="#3c0a66", sw=8))
    o.append(pill(604, 104, 268, 78, "#8ce1ff", "#2b8fd6"))
    o.append(C(646, 143, 30, lgrad("#fff3a0", "#f5a800"), 'stroke="#ffffff" stroke-width="4"'))
    o.append(T(646, 156, "7", 36, fill="#8a4b00", stroke=None))
    o.append(RR(682, 124, 160, 38, 19, "#0a4a8f"))
    o.append(RR(686, 128, 104, 30, 15, lgrad("#ffe066", "#f3a000")))
    o.append(btn(892, 100, 140, 86, 28, "#9bf07a", "#2fa84f"))
    o.append(T(962, 164, "☰", 46, fill="#ffffff", fam=F))
    # заказ
    o.append(RR(48, 206, 420, 136, 38, lgrad("#fff6e2", "#ffd9a0"), 'stroke="#b96d00" stroke-width="5"'))
    o.append(T(80, 258, "ЗАКАЗ ОТ ПЕКАРНИ", 26, fill="#a85c00", anchor="start", ls=1))
    for i in range(3):
        x = 92 + i * 92
        o.append(RR(x - 34, 274, 68, 52, 16, "#ffffff", 'stroke="#d8a257" stroke-width="4"'))
        o.append(crop(x - 10, 320, 0.4, ("wheat", "carrot", "berry")[i], 2))
        o.append(T(x + 22, 322, "×2", 24, fill="#5a3000"))
    o.append(btn(352, 254, 96, 68, 24, "#9bf07a", "#2fa84f"))
    o.append(T(400, 300, "✓", 42, fill="#ffffff", fam=F, stroke="#176b31", sw=5))

    # нижняя панель
    o.append(RR(-20, 1620, W + 40, 340, 52, lgrad("#8a5a2c", "#5c3515"), 'stroke="#ffd979" stroke-width="6"'))
    o.append(btn(60, 1660, 400, 130, 40, "#9bf07a", "#2fa84f"))
    o.append(T(260, 1742, "СОБРАТЬ ВСЁ", 42, fill="#ffffff", stroke="#176b31", sw=8))
    for i in range(3):
        x = 520 + i * 180
        o.append(btn(x, 1660, 156, 130, 38, "#ffd979", "#e8870b"))
        o.append(crop(x + 60, 1768, 0.72, ("wheat", "carrot", "berry")[i], 2))
    tabs = [("⌂", "ФЕРМА", True), ("☘", "ПОЛЯ", False), ("⚲", "МАГАЗИН", False),
            ("⚑", "ДРУЗЬЯ", False), ("☰", "ЕЩЁ", False)]
    for i, (ic, lb, act) in enumerate(tabs):
        x = 70 + i * 196
        col = "#5a3000" if act else "#ffffff"
        if act:
            o.append(RR(x - 14, 1812, 168, 108, 36, lgrad("#ffd979", "#e8870b"),
                        'stroke="#ffffff" stroke-width="4"'))
        o.append(T(x + 70, 1872, ic, 46, fill=col, fam=F))
        o.append(T(x + 70, 1906, lb, 23, fill=col, ls=1))
    return "".join(o)


# ----------------------------------------------------------------------------
# 9. СЛОВА
# ----------------------------------------------------------------------------
def screen_words():
    o = []
    o.append(RR(0, 0, W, H, 0, lgrad3("#1fa2b8", "#1b6ca8", "#15325e")))
    o.append(bg_blobs(["#8ef1ff", "#ffd166", "#6ee7c8"], seed=13, n=6, op=0.3))
    o.append(confetti(seed=5, n=40, colors=("#ffffff", "#8ef1ff"), op=0.25))
    o.append(statusbar())

    o.append(btn(48, 104, 92, 92, 30, "#2bc3d6", "#0d6f8a"))
    o.append(T(94, 170, "←", 52, fill="#ffffff", fam=F))
    o.append(pill(330, 108, 420, 86, "#ffd979", "#e8870b"))
    o.append(T(540, 168, "УРОВЕНЬ 412", 42, stroke="#8a4b00", sw=8))
    o.append(pill(790, 108, 242, 86, "#2bc3d6", "#0d6f8a"))
    o.append(coin(834, 151, 30))
    o.append(T(936, 166, "860", 38, stroke="#073f52", sw=8))

    # сетка кроссворда
    cell, gx, gy = 112, 148, 236
    letters = {(0, 1): "К", (0, 2): "Р", (0, 3): "А", (0, 4): "Б",
               (1, 1): "О", (1, 4): "О",
               (2, 1): "Р", (2, 3): "Л", (2, 4): "А", (2, 5): "К",
               (3, 1): "А", (5, 0): "К", (5, 1): "О", (5, 2): "Р", (5, 3): "А"}
    empty = [(5, 4), (5, 5), (5, 6)]
    for (r, c), ch in sorted(letters.items()):
        x, y = gx + c * cell, gy + r * cell
        o.append(RR(x + 6, y + 10, cell - 12, cell - 12, 26, "#00000030"))
        o.append(RR(x + 6, y + 6, cell - 12, cell - 12, 26, lgrad("#ffffff", "#d7ecf5"),
                    'stroke="#0d6f8a" stroke-width="5"'))
        o.append(T(x + cell / 2, y + cell / 2 + 22, ch, 62, fill="#0d4a66", fam=FB))
    for (r, c) in empty:
        x, y = gx + c * cell, gy + r * cell
        o.append(RR(x + 6, y + 6, cell - 12, cell - 12, 26, "#0b3f5c",
                    'stroke="#ffffff" stroke-opacity="0.4" stroke-width="4"'))
    o.append(RR(gx + 4 * cell + 6, gy + 5 * cell + 6, cell - 12, cell - 12, 26, "none",
                'stroke="#ffd166" stroke-width="6" stroke-dasharray="18 14" filter="url(#glow)"'))
    o.append(pill(380, 920, 320, 76, "#9bf07a", "#2fa84f"))
    o.append(T(540, 974, "БОНУС +15", 34, stroke="#176b31", sw=7))

    # текущее слово
    word = "КРАБ"
    bw = 100
    for i, ch in enumerate(word):
        x = 540 - (len(word) * bw) / 2 + i * bw + bw / 2
        o.append(RR(x - 44, 1010, 88, 92, 24, lgrad("#ffd979", "#e8870b"), 'stroke="#ffffff" stroke-width="5"'))
        o.append(T(x, 1078, ch, 54, fill="#ffffff", stroke="#8a4b00", sw=7))

    # колесо букв
    ccx, ccy, rad = 540, 1480, 220
    o.append(C(ccx, ccy, rad + 90, "#0b3f5c", 'opacity="0.55"'))
    o.append(C(ccx, ccy, rad + 90, "none", 'stroke="#2bc3d6" stroke-width="6" opacity="0.8"'))
    wheel = "КОРАБЛЬ"
    sel = [0, 2, 3, 4]
    pts = []
    for i, ch in enumerate(wheel):
        a = math.radians(-90 + i * 360.0 / len(wheel))
        x, y = ccx + rad * math.cos(a), ccy + rad * math.sin(a)
        pts.append((x, y, ch, i in sel))
    sp = [(x, y) for (x, y, ch, s) in pts if s]
    o.append('<polyline points="%s" fill="none" stroke="#ffd166" stroke-width="14" '
             'stroke-linecap="round" stroke-linejoin="round" opacity="0.9"/>'
             % " ".join("%.1f,%.1f" % (x, y) for (x, y) in sp))
    for (x, y, ch, s) in pts:
        if s:
            o.append(C(x, y, 62, lgrad("#ffd979", "#e8870b"), 'stroke="#ffffff" stroke-width="6"'))
            o.append(T(x, y + 22, ch, 58, fill="#ffffff", stroke="#8a4b00", sw=7))
        else:
            o.append(C(x, y + 5, 58, "#00000035"))
            o.append(C(x, y, 58, lgrad("#ffffff", "#cfe6f0"), 'stroke="#0d6f8a" stroke-width="5"'))
            o.append(T(x, y + 20, ch, 54, fill="#0d4a66", fam=FB))
    o.append(btn(ccx - 66, ccy - 60, 132, 120, 40, "#2bc3d6", "#0d6f8a"))
    o.append(T(ccx, ccy + 18, "↻", 62, fill="#ffffff", fam=F))

    o.append(btn(60, 1700, 160, 150, 44, "#ffd979", "#e8870b"))
    o.append(T(140, 1788, "✦", 62, fill="#ffffff", fam=F, stroke="#8a4b00", sw=5))
    o.append(T(140, 1830, "ПОДСКАЗКА", 22, fill="#ffffff", ls=1))
    o.append(btn(860, 1700, 160, 150, 44, "#9bf07a", "#2fa84f"))
    o.append(T(940, 1790, "☰", 58, fill="#ffffff", fam=F, stroke="#176b31", sw=5))
    o.append(T(940, 1830, "БОНУС", 22, fill="#ffffff", ls=1))
    return "".join(o)


# ----------------------------------------------------------------------------
# 10. ПАСЬЯНС
# ----------------------------------------------------------------------------
SUITS = {"s": ("♠", "#2a2338"), "h": ("♥", "#d11149"),
         "d": ("♦", "#d11149"), "c": ("♣", "#2a2338")}


def card_face(cx, cy, rank, suit, w=132, h=184, rot=0):
    sym, col = SUITS[suit]
    g = ['<g transform="rotate(%s %s %s)">' % (rot, cx, cy)]
    g.append(RR(cx - w / 2, cy - h / 2 + 8, w, h, 20, "#00000038"))
    g.append(RR(cx - w / 2, cy - h / 2, w, h, 20, lgrad("#ffffff", "#e8eef5"),
                'stroke="#b9c3d0" stroke-width="4"'))
    g.append(T(cx - w / 2 + 22, cy - h / 2 + 50, rank, 40, fill=col, anchor="middle", fam=FB))
    g.append(T(cx - w / 2 + 22, cy - h / 2 + 84, sym, 30, fill=col, fam=F))
    g.append(T(cx, cy + 36, sym, 86, fill=col, fam=F))
    g.append("</g>")
    return "".join(g)


def card_back(cx, cy, w=132, h=184, rot=0):
    g = ['<g transform="rotate(%s %s %s)">' % (rot, cx, cy)]
    g.append(RR(cx - w / 2, cy - h / 2 + 8, w, h, 20, "#00000038"))
    g.append(RR(cx - w / 2, cy - h / 2, w, h, 20, lgrad("#6a8dff", "#2b3fa8"),
                'stroke="#ffffff" stroke-width="5"'))
    g.append(RR(cx - w / 2 + 16, cy - h / 2 + 16, w - 32, h - 32, 14, "none",
                'stroke="#ffffff" stroke-opacity="0.55" stroke-width="4"'))
    for i in range(3):
        g.append(sparkle(cx, cy - 36 + i * 36, 18, "#ffffff", 0.5))
    g.append("</g>")
    return "".join(g)


def screen_solitaire():
    o = []
    o.append(RR(0, 0, W, H, 0, lgrad3("#2f9e5e", "#17764a", "#0b3d2c")))
    o.append(C(540, 900, 760, fade("#9bf07a", 0.35, 0.0)))
    o.append(confetti(seed=19, n=40, colors=("#ffffff",), op=0.12))
    o.append(statusbar())

    o.append(btn(48, 104, 92, 92, 30, "#2fa84f", "#176b31"))
    o.append(T(94, 170, "←", 52, fill="#ffffff", fam=F))
    o.append(pill(300, 108, 300, 86, "#7b4bd6", "#3a1b73"))
    o.append(T(450, 168, "УР. 240", 42, stroke="#1d0d45", sw=8))
    for i in range(3):
        o.append(star(640 + i * 62, 150, 30, lgrad("#fff3a0", "#f5a800") if i < 2 else "#1d0d45",
                      stroke="#b06a00" if i < 2 else "#0b3d2c", sw=5))
    o.append(pill(820, 108, 212, 86, "#ffd979", "#e8870b"))
    o.append(coin(862, 151, 30))
    o.append(T(958, 166, "420", 38, stroke="#8a4b00", sw=8))

    # три пика
    peaks = (248, 540, 832)
    cw, ch = 118, 166
    random.seed(3)
    for px in peaks:
        o.append(card_back(px, 356, w=cw, h=ch, rot=random.randint(-3, 3)))
    for px in peaks:
        for dx in (-62, 62):
            o.append(card_back(px + dx, 470, w=cw, h=ch, rot=random.randint(-3, 3)))
    for px in peaks:
        for dx in (-124, 0, 124):
            o.append(card_back(px + dx, 584, w=cw, h=ch, rot=random.randint(-3, 3)))
    faces = [("7", "h"), ("Д", "s"), ("3", "d"), ("К", "c"), ("9", "h"), ("2", "s"),
             ("В", "d"), ("5", "c"), ("10", "h"), ("Т", "s")]
    for i, (rk, st) in enumerate(faces):
        o.append(card_face(96 + i * 98, 700, rk, st))

    # стопка и текущая карта
    for i in range(4):
        o.append(card_back(250 - i * 6, 1180 - i * 6, w=150, h=208))
    o.append(C(336, 1104, 40, lgrad("#ff6b8a", "#d11149"), 'stroke="#ffffff" stroke-width="5"'))
    o.append(T(336, 1120, "17", 34, stroke=None))
    o.append(T(250, 1340, "КОЛОДА", 28, fill="#ffffff", op=0.85, ls=3))
    o.append(card_face(600, 1180, "8", "d", w=168, h=232))
    o.append(T(600, 1340, "В ИГРЕ", 28, fill="#ffffff", op=0.85, ls=3))
    o.append(btn(830, 1086, 190, 190, 52, "#ffd979", "#e8870b"))
    o.append(T(925, 1198, "★", 80, fill="#ffffff", fam=F, stroke="#8a4b00", sw=6))
    o.append(T(925, 1340, "ДЖОКЕР", 28, fill="#ffffff", op=0.85, ls=3))
    # подсказка хода
    o.append('<path d="M 430 760 Q 500 980 560 1080" fill="none" stroke="#ffd166" stroke-width="9" '
             'stroke-dasharray="6 26" stroke-linecap="round" opacity="0.9"/>')

    o.append(RR(0, 1420, W, 500, 0, "#00000025"))
    o.append(RR(60, 1452, 960, 180, 48, lgrad("#0f5a3c", "#07331f"), 'stroke="#9bf07a" stroke-width="5"'))
    o.append(T(120, 1530, "ОЧКИ", 28, fill="#9bf07a", anchor="start", ls=3))
    o.append(T(120, 1592, "18 460", 50, fill="#ffffff", anchor="start"))
    o.append(T(560, 1530, "КОМБО", 28, fill="#9bf07a", anchor="start", ls=3))
    o.append(T(560, 1592, "× 6", 50, fill="#ffd166", anchor="start"))
    o.append(RR(800, 1480, 180, 124, 36, lgrad("#ffd979", "#e8870b"), 'stroke="#ffffff" stroke-width="4"'))
    o.append(T(890, 1546, "⏱", 44, fill="#ffffff", fam=F))
    o.append(T(890, 1586, "2:14", 30, fill="#ffffff"))
    o.append(btn(90, 1690, 420, 150, 48, "#2bc3d6", "#0d6f8a"))
    o.append(T(300, 1780, "↶  ОТМЕНА", 42, fill="#ffffff", stroke="#073f52", sw=8))
    o.append(btn(570, 1690, 420, 150, 48, "#9bf07a", "#2fa84f"))
    o.append(T(780, 1780, "▶  +5 КАРТ", 42, fill="#ffffff", stroke="#176b31", sw=8))
    return "".join(o)


# ----------------------------------------------------------------------------
# 11. БЛОК-ПАЗЛ
# ----------------------------------------------------------------------------
BLOCKC = [("#ff8aa0", "#d11149"), ("#8ad6ff", "#1273de"), ("#ffe066", "#f49200"),
          ("#9bf07a", "#2fa84f"), ("#d9a6ff", "#7b2cbf"), ("#ffb08a", "#e2560f")]


def blk(x, y, s, k, op=1.0):
    c1, c2 = BLOCKC[k % len(BLOCKC)]
    return (RR(x + 3, y + 3, s - 6, s - 6, s * 0.22, lgrad(c1, c2),
               'stroke="#00000033" stroke-width="3" opacity="%s"' % op) +
            RR(x + 10, y + 10, s - 20, s * 0.3, s * 0.12, "#ffffff", 'opacity="%s"' % (0.38 * op)))


def screen_blocks():
    o = []
    o.append(RR(0, 0, W, H, 0, lgrad3("#2b3b8f", "#1b2259", "#0d1030")))
    o.append(bg_blobs(["#4cc9f0", "#7b5bff"], seed=23, n=5, op=0.35))
    o.append(confetti(seed=29, n=45, colors=("#ffffff", "#8ef1ff"), op=0.3))
    o.append(statusbar())

    o.append(btn(48, 104, 92, 92, 30, "#5b6bd6", "#2b2f7a"))
    o.append(RR(76, 130, 14, 40, 6, "#ffffff"))
    o.append(RR(100, 130, 14, 40, 6, "#ffffff"))
    o.append(T(540, 190, "45 820", 92, fill="#ffffff", stroke="#0d1030", sw=14))
    o.append(T(540, 238, "ОЧКИ", 30, fill="#8ef1ff", ls=6))
    o.append(pill(790, 104, 242, 86, "#ffd979", "#e8870b"))
    o.append(star(834, 147, 30, lgrad("#fff3a0", "#f5a800")))
    o.append(T(940, 162, "61 300", 30, stroke="#8a4b00", sw=7))

    # поле 10x10
    cell, gx, gy = 96, 60, 400
    o.append(RR(gx - 22, gy - 22, cell * 10 + 44, cell * 10 + 44, 40, "#00000040"))
    o.append(RR(gx - 22, gy - 22, cell * 10 + 44, cell * 10 + 44, 40, lgrad("#1b2259", "#11153a"),
                'stroke="#5b6bd6" stroke-width="6"'))
    random.seed(77)
    grid = [[None] * 10 for _ in range(10)]
    for r in range(10):
        for c in range(10):
            if random.random() < 0.34:
                grid[r][c] = random.randint(0, 5)
    for c in range(10):
        grid[6][c] = 2 if c < 9 else None
    for r in range(10):
        for c in range(10):
            x, y = gx + c * cell, gy + r * cell
            o.append(RR(x + 6, y + 6, cell - 12, cell - 12, 20, "#ffffff", 'opacity="0.06"'))
            if grid[r][c] is not None:
                o.append(blk(x, y, cell, grid[r][c]))
    o.append(RR(gx - 6, gy + 6 * cell - 6, cell * 10 + 12, cell + 12, 24, "none",
                'stroke="#ffd166" stroke-width="7" filter="url(#glow)"'))
    o.append(T(980, gy + 6 * cell + 64, "!", 56, fill="#ffd166", stroke="#5a3000", sw=6))
    o.append(pill(380, 1380, 320, 78, "#ffd979", "#e8870b"))
    o.append(T(540, 1434, "КОМБО ×3", 38, stroke="#8a4b00", sw=8))

    # фигуры снизу
    o.append(RR(-20, 1500, W + 40, 440, 52, lgrad("#1b2259", "#0d1030"), 'stroke="#5b6bd6" stroke-width="6"'))
    shapes = [([(0, 0), (0, 1), (1, 0), (1, 1)], 1, 160, 1600, 86),
              ([(0, 0), (1, 0), (2, 0), (2, 1)], 3, 480, 1556, 86),
              ([(0, 0), (0, 1), (0, 2)], 4, 760, 1644, 86)]
    for (cells, k, ox, oy, s) in shapes:
        lifted = ox == 480
        if lifted:
            for (r, c) in cells:
                o.append(RR(ox + c * s + 10, oy + r * s + 26, s - 6, s - 6, s * 0.22,
                            "#000000", 'opacity="0.3"'))
        for (r, c) in cells:
            o.append(blk(ox + c * s, oy + r * s - (14 if lifted else 0), s, k))
    o.append(T(540, 1888, "ПЕРЕТАЩИ ФИГУРУ НА ПОЛЕ", 32, fill="#8ef1ff", ls=2, op=0.9))
    return "".join(o)


# ----------------------------------------------------------------------------
# 12. TRIPLE MATCH
# ----------------------------------------------------------------------------
TM = [("#ff8fa8", "#d6234f"), ("#8ce1ff", "#2b8fd6"), ("#ffd979", "#e8870b"),
      ("#9bf07a", "#2fa84f"), ("#d9a6ff", "#7b2cbf"), ("#ffb08a", "#e2560f"),
      ("#6ee7c8", "#13a383")]


def item(cx, cy, s, k, rot=0):
    c1, c2 = TM[k]
    g = ['<g transform="rotate(%s %s %s)">' % (rot, cx, cy)]
    g.append(RR(cx - 58 * s, cy - 52 * s, 116 * s, 116 * s, 34 * s, "#00000035"))
    g.append(RR(cx - 58 * s, cy - 58 * s, 116 * s, 116 * s, 34 * s, lgrad(c1, c2),
                'stroke="#ffffff" stroke-width="%s"' % (5 * s)))
    g.append(RR(cx - 44 * s, cy - 46 * s, 88 * s, 30 * s, 15 * s, "#ffffff", 'opacity="0.3"'))
    w = "#ffffff"
    if k == 0:      # кекс
        g.append('<path d="M %s %s a %s %s 0 0 1 %s 0 Z" fill="%s"/>'
                 % (cx - 36 * s, cy - 2 * s, 36 * s, 36 * s, 72 * s, w))
        g.append(RR(cx - 32 * s, cy, 64 * s, 36 * s, 10 * s, w, 'opacity="0.85"'))
    elif k == 1:    # часы
        g.append(C(cx, cy, 36 * s, "none", 'stroke="%s" stroke-width="%s"' % (w, 9 * s)))
        g.append('<path d="M %s %s L %s %s L %s %s" fill="none" stroke="%s" stroke-width="%s" '
                 'stroke-linecap="round" stroke-linejoin="round"/>'
                 % (cx, cy - 22 * s, cx, cy, cx + 18 * s, cy + 8 * s, w, 8 * s))
    elif k == 2:    # ключ
        g.append(C(cx - 10 * s, cy - 14 * s, 22 * s, "none", 'stroke="%s" stroke-width="%s"' % (w, 9 * s)))
        g.append(RR(cx + 2 * s, cy - 2 * s, 12 * s, 46 * s, 6 * s, w))
        g.append(RR(cx + 2 * s, cy + 24 * s, 30 * s, 11 * s, 5 * s, w))
    elif k == 3:    # лист
        g.append('<path d="M %s %s C %s %s %s %s %s %s C %s %s %s %s %s %s Z" fill="%s"/>'
                 % (cx, cy - 40 * s, cx + 42 * s, cy - 20 * s, cx + 30 * s, cy + 30 * s, cx, cy + 40 * s,
                    cx - 30 * s, cy + 30 * s, cx - 42 * s, cy - 20 * s, cx, cy - 40 * s, w))
        g.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" opacity="0.45"/>'
                 % (cx, cy - 30 * s, cx, cy + 34 * s, c2, 6 * s))
    elif k == 4:    # звезда
        g.append(star(cx, cy, 42 * s, w, stroke="none", sw=0))
    elif k == 5:    # мяч
        g.append(C(cx, cy, 38 * s, w))
        g.append('<path d="M %s %s q %s %s %s 0" fill="none" stroke="%s" stroke-width="%s"/>'
                 % (cx - 30 * s, cy - 8 * s, 30 * s, 26 * s, 60 * s, c2, 7 * s))
        g.append('<path d="M %s %s q %s %s %s 0" fill="none" stroke="%s" stroke-width="%s"/>'
                 % (cx - 30 * s, cy + 14 * s, 30 * s, -26 * s, 60 * s, c2, 7 * s))
    else:           # шестерёнка
        g.append(poly(cx, cy, 42 * s, 8, 22, w, "none", 0))
        g.append(C(cx, cy, 16 * s, c2))
    g.append("</g>")
    return "".join(g)


def screen_triple():
    o = []
    o.append(RR(0, 0, W, H, 0, lgrad3("#5f4bb6", "#8a5fd0", "#3a1b73")))
    o.append(bg_blobs(["#ff6ec7", "#8ef1ff", "#ffd166"], seed=41, n=6, op=0.35))
    o.append(confetti(seed=43, n=50, colors=("#ffffff", "#ffd166"), op=0.28))
    o.append(statusbar())

    o.append(btn(48, 104, 92, 92, 30, "#8c6bd6", "#4a2a8f"))
    o.append(RR(76, 130, 14, 40, 6, "#ffffff"))
    o.append(RR(100, 130, 14, 40, 6, "#ffffff"))
    o.append(pill(300, 108, 300, 86, "#7b4bd6", "#2e1566"))
    o.append(T(450, 168, "УР. 58", 42, stroke="#1d0d45", sw=8))
    o.append(C(700, 150, 54, "#2e1566", 'stroke="#ffd166" stroke-width="7"'))
    o.append('<path d="M 700 96 a 54 54 0 0 1 44 84" fill="none" stroke="#ffd166" stroke-width="9" '
             'stroke-linecap="round"/>')
    o.append(T(700, 166, "1:32", 28, fill="#ffffff", fam=F, w=800))
    o.append(pill(790, 108, 242, 86, "#ffd979", "#e8870b"))
    o.append(coin(834, 151, 30))
    o.append(T(936, 166, "1 980", 34, stroke="#8a4b00", sw=8))

    # цель
    o.append(RR(300, 228, 480, 86, 43, lgrad("#2e1566", "#1a0b40"), 'stroke="#c9a3ff" stroke-width="5"'))
    o.append(T(348, 284, "ЦЕЛЬ:", 32, fill="#c9a3ff", anchor="start", fam=F, w=800))
    o.append(item(500, 268, 0.34, 0))
    o.append(T(556, 284, "× 9", 34, fill="#ffffff", anchor="start"))
    o.append(item(660, 268, 0.34, 3))
    o.append(T(716, 284, "× 6", 34, fill="#ffffff", anchor="start"))

    # россыпь предметов
    random.seed(55)
    o.append(RR(70, 360, 940, 960, 56, "#00000030"))
    o.append(RR(70, 360, 940, 960, 56, lgrad("#6f55c9", "#42288f"), 'stroke="#c9a3ff" stroke-width="6"'))
    spots = []
    for r in range(5):
        for c in range(5):
            x = 180 + c * 180 + random.randint(-26, 26)
            y = 460 + r * 180 + random.randint(-24, 24)
            spots.append((x, y, random.randint(0, 6), random.randint(-22, 22)))
    for (x, y, k, rot) in spots:
        o.append(item(x, y, 0.82, k, rot))
    o.append(RR(176, 440, 124, 124, 36, "none",
                'stroke="#ffd166" stroke-width="7" stroke-dasharray="20 16" filter="url(#glow)"'))

    # лоток
    o.append(RR(40, 1400, 1000, 200, 54, "#00000035"))
    o.append(RR(40, 1400, 1000, 200, 54, lgrad("#2e1566", "#160b36"), 'stroke="#ffd166" stroke-width="6"'))
    tray = [0, 0, 3, 5, None, None, None]
    for i, k in enumerate(tray):
        x = 100 + i * 134
        o.append(RR(x - 58, 1442, 116, 116, 32, "#ffffff", 'opacity="0.10"'))
        o.append(RR(x - 58, 1442, 116, 116, 32, "none",
                    'stroke="#ffffff" stroke-opacity="0.35" stroke-width="4"'))
        if k is not None:
            o.append(item(x, 1500, 0.78, k))
    o.append(RR(36, 1436, 274, 128, 38, "none",
                'stroke="#9bf07a" stroke-width="7" filter="url(#glow)"'))
    o.append(T(540, 1648, "СОБЕРИ ТРИ ОДИНАКОВЫХ", 34, fill="#ffffff", ls=2, op=0.9))

    # бустеры
    boosters = [("↶", "ОТМЕНА", "#8ce1ff", "#2b8fd6", None),
                ("❄", "СТОП", "#9bf07a", "#2fa84f", "2"),
                ("↻", "МИКС", "#ff9e6b", "#e2560f", "1"),
                ("+3", "СЛОТА", "#ffd979", "#e8870b", "▶")]
    for i, (ic, lb, c1, c2, badge) in enumerate(boosters):
        x = 56 + i * 248
        o.append(btn(x, 1700, 200, 150, 44, c1, c2))
        o.append(T(x + 100, 1792, ic, 54, fill="#ffffff", fam=F, stroke="#00000030", sw=4))
        o.append(T(x + 100, 1832, lb, 24, fill="#ffffff", ls=1))
        if badge:
            o.append(C(x + 184, 1708, 28, lgrad("#ff6b8a", "#d11149"), 'stroke="#ffffff" stroke-width="4"'))
            o.append(T(x + 184, 1720, badge, 28, stroke=None, fam=FB if badge != "▶" else F))
    return "".join(o)


SCREENS2 = [("Slime_Defense", screen_td, "Slime Defense"),
            ("Happy_Harvest", screen_farm, "Happy Harvest"),
            ("WordSea", screen_words, "WordSea"),
            ("TriPeaks_Royal", screen_solitaire, "TriPeaks Royal"),
            ("Block_Nova", screen_blocks, "Block Nova"),
            ("Tile_Trio_Rush", screen_triple, "Tile Trio Rush")]

if __name__ == "__main__":
    for name, fn, title in SCREENS2:
        DEFS[:] = []
        CNT[0] = 0
        write(name, fn(), title)
