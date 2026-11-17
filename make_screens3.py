# -*- coding: utf-8 -*-
"""Полноэкранные макеты по присланным референсам: 1080x1920, без рамки телефона
и без строки состояния. Рендер — render3.ps1."""

import math, os, random

import make_screens as ms
from make_screens import (W, H, F, FB, DEFS, CNT, T, RR, C, btn, pill, coin, star,
                          heart, poly, sparkle, lgrad, lgrad3, rgrad, fade, write)
from screens3_lib import *

ROOT = os.path.dirname(os.path.abspath(__file__))
ms.HTML_DIR = os.path.join(ROOT, "html3")


# ----------------------------------------------------------------------------
# фоны
# ----------------------------------------------------------------------------
def palm_frond(cx, cy, r, ang, c1="#9bf07a", c2="#1f6b2f"):
    o = [f'<g transform="rotate({ang} {cx} {cy})">']
    o.append(f'<path d="M {cx} {cy} q {r*0.5} {-r*0.1} {r} {-r*0.05}" fill="none" stroke="#1f6b2f" '
             f'stroke-width="{r*0.06}" stroke-linecap="round"/>')
    for i in range(7):
        t = 0.1 + i * 0.13
        bx, by = cx + r * t, cy - r * 0.05 * t
        for s in (-1, 1):
            o.append(f'<ellipse cx="{bx+r*0.12:.1f}" cy="{by+s*r*0.16:.1f}" rx="{r*0.19}" ry="{r*0.075}" '
                     f'fill="{lgrad(c1, c2)}" transform="rotate({s*26} {bx:.1f} {by:.1f})"/>')
    o.append('</g>')
    return "".join(o)


def bush(cx, cy, r, c1="#9bf07a", c2="#1f6b2f"):
    return (C(cx, cy, r, rgrad(c1, c2)) + C(cx - r * 0.8, cy + r * 0.26, r * 0.72, rgrad(c1, c2)) +
            C(cx + r * 0.82, cy + r * 0.3, r * 0.66, rgrad(c1, c2)))


def tree(cx, cy, s, c1="#9bf07a", c2="#1f6b2f"):
    return (RR(cx - 22 * s, cy - 150 * s, 44 * s, 170 * s, 18 * s, lgrad("#a9703f", "#6d4220")) +
            C(cx, cy - 190 * s, 96 * s, rgrad(c1, c2)) +
            C(cx - 76 * s, cy - 136 * s, 64 * s, rgrad(c1, c2)) +
            C(cx + 78 * s, cy - 142 * s, 58 * s, rgrad(c1, c2)))


def small_flower(cx, cy, r, c="#ffffff", core="#ffd166"):
    o = []
    for i in range(5):
        a = math.radians(i * 72)
        o.append(C(cx + r * 0.7 * math.cos(a), cy + r * 0.7 * math.sin(a), r * 0.46, c))
    o.append(C(cx, cy, r * 0.4, core))
    return "".join(o)


def clouds(items, c="#ffffff", op=0.9):
    o = []
    for (cx, cy, s) in items:
        o.append(f'<g opacity="{op}"><ellipse cx="{cx}" cy="{cy}" rx="{96*s}" ry="{56*s}" fill="{c}"/>'
                 f'<ellipse cx="{cx-76*s}" cy="{cy+16*s}" rx="{62*s}" ry="{38*s}" fill="{c}"/>'
                 f'<ellipse cx="{cx+78*s}" cy="{cy+18*s}" rx="{56*s}" ry="{34*s}" fill="{c}"/></g>')
    return "".join(o)


def starfield(seed, n, y0, y1, colors=("#ffffff",), rmax=4, op=(0.3, 0.95)):
    random.seed(seed)
    o = []
    for _ in range(n):
        o.append(C(random.randint(0, W), random.randint(y0, y1), random.choice([2, 3, rmax]),
                   random.choice(colors), f'opacity="{round(random.uniform(*op), 2)}"'))
    return "".join(o)


# ----------------------------------------------------------------------------
# 1. TROPIC FRUIT POP  (референс 1)
# ----------------------------------------------------------------------------
def scene_tropic():
    o = [RR(0, 0, W, H, 0, lgrad3("#bfe9a8", "#8ad46a", "#4e9440"))]
    o.append(C(540, 420, 760, fade("#ffffff", 0.35, 0.0)))
    o.append(palm_frond(-40, 120, 380, 18))
    o.append(palm_frond(1120, 90, 400, 162))
    o.append(palm_frond(-20, 430, 300, -24))
    o.append(palm_frond(1100, 470, 320, 204))
    for (x, y, s) in ((70, 1700, 1.0), (1010, 1660, 0.9), (150, 1880, 0.8), (930, 1890, 0.7)):
        o.append(bush(x, y, 90 * s))
    random.seed(2)
    for _ in range(16):
        x, y = random.randint(20, 1060), random.randint(1560, 1900)
        o.append(small_flower(x, y, random.randint(14, 22),
                              random.choice(["#ffffff", "#ffd1e8", "#fff3a0"])))
    o.append(RR(-20, 1540, W + 40, 60, 30, "#5aa83c", 'opacity="0.5"'))

    # HUD
    o.append(round_btn(96, 108, 52, "#c08a52", "#7a4520"))
    o.append(RR(80, 86, 14, 44, 6, "#ffffff"))
    o.append(RR(102, 86, 14, 44, 6, "#ffffff"))
    o.append(round_btn(216, 108, 52, "#c08a52", "#7a4520"))
    o.append(f'<path d="M 196 92 L 214 92 L 232 74 L 232 142 L 214 124 L 196 124 Z" fill="#ffffff"/>')
    o.append(f'<path d="M 244 90 q 20 18 0 36" fill="none" stroke="#ffffff" stroke-width="7" '
             f'stroke-linecap="round"/>')
    o.append(T(560, 126, "SCORE: 12,450", 58, fill="#ffffff", stroke="#2b5a1e", sw=12))
    o.append(T(930, 72, "LEVEL 14", 40, fill="#ffffff", stroke="#2b5a1e", sw=10))
    o.append(s_star(886, 126, 36))
    o.append(T(956, 142, "2/3", 38, fill="#ffffff", stroke="#2b5a1e", sw=9))

    # доска
    bx, by, cols, rows, cell = 54, 186, 7, 8, 138
    bw, bh = cols * cell, rows * cell
    o.append(RR(bx - 22, by - 22, bw + 44, bh + 52, 44, "#00000035"))
    o.append(RR(bx - 22, by - 22, bw + 44, bh + 44, 44, lgrad("#b5793f", "#8a5324"),
                'stroke="#5a3515" stroke-width="7"'))
    o.append(RR(bx - 4, by - 4, bw + 8, bh + 8, 30, lgrad("#8a5a2c", "#6d4220")))
    icons = [f_strawberry, f_orange, f_greenapple, f_grapes, f_pineapple, f_kiwi, f_banana,
             f_orange_slice, f_apple]
    random.seed(21)
    hole = {(3, 2), (3, 3), (4, 2), (4, 3), (4, 4), (5, 3)}
    for r_ in range(rows):
        for c_ in range(cols):
            cx = bx + c_ * cell + cell / 2
            cy = by + r_ * cell + cell / 2
            o.append(RR(cx - cell / 2 + 7, cy - cell / 2 + 7, cell - 14, cell - 14, 18,
                        "#ffffff", f'opacity="{0.10 if (r_+c_) % 2 == 0 else 0.04}"'))
            if (r_, c_) in hole:
                continue
            o.append(f'<g filter="url(#shs)">{random.choice(icons)(cx, cy, 56)}</g>')
    # взрыв в центре
    o.append(burst(540, 700, 150))
    for (cx, cy) in ((470, 648), (628, 648), (536, 760)):
        o.append(f'<g filter="url(#shs)">{f_strawberry(cx, cy, 62)}</g>')
    o.append(pop_label(372, 612, "POP!", 48, -14))
    o.append(pop_label(690, 740, "POP!", 44, 12))
    o.append(pop_label(380, 760, "POP!", 40, -8))
    o.append(pop_label(660, 580, "POP!", 36, 16))

    # траектория и пушка
    o.append(dotted([(540, 1480), (540, 820)], w=10, gap="3 30"))
    o.append(f'<path d="M 540 790 l -26 44 l 52 0 Z" fill="#ffffff" opacity="0.9"/>')
    o.append(C(540, 1610, 118, "#00000030"))
    o.append(f_pineapple(540, 1600, 112))
    o.append(RR(452, 1480, 176, 46, 23, lgrad("#cfd9e8", "#8c9bb5"), 'stroke="#44506b" stroke-width="5"'))
    o.append(f'<g filter="url(#shs)">{f_strawberry(540, 1420, 66)}</g>')
    for sx in (-1, 1):
        o.append(C(540 + sx * 128, 1690, 38, lgrad("#6d4220", "#3b2410"), 'stroke="#2a1a08" stroke-width="5"'))
        o.append(C(540 + sx * 128, 1690, 14, "#c08a52"))
    # панель следующих
    o.append(RR(912, 1372, 132, 380, 56, "#00000030"))
    o.append(RR(912, 1372, 132, 380, 56, lgrad("#b5793f", "#7a4520"), 'stroke="#5a3515" stroke-width="6"'))
    for i, fn in enumerate((f_orange, f_greenapple, f_grapes)):
        o.append(fn(978, 1452 + i * 116, 48))
    return "".join(o)


