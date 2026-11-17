# -*- coding: utf-8 -*-
"""Библиотека иконок, маскотов и элементов UI для полноэкранных макетов
(make_screens3.py). Базовые примитивы берутся из make_screens."""

import math

from make_screens import (T, RR, C, star, poly, sparkle, lgrad, lgrad3, rgrad, fade,
                          F, FB, W, H)


# ----------------------------------------------------------------------------
# мелочь
# ----------------------------------------------------------------------------
def hl(cx, cy, rx, ry, rot=-28, op=0.55, c="#ffffff"):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{c}" opacity="{op}" '
            f'transform="rotate({rot} {cx} {cy})"/>')


def leaf(cx, cy, r, ang=-30, c1="#9bf07a", c2="#2b8a34", sw=None):
    sw = sw if sw is not None else max(2, r * 0.14)
    d = (f"M {cx-r} {cy} Q {cx-r*0.2} {cy-r*0.85} {cx+r} {cy-r*0.1} "
         f"Q {cx-r*0.1} {cy+r*0.55} {cx-r} {cy} Z")
    return (f'<g transform="rotate({ang} {cx} {cy})">'
            f'<path d="{d}" fill="{lgrad(c1, c2)}" stroke="#1f6b2f" stroke-width="{sw}" '
            f'stroke-linejoin="round"/></g>')


def stem(cx, cy, r, c="#6d4220"):
    return (f'<path d="M {cx} {cy} q {r*0.08} {-r*0.42} {r*0.36} {-r*0.52}" fill="none" '
            f'stroke="{c}" stroke-width="{max(3, r*0.16)}" stroke-linecap="round"/>')


def face(cx, cy, s, blush=True, smile=True, happy=False, eye="#2a2338"):
    o = []
    if happy:
        for dx in (-1, 1):
            o.append(f'<path d="M {cx+dx*14*s-9*s} {cy+2*s} q {9*s} {-11*s} {18*s} 0" fill="none" '
                     f'stroke="{eye}" stroke-width="{4.5*s}" stroke-linecap="round"/>')
    else:
        for dx in (-1, 1):
            o.append(C(cx + dx * 14 * s, cy, 6.5 * s, eye))
            o.append(C(cx + dx * 14 * s - 2 * s, cy - 2.5 * s, 2.4 * s, "#ffffff"))
    if blush:
        o.append(f'<ellipse cx="{cx-27*s}" cy="{cy+11*s}" rx="{8*s}" ry="{5.5*s}" fill="#ff9bb0" opacity="0.75"/>')
        o.append(f'<ellipse cx="{cx+27*s}" cy="{cy+11*s}" rx="{8*s}" ry="{5.5*s}" fill="#ff9bb0" opacity="0.75"/>')
    if smile:
        o.append(f'<path d="M {cx-10*s} {cy+14*s} q {10*s} {11*s} {20*s} 0" fill="none" '
                 f'stroke="{eye}" stroke-width="{4*s}" stroke-linecap="round"/>')
    return "".join(o)


# ----------------------------------------------------------------------------
# фрукты и ягоды
# ----------------------------------------------------------------------------
def f_apple(cx, cy, r, c1="#ff7a7a", c2="#c01c1c", dark="#7d0c12"):
    return (C(cx, cy + r * 0.06, r * 0.97, rgrad(c1, c2), f'stroke="{dark}" stroke-width="{r*0.1}"') +
            stem(cx, cy - r * 0.9, r) + leaf(cx + r * 0.52, cy - r * 1.12, r * 0.46) +
            hl(cx - r * 0.36, cy - r * 0.32, r * 0.25, r * 0.14))


def f_greenapple(cx, cy, r):
    return f_apple(cx, cy, r, "#b8f07a", "#3f9c2a", "#1f6b1a")


def f_orange(cx, cy, r):
    o = [C(cx, cy, r * 0.97, rgrad("#ffc46b", "#ef7215"), f'stroke="#a63d00" stroke-width="{r*0.1}"')]
    for a in (20, 95, 165, 250, 310):
        o.append(C(cx + r * 0.5 * math.cos(math.radians(a)), cy + r * 0.5 * math.sin(math.radians(a)),
                   r * 0.055, "#d35f00", 'opacity="0.5"'))
    o.append(C(cx, cy - r * 0.92, r * 0.13, "#8a4b00"))
    o.append(leaf(cx + r * 0.5, cy - r * 1.02, r * 0.42))
    o.append(hl(cx - r * 0.36, cy - r * 0.34, r * 0.24, r * 0.14))
    return "".join(o)


def f_orange_slice(cx, cy, r):
    o = [C(cx, cy, r, rgrad("#ffd9a0", "#f0a24a"), 'stroke="#c96a12" stroke-width="5"'),
         C(cx, cy, r * 0.84, lgrad("#ffb14a", "#f07a12"))]
    for i in range(8):
        a1 = math.radians(i * 45 + 4)
        a2 = math.radians((i + 1) * 45 - 4)
        o.append(f'<path d="M {cx} {cy} L {cx+r*0.78*math.cos(a1):.1f} {cy+r*0.78*math.sin(a1):.1f} '
                 f'A {r*0.78} {r*0.78} 0 0 1 {cx+r*0.78*math.cos(a2):.1f} {cy+r*0.78*math.sin(a2):.1f} Z" '
                 f'fill="#ffb86b" stroke="#ffe3bd" stroke-width="3"/>')
    o.append(C(cx, cy, r * 0.12, "#ffe3bd"))
    return "".join(o)


def f_strawberry(cx, cy, r, c1="#ff7a8f", c2="#d11128"):
    d = (f"M {cx} {cy+r*1.08} C {cx-r*1.0} {cy+r*0.42} {cx-r*0.92} {cy-r*0.78} {cx} {cy-r*0.72} "
         f"C {cx+r*0.92} {cy-r*0.78} {cx+r*1.0} {cy+r*0.42} {cx} {cy+r*1.08} Z")
    o = [f'<path d="{d}" fill="{rgrad(c1, c2)}" stroke="#8c0a1e" stroke-width="{r*0.09}" '
         f'stroke-linejoin="round"/>']
    for (dx, dy) in ((-0.42, -0.18), (0.0, -0.3), (0.42, -0.18), (-0.26, 0.24), (0.26, 0.24), (0.0, 0.6)):
        o.append(f'<ellipse cx="{cx+dx*r}" cy="{cy+dy*r}" rx="{r*0.09}" ry="{r*0.13}" fill="#ffe9a8"/>')
    o.append(star(cx, cy - r * 0.78, r * 0.52, lgrad("#9bf07a", "#2b8a34"), stroke="#1f6b2f",
                  sw=max(2, r * 0.08), rot=-90, inner=0.5))
    o.append(f'<rect x="{cx-r*0.08}" y="{cy-r*1.26}" width="{r*0.16}" height="{r*0.34}" rx="{r*0.08}" '
             f'fill="#2b8a34"/>')
    o.append(hl(cx - r * 0.34, cy - r * 0.2, r * 0.2, r * 0.11))
    return "".join(o)


def f_banana(cx, cy, r):
    d = (f"M {cx-r*0.92} {cy-r*0.62} Q {cx} {cy+r*2.0} {cx+r*0.92} {cy-r*0.56} "
         f"Q {cx+r*0.46} {cy+r*0.08} {cx} {cy+r*0.2} Q {cx-r*0.46} {cy+r*0.08} {cx-r*0.92} {cy-r*0.62} Z")
    return (f'<path d="{d}" fill="{lgrad("#ffe066", "#f0a500")}" stroke="#a85c00" '
            f'stroke-width="{r*0.09}" stroke-linejoin="round"/>'
            f'<circle cx="{cx-r*0.9}" cy="{cy-r*0.5}" r="{r*0.11}" fill="#6d4220"/>'
            f'<circle cx="{cx+r*0.9}" cy="{cy-r*0.44}" r="{r*0.11}" fill="#6d4220"/>'
            + hl(cx - r * 0.2, cy + r * 0.18, r * 0.3, r * 0.08, rot=12, op=0.45))


def f_grapes(cx, cy, r):
    o = [leaf(cx + r * 0.3, cy - r * 1.0, r * 0.45, ang=-10)]
    pts = [(-0.5, -0.3), (0.0, -0.42), (0.5, -0.3), (-0.28, 0.1), (0.28, 0.1), (0.0, 0.5)]
    for (dx, dy) in pts:
        o.append(C(cx + dx * r, cy + dy * r, r * 0.34, rgrad("#c9a3ff", "#6a2fd0"),
                   f'stroke="#3c0a66" stroke-width="{r*0.07}"'))
    o.append(hl(cx - r * 0.44, cy - r * 0.38, r * 0.12, r * 0.07))
    return "".join(o)


def f_pineapple(cx, cy, r):
    o = []
    for (dx, ang) in ((-0.42, -34), (0.0, 0), (0.42, 34)):
        o.append(f'<path d="M {cx+dx*r} {cy-r*0.6} L {cx+dx*r-r*0.2} {cy-r*1.5} '
                 f'L {cx+dx*r+r*0.2} {cy-r*1.5} Z" fill="{lgrad("#9bf07a", "#2b8a34")}" '
                 f'stroke="#1f6b2f" stroke-width="{r*0.08}" stroke-linejoin="round" '
                 f'transform="rotate({ang} {cx+dx*r} {cy-r*0.6})"/>')
    o.append(RR(cx - r * 0.78, cy - r * 0.68, r * 1.56, r * 1.72, r * 0.52,
                rgrad("#ffe066", "#e08a00"), f'stroke="#a85c00" stroke-width="{r*0.09}"'))
    for i in range(-2, 3):
        o.append(f'<line x1="{cx-r*0.74}" y1="{cy+i*r*0.36}" x2="{cx+r*0.74}" y2="{cy+i*r*0.36+r*0.5}" '
                 f'stroke="#c47700" stroke-width="{r*0.07}" opacity="0.6"/>')
        o.append(f'<line x1="{cx-r*0.74}" y1="{cy+i*r*0.36+r*0.5}" x2="{cx+r*0.74}" y2="{cy+i*r*0.36}" '
                 f'stroke="#c47700" stroke-width="{r*0.07}" opacity="0.6"/>')
    o.append(hl(cx - r * 0.34, cy - r * 0.26, r * 0.18, r * 0.1))
    return "".join(o)


def f_kiwi(cx, cy, r):
    o = [C(cx, cy, r * 0.95, lgrad("#a9703f", "#6d4220"), 'stroke="#4a2a10" stroke-width="4"'),
         C(cx, cy, r * 0.78, rgrad("#b8f07a", "#5aa83c")),
         C(cx, cy, r * 0.24, "#f4ffe8")]
    for i in range(10):
        a = math.radians(i * 36)
        o.append(f'<ellipse cx="{cx+r*0.48*math.cos(a):.1f}" cy="{cy+r*0.48*math.sin(a):.1f}" '
                 f'rx="{r*0.07}" ry="{r*0.05}" fill="#2a2338"/>')
    return "".join(o)