# ----------------------------------------------------------------------------
# 2. SKY LEAP  (референс 2)
# ----------------------------------------------------------------------------
def scene_skyleap():
    o = [RR(0, 0, W, H, 0, lgrad3("#1d3b96", "#2f7fd6", "#9fdcff"))]
    o.append(starfield(7, 90, 120, 1500, ("#ffffff", "#fff3a0", "#bfe9ff")))
    o.append(C(180, 420, 46, rgrad("#d9c2ff", "#8a6ad0"), 'opacity="0.9"'))
    o.append(f'<ellipse cx="180" cy="420" rx="86" ry="20" fill="none" stroke="#e8dcff" '
             f'stroke-width="7" transform="rotate(-20 180 420)" opacity="0.9"/>')
    o.append(C(900, 520, 40, rgrad("#ffffff", "#b9c6e0"), 'opacity="0.85"'))
    o.append(C(960, 1120, 30, rgrad("#ffffff", "#b9c6e0"), 'opacity="0.6"'))
    o.append(f'<path d="M 700 300 l 120 -70 l -34 86 Z" fill="#ffffff" opacity="0.55"/>')
    pastel = [("#ffd1e8", "#ff9bd0"), ("#d9f7a8", "#86d46a"), ("#ffe9a8", "#ffc46b"),
              ("#cfe6ff", "#8ad6ff"), ("#e6d1ff", "#b48aff")]
    random.seed(11)
    for i in range(12):
        c1, c2 = pastel[i % len(pastel)]
        cx, cy = random.randint(60, 1020), random.randint(380, 1500)
        s = random.uniform(0.35, 0.8)
        o.append(f'<g opacity="0.95"><ellipse cx="{cx}" cy="{cy}" rx="{110*s}" ry="{58*s}" '
                 f'fill="{lgrad(c1, c2)}"/><ellipse cx="{cx-72*s}" cy="{cy+16*s}" rx="{64*s}" '
                 f'ry="{40*s}" fill="{lgrad(c1, c2)}"/><ellipse cx="{cx+76*s}" cy="{cy+18*s}" '
                 f'rx="{58*s}" ry="{36*s}" fill="{lgrad(c1, c2)}"/></g>')
    for (x, y, s) in ((120, 1660, 1.3), (520, 1760, 1.6), (900, 1650, 1.2), (320, 1880, 1.4),
                      (760, 1900, 1.3)):
        o.append(clouds([(x, y, s)], "#ffffff", 0.95))
    o.append(RR(-20, 1820, W + 40, 140, 70, "#ffffff", 'opacity="0.9"'))

    # логотип
    o.append(logo(540, 128, "SKY LEAP", None, 96, c1="#ffffff", c2="#cfe6ff",
                  stroke="#2b4a9c", sw=18))

    # HUD
    o.append(T(60, 236, "SCORE:", 40, fill="#ffffff", anchor="start", stroke="#1d3b96", sw=9))
    o.append(s_star(96, 306, 46))
    o.append(T(148, 326, "4,850", 64, fill="#ffe066", anchor="start", stroke="#1d3b96", sw=12))
    o.append(progress(60, 364, 560, 44, 0.33, "#ffe066", "#f0a500", "#1d3b96"))
    o.append(T(600, 398, "15,000", 30, fill="#ffffff", anchor="end", stroke="#1d3b96", sw=7))
    o.append(T(1020, 236, "BEST: 22,100", 38, fill="#ffffff", anchor="end", stroke="#1d3b96", sw=9))
    o.append(clouds([(912, 310, 0.34)], "#ffffff", 1.0))
    o.append(s_star(934, 290, 20))
    o.append(T(1020, 326, "× 3", 42, fill="#ffffff", anchor="end", stroke="#1d3b96", sw=9))

    # шкала MILESTONES
    o.append(RR(998, 520, 34, 700, 17, "#1d3b96", 'stroke="#ffffff" stroke-width="4" opacity="0.85"'))
    o.append(RR(1002, 900, 26, 316, 13, lgrad("#ffe066", "#f0a500")))
    for i in range(4):
        o.append(s_star(1015, 560 + i * 170, 22))
    o.append(T(0, 0, "MILESTONES", 30, fill="#ffffff", stroke="#1d3b96", sw=7,
               extra='transform="translate(962 870) rotate(-90)"'))

    # герой и звёзды
    o.append(s_star(760, 820, 86))
    o.append(C(760, 820, 150, fade("#fff3a0", 0.55, 0.0)))
    for (x, y, r) in ((300, 760, 38), (420, 660, 32), (640, 700, 30), (330, 980, 28),
                      (860, 1060, 34), (240, 1180, 26)):
        o.append(s_star(x, y, r))
    o.append(f'<g filter="url(#shs)">{mascot_cloud(452, 880, 1.15)}</g>')
    o.append(star(756, 1180, 54, lgrad("#fff3a0", "#f0a500"), stroke="#b06a00", sw=5))
    o.append(f'<path d="M 700 1156 q -56 -30 -96 2 q 54 10 96 -2 Z" fill="#ffffff" opacity="0.95"/>')
    return "".join(o)