def f_watermelon(cx, cy, r):
    o = [f'<path d="M {cx-r} {cy+r*0.45} A {r} {r} 0 0 1 {cx+r} {cy+r*0.45} Z" '
         f'fill="{lgrad("#9bf07a", "#2b8a34")}" stroke="#1f6b2f" stroke-width="4"/>',
         f'<path d="M {cx-r*0.86} {cy+r*0.45} A {r*0.86} {r*0.86} 0 0 1 {cx+r*0.86} {cy+r*0.45} Z" '
         f'fill="#f4ffe8"/>',
         f'<path d="M {cx-r*0.74} {cy+r*0.45} A {r*0.74} {r*0.74} 0 0 1 {cx+r*0.74} {cy+r*0.45} Z" '
         f'fill="{lgrad("#ff7a8f", "#d11128")}"/>']
    for (dx, dy) in ((-0.36, -0.06), (0.0, -0.2), (0.36, -0.06), (-0.18, 0.2), (0.18, 0.2)):
        o.append(f'<ellipse cx="{cx+dx*r}" cy="{cy+dy*r+r*0.2}" rx="{r*0.07}" ry="{r*0.1}" fill="#2a2338"/>')
    return "".join(o)


def f_blueberry(cx, cy, r):
    return (C(cx, cy, r * 0.92, rgrad("#8ab4ff", "#2b47c9"), f'stroke="#12256e" stroke-width="{r*0.09}"') +
            star(cx, cy - r * 0.5, r * 0.34, "#4a6ad6", stroke="#12256e", sw=max(2, r * 0.06), rot=-90) +
            hl(cx - r * 0.32, cy - r * 0.3, r * 0.22, r * 0.13))


def f_plum(cx, cy, r):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{r*0.86}" ry="{r*0.96}" fill="{rgrad("#d9a6ff", "#6a2fd0")}" '
            f'stroke="#3c0a66" stroke-width="{r*0.09}"/>'
            f'<path d="M {cx} {cy-r*0.9} q {-r*0.16} {r*0.9} 0 {r*1.8}" fill="none" stroke="#3c0a66" '
            f'stroke-width="{r*0.07}" opacity="0.5"/>'
            + leaf(cx + r * 0.46, cy - r * 1.02, r * 0.4) + hl(cx - r * 0.34, cy - r * 0.34, r * 0.2, r * 0.12))


def f_lemon(cx, cy, r):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{r*0.98}" ry="{r*0.74}" fill="{rgrad("#fff3a0", "#f0c000")}" '
            f'stroke="#a88400" stroke-width="{r*0.09}" transform="rotate(-18 {cx} {cy})"/>'
            + hl(cx - r * 0.3, cy - r * 0.24, r * 0.24, r * 0.1))


FRUITS = [f_apple, f_orange, f_strawberry, f_grapes, f_pineapple, f_greenapple,
          f_banana, f_kiwi, f_watermelon]


# ----------------------------------------------------------------------------
# сад: цветы и овощи (с мордочками)
# ----------------------------------------------------------------------------
def g_flower(cx, cy, r, petal1, petal2, core="#ffd166", n=8, fc=True):
    o = []
    for i in range(n):
        a = math.radians(i * 360.0 / n)
        px, py = cx + r * 0.62 * math.cos(a), cy + r * 0.62 * math.sin(a)
        o.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{r*0.42}" ry="{r*0.3}" '
                 f'fill="{lgrad(petal1, petal2)}" stroke="#00000022" stroke-width="2" '
                 f'transform="rotate({i*360.0/n} {px:.1f} {py:.1f})"/>')
    o.append(C(cx, cy, r * 0.52, rgrad("#fff3a0", core), 'stroke="#a85c00" stroke-width="3"'))
    if fc:
        o.append(face(cx, cy + r * 0.02, r * 0.016))
    return "".join(o)


def g_rose(cx, cy, r):
    return g_flower(cx, cy, r, "#ff8fa8", "#d11149", "#ffb0c0", n=7)


def g_daisy(cx, cy, r):
    return g_flower(cx, cy, r, "#ffffff", "#dfe6ef", "#f0a500", n=9)


def g_sunflower(cx, cy, r):
    return g_flower(cx, cy, r, "#ffe066", "#f0a500", "#a85c00", n=10)


def g_tomato(cx, cy, r):
    return (C(cx, cy, r * 0.94, rgrad("#ff7a6b", "#c81e1e"), f'stroke="#7d0c12" stroke-width="{r*0.09}"') +
            star(cx, cy - r * 0.74, r * 0.46, lgrad("#9bf07a", "#2b8a34"), stroke="#1f6b2f", sw=3, rot=-90) +
            face(cx, cy + r * 0.08, r * 0.016) + hl(cx - r * 0.38, cy - r * 0.3, r * 0.2, r * 0.12))


def g_eggplant(cx, cy, r):
    return (f'<ellipse cx="{cx}" cy="{cy+r*0.1}" rx="{r*0.76}" ry="{r*0.92}" '
            f'fill="{rgrad("#c9a3ff", "#5a1e9c")}" stroke="#2e0a52" stroke-width="{r*0.09}"/>'
            + star(cx, cy - r * 0.78, r * 0.44, lgrad("#9bf07a", "#2b8a34"), stroke="#1f6b2f", sw=3, rot=-90)
            + face(cx, cy + r * 0.14, r * 0.015) + hl(cx - r * 0.3, cy - r * 0.2, r * 0.16, r * 0.1))


def g_carrot(cx, cy, r):
    o = [f'<path d="M {cx-r*0.52} {cy-r*0.46} L {cx+r*0.52} {cy-r*0.46} L {cx} {cy+r*1.0} Z" '
         f'fill="{lgrad("#ffb15c", "#e2560f")}" stroke="#8f3203" stroke-width="{r*0.09}" '
         f'stroke-linejoin="round"/>']
    for a in (-30, 0, 30):
        o.append(f'<line x1="{cx}" y1="{cy-r*0.5}" x2="{cx+a*r*0.016}" y2="{cy-r*1.12}" '
                 f'stroke="#2b8a34" stroke-width="{r*0.16}" stroke-linecap="round"/>')
    o.append(face(cx, cy - r * 0.06, r * 0.013))
    return "".join(o)


# ----------------------------------------------------------------------------
# кубо-фрукты с мордочками
# ----------------------------------------------------------------------------
CUBES = {"apple": ("#ff8a7a", "#d12a1e", "#7d0c12"),
         "orange": ("#ffc46b", "#ef7215", "#a63d00"),
         "lemon": ("#ffe98a", "#f0c000", "#a88400"),
         "lime": ("#b8f07a", "#4aa02a", "#1f6b1a"),
         "grape": ("#d9a6ff", "#7b2cbf", "#3c0a66"),
         "pine": ("#ffe066", "#e0a000", "#a85c00")}


def cube_fruit(cx, cy, s, kind, rot=0):
    c1, c2, cd = CUBES[kind]
    o = [f'<g transform="rotate({rot} {cx} {cy})">']
    o.append(RR(cx - 50 * s, cy - 46 * s, 100 * s, 96 * s, 34 * s, rgrad(c1, c2),
                f'stroke="{cd}" stroke-width="{5*s}"'))
    o.append(RR(cx - 36 * s, cy - 34 * s, 46 * s, 22 * s, 11 * s, "#ffffff", 'opacity="0.42"'))
    if kind == "pine":
        for i in range(-1, 2):
            o.append(f'<line x1="{cx-34*s}" y1="{cy+i*22*s}" x2="{cx+34*s}" y2="{cy+i*22*s+16*s}" '
                     f'stroke="{cd}" stroke-width="{3*s}" opacity="0.35"/>')
    o.append(leaf(cx + 26 * s, cy - 54 * s, 22 * s, ang=-22))
    o.append(face(cx, cy + 6 * s, s * 0.92))
    o.append("</g>")
    return "".join(o)


# ----------------------------------------------------------------------------
# космос
# ----------------------------------------------------------------------------
def s_galaxy(cx, cy, r, c1="#8ef1ff", c2="#2b6ad6"):
    o = [C(cx, cy, r, fade(c1, 0.35, 0.0))]
    for ang in (0, 180):
        o.append(f'<path d="M {cx} {cy} Q {cx+r*0.95} {cy-r*0.25} {cx+r*0.15} {cy+r*0.92}" '
                 f'fill="none" stroke="{lgrad(c1, c2)}" stroke-width="{r*0.34}" stroke-linecap="round" '
                 f'transform="rotate({ang} {cx} {cy})"/>')
    o.append(C(cx, cy, r * 0.26, "#ffffff", 'opacity="0.95"'))
    return "".join(o)


def s_planet(cx, cy, r, c1="#ffd979", c2="#e2560f", ring=True):
    o = [C(cx, cy, r * 0.88, rgrad(c1, c2), 'stroke="#00000033" stroke-width="4"'),
         hl(cx - r * 0.34, cy - r * 0.32, r * 0.22, r * 0.12)]
    if ring:
        o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r*1.28}" ry="{r*0.4}" fill="none" '
                 f'stroke="{lgrad("#ffe9a8", "#d98e34")}" stroke-width="{r*0.16}" '
                 f'transform="rotate(-22 {cx} {cy})"/>')
    return "".join(o)


def s_earth(cx, cy, r):
    o = [C(cx, cy, r * 0.9, rgrad("#8ad6ff", "#1273de"), 'stroke="#0a4a8f" stroke-width="4"')]
    for (dx, dy, rr) in ((-0.3, -0.2, 0.34), (0.3, 0.16, 0.3), (0.05, -0.5, 0.2)):
        o.append(C(cx + dx * r, cy + dy * r, rr * r, "#5bbf5b", 'opacity="0.9"'))
    o.append(hl(cx - r * 0.34, cy - r * 0.36, r * 0.2, r * 0.11))
    return "".join(o)


def s_mars(cx, cy, r):
    o = [C(cx, cy, r * 0.88, rgrad("#ffb08a", "#c23b0c"), 'stroke="#7d2a08" stroke-width="4"')]
    for (dx, dy, rr) in ((-0.28, -0.24, 0.17), (0.26, 0.1, 0.13), (0.0, 0.42, 0.1)):
        o.append(C(cx + dx * r, cy + dy * r, rr * r, "#9c3a10", 'opacity="0.45"'))
    return "".join(o)


def s_star(cx, cy, r, c1="#fff3a0", c2="#f0a500"):
    return (star(cx, cy, r, lgrad(c1, c2), stroke="#b06a00", sw=max(2, r * 0.1)) +
            hl(cx - r * 0.2, cy - r * 0.28, r * 0.2, r * 0.1, op=0.6))