# ----------------------------------------------------------------------------
# 3. MEDITATION / SLEEP  (референс 3)
# ----------------------------------------------------------------------------
def scene_meditation():
    o = [RR(0, 0, W, H, 0, lgrad3("#1b2a6b", "#2b4a9c", "#8a6ad0"))]
    o.append(starfield(5, 70, 60, 900, ("#ffffff", "#dfe6ff")))
    o.append(C(300, 330, 60, "#dfe6ff", 'opacity="0.0"'))
    o.append(f'<path d="M 318 268 a 76 76 0 1 0 2 128 a 62 62 0 1 1 -2 -128 Z" fill="#e8eeff" '
             f'opacity="0.95"/>')
    o.append(sparkle(236, 400, 20, "#ffffff", 0.9))
    o.append(sparkle(880, 250, 16, "#ffffff", 0.7))
    o.append(clouds([(180, 180, 0.5), (860, 140, 0.4)], "#ffffff", 0.35))
    # солнце/луна
    o.append(C(620, 520, 230, fade("#ffd9c0", 0.5, 0.0)))
    o.append(C(620, 520, 148, rgrad("#ffe9d8", "#ffc9a8")))
    # горы
    o.append(f'<path d="M -40 980 L 240 520 L 470 980 Z" fill="{lgrad("#4a63b5", "#2b3f8f")}"/>')
    o.append(f'<path d="M 320 980 L 700 440 L 1120 980 Z" fill="{lgrad("#3a53a5", "#1f2f7a")}"/>')
    o.append(f'<path d="M -40 1060 L 300 640 L 700 1060 Z" fill="{lgrad("#2f4a9c", "#17266b")}"/>')
    o.append(f'<path d="M 520 1060 L 900 700 L 1180 1060 Z" fill="{lgrad("#27409c" , "#13205c")}"/>')
    # светило в долине
    o.append(C(540, 1010, 260, fade("#ffb98a", 0.55, 0.0)))
    o.append(C(540, 1010, 150, rgrad("#ffe3c0", "#ff9e6b")))
    o.append(f'<path d="M -40 1060 Q 300 1010 540 1070 Q 820 1130 1120 1060 L 1120 1920 L -40 1920 Z" '
             f'fill="{lgrad("#1b2f7a", "#0d1740")}"/>')
    # озеро
    o.append(f'<ellipse cx="560" cy="1300" rx="330" ry="86" fill="{lgrad("#5a8fd6", "#2b4a9c")}" '
             f'opacity="0.95"/>')
    o.append(f'<ellipse cx="300" cy="1420" rx="190" ry="52" fill="{lgrad("#5a8fd6", "#2b4a9c")}" '
             f'opacity="0.8"/>')
    o.append(RR(420, 1272, 260, 10, 5, "#ffd9c0", 'opacity="0.55"'))
    o.append(RR(470, 1308, 160, 8, 4, "#ffd9c0", 'opacity="0.4"'))
    # ели
    random.seed(9)
    for (x, y, s) in ((80, 1240, 1.0), (170, 1300, 1.3), (980, 1220, 1.1), (900, 1300, 1.4),
                      (1040, 1340, 1.2), (30, 1360, 1.2)):
        o.append(f'<path d="M {x} {y-130*s} L {x+46*s} {y} L {x-46*s} {y} Z" fill="#0b1a46"/>')
        o.append(f'<path d="M {x} {y-180*s} L {x+36*s} {y-70*s} L {x-36*s} {y-70*s} Z" fill="#0b1a46"/>')

    # верхняя подпись
    o.append(f'<path d="M 52 70 a 26 26 0 1 1 0.1 0" fill="none" stroke="#ffffff" stroke-width="5" '
             f'opacity="0.85"/>')
    o.append(f'<path d="M 65 56 L 65 72 L 78 78" fill="none" stroke="#ffffff" stroke-width="5" '
             f'stroke-linecap="round" opacity="0.85"/>')
    o.append(C(458, 122, 22, rgrad("#8a6ad0", "#3a2a8f"), 'stroke="#ffffff" stroke-width="3"'))
    o.append(f'<path d="M 466 112 a 13 13 0 1 0 0.4 22 a 11 11 0 1 1 -0.4 -22 Z" fill="#ffffff"/>')
    o.append(T(500, 134, "Meditation / SLEEP", 32, fill="#ffffff", anchor="start", fam=F, w=700, op=0.95))

    # плеер
    o.append(f'<path d="M 212 1646 L 212 1726 M 212 1686 L 282 1640 L 282 1732 Z" fill="#ffffff" '
             f'stroke="#ffffff" stroke-width="12" stroke-linejoin="round"/>')
    o.append(f'<path d="M 490 1618 L 616 1690 L 490 1762 Z" fill="#ffffff"/>')
    o.append(f'<path d="M 868 1646 L 868 1726 M 868 1686 L 798 1640 L 798 1732 Z" fill="#ffffff" '
             f'stroke="#ffffff" stroke-width="12" stroke-linejoin="round"/>')
    o.append(RR(120, 1832, 840, 10, 5, "#ffffff", 'opacity="0.45"'))
    o.append(RR(120, 1832, 180, 10, 5, "#ffffff"))
    o.append(C(300, 1837, 20, "#ffffff"))
    return "".join(o)


# ----------------------------------------------------------------------------
# 4. HAPPY CUBES MATCH  (референс 4)
# ----------------------------------------------------------------------------
def scene_cubes():
    o = [RR(0, 0, W, H, 0, lgrad3("#a8e4ff", "#d9f3a8", "#79c45a"))]
    o.append(clouds([(180, 150, 0.7), (880, 110, 0.55)], "#ffffff", 0.9))
    o.append(f'<path d="M -40 470 Q 280 360 620 450 Q 880 516 1120 420 L 1120 1920 L -40 1920 Z" '
             f'fill="{lgrad("#c9ea84", "#86c45a")}"/>')
    o.append(f'<path d="M -40 640 Q 320 560 700 650 Q 920 700 1120 630 L 1120 1920 L -40 1920 Z" '
             f'fill="{lgrad("#a8dc6a", "#5aa83c")}"/>')
    random.seed(4)
    for _ in range(26):
        x, y = random.randint(10, 1070), random.randint(500, 1900)
        o.append(small_flower(x, y, random.randint(12, 20),
                              random.choice(["#ffffff", "#ffd1e8", "#fff3a0", "#d9c2ff"])))
    for (x, y, rx) in ((250, 1500, 62), (430, 1560, 48), (650, 1520, 54), (840, 1580, 44)):
        o.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{rx*0.5}" fill="#c9c4b5" '
                 f'stroke="#9a9484" stroke-width="4"/>')
    # кубики вокруг доски
    random.seed(8)
    outside = [(120, 420, 0.8), (300, 370, 0.7), (470, 410, 0.75), (690, 360, 0.72),
               (860, 420, 0.8), (150, 1430, 0.9), (330, 1470, 0.75), (700, 1460, 0.8),
               (930, 1420, 0.85), (520, 1380, 0.6)]
    kinds = list(CUBES.keys())
    for (x, y, s) in outside:
        o.append(cube_fruit(x, y, s, random.choice(kinds), rot=random.randint(-12, 12)))

    # верхние панели
    o.append(dark_panel(44, 60, 540, 170, 34, "#3f5a33", "#1d2f16", "#c9ea84", 5))
    o.append(f'<ellipse cx="124" cy="150" rx="58" ry="42" fill="{lgrad("#d9a05b", "#8a5324")}" '
             f'stroke="#5a3515" stroke-width="5"/>')
    o.append(f_apple(104, 112, 30))
    o.append(f_greenapple(150, 120, 26))
    o.append(T(208, 128, "Goal: 30 Apples", 38, fill="#ffffff", anchor="start", fam=F, w=800))
    o.append(T(208, 192, "Score: 1,850", 38, fill="#ffe066", anchor="start", fam=F, w=800))
    o.append(dark_panel(700, 60, 336, 170, 34, "#3f5a33", "#1d2f16", "#c9ea84", 5))
    o.append(T(868, 126, "Moves Left:", 34, fill="#ffffff", fam=F, w=800))
    o.append(T(868, 196, "25", 56, fill="#ffe066"))

    # доска
    bx, by, cols, rows, cell = 40, 600, 6, 5, 132
    bw, bh = cols * cell, rows * cell
    o.append(RR(bx - 18, by - 18, bw + 36, bh + 44, 40, "#00000030"))
    o.append(RR(bx - 18, by - 18, bw + 36, bh + 36, 40, lgrad("#8fc96a", "#4e8c34"),
                'stroke="#2f6b20" stroke-width="7"'))
    random.seed(33)
    for r_ in range(rows):
        for c_ in range(cols):
            cx = bx + c_ * cell + cell / 2
            cy = by + r_ * cell + cell / 2
            o.append(cube_fruit(cx, cy, 1.18, random.choice(kinds)))
    # россыпь монет
    random.seed(12)
    for i in range(22):
        a = random.uniform(0, 6.28)
        d = random.uniform(0, 150)
        o.append(coin(430 + math.cos(a) * d, 960 + math.sin(a) * d * 0.7,
                      random.randint(18, 28), sym=""))
    o.append(burst(430, 960, 120, "#fff3a0", "#ffd166"))

    # правая колонка кнопок
    tools = [("Level\nProgress\n13 / 100", "#8a5a2c", "#5c3515", "pin"),
             ("Level\nProgress\n14 / 100", "#8a5a2c", "#5c3515", "pin"),
             ("Hint", "#5a6a7d", "#2d3a4a", "layers"),
             ("Undo", "#5a6a7d", "#2d3a4a", "ruler"),
             ("Booster", "#7d5a8a", "#3f2a4a", "rainbow"),
             ("Shuffle", "#5a6a7d", "#2d3a4a", "circle"),
             ("Level\nProgress\n12 / 100", "#8a5a2c", "#5c3515", "pin")]
    for i, (label, c1, c2, icon) in enumerate(tools):
        cy = 420 + i * 184
        o.append(round_btn(982, cy, 64, c1, c2, stroke="#e8d9b5", sw=5))
        if icon == "pin":
            o.append(f'<path d="M 982 {cy-26} a 24 24 0 1 1 -0.1 0 M 982 {cy+30} L 962 {cy-6} '
                     f'L 1002 {cy-6} Z" fill="#e8d9b5"/>')
            o.append(C(982, cy - 12, 10, c2))
        elif icon == "layers":
            for k in range(3):
                o.append(f'<path d="M 982 {cy-24+k*18} l 32 16 l -32 16 l -32 -16 Z" fill="#e8d9b5" '
                         f'opacity="{0.6+k*0.2}"/>')
        elif icon == "ruler":
            o.append(RR(950, cy - 16, 64, 32, 8, "#e8d9b5", f'transform="rotate(-20 982 {cy})"'))
        elif icon == "rainbow":
            for k, cc in enumerate(("#ff6b8a", "#ffd166", "#9bf07a", "#8ad6ff")):
                o.append(f'<path d="M {982-34+k*5} {cy+18} a {34-k*5} {34-k*5} 0 0 1 {(34-k*5)*2} 0" '
                         f'fill="none" stroke="{cc}" stroke-width="7"/>')
            o.append(f_apple(982, cy + 2, 16))
        else:
            o.append(C(982, cy, 26, "none", 'stroke="#e8d9b5" stroke-width="7"'))
            o.append(C(982, cy, 10, "#e8d9b5"))
        lines = label.split("\n")
        for k, ln in enumerate(lines):
            o.append(T(982, cy + 86 + k * 28, ln, 24, fill="#ffffff", fam=F, w=800,
                       stroke="#2b3f1a", sw=5))

    # баннер и нижняя навигация
    o.append(RR(240, 1596, 600, 110, 55, "#00000030"))
    o.append(RR(240, 1596, 600, 110, 55, lgrad("#b8f07a", "#4e9c2a"), 'stroke="#2f6b20" stroke-width="5"'))
    o.append(T(392, 1648, "☝", 46, fill="#ffe066", fam=F))
    o.append(T(580, 1646, "Успех!", 40, fill="#ffffff", stroke="#2f6b20", sw=7))
    o.append(T(580, 1690, "К Уровню 13", 30, fill="#ffffff", fam=F, w=800))
    o.append(RR(24, 1762, 1032, 140, 44, "#00000025"))
    o.append(RR(24, 1762, 1032, 140, 44, lgrad("#fff6e2", "#e8d9b5"), 'stroke="#b08f5a" stroke-width="5"'))
    navs = [("Home", "#4e9c2a"), ("Shop", "#e2560f"), ("Profile", "#2b8fd6")]
    for i, (lb, cc) in enumerate(navs):
        x = 196 + i * 344
        if lb == "Home":
            o.append(f'<path d="M {x-36} {1830} L {x} {1794} L {x+36} {1830} L {x+36} {1864} '
                     f'L {x-36} {1864} Z" fill="{cc}"/>')
        elif lb == "Shop":
            o.append(RR(x - 36, 1812, 72, 52, 10, cc))
            o.append(f'<path d="M {x-44} {1812} L {x-28} {1788} L {x+28} {1788} L {x+44} {1812} Z" fill="{cc}"/>')
        else:
            o.append(C(x, 1810, 22, cc))
            o.append(f'<path d="M {x-34} {1864} a 34 34 0 0 1 68 0 Z" fill="{cc}"/>')
        o.append(T(x, 1896, lb, 30, fill="#5a3000", fam=F, w=800))
    return "".join(o)


# ----------------------------------------------------------------------------
# 5. ENCHANTED MATCH QUEST  (референс 5)
# ----------------------------------------------------------------------------
def scene_enchanted():
    o = [RR(0, 0, W, H, 0, lgrad3("#15304a", "#1b4a52", "#0a1a2a"))]
    o.append(C(620, 300, 520, fade("#8ef1ff", 0.22, 0.0)))
    o.append(starfield(14, 60, 60, 700, ("#ffffff", "#8ef1ff")))
    o.append(f'<path d="M 760 300 a 60 60 0 1 0 2 100 a 48 48 0 1 1 -2 -100 Z" fill="#dff6ff" opacity="0.9"/>')
    # замок
    for (x, h, w_) in ((880, 300, 44), (946, 380, 52), (1016, 290, 42)):
        o.append(RR(x, 620 - h, w_, h, 10, lgrad("#8ef1ff", "#2b6ad6"), 'opacity="0.55"'))
        o.append(f'<path d="M {x-8} {620-h} L {x+w_/2} {620-h-70} L {x+w_+8} {620-h} Z" '
                 f'fill="#8ef1ff" opacity="0.6"/>')
    # деревья по краям
    for (x, s, flip) in ((70, 1.5, 1), (1010, 1.4, -1)):
        o.append(f'<path d="M {x} 1700 C {x-40*s} 1200 {x+60*s} 900 {x-10*s} 420 '
                 f'L {x+70*s} 400 C {x+120*s} 900 {x+30*s} 1240 {x+90*s} 1720 Z" '
                 f'fill="{lgrad("#2b5a52", "#102a2a")}"/>')
        for i in range(5):
            o.append(C(x + flip * (40 + i * 40) * s, 300 + i * 60, 90 * s,
                       fade("#3fe8c8", 0.25, 0.0)))
    random.seed(17)
    for _ in range(40):
        x, y = random.randint(0, W), random.randint(200, 1860)
        o.append(C(x, y, random.choice([3, 4, 6]), "#9bf0d8",
                   f'opacity="{round(random.uniform(0.3, 0.9), 2)}"'))
    # земля, руины, книги
    o.append(f'<path d="M -40 1560 Q 300 1500 560 1560 Q 840 1620 1120 1540 L 1120 1920 L -40 1920 Z" '
             f'fill="{lgrad("#2b5a42", "#0e2a22")}"/>')
    o.append(RR(90, 1380, 130, 190, 20, lgrad("#8a9ab5", "#46566b"), 'stroke="#2a3447" stroke-width="5"'))
    o.append(f'<path d="M 90 1380 a 65 65 0 0 1 130 0 Z" fill="{lgrad("#8a9ab5", "#46566b")}" '
             f'stroke="#2a3447" stroke-width="5"/>')
    o.append(f'<path d="M 155 1410 L 155 1520 M 120 1448 L 190 1448" stroke="#2a3447" stroke-width="9"/>')
    for (x, y, s, c1, c2) in ((250, 1760, 1.0, "#b48aff", "#5a2a9c"), (870, 1740, 1.1, "#ff9e6b", "#8a3a0c")):
        o.append(f'<g transform="rotate({-8 if s > 1 else 6} {x} {y})">'
                 + RR(x - 90 * s, y - 56 * s, 180 * s, 112 * s, 14 * s, lgrad(c1, c2),
                      'stroke="#2a1a3a" stroke-width="5"')
                 + RR(x - 78 * s, y - 44 * s, 156 * s, 88 * s, 10 * s, "#ffffff", 'opacity="0.12"')
                 + C(x, y, 26 * s, "none", 'stroke="#ffe9a8" stroke-width="5" opacity="0.9"')
                 + '</g>')
    for (x, y) in ((430, 1800), (1000, 1850), (150, 1850)):
        o.append(f'<path d="M {x-40} {y} q 40 -70 80 0 q -40 26 -80 0 Z" '
                 f'fill="{lgrad("#c08a52", "#6d4220")}" stroke="#3b2410" stroke-width="4"/>')
        o.append(C(x + 10, y - 26, 10, "#ff8fa8"))
    for (x, y, s) in ((330, 1680, 1.0), (640, 1740, 0.8), (980, 1640, 0.9)):
        o.append(f'<path d="M {x-26*s} {y} L {x-10*s} {y-40*s} L {x+10*s} {y-40*s} L {x+26*s} {y} Z" '
                 f'fill="#e8f6ff" opacity="0.9"/>')
        o.append(f'<ellipse cx="{x}" cy="{y-42*s}" rx="{40*s}" ry="{24*s}" fill="#ff7a8f"/>')
        o.append(C(x - 12 * s, y - 48 * s, 6 * s, "#ffffff"))
        o.append(C(x + 14 * s, y - 44 * s, 5 * s, "#ffffff"))

    # доска
    bx, by, cols, rows, cell = 120, 330, 7, 10, 120
    bw, bh = cols * cell, rows * cell
    o.append(RR(bx - 26, by - 26, bw + 52, bh + 60, 30, "#00000045"))
    o.append(RR(bx - 26, by - 26, bw + 52, bh + 52, 30, lgrad("#6b5a3a", "#3a2f1c"),
                'stroke="#c9a96a" stroke-width="7"'))
    o.append(RR(bx - 8, by - 8, bw + 16, bh + 16, 18, lgrad("#5a4a2e", "#2e2614")))
    items = [f_apple, f_orange, m_leaf, m_gem, m_gem_violet, f_apple, m_leaf, m_gem]
    special = {(0, 6): m_knight, (2, 3): m_shield, (3, 7): m_wolf, (5, 2): m_knight,
               (6, 5): m_shield, (8, 1): m_wolf}
    random.seed(29)
    for r_ in range(rows):
        for c_ in range(cols):
            cx = bx + c_ * cell + cell / 2
            cy = by + r_ * cell + cell / 2
            o.append(RR(cx - cell / 2 + 5, cy - cell / 2 + 5, cell - 10, cell - 10, 12,
                        "#ffffff", 'opacity="0.05"'))
            fn = special.get((r_, c_), random.choice(items))
            o.append(f'<g filter="url(#shs)">{fn(cx, cy, 46)}</g>')
    return "".join(o)