def s_starcrystal(cx, cy, r):
    return (star(cx, cy, r, lgrad("#d9fbff", "#7b5bff"), stroke="#3c2a8f", sw=max(2, r * 0.09), inner=0.52) +
            star(cx, cy, r * 0.5, "#ffffff", stroke="none", sw=0, op=0.75))


# ----------------------------------------------------------------------------
# фэнтези
# ----------------------------------------------------------------------------
def m_gem(cx, cy, r, c1="#8ef1ff", c2="#1273de", cd="#0a4a8f"):
    d = (f"M {cx} {cy-r} L {cx+r*0.82} {cy} L {cx} {cy+r} L {cx-r*0.82} {cy} Z")
    return (f'<path d="{d}" fill="{lgrad(c1, c2)}" stroke="{cd}" stroke-width="{r*0.11}" '
            f'stroke-linejoin="round"/>'
            f'<path d="M {cx} {cy-r} L {cx-r*0.82} {cy} L {cx} {cy*1.0} Z" fill="#ffffff" opacity="0.3"/>')


def m_gem_violet(cx, cy, r):
    return m_gem(cx, cy, r, "#f3b6ff", "#b32ce0", "#5c0a80")


def m_shield(cx, cy, r):
    d = (f"M {cx-r*0.8} {cy-r*0.82} L {cx+r*0.8} {cy-r*0.82} L {cx+r*0.8} {cy+r*0.1} "
         f"Q {cx+r*0.8} {cy+r*0.82} {cx} {cy+r*1.0} Q {cx-r*0.8} {cy+r*0.82} {cx-r*0.8} {cy+r*0.1} Z")
    return (f'<path d="{d}" fill="{lgrad("#f4f7fb", "#9aa8bd")}" stroke="#44506b" '
            f'stroke-width="{r*0.11}" stroke-linejoin="round"/>'
            f'<path d="M {cx} {cy-r*0.82} L {cx} {cy+r*1.0}" stroke="#c0392b" stroke-width="{r*0.12}" '
            f'opacity="0.0"/>'
            f'<path d="M {cx-r*0.8} {cy-r*0.82} L {cx} {cy-r*0.82} L {cx} {cy+r*1.0} '
            f'Q {cx-r*0.8} {cy+r*0.82} {cx-r*0.8} {cy+r*0.1} Z" fill="#c0392b" opacity="0.75"/>')


def m_knight(cx, cy, r):
    o = [C(cx, cy + r * 0.1, r * 0.92, lgrad("#cfd9e8", "#8c9bb5"), 'stroke="#44506b" stroke-width="4"'),
         C(cx, cy, r * 0.62, lgrad("#ffe0bd", "#e0ab82"), 'stroke="#8a5a3a" stroke-width="3"'),
         f'<path d="M {cx-r*0.66} {cy-r*0.2} a {r*0.66} {r*0.66} 0 0 1 {r*1.32} 0 Z" fill="#8a5a3a"/>',
         C(cx - r * 0.2, cy + r * 0.06, r * 0.08, "#2a2338"),
         C(cx + r * 0.2, cy + r * 0.06, r * 0.08, "#2a2338"),
         f'<path d="M {cx-r*0.16} {cy+r*0.3} q {r*0.16} {r*0.16} {r*0.32} 0" fill="none" '
         f'stroke="#2a2338" stroke-width="{r*0.08}" stroke-linecap="round"/>']
    return "".join(o)


def m_wolf(cx, cy, r):
    o = [f'<path d="M {cx-r*0.86} {cy-r*0.4} L {cx-r*0.56} {cy-r*1.0} L {cx-r*0.22} {cy-r*0.56} Z" '
         f'fill="{lgrad("#9fb6ff", "#3a4fb5")}" stroke="#1d2a6b" stroke-width="3"/>',
         f'<path d="M {cx+r*0.86} {cy-r*0.4} L {cx+r*0.56} {cy-r*1.0} L {cx+r*0.22} {cy-r*0.56} Z" '
         f'fill="{lgrad("#9fb6ff", "#3a4fb5")}" stroke="#1d2a6b" stroke-width="3"/>',
         C(cx, cy, r * 0.86, rgrad("#9fb6ff", "#3a4fb5"), 'stroke="#1d2a6b" stroke-width="4"'),
         f'<ellipse cx="{cx}" cy="{cy+r*0.34}" rx="{r*0.46}" ry="{r*0.36}" fill="#d9e2ff"/>',
         C(cx - r * 0.3, cy - r * 0.12, r * 0.13, "#ffd166"),
         C(cx + r * 0.3, cy - r * 0.12, r * 0.13, "#ffd166"),
         C(cx, cy + r * 0.24, r * 0.1, "#2a2338")]
    return "".join(o)


def m_leaf(cx, cy, r):
    return leaf(cx, cy, r * 0.95, ang=-20, c1="#a8f07a", c2="#2b8a34")


# ----------------------------------------------------------------------------
# маскоты
# ----------------------------------------------------------------------------
def mascot_bear(cx, cy, s=1.0, c1="#8ce1ff", c2="#2b8fd6"):
    """cy — низ фигуры"""
    o = [f'<ellipse cx="{cx}" cy="{cy+6*s}" rx="{86*s}" ry="{20*s}" fill="#000000" opacity="0.2"/>']
    o.append(RR(cx - 78 * s, cy - 170 * s, 156 * s, 176 * s, 62 * s, rgrad(c1, c2),
                f'stroke="#0a4a8f" stroke-width="{5*s}"'))
    o.append(f'<ellipse cx="{cx}" cy="{cy-66*s}" rx="{58*s}" ry="{64*s}" fill="#fff3e2"/>')
    for sx in (-1, 1):
        o.append(f'<g transform="rotate({sx*30} {cx+sx*72*s} {cy-150*s})">'
                 + RR(cx + sx * 72 * s - 26 * s, cy - 164 * s, 52 * s, 120 * s, 26 * s, rgrad(c1, c2),
                      f'stroke="#0a4a8f" stroke-width="{4*s}"') + '</g>')
    for sx in (-1, 1):
        o.append(C(cx + sx * 66 * s, cy - 268 * s, 34 * s, rgrad(c1, c2), f'stroke="#0a4a8f" stroke-width="{4*s}"'))
        o.append(C(cx + sx * 66 * s, cy - 268 * s, 18 * s, "#ffc9d8"))
    o.append(C(cx, cy - 212 * s, 76 * s, rgrad(c1, c2), f'stroke="#0a4a8f" stroke-width="{5*s}"'))
    o.append(f'<ellipse cx="{cx}" cy="{cy-186*s}" rx="{40*s}" ry="{30*s}" fill="#fff3e2"/>')
    o.append(C(cx, cy - 196 * s, 10 * s, "#2a2338"))
    o.append(face(cx, cy - 226 * s, 1.15 * s, blush=True, smile=False, happy=True))
    o.append(f'<path d="M {cx-16*s} {cy-178*s} q {16*s} {16*s} {32*s} 0" fill="none" stroke="#2a2338" '
             f'stroke-width="{4.5*s}" stroke-linecap="round"/>')
    o.append(RR(cx - 62 * s, cy - 150 * s, 124 * s, 26 * s, 13 * s, lgrad("#ffd166", "#e8870b"),
                f'stroke="#8a4b00" stroke-width="{3*s}"'))
    return "".join(o)


def mascot_astronaut(cx, cy, s=1.0):
    o = [f'<ellipse cx="{cx}" cy="{cy+6*s}" rx="{78*s}" ry="{18*s}" fill="#000000" opacity="0.18"/>']
    o.append(RR(cx + 46 * s, cy - 196 * s, 56 * s, 120 * s, 26 * s, lgrad("#e8eef7", "#9aa8bd"),
                f'stroke="#5a6a85" stroke-width="{4*s}"'))
    o.append(RR(cx - 74 * s, cy - 182 * s, 148 * s, 188 * s, 56 * s, lgrad("#ffffff", "#c9d4e4"),
                f'stroke="#5a6a85" stroke-width="{5*s}"'))
    o.append(RR(cx - 34 * s, cy - 130 * s, 68 * s, 58 * s, 18 * s, lgrad("#8ce1ff", "#2b8fd6"),
                f'stroke="#0a4a8f" stroke-width="{4*s}"'))
    for sx in (-1, 1):
        o.append(f'<g transform="rotate({sx*26} {cx+sx*70*s} {cy-160*s})">'
                 + RR(cx + sx * 70 * s - 25 * s, cy - 174 * s, 50 * s, 116 * s, 25 * s,
                      lgrad("#ffffff", "#c9d4e4"), f'stroke="#5a6a85" stroke-width="{4*s}"') + '</g>')
    o.append(C(cx, cy - 234 * s, 88 * s, lgrad("#ffffff", "#cfd9e8"), f'stroke="#5a6a85" stroke-width="{6*s}"'))
    o.append(C(cx, cy - 234 * s, 70 * s, rgrad("#2b4a8f", "#101a46"), f'stroke="#1b2a5c" stroke-width="{4*s}"'))
    o.append(face(cx, cy - 240 * s, 1.1 * s, blush=True, smile=True, eye="#9bf0ff"))
    o.append(f'<path d="M {cx-60*s} {cy-270*s} a {70*s} {70*s} 0 0 1 {44*s} {-24*s}" fill="none" '
             f'stroke="#ffffff" stroke-width="{10*s}" stroke-linecap="round" opacity="0.6"/>')
    o.append(f'<path d="M {cx+40*s} {cy-70*s} l {26*s} {34*s} l {-30*s} {10*s} Z" '
             f'fill="{lgrad("#ff9e6b", "#e2560f")}"/>')
    return "".join(o)