# ----------------------------------------------------------------------------
# 6 и 7. POP ADVENTURE  (референсы 6 и 7)
# ----------------------------------------------------------------------------
def pop_adventure(theme):
    o = []
    if theme == "berry":
        o.append(RR(0, 0, W, H, 0, lgrad3("#bfe9ff", "#c9ea84", "#5aa83c")))
        o.append(f'<path d="M -40 520 Q 300 430 620 510 Q 880 570 1120 480 L 1120 1920 L -40 1920 Z" '
                 f'fill="{lgrad("#9fd96a", "#3f8c2a")}"/>')
        for (x, y, s) in ((110, 560, 1.1), (330, 500, 0.8), (780, 520, 0.9), (1000, 580, 1.2)):
            o.append(tree(x, y, s))
        random.seed(6)
        for _ in range(22):
            x, y = random.randint(10, 1070), random.randint(560, 1880)
            o.append(small_flower(x, y, random.randint(12, 20),
                                  random.choice(["#ffffff", "#ffd1e8", "#fff3a0"])))
        for (x, y, s) in ((90, 1780, 1.0), (980, 1820, 1.2), (250, 1880, 0.8)):
            o.append(f'<path d="M {x-40*s} {y} L {x-16*s} {y-44*s} L {x+16*s} {y-44*s} L {x+40*s} {y} Z" '
                     f'fill="#f4ffe8"/>')
            o.append(f'<ellipse cx="{x}" cy="{y-46*s}" rx="{54*s}" ry="{32*s}" fill="#ff7a8f"/>')
            o.append(C(x - 16 * s, y - 54 * s, 8 * s, "#ffffff"))
            o.append(C(x + 18 * s, y - 48 * s, 7 * s, "#ffffff"))
        logo_lines = ("BERRY POP", "ADVENTURES")
        logo_cols = ("#8ad6ff", "#1273de", "#ff8fa8", "#d11149")
        board_c = ("#2b4a8f", "#13265c", "#8ad6ff")
        icons = [f_blueberry, f_strawberry, s_star, m_leaf, f_plum,
                 lambda cx, cy, r: heart(cx, cy, r * 0.95, "#ff8fa8", "#e01e46")]
        focus = f_blueberry
        pts = "+200 pts!"
        goal = ("Match 15 BLUEBERRIES, 10 STARS", "7/15", "4/10", 7 / 15.0, 0.4)
        stats = ("98,450", "125,700", "12")
        heart_c = ("#ff8fa8", "#e01e46")
        boosters = [("hammer", "x2"), ("bomb", "x1"), ("shuffle", "x3")]
        nav = [("HOME", "home"), ("LEADERBOARD", "cup"), ("PLAY", "play"), ("SHOP", "shop"),
               ("EVENTS", "cal")]
        navbar = ("#2b8fd6", "#1273de")
        mascot = lambda: mascot_bear(880, 1330, 0.72)
    else:
        o.append(RR(0, 0, W, H, 0, lgrad3("#2b1b6b", "#4a2a9c", "#1b1046")))
        o.append(starfield(21, 110, 60, 1900, ("#ffffff", "#8ef1ff", "#ffd1e8")))
        o.append(C(140, 300, 120, rgrad("#cfd9e8", "#7c8aa8"), 'opacity="0.85"'))
        o.append(C(980, 240, 86, rgrad("#ffd1e8", "#c454f0"), 'opacity="0.8"'))
        o.append(s_planet(960, 1500, 120))
        o.append(s_planet(120, 1700, 90, "#8ce1ff", "#2b8fd6", ring=False))
        logo_lines = ("Celestial Merge", "Adventure")
        logo_cols = ("#8ef1ff", "#2b8fd6", "#ffd166", "#f0820b")
        board_c = ("#3a2a8f", "#1b1046", "#c9a3ff")
        icons = [s_galaxy, lambda cx, cy, r: s_planet(cx, cy, r), s_earth, s_mars, s_starcrystal,
                 lambda cx, cy, r: s_galaxy(cx, cy, r, "#f3b6ff", "#7b2cbf")]
        focus = s_starcrystal
        pts = "+350 pts!"
        goal = ("Collect 25 STAR DUST, 15 PLANETS", "8/25", "5/15", 8 / 25.0, 1 / 3.0)
        stats = ("115,200", "168,000", "18")
        heart_c = ("#8ce1ff", "#2b8fd6")
        boosters = [("comet", "x2"), ("bomb", "x1"), ("planet", "x3")]
        nav = [("HOME", "rocket"), ("LEADERBOARD", "cup"), ("LAUNCH", "play"), ("SHOP", "shop"),
               ("EVENTS", "comet")]
        navbar = ("#2b8fd6", "#1273de")
        mascot = lambda: mascot_astronaut(880, 1320, 0.68)

    # логотип
    o.append(logo(540, 150, logo_lines[0], logo_lines[1], 76, 60,
                  c1=logo_cols[0], c2=logo_cols[1], stroke="#1b2a5c", sw=16,
                  c3=logo_cols[2], c4=logo_cols[3]))
    for (x, y, r) in ((176, 120, 24), (916, 108, 20), (250, 214, 16)):
        o.append(s_star(x, y, r))

    # статистика
    o.append(coin(104, 322, 34))
    o.append(T(150, 300, "Score", 26, fill="#ffffff", anchor="start", fam=F, w=800, op=0.85))
    o.append(T(150, 344, stats[0], 40, fill="#ffffff", anchor="start", stroke="#1b2a5c", sw=8))
    o.append(T(430, 300, "High Score", 26, fill="#ffffff", fam=F, w=800, op=0.85))
    o.append(T(430, 344, stats[1], 40, fill="#ffffff", stroke="#1b2a5c", sw=8))
    o.append(T(690, 300, "Level", 26, fill="#ffffff", fam=F, w=800, op=0.85))
    o.append(T(690, 344, stats[2], 40, fill="#ffffff", stroke="#1b2a5c", sw=8))
    o.append(T(900, 300, "Lives", 26, fill="#ffffff", fam=F, w=800, op=0.85))
    for i in range(3):
        o.append(heart(858 + i * 46, 332, 20, heart_c[0], heart_c[1]))

    # цель
    o.append(panel(60, 384, 960, 150, 34, "#fff6e2", "#ffe9c0", "#b96d00", 5))
    o.append(T(540, 440, f"LEVEL {stats[2]} GOAL:", 32, fill="#a85c00", ls=1))
    o.append(T(540, 486, goal[0], 32, fill="#2b2a3a", fam=F, w=800))
    o.append(progress(104, 496, 360, 40, goal[3], "#8ad6ff", "#1273de", "#d8c9a8"))
    o.append(T(284, 528, goal[1], 26, fill="#ffffff", stroke="#0a4a8f", sw=6))
    o.append(progress(616, 496, 360, 40, goal[4], "#ffe066", "#f0a500", "#d8c9a8"))
    o.append(T(796, 528, goal[2], 26, fill="#ffffff", stroke="#8a4b00", sw=6))

    # поле
    bx, by, cols, rows, cell = 86, 580, 8, 8, 114
    bw, bh = cols * cell, rows * cell
    o.append(RR(bx - 20, by - 20, bw + 40, bh + 48, 40, "#00000035"))
    o.append(RR(bx - 20, by - 20, bw + 40, bh + 40, 40, lgrad(board_c[0], board_c[1]),
                f'stroke="{board_c[2]}" stroke-width="6"'))
    random.seed(44 if theme == "berry" else 55)
    cluster = {(3, 3), (3, 4), (3, 5), (4, 2), (4, 3), (4, 4), (5, 2), (5, 3)}
    for r_ in range(rows):
        for c_ in range(cols):
            cx = bx + c_ * cell + cell / 2
            cy = by + r_ * cell + cell / 2
            o.append(RR(cx - cell / 2 + 5, cy - cell / 2 + 5, cell - 10, cell - 10, 18,
                        "#ffffff", 'opacity="0.06"'))
            fn = focus if (r_, c_) in cluster else random.choice(icons)
            o.append(f'<g filter="url(#shs)">{fn(cx, cy, 44)}</g>')
    o.append(C(bx + 3.6 * cell, by + 4.2 * cell, 230, fade("#ffffff", 0.5, 0.0)))
    for (dx, dy) in ((-1.2, -0.8), (1.4, 0.4), (0.2, 1.6), (-1.6, 1.0)):
        o.append(sparkle(bx + (3.6 + dx) * cell, by + (4.2 + dy) * cell, 26, "#ffffff", 0.85))
    o.append(T(840, 880, pts, 46, fill="#ffe066", stroke="#8a4b00", sw=10))
    o.append(f'<g filter="url(#shs)">{mascot()}</g>')

    # бустеры
    for i, (kind, mult) in enumerate(boosters):
        x = 160 + i * 300
        o.append(RR(x - 110, 1430, 220, 150, 40, "#00000030"))
        o.append(RR(x - 110, 1430, 220, 150, 40, lgrad("#ffffff", "#dfe6ef"),
                    'stroke="#9aa8bd" stroke-width="5"'))
        if kind == "hammer":
            o.append(RR(x - 16, 1480, 30, 86, 12, lgrad("#c08a52", "#6d4220"),
                        f'transform="rotate(16 {x} 1500)"'))
            o.append(RR(x - 60, 1462, 120, 50, 16, lgrad("#cfd9e8", "#7c8aa8"),
                        f'stroke="#44506b" stroke-width="4" transform="rotate(16 {x} 1500)"'))
        elif kind == "bomb":
            o.append(C(x, 1516, 48, rgrad("#5a6070", "#1d2029"), 'stroke="#0d0f14" stroke-width="4"'))
            o.append(f'<path d="M {x+22} {1472} q 26 -28 44 -6" fill="none" stroke="#ffd166" '
                     f'stroke-width="9" stroke-linecap="round"/>')
            o.append(sparkle(x + 72, 1458, 20, "#fff3a0", 0.95))
        elif kind == "shuffle":
            o.append(f'<path d="M {x-44} {1540} a 54 54 0 1 1 20 34" fill="none" stroke="#2fa84f" '
                     f'stroke-width="14" stroke-linecap="round"/>')
            o.append(f'<path d="M {x-56} {1498} l 24 10 l -8 26 Z" fill="#2fa84f"/>')
        elif kind == "comet":
            o.append(s_star(x + 10, 1500, 40))
            o.append(f'<path d="M {x-20} {1524} l -56 42" stroke="#8ef1ff" stroke-width="12" '
                     f'stroke-linecap="round"/>')
        else:
            o.append(s_planet(x, 1506, 46))
        o.append(RR(x + 30, 1536, 76, 50, 25, lgrad("#ff6b8a", "#d11149"), 'stroke="#ffffff" stroke-width="4"'))
        o.append(T(x + 68, 1572, mult, 30, fill="#ffffff"))

    # нижняя панель
    o.append(RR(-20, 1630, W + 40, 300, 54, lgrad(navbar[0], navbar[1]),
                'stroke="#ffffff" stroke-width="5"'))
    for i, (lb, icon) in enumerate(nav):
        x = 130 + i * 190
        if icon == "play":
            o.append(RR(x - 150, 1660, 300, 130, 65, "#00000030"))
            o.append(RR(x - 150, 1660, 300, 130, 65, lgrad("#9bf07a", "#2fa84f"),
                        'stroke="#ffffff" stroke-width="6"'))
            o.append(T(x, 1748, lb, 54, fill="#ffffff", stroke="#176b31", sw=9))
            continue
        if icon == "home":
            o.append(f'<path d="M {x-26} {1726} L {x} {1700} L {x+26} {1726} L {x+26} {1752} '
                     f'L {x-26} {1752} Z" fill="#ffffff"/>')
        elif icon == "cup":
            o.append(RR(x - 22, 1700, 44, 36, 10, "#ffd166"))
            o.append(RR(x - 10, 1736, 20, 16, 4, "#ffd166"))
            o.append(RR(x - 24, 1752, 48, 10, 5, "#ffd166"))
        elif icon == "shop":
            o.append(RR(x - 26, 1714, 52, 40, 8, "#ffffff"))
            o.append(f'<path d="M {x-32} {1714} L {x-20} {1694} L {x+20} {1694} L {x+32} {1714} Z" '
                     f'fill="#ffd166"/>')
        elif icon == "cal":
            o.append(RR(x - 26, 1700, 52, 52, 10, "#ffffff"))
            o.append(RR(x - 26, 1700, 52, 16, 8, "#ff8fa8"))
        elif icon == "rocket":
            o.append(f'<path d="M {x} {1694} q 22 26 22 56 l -44 0 q 0 -30 22 -56 Z" fill="#ffffff"/>')
            o.append(f'<path d="M {x-22} {1744} l -12 16 l 18 -4 Z M {x+22} {1744} l 12 16 l -18 -4 Z" '
                     f'fill="#ff8fa8"/>')
        else:
            o.append(s_star(x, 1718, 24))
            o.append(f'<path d="M {x-16} {1736} l -22 20" stroke="#8ef1ff" stroke-width="8" '
                     f'stroke-linecap="round"/>')
        o.append(T(x, 1790, lb, 22, fill="#ffffff", ls=1))
    o.append(RR(420, 1886, 240, 10, 5, "#ffffff", 'opacity="0.8"'))
    return "".join(o)