def mascot_monkey(cx, cy, s=1.0):
    o = [f'<ellipse cx="{cx}" cy="{cy+6*s}" rx="{72*s}" ry="{18*s}" fill="#000000" opacity="0.22"/>']
    o.append(RR(cx - 62 * s, cy - 150 * s, 124 * s, 156 * s, 54 * s, rgrad("#c8864a", "#8a5324"),
                f'stroke="#5a3515" stroke-width="{5*s}"'))
    o.append(f'<ellipse cx="{cx}" cy="{cy-58*s}" rx="{46*s}" ry="{52*s}" fill="#f3d3a8"/>')
    for sx in (-1, 1):
        o.append(f'<g transform="rotate({sx*34} {cx+sx*58*s} {cy-132*s})">'
                 + RR(cx + sx * 58 * s - 22 * s, cy - 146 * s, 44 * s, 110 * s, 22 * s,
                      rgrad("#c8864a", "#8a5324"), f'stroke="#5a3515" stroke-width="{4*s}"') + '</g>')
        o.append(C(cx + sx * 74 * s, cy - 220 * s, 32 * s, rgrad("#c8864a", "#8a5324"),
                   f'stroke="#5a3515" stroke-width="{4*s}"'))
        o.append(C(cx + sx * 74 * s, cy - 220 * s, 17 * s, "#f3d3a8"))
    o.append(C(cx, cy - 212 * s, 70 * s, rgrad("#c8864a", "#8a5324"), f'stroke="#5a3515" stroke-width="{5*s}"'))
    o.append(f'<ellipse cx="{cx}" cy="{cy-192*s}" rx="{48*s}" ry="{40*s}" fill="#f3d3a8"/>')
    o.append(C(cx - 12 * s, cy - 186 * s, 5 * s, "#5a3515"))
    o.append(C(cx + 12 * s, cy - 186 * s, 5 * s, "#5a3515"))
    o.append(f'<path d="M {cx-18*s} {cy-172*s} q {18*s} {16*s} {36*s} 0" fill="none" stroke="#5a3515" '
             f'stroke-width="{4*s}" stroke-linecap="round"/>')
    o.append(face(cx, cy - 228 * s, 1.0 * s, blush=True, smile=False, happy=True))
    o.append(leaf(cx + 10 * s, cy - 278 * s, 42 * s, ang=-24))
    return "".join(o)


def mascot_farmer(cx, cy, s=1.0):
    o = [f'<ellipse cx="{cx}" cy="{cy+6*s}" rx="{68*s}" ry="{16*s}" fill="#000000" opacity="0.2"/>']
    o.append(RR(cx - 56 * s, cy - 148 * s, 112 * s, 154 * s, 44 * s, lgrad("#8ce1ff", "#2b8fd6"),
                f'stroke="#0a4a8f" stroke-width="{5*s}"'))
    o.append(RR(cx - 34 * s, cy - 120 * s, 68 * s, 78 * s, 20 * s, "#ffffff", 'opacity="0.35"'))
    for sx in (-1, 1):
        o.append(f'<g transform="rotate({sx*40} {cx+sx*52*s} {cy-128*s})">'
                 + RR(cx + sx * 52 * s - 20 * s, cy - 140 * s, 40 * s, 104 * s, 20 * s,
                      lgrad("#8ce1ff", "#2b8fd6"), f'stroke="#0a4a8f" stroke-width="{4*s}"') + '</g>')
    o.append(C(cx, cy - 206 * s, 68 * s, lgrad("#ffe0bd", "#e8b48a"), f'stroke="#8a5a3a" stroke-width="{5*s}"'))
    o.append(f'<path d="M {cx-62*s} {cy-230*s} a {62*s} {62*s} 0 0 1 {124*s} 0 Z" fill="#8a5324"/>')
    o.append(f'<ellipse cx="{cx}" cy="{cy-242*s}" rx="{96*s}" ry="{22*s}" fill="{lgrad("#ffd979", "#d89b2a")}" '
             f'stroke="#8a5a1a" stroke-width="{4*s}"/>')
    o.append(f'<path d="M {cx-52*s} {cy-246*s} a {52*s} {52*s} 0 0 1 {104*s} 0 Z" '
             f'fill="{lgrad("#ffe9a8", "#e0a93c")}" stroke="#8a5a1a" stroke-width="{4*s}"/>')
    o.append(face(cx, cy - 202 * s, 1.0 * s))
    return "".join(o)


def mascot_cloud(cx, cy, s=1.0, trail=True):
    o = []
    if trail:
        for i, (dx, dy, rr, op) in enumerate(((-120, 90, 34, 0.5), (-180, 150, 24, 0.35),
                                              (-228, 206, 16, 0.22))):
            o.append(C(cx + dx * s, cy + dy * s, rr * s, "#ffffff", f'opacity="{op}"'))
    o.append(f'<ellipse cx="{cx}" cy="{cy+8*s}" rx="{96*s}" ry="{62*s}" fill="#ffffff"/>')
    o.append(C(cx - 62 * s, cy + 4 * s, 48 * s, "#ffffff"))
    o.append(C(cx + 62 * s, cy + 6 * s, 44 * s, "#ffffff"))
    o.append(C(cx - 18 * s, cy - 44 * s, 52 * s, "#ffffff"))
    o.append(C(cx + 34 * s, cy - 36 * s, 42 * s, "#ffffff"))
    o.append(f'<ellipse cx="{cx}" cy="{cy+40*s}" rx="{88*s}" ry="{26*s}" fill="#d8ecff" opacity="0.8"/>')
    o.append(face(cx, cy - 2 * s, 1.25 * s, blush=True, smile=False, happy=True))
    o.append(f'<path d="M {cx-22*s} {cy+22*s} q {22*s} {26*s} {44*s} 0 q {-22*s} {-6*s} {-44*s} 0 Z" '
             f'fill="#ff7a8f"/>')
    return "".join(o)