def scene_berrypop():
    return pop_adventure("berry")


def scene_celestial():
    return pop_adventure("space")


# ----------------------------------------------------------------------------
# 8. GARDEN BLAST  (референс 8)
# ----------------------------------------------------------------------------
def scene_garden():
    o = [RR(0, 0, W, H, 0, lgrad3("#a8e4ff", "#d9f3a8", "#6cae46"))]
    o.append(clouds([(220, 130, 0.6), (900, 170, 0.5)], "#ffffff", 0.85))
    o.append(f'<path d="M -40 520 Q 320 430 660 520 Q 900 580 1120 500 L 1120 1920 L -40 1920 Z" '
             f'fill="{lgrad("#9fd96a", "#4e9440")}"/>')
    # домик
    o.append(RR(830, 360, 220, 160, 16, lgrad("#fff6e2", "#e8d9b5"), 'stroke="#8a5a3a" stroke-width="6"'))
    o.append(f'<path d="M 806 362 L 940 250 L 1074 362 Z" fill="{lgrad("#ff8fa8", "#c01c3c")}" '
             f'stroke="#7d0c26" stroke-width="6" stroke-linejoin="round"/>')
    o.append(RR(900, 430, 80, 90, 10, lgrad("#c08a52", "#6d4220"), 'stroke="#4a2a10" stroke-width="5"'))
    # пруд и дорожка
    o.append(f'<ellipse cx="700" cy="560" rx="150" ry="52" fill="{lgrad("#8ad6ff", "#2b8fd6")}" '
             f'stroke="#1b6ca8" stroke-width="5"/>')
    o.append(f'<path d="M 300 1920 Q 420 1500 300 1080 Q 220 800 340 560" fill="none" '
             f'stroke="#e8d9b5" stroke-width="90" opacity="0.65"/>')
    random.seed(3)
    for _ in range(30):
        x, y = random.randint(10, 1070), random.randint(540, 1900)
        o.append(small_flower(x, y, random.randint(12, 22),
                              random.choice(["#ffffff", "#ffd1e8", "#fff3a0", "#d9c2ff"])))
    for (x, y, s) in ((80, 620, 0.8), (1010, 640, 0.7)):
        o.append(tree(x, y, s))

    # логотип
    o.append(logo(300, 120, "Garden", "Blast!", 82, 72, c1="#b8f07a", c2="#2b8a34",
                  stroke="#17441a", sw=16, c3="#ff8fa8", c4="#d11149"))
    o.append(leaf(120, 96, 44, ang=-40))
    o.append(leaf(470, 104, 40, ang=24))

    # панель уровня
    o.append(panel(60, 226, 960, 180, 40, "#fff6e2", "#f0dcb0", "#b96d00", 6))
    for i in range(3):
        o.append(star(150 + i * 56, 268, 28, lgrad("#fff3a0", "#f5a800") if i < 2 else "#d8c9a8",
                      stroke="#b06a00" if i < 2 else "#b09a74", sw=4))
    o.append(RR(378, 238, 324, 64, 32, lgrad("#ffd979", "#e8870b"), 'stroke="#8a4b00" stroke-width="4"'))
    o.append(T(540, 286, "LEVEL 45", 42, fill="#ffffff", stroke="#8a4b00", sw=8))
    cols3 = [("SCORE:", "12,450", 212), ("TARGET:", "8,000", 540), ("MOVES LEFT:", "21", 866)]
    for (lb, val, x) in cols3:
        o.append(T(x, 346, lb, 26, fill="#a85c00", fam=F, w=800, ls=1))
        o.append(T(x, 392, val, 40, fill="#5a3000"))
    o.append(T(760, 392, "⏱", 34, fill="#e2560f", fam=F))

    # доска
    bx, by, cols, rows, cell = 70, 440, 8, 9, 118
    bw, bh = cols * cell, rows * cell
    o.append(RR(bx - 20, by - 20, bw + 40, bh + 48, 38, "#00000030"))
    o.append(RR(bx - 20, by - 20, bw + 40, bh + 40, 38, lgrad("#b5793f", "#7a4520"),
                'stroke="#4a2a10" stroke-width="7"'))
    o.append(RR(bx - 4, by - 4, bw + 8, bh + 8, 26, lgrad("#8a5a2c", "#6d4220")))
    icons = [g_rose, g_daisy, g_sunflower, g_tomato, g_eggplant, g_carrot,
             lambda cx, cy, r: f_strawberry(cx, cy, r * 0.95),
             lambda cx, cy, r: f_plum(cx, cy, r * 0.95)]
    random.seed(61)
    cluster = {(4, 3), (4, 4), (4, 5), (5, 4)}
    for r_ in range(rows):
        for c_ in range(cols):
            cx = bx + c_ * cell + cell / 2
            cy = by + r_ * cell + cell / 2
            o.append(RR(cx - cell / 2 + 6, cy - cell / 2 + 6, cell - 12, cell - 12, 16,
                        "#ffffff", f'opacity="{0.09 if (r_+c_) % 2 == 0 else 0.03}"'))
            fn = g_tomato if (r_, c_) in cluster else random.choice(icons)
            o.append(f'<g filter="url(#shs)">{fn(cx, cy, 48)}</g>')
    o.append(C(bx + 4.5 * cell, by + 4.6 * cell, 180, fade("#ffffff", 0.55, 0.0)))
    for (dx, dy) in ((-1.1, -0.7), (1.2, 0.3), (0.1, 1.3)):
        o.append(sparkle(bx + (4.5 + dx) * cell, by + (4.6 + dy) * cell, 24, "#ffffff", 0.9))

    # фермер и пёс
    o.append(f'<g filter="url(#shs)">{mascot_farmer(912, 1620, 0.62)}</g>')
    o.append(pet_dog(1018, 1636, 0.6))

    # бустеры
    boosters = [("can", "15", "#8ce1ff", "#2b8fd6"), ("snail", "9", "#c9a3ff", "#6a2fd0"),
                ("bomb", "4", "#5a6070", "#1d2029"), ("shuffle", "8", "#9bf07a", "#2fa84f")]
    for i, (kind, n, c1, c2) in enumerate(boosters):
        x = 150 + i * 196
        o.append(RR(x - 82, 1452, 164, 140, 40, "#00000030"))
        o.append(RR(x - 82, 1452, 164, 140, 40, lgrad("#fff6e2", "#e8d9b5"),
                    'stroke="#b08f5a" stroke-width="5"'))
        if kind == "can":
            o.append(RR(x - 40, 1500, 76, 62, 14, lgrad(c1, c2), 'stroke="#0a4a8f" stroke-width="4"'))
            o.append(f'<path d="M {x+36} {1510} l 36 -26 l 8 12 l -32 28 Z" fill="{lgrad(c1, c2)}" '
                     f'stroke="#0a4a8f" stroke-width="4"/>')
            o.append(f'<path d="M {x-40} {1506} q -24 16 -8 44" fill="none" stroke="#0a4a8f" stroke-width="6"/>')
        elif kind == "snail":
            o.append(f'<ellipse cx="{x+6}" cy="{1540}" rx="54" ry="26" fill="{lgrad("#c08a52", "#6d4220")}"/>')
            o.append(C(x + 6, 1512, 36, lgrad(c1, c2), 'stroke="#3c0a66" stroke-width="4"'))
            o.append(C(x + 6, 1512, 16, "#ffffff", 'opacity="0.5"'))
            o.append(f'<path d="M {x-48} {1536} q -14 -26 2 -40" fill="none" stroke="#6d4220" stroke-width="6"/>')
        elif kind == "bomb":
            o.append(C(x, 1530, 42, rgrad(c1, c2), 'stroke="#0d0f14" stroke-width="4"'))
            o.append(f'<path d="M {x+20} {1492} q 24 -24 40 -4" fill="none" stroke="#ffd166" '
                     f'stroke-width="8" stroke-linecap="round"/>')
        else:
            o.append(f'<path d="M {x-40} {1552} a 48 48 0 1 1 18 30" fill="none" stroke="{c2}" '
                     f'stroke-width="13" stroke-linecap="round"/>')
            o.append(f'<path d="M {x-52} {1514} l 22 10 l -8 24 Z" fill="{c2}"/>')
        o.append(RR(x + 16, 1546, 66, 44, 22, lgrad("#9bf07a", "#2fa84f"), 'stroke="#ffffff" stroke-width="4"'))
        o.append(T(x + 49, 1578, n, 28, fill="#ffffff"))

    # нижняя навигация
    o.append(RR(24, 1708, 1032, 180, 48, "#00000025"))
    o.append(RR(24, 1708, 1032, 180, 48, lgrad("#fff6e2", "#e8d9b5"), 'stroke="#b08f5a" stroke-width="5"'))
    navs = [("Home", "#4e9c2a", False), ("Levels", "#e8870b", True), ("Shop", "#d11149", False),
            ("Settings", "#5a6a7d", False)]
    for i, (lb, cc, act) in enumerate(navs):
        x = 168 + i * 248
        if act:
            o.append(RR(x - 92, 1722, 184, 152, 40, lgrad("#ffe9a8", "#ffd166"),
                        'stroke="#b96d00" stroke-width="4"'))
        if lb == "Home":
            o.append(f'<path d="M {x-34} {1810} L {x} {1776} L {x+34} {1810} L {x+34} {1842} '
                     f'L {x-34} {1842} Z" fill="{cc}"/>')
        elif lb == "Levels":
            o.append(f'<path d="M {x-36} {1790} L {x+36} {1790} L {x+22} {1842} L {x-22} {1842} Z" '
                     f'fill="{cc}"/>')
            o.append(T(x, 1828, "3", 32, fill="#ffffff"))
        elif lb == "Shop":
            o.append(RR(x - 34, 1796, 68, 46, 8, cc))
            o.append(f'<path d="M {x-40} {1796} L {x-28} {1776} L {x+28} {1776} L {x+40} {1796} Z" fill="{cc}"/>')
        else:
            o.append(C(x, 1810, 26, "none", f'stroke="{cc}" stroke-width="10"'))
            for a in range(0, 360, 60):
                rad = math.radians(a)
                o.append(f'<rect x="{x-5+36*math.cos(rad):.1f}" y="{1810-5+36*math.sin(rad):.1f}" '
                         f'width="10" height="10" rx="3" fill="{cc}"/>')
        o.append(T(x, 1876, lb, 28, fill="#5a3000", fam=F, w=800))
    return "".join(o)