def pet_dog(cx, cy, s=1.0):
    o = [f'<ellipse cx="{cx}" cy="{cy+4*s}" rx="{44*s}" ry="{12*s}" fill="#000000" opacity="0.2"/>']
    o.append(RR(cx - 40 * s, cy - 72 * s, 80 * s, 76 * s, 30 * s, rgrad("#ffe0a8", "#c98a3a"),
                f'stroke="#7d5218" stroke-width="{4*s}"'))
    o.append(C(cx + 6 * s, cy - 104 * s, 44 * s, rgrad("#ffe0a8", "#c98a3a"), f'stroke="#7d5218" stroke-width="{4*s}"'))
    o.append(f'<ellipse cx="{cx-34*s}" cy="{cy-104*s}" rx="{16*s}" ry="{28*s}" fill="#9c6a28" '
             f'transform="rotate(-18 {cx-34*s} {cy-104*s})"/>')
    o.append(f'<ellipse cx="{cx+44*s}" cy="{cy-104*s}" rx="{15*s}" ry="{26*s}" fill="#9c6a28" '
             f'transform="rotate(14 {cx+44*s} {cy-104*s})"/>')
    o.append(C(cx - 6 * s, cy - 108 * s, 5 * s, "#2a2338"))
    o.append(C(cx + 18 * s, cy - 108 * s, 5 * s, "#2a2338"))
    o.append(f'<ellipse cx="{cx+8*s}" cy="{cy-90*s}" rx="{9*s}" ry="{7*s}" fill="#2a2338"/>')
    o.append(f'<path d="M {cx-4*s} {cy-78*s} q {12*s} {12*s} {24*s} 0" fill="none" stroke="#2a2338" '
             f'stroke-width="{3.5*s}" stroke-linecap="round"/>')
    return "".join(o)


# ----------------------------------------------------------------------------
# элементы UI
# ----------------------------------------------------------------------------
def logo(cx, cy, line1, line2=None, size1=92, size2=54, c1="#ffe066", c2="#f0820b",
         stroke="#5a2d0c", sw=16, c3=None, c4=None):
    o = [T(cx, cy, line1, size1, fill=lgrad(c1, c2), stroke=stroke, sw=sw, ls=2)]
    if line2:
        o.append(T(cx, cy + size1 * 0.78, line2, size2,
                   fill=lgrad(c3 or "#ffffff", c4 or "#bfe0ff"), stroke=stroke, sw=sw * 0.72, ls=4))
    return "".join(o)


def panel(x, y, w, h, r=34, c1="#fff6e2", c2="#ffdfb0", stroke="#b96d00", sw=5, shadow=True):
    o = []
    if shadow:
        o.append(RR(x, y + 8, w, h, r, "#00000030"))
    o.append(RR(x, y, w, h, r, lgrad(c1, c2), f'stroke="{stroke}" stroke-width="{sw}"'))
    return "".join(o)


def dark_panel(x, y, w, h, r=34, c1="#2f4a2a", c2="#16290f", stroke="#9bf07a", sw=4):
    return RR(x, y + 8, w, h, r, "#00000035") + RR(x, y, w, h, r, lgrad(c1, c2),
                                                   f'stroke="{stroke}" stroke-width="{sw}"')


def progress(x, y, w, h, frac, c1="#9bf07a", c2="#2fa84f", bg="#1d2a1a"):
    return (RR(x, y, w, h, h / 2, bg, 'stroke="#00000033" stroke-width="3"') +
            RR(x + 4, y + 4, max(h - 8, (w - 8) * frac), h - 8, (h - 8) / 2, lgrad(c1, c2)) +
            RR(x + 12, y + 8, max(0, (w - 8) * frac - 24), (h - 8) * 0.34, h * 0.14, "#ffffff",
               'opacity="0.35"'))


def pop_label(cx, cy, text="POP!", size=46, rot=-10, c="#fff3a0", stroke="#d11128"):
    return (f'<g transform="rotate({rot} {cx} {cy})">' +
            T(cx, cy, text, size, fill=c, stroke=stroke, sw=10) + '</g>')


def burst(cx, cy, r, c1="#fff3a0", c2="#ff7a8f", n=12):
    o = [C(cx, cy, r * 1.25, fade("#ffffff", 0.75, 0.0))]
    for i in range(n):
        a = math.radians(i * 360.0 / n + 8)
        x1, y1 = cx + r * 0.62 * math.cos(a), cy + r * 0.62 * math.sin(a)
        x2, y2 = cx + r * 1.22 * math.cos(a), cy + r * 1.22 * math.sin(a)
        o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{c1 if i % 2 else c2}" stroke-width="{r*0.1}" stroke-linecap="round" '
                 f'opacity="0.95"/>')
    for i in range(6):
        a = math.radians(i * 60 + 30)
        o.append(sparkle(cx + r * 1.45 * math.cos(a), cy + r * 1.45 * math.sin(a), r * 0.22, "#ffffff", 0.9))
    return "".join(o)


def dotted(points, c="#ffffff", w=9, gap="4 28", op=0.9):
    d = " ".join(("M" if i == 0 else "L") + f" {x} {y}" for i, (x, y) in enumerate(points))
    return (f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" '
            f'stroke-dasharray="{gap}" opacity="{op}"/>')


def round_btn(cx, cy, r, c1, c2, stroke="#ffffff", sw=5):
    return (C(cx, cy + 6, r, "#00000035") +
            C(cx, cy, r, lgrad(c1, c2), f'stroke="{stroke}" stroke-width="{sw}"') +
            hl(cx - r * 0.3, cy - r * 0.42, r * 0.44, r * 0.2, rot=-20, op=0.35))


def badge(cx, cy, r, text, c1="#ff6b8a", c2="#d11149", size=None):
    size = size or r * 1.1
    return (C(cx, cy, r, lgrad(c1, c2), 'stroke="#ffffff" stroke-width="4"') +
            T(cx, cy + size * 0.36, text, size, fill="#ffffff", fam=FB))