# ----------------------------------------------------------------------------
# 9. FRUIT BURST QUEST  (референс 9)
# ----------------------------------------------------------------------------
def scene_fruitburst():
    o = [RR(0, 0, W, H, 0, lgrad3("#9fe3b0", "#4e9c5a", "#1f6b3a"))]
    o.append(C(540, 420, 720, fade("#fff3a0", 0.3, 0.0)))
    for i in range(7):
        o.append(f'<path d="M 540 120 L {120+i*160} 980 L {200+i*160} 980 Z" fill="#ffffff" '
                 f'opacity="0.05"/>')
    # водопад
    o.append(RR(420, 300, 240, 820, 40, lgrad3("#e8f9ff", "#8ad6ff", "#2b8fd6"), 'opacity="0.85"'))
    o.append(f'<ellipse cx="540" cy="1140" rx="190" ry="54" fill="#cfeaff" opacity="0.8"/>')
    for i in range(6):
        o.append(RR(450 + i * 36, 320, 10, 780, 5, "#ffffff", 'opacity="0.35"'))
    o.append(palm_frond(-40, 260, 360, 16))
    o.append(palm_frond(1120, 230, 380, 164))
    o.append(palm_frond(-30, 620, 300, -20))
    o.append(palm_frond(1110, 640, 320, 200))
    for (x, y, s) in ((120, 1500, 1.2), (980, 1540, 1.1), (300, 1880, 1.0), (840, 1900, 0.9)):
        o.append(bush(x, y, 96 * s))

    # логотип
    o.append(logo(540, 110, "FRUIT BURST", "QUEST", 76, 56, c1="#ffe066", c2="#f0820b",
                  stroke="#2b5a1e", sw=15, c3="#ff8fa8", c4="#d11149"))

    # HUD
    o.append(T(60, 206, "SCORE:", 28, fill="#fff3a0", anchor="start", fam=F, w=800, ls=1))
    o.append(T(60, 256, "24,650", 46, fill="#ffffff", anchor="start", stroke="#2b5a1e", sw=10))
    o.append(T(1020, 206, "LIVES:", 28, fill="#fff3a0", anchor="end", fam=F, w=800, ls=1))
    for i in range(3):
        o.append(heart(900 + i * 56, 252, 24))
    o.append(RR(60, 296, 150, 88, 26, lgrad("#ffd979", "#e8870b"), 'stroke="#8a4b00" stroke-width="5"'))
    o.append(T(135, 330, "LEVEL", 24, fill="#5a3000", fam=F, w=800))
    o.append(T(135, 372, "42", 36, fill="#ffffff", stroke="#8a4b00", sw=7))
    o.append(T(560, 306, "GOAL:", 26, fill="#fff3a0", fam=F, w=800, ls=1))
    o.append(T(560, 344, "MATCH 25 STRAWBERRIES", 32, fill="#ffffff", stroke="#2b5a1e", sw=8))
    o.append(progress(300, 356, 520, 34, 19 / 25.0, "#9bf07a", "#2fa84f", "#1b4a2a"))
    o.append(T(560, 383, "19/25", 24, fill="#ffffff", stroke="#176b31", sw=5))
    o.append(coin(892, 336, 26))
    o.append(T(1020, 350, "1,280", 34, fill="#ffffff", anchor="end", stroke="#2b5a1e", sw=8))

    # верхняя сетка
    bx, by, cols, rows, cell = 52, 420, 9, 4, 110
    bw, bh = cols * cell, rows * cell
    o.append(RR(bx - 14, by - 14, bw + 28, bh + 28, 28, "#ffffff", 'opacity="0.25"'))
    o.append(RR(bx - 14, by - 14, bw + 28, bh + 28, 28, lgrad("#b5793f", "#8a5324"),
                'stroke="#f4ffe8" stroke-width="5" fill-opacity="0.92"'))
    icons = [f_strawberry, f_watermelon, f_orange, f_greenapple, f_grapes, f_banana,
             f_pineapple, f_apple, f_lemon]
    random.seed(71)
    for r_ in range(rows):
        for c_ in range(cols):
            cx = bx + c_ * cell + cell / 2
            cy = by + r_ * cell + cell / 2
            o.append(RR(cx - cell / 2 + 5, cy - cell / 2 + 5, cell - 10, cell - 10, 14,
                        "#ffffff", 'opacity="0.10"'))
            o.append(f'<g filter="url(#shs)">{random.choice(icons)(cx, cy, 44)}</g>')
    o.append(RR(bx - 18, by - 18, bw + 36, bh + 36, 30, "none",
                'stroke="#8ef1ff" stroke-width="5" opacity="0.85" filter="url(#glow)"'))

    # зона шутера
    o.append(burst(620, 1070, 190, "#fff3a0", "#ff7a8f", 14))
    cluster = [(500, 990), (620, 960), (740, 1000), (560, 1090), (690, 1100), (620, 1190),
               (470, 1110), (800, 1090)]
    for (cx, cy) in cluster:
        o.append(f'<g filter="url(#shs)">{f_strawberry(cx, cy, 54)}</g>')
    o.append(T(880, 980, "+500", 52, fill="#ffe066", stroke="#8a4b00", sw=10))
    o.append(pop_label(846, 1064, "POP!", 44, 12))
    o.append(pop_label(770, 1186, "POP!", 38, -10))
    random.seed(13)
    for _ in range(16):
        a = random.uniform(0, 6.28)
        d = random.uniform(180, 260)
        o.append(star(620 + math.cos(a) * d, 1070 + math.sin(a) * d * 0.8, random.randint(10, 20),
                      "#ffe066", stroke="none", sw=0, op=0.9))

    # пушка, маскот, следующие
    o.append(dotted([(610, 1500), (560, 1280)], w=9, gap="3 26"))
    o.append(C(612, 1512, 96, "#00000030"))
    o.append(RR(528, 1430, 168, 150, 54, lgrad("#9bf07a", "#2b8a34"), 'stroke="#17441a" stroke-width="6"'))
    o.append(C(612, 1516, 54, lgrad("#ffd979", "#e8870b"), 'stroke="#8a4b00" stroke-width="6"'))
    o.append(f_strawberry(612, 1510, 40))
    o.append(leaf(560, 1404, 44, ang=-40))
    o.append(f'<g filter="url(#shs)">{mascot_monkey(250, 1620, 0.78)}</g>')
    o.append(f_strawberry(352, 1400, 40))
    o.append(RR(800, 1440, 230, 120, 36, "#ffffff", 'opacity="0.2"'))
    o.append(RR(800, 1440, 230, 120, 36, "none", 'stroke="#8ef1ff" stroke-width="5"'))
    o.append(f_pineapple(858, 1500, 40))
    o.append(T(920, 1516, "+", 44, fill="#ffffff", stroke="#2b5a1e", sw=7))
    o.append(f_strawberry(976, 1500, 38))

    # нижняя панель
    o.append(RR(40, 1706, 1000, 170, 44, "#00000035"))
    o.append(RR(40, 1706, 1000, 170, 44, lgrad("#1b4a6b", "#0d2a46"), 'stroke="#8ef1ff" stroke-width="5"'))
    items = [("BOOSTERS", "bomb", "#5a6070", "#1d2029"), ("RAINBOW FRUIT", "rainbow", "#8ad6ff", "#2b8fd6"),
             ("FIREBALL", "fire", "#ff9e6b", "#e2560f"), ("PAUSE", "pause", "#8ce1ff", "#1273de")]
    for i, (lb, kind, c1, c2) in enumerate(items):
        x = 180 + i * 240
        o.append(round_btn(x, 1768, 54, c1, c2))
        if kind == "bomb":
            o.append(C(x, 1774, 28, "#20202c", 'stroke="#ffffff" stroke-width="4"'))
            o.append(f'<path d="M {x+14} {1748} q 16 -16 28 -4" fill="none" stroke="#ffd166" '
                     f'stroke-width="7" stroke-linecap="round"/>')
        elif kind == "rainbow":
            for k, cc in enumerate(("#ff6b8a", "#ffd166", "#9bf07a", "#8ad6ff")):
                o.append(f'<path d="M {x-32+k*6} {1790} a {32-k*6} {32-k*6} 0 0 1 {(32-k*6)*2} 0" '
                         f'fill="none" stroke="{cc}" stroke-width="8"/>')
        elif kind == "fire":
            o.append(f'<path d="M {x} {1736} q 34 32 20 62 q -8 18 -20 18 q -12 0 -20 -18 '
                     f'q -14 -30 20 -62 Z" fill="{lgrad("#fff3a0", "#e2560f")}"/>')
        else:
            o.append(RR(x - 18, 1746, 14, 44, 6, "#ffffff"))
            o.append(RR(x + 4, 1746, 14, 44, 6, "#ffffff"))
        o.append(T(x, 1850, lb, 22, fill="#ffffff", ls=1))
    return "".join(o)


SCREENS3 = [("Tropic_Fruit_Pop", scene_tropic, "Tropic Fruit Pop"),
            ("Sky_Leap", scene_skyleap, "Sky Leap"),
            ("Meditation_Sleep", scene_meditation, "Meditation / Sleep"),
            ("Happy_Cubes_Match", scene_cubes, "Happy Cubes Match"),
            ("Enchanted_Match_Quest", scene_enchanted, "Enchanted Match Quest"),
            ("Berry_Pop_Adventures", scene_berrypop, "Berry Pop Adventures"),
            ("Celestial_Merge_Adventure", scene_celestial, "Celestial Merge Adventure"),
            ("Garden_Blast", scene_garden, "Garden Blast"),
            ("Fruit_Burst_Quest", scene_fruitburst, "Fruit Burst Quest")]

if __name__ == "__main__":
    for name, fn, title in SCREENS3:
        DEFS[:] = []
        CNT[0] = 0
        write(name, fn(), title)
