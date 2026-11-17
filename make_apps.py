# -*- coding: utf-8 -*-
"""Макеты экранов реальных приложений (1080x1920, без рамки телефона
и строки состояния). Рендер — render_apps.ps1."""

import math, os, random

import make_screens as ms
from make_screens import (W, H, DEFS, CNT, T, RR, C, star, sparkle, lgrad, lgrad3,
                          rgrad, fade, write)
from apps_lib import *

ROOT = os.path.dirname(os.path.abspath(__file__))
ms.HTML_DIR = os.path.join(ROOT, "html_apps")


# ----------------------------------------------------------------------------
# 1. ЦВЕТЫ — «Флора»
# ----------------------------------------------------------------------------
def app_flowers():
    ACC, ACC2 = "#e2548a", "#b8306b"
    o = [RR(0, 0, W, H, 0, "#fdf6fa")]
    o.append(C(900, 60, 320, fade("#ffd1e8", 0.5, 0.0)))

    o.append(ic("pin", 76, 108, 0.95, ACC))
    o.append(txt(112, 98, "Доставка", 24, MUTE, 600))
    o.append(txt(112, 136, "Москва, Тверская 12", 32, INK, 700))
    o.append(ic("chev_d", 448, 124, 0.7, MUTE))
    o.append(C(1000, 110, 46, "#ffffff", 'stroke="#f0e2ea" stroke-width="2"'))
    o.append(ic("bell", 1000, 110, 0.85, INK))
    o.append(C(1018, 92, 11, ACC, 'stroke="#ffffff" stroke-width="3"'))

    o.append(field(48, 196, 860, 96, "Поиск букетов и подарков"))
    o.append(RR(930, 196, 102, 96, 30, lgrad(ACC, ACC2)))
    o.append(ic("filter", 981, 244, 0.95, "#ffffff"))

    # промо
    o.append(card(48, 326, 984, 230, 40, lgrad("#ff9bc4", "#d6347b"), shadow=True))
    o.append(C(900, 400, 190, "#ffffff", 'opacity="0.12"'))
    o.append(txt(88, 400, "Скидка 20%", 52, "#ffffff", 800))
    o.append(txt(88, 452, "на первый заказ по промокоду FLOWER", 28, "#ffffff", 600, op=0.9))
    o.append(pill_btn(88, 478, 260, 62, "Забрать", "#ffffff", "#ffe9f3", 28, ACC2))
    o.append(bouquet(880, 520, 1.05, [("#ffffff", "#ffd9ea"), ("#ffd166", "#f0920b"),
                                      ("#ff8fb0", "#d6347b")], heads=6))

    chips = [("Все", True), ("Розы", False), ("Пионы", False), ("Авторские", False), ("Шары", False)]
    x = 48
    for (lb, act) in chips:
        w_ = 70 + len(lb) * 20
        o.append(chip(x, 592, w_, 72, lb, act, ACC, 28))
        x += w_ + 18

    # карточки товаров
    goods = [("Нежность", "15 пионов", "4 290 ₽", [("#ffd1e8", "#f093c0"), ("#ffffff", "#ffe9f3")], "Хит"),
             ("Рассвет", "25 роз", "5 150 ₽", [("#ffb3a0", "#e2543c"), ("#ffd166", "#f0920b")], None),
             ("Лавандовый", "Авторский", "3 780 ₽", [("#d9c2ff", "#8a6ad0"), ("#ffffff", "#efe6ff")], None),
             ("Солнечный", "19 гербер", "4 650 ₽", [("#ffe066", "#f0a500"), ("#ffd1e8", "#f093c0")], "-15%")]
    for i, (name, sub, price, pal, tag) in enumerate(goods):
        cx_ = 48 + (i % 2) * 514
        cy_ = 700 + (i // 2) * 530
        o.append(card(cx_, cy_, 470, 500, 36))
        o.append(RR(cx_ + 16, cy_ + 16, 438, 286, 28, lgrad("#fdf2f8", "#f6e4ef")))
        o.append(bouquet(cx_ + 235, cy_ + 268, 0.86, pal, heads=6))
        o.append(C(cx_ + 404, cy_ + 60, 34, "#ffffff", 'stroke="#f0e2ea" stroke-width="2"'))
        o.append(ic("heart", cx_ + 404, cy_ + 60, 0.62, ACC if i == 0 else "#dfe4ee"))
        if tag:
            o.append(RR(cx_ + 32, cy_ + 34, 112, 52, 26, lgrad(ACC, ACC2)))
            o.append(txt(cx_ + 88, cy_ + 68, tag, 26, "#ffffff", 700, "middle"))
        o.append(txt(cx_ + 32, cy_ + 358, name, 36, INK, 700))
        o.append(txt(cx_ + 32, cy_ + 400, sub, 26, MUTE, 600))
        o.append(txt(cx_ + 32, cy_ + 462, price, 38, INK, 800))
        o.append(RR(cx_ + 362, cy_ + 418, 76, 76, 26, lgrad(ACC, ACC2)))
        o.append(ic("plus", cx_ + 400, cy_ + 456, 0.8, "#ffffff"))

    o.append(tabbar([("Каталог", "home"), ("Избранное", "heart"), ("Корзина", "cart"),
                     ("Заказы", "list"), ("Профиль", "user")], 0, ACC))
    o.append(C(690, 1766, 15, ACC, 'stroke="#ffffff" stroke-width="4"'))
    return "".join(o)


# ----------------------------------------------------------------------------
# 2. ГАЗ — «МойГаз»
# ----------------------------------------------------------------------------
def app_gas():
    ACC, ACC2 = "#2b74d6", "#174f9c"
    o = [RR(0, 0, W, H, 0, "#f2f5fb")]
    o.append(RR(0, 0, W, 300, 0, lgrad(ACC, ACC2)))
    o.append(C(960, 40, 280, fade("#ffffff", 0.16, 0.0)))
    o.append(RR(48, 70, 80, 80, 26, "#ffffff", 'opacity="0.18"'))
    o.append(ic("gas", 88, 110, 1.0, "#ffffff"))
    o.append(txt(152, 98, "МойГаз", 36, "#ffffff", 800))
    o.append(txt(152, 140, "Лицевой счёт 4512 8830", 26, "#ffffff", 600, op=0.85))
    o.append(C(1000, 110, 46, "#ffffff", 'opacity="0.18"'))
    o.append(ic("bell", 1000, 110, 0.85, "#ffffff"))

    # к оплате
    o.append(card(48, 208, 984, 330, 40))
    o.append(txt(88, 282, "К оплате за октябрь", 30, MUTE, 600))
    o.append(txt(88, 368, "1 248,60 ₽", 76, INK, 800))
    o.append(RR(88, 400, 300, 56, 28, "#fff2e2"))
    o.append(ic("clock", 124, 428, 0.7, "#e2800f"))
    o.append(txt(152, 438, "до 10 ноября", 28, "#e2800f", 700))
    o.append(pill_btn(600, 282, 392, 96, "Оплатить", ACC, ACC2, 34))
    o.append(txt(796, 430, "Через СБП без комиссии", 24, MUTE, 600, "middle"))
    o.append(divider(88, 472, 904))
    o.append(ic("doc", 116, 510, 0.75, MUTE))
    o.append(txt(152, 520, "Квитанция за октябрь · PDF", 28, INK, 600))
    o.append(ic("chev_r", 976, 510, 0.7, MUTE))

    # счётчик
    o.append(card(48, 572, 984, 330, 40))
    o.append(RR(88, 608, 76, 76, 26, "#eaf2ff"))
    o.append(ic("meter", 126, 646, 0.85, ACC))
    o.append(txt(188, 638, "Показания счётчика", 32, INK, 700))
    o.append(txt(188, 678, "Передано 12.10 · 01279 м³", 26, MUTE, 600))
    for i, d in enumerate("01284"):
        bx = 88 + i * 128
        act = i >= 3
        o.append(RR(bx, 716, 110, 110, 28, "#ffffff",
                    f'stroke="{ACC if act else LINE}" stroke-width="{4 if act else 2}"'))
        o.append(txt(bx + 55, 790, d, 48, INK if act else MUTE, 800, "middle"))
    o.append(pill_btn(736, 716, 256, 110, "Передать", ACC, ACC2, 30))
    o.append(txt(88, 872, "Расход за месяц: 5 м³", 26, MUTE, 600))

    # график
    o.append(card(48, 936, 984, 400, 40))
    o.append(txt(88, 1006, "Потребление, м³", 32, INK, 700))
    o.append(txt(992, 1006, "6 месяцев", 26, ACC, 700, "end"))
    o.append(bars(96, 1056, 880, 180, [7, 6, 4, 3, 4, 5],
                  ["май", "июн", "июл", "авг", "сен", "окт"], "#6aa8ff", ACC, hi=5,
                  val_fmt="%d м³"))

    # быстрые действия
    acts = [("История", "list"), ("Квитанции", "doc"), ("Заявка", "chat"), ("Поддержка", "user")]
    for i, (lb, icon_name) in enumerate(acts):
        x = 48 + i * 252
        o.append(card(x, 1374, 228, 190, 34))
        o.append(RR(x + 76, 1410, 76, 76, 26, "#eaf2ff"))
        o.append(ic(icon_name, x + 114, 1448, 0.85, ACC))
        o.append(txt(x + 114, 1534, lb, 26, INK, 600, "middle"))

    o.append(card(48, 1598, 984, 108, 34, "#fff6e2", "#f0d9a8"))
    o.append(ic("bell", 112, 1652, 0.8, "#e2800f"))
    o.append(txt(160, 1644, "Передайте показания до 25 числа,", 27, "#8a5a1a", 700))
    o.append(txt(160, 1682, "иначе расчёт пойдёт по нормативу", 25, "#a87a3a", 600))

    o.append(tabbar([("Главная", "home"), ("Платежи", "wallet"), ("Счётчики", "meter"),
                     ("Чат", "chat"), ("Профиль", "user")], 0, ACC))
    return "".join(o)


# ----------------------------------------------------------------------------
# 3. ТАКСИ — «Поехали»
# ----------------------------------------------------------------------------
def app_taxi():
    ACC, ACC2 = "#1f2a44", "#0e1526"
    YEL, YEL2 = "#ffd14a", "#f0a500"
    o = [map_bg(0, 0, W, 1320)]
    # маршрут
    route = [(250, 1130), (250, 860), (560, 860), (560, 520), (840, 520), (840, 360)]
    d = " ".join(("M" if i == 0 else "L") + f" {x} {y}" for i, (x, y) in enumerate(route))
    o.append(f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="26" stroke-linecap="round" '
             f'stroke-linejoin="round"/>')
    o.append(f'<path d="{d}" fill="none" stroke="{lgrad("#3f7ae0", "#1f4fb0")}" stroke-width="16" '
             f'stroke-linecap="round" stroke-linejoin="round"/>')
    o.append(map_pin(250, 1130, "#2fa84f", 1.1))
    o.append(map_pin(840, 360, "#e2443c", 1.1))
    o.append(RR(600, 760, 110, 64, 22, "#ffffff", 'filter="url(#shs)"'))
    o.append(ic("car", 655, 792, 0.9, ACC))
    o.append(RR(338, 1066, 220, 68, 34, "#ffffff", 'filter="url(#shs)"'))
    o.append(txt(448, 1110, "4 мин · 2,8 км", 26, INK, 700, "middle"))

    # адреса
    o.append(card(48, 56, 984, 244, 40))
    o.append(C(104, 136, 16, "#2fa84f"))
    o.append(txt(148, 124, "Откуда", 24, MUTE, 600))
    o.append(txt(148, 160, "ул. Ленина, 14", 34, INK, 700))
    o.append(divider(148, 190, 700))
    o.append(RR(90, 218, 28, 28, 8, "#e2443c"))
    o.append(txt(148, 212, "Куда", 24, MUTE, 600))
    o.append(txt(148, 248, "Аэропорт Шереметьево, терминал B", 34, INK, 700))
    o.append(C(948, 186, 50, "#f2f5fb"))
    o.append(ic("swap", 948, 186, 0.8, ACC))

    o.append(C(1000, 376, 54, "#ffffff", 'filter="url(#shs)"'))
    o.append(ic("pin", 1000, 376, 0.9, ACC))
    o.append(C(1000, 500, 54, "#ffffff", 'filter="url(#shs)"'))
    o.append(ic("arrow_up", 1000, 500, 0.9, ACC))

    # нижняя шторка
    o.append(RR(0, 1216, W, 760, 56, "#1d233520"))
    o.append(RR(0, 1224, W, 760, 56, "#ffffff"))
    o.append(RR(486, 1256, 108, 12, 6, "#d7dced"))
    o.append(txt(48, 1340, "Выберите тариф", 38, INK, 800))
    o.append(txt(1032, 1340, "4 мин", 30, MUTE, 700, "end"))
    tariffs = [("Эконом", "420 ₽", "4 мин", False), ("Комфорт", "610 ₽", "3 мин", True),
               ("Бизнес", "980 ₽", "7 мин", False)]
    for i, (name, price, eta, act) in enumerate(tariffs):
        x = 48 + i * 328
        o.append(RR(x, 1380, 304, 268, 36, "#ffffff" if act else "#f6f8fc",
                    f'stroke="{YEL2 if act else LINE}" stroke-width="{4 if act else 2}"'))
        if act:
            o.append(RR(x, 1380, 304, 268, 36, YEL, 'opacity="0.1"'))
        o.append(RR(x + 86, 1414, 132, 86, 22, "#eef2f8"))
        o.append(ic("car", x + 152, 1458, 1.3 if act else 1.1, ACC if act else "#8b93a7"))
        o.append(txt(x + 152, 1552, name, 32, INK, 700, "middle"))
        o.append(txt(x + 152, 1600, price, 36, INK if act else MUTE, 800, "middle"))
        o.append(txt(x + 152, 1634, eta, 24, MUTE, 600, "middle"))
    o.append(divider(48, 1690, 984))
    o.append(RR(48, 1716, 96, 68, 20, "#f2f5fb"))
    o.append(ic("card", 96, 1750, 0.8, ACC))
    o.append(txt(168, 1762, "Картой · •••• 4821", 32, INK, 700))
    o.append(ic("chev_r", 996, 1750, 0.7, MUTE))
    o.append(pill_btn(48, 1812, 984, 112, "Заказать за 610 ₽", YEL, YEL2, 38, ACC))
    return "".join(o)


# ----------------------------------------------------------------------------
# 4. БАНК — «Капитал»
# ----------------------------------------------------------------------------
def app_bank():
    ACC, ACC2 = "#5a3fd6", "#2e1f8f"
    o = [RR(0, 0, W, H, 0, "#f3f4fb")]
    o.append(avatar(96, 112, 46))
    o.append(txt(170, 96, "Добрый день,", 26, MUTE, 600))
    o.append(txt(170, 140, "Сергей", 38, INK, 800))
    o.append(C(1000, 112, 46, "#ffffff", 'stroke="#e6e9f2" stroke-width="2"'))
    o.append(ic("bell", 1000, 112, 0.85, INK))
    o.append(C(1018, 94, 11, "#e2443c", 'stroke="#ffffff" stroke-width="3"'))

    # карта
    o.append(card(48, 196, 984, 340, 44, lgrad3("#6a4fe0", "#4a2fc0", "#2a1a86")))
    o.append(C(960, 230, 220, fade("#ffffff", 0.16, 0.0)))
    o.append(C(140, 520, 200, fade("#ffffff", 0.1, 0.0)))
    o.append(txt(96, 268, "Дебетовая карта", 26, "#ffffff", 600, op=0.8))
    o.append(RR(92, 296, 86, 64, 14, lgrad("#ffe9a8", "#e0a93c")))
    o.append(RR(112, 316, 46, 24, 6, "#c08a2a"))
    o.append(txt(96, 436, "124 350,20 ₽", 64, "#ffffff", 800))
    o.append(txt(96, 490, "•••• 4821", 32, "#ffffff", 600, op=0.85))
    o.append(txt(992, 492, "МИР", 36, "#ffffff", 800, "end", op=0.9))
    o.append(RR(880, 280, 110, 60, 30, "#ffffff", 'opacity="0.18"'))
    o.append(txt(935, 318, "+ 2,4%", 24, "#ffffff", 700, "middle"))

    acts = [("Перевести", "swap"), ("Пополнить", "plus"), ("Оплатить", "card"), ("Ещё", "list")]
    for i, (lb, icon_name) in enumerate(acts):
        x = 48 + i * 252
        o.append(card(x, 576, 228, 176, 34))
        o.append(C(x + 114, 640, 40, "#f0edff"))
        o.append(ic(icon_name, x + 114, 640, 0.8, ACC))
        o.append(txt(x + 114, 718, lb, 26, INK, 600, "middle"))

    # траты
    o.append(card(48, 788, 984, 404, 40))
    o.append(txt(88, 856, "Траты в ноябре", 34, INK, 700))
    o.append(txt(992, 856, "Отчёт", 28, ACC, 700, "end"))
    segs = [(0.38, "#5a3fd6"), (0.22, "#ff8a5c"), (0.18, "#2fa84f"), (0.22, "#8ab4ff")]
    o.append(donut(260, 1040, 120, segs, 46))
    o.append(txt(260, 1030, "48 200 ₽", 38, INK, 800, "middle"))
    o.append(txt(260, 1072, "всего", 26, MUTE, 600, "middle"))
    legend = [("Продукты", "18 300 ₽", "#5a3fd6"), ("Транспорт", "10 600 ₽", "#ff8a5c"),
              ("Кафе", "8 700 ₽", "#2fa84f"), ("Прочее", "10 600 ₽", "#8ab4ff")]
    for i, (lb, val, col) in enumerate(legend):
        y = 920 + i * 62
        o.append(C(470, y - 10, 14, col))
        o.append(txt(506, y, lb, 28, INK, 600))
        o.append(txt(992, y, val, 28, INK, 700, "end"))

    # операции
    o.append(txt(48, 1252, "Операции", 36, INK, 800))
    o.append(txt(1032, 1252, "Все", 28, ACC, 700, "end"))
    ops = [("Пятёрочка", "Продукты · сегодня", "−840 ₽", "#ff8a5c", "cart", False),
           ("Поехали Такси", "Транспорт · вчера", "−310 ₽", "#8ab4ff", "car", False),
           ("ООО «Ромашка»", "Зарплата · 25 окт", "+95 000 ₽", "#2fa84f", "arrow_dl", True),
           ("Кофемания", "Кафе · 24 окт", "−480 ₽", "#f0a500", "list", False)]
    for i, (name, sub, val, col, icon_name, plus) in enumerate(ops):
        y = 1288 + i * 104
        o.append(card(48, y, 984, 92, 30, shadow=False, stroke=LINE))
        o.append(C(108, y + 48, 34, col, 'opacity="0.16"'))
        o.append(ic(icon_name, 108, y + 48, 0.68, col))
        o.append(txt(164, y + 42, name, 30, INK, 700))
        o.append(txt(164, y + 78, sub, 24, MUTE, 600))
        o.append(txt(992, y + 60, val, 32, "#2fa84f" if plus else INK, 800, "end"))

    o.append(tabbar([("Главная", "home"), ("Платежи", "card"), ("История", "chart"),
                     ("Чат", "chat"), ("Профиль", "user")], 0, ACC))
    return "".join(o)


# ----------------------------------------------------------------------------
# 5. ПОГОДА
# ----------------------------------------------------------------------------
def app_weather():
    o = [RR(0, 0, W, H, 0, lgrad3("#3f93e8", "#6fb6f2", "#bfe0ff"))]
    o.append(C(880, 300, 280, fade("#ffffff", 0.45, 0.0)))
    o.append(C(880, 300, 120, "#fff3a0"))
    for (cx, cy, s, op) in ((164, 300, 0.95, 0.85), (806, 598, 0.7, 0.55), (420, 212, 0.45, 0.45)):
        o.append(f'<g opacity="{op}"><ellipse cx="{cx}" cy="{cy}" rx="{110*s}" ry="{58*s}" fill="#ffffff"/>'
                 f'<ellipse cx="{cx-80*s}" cy="{cy+16*s}" rx="{64*s}" ry="{40*s}" fill="#ffffff"/>'
                 f'<ellipse cx="{cx+82*s}" cy="{cy+18*s}" rx="{58*s}" ry="{36*s}" fill="#ffffff"/></g>')

    o.append(ic("pin", 76, 96, 0.85, "#ffffff"))
    o.append(txt(110, 108, "Москва", 40, "#ffffff", 800))
    o.append(ic("chev_d", 296, 98, 0.7, "#ffffff"))
    o.append(C(1000, 96, 46, "#ffffff", 'opacity="0.25"'))
    o.append(ic("plus", 1000, 96, 0.8, "#ffffff"))
    o.append(txt(540, 196, "Среда, 29 октября · 14:20", 30, "#ffffff", 600, "middle", op=0.9))

    o.append(txt(540, 460, "18°", 220, "#ffffff", 800, "middle"))
    o.append(txt(540, 528, "Малооблачно", 42, "#ffffff", 700, "middle"))
    o.append(txt(540, 582, "Ощущается как 16°  ·  ↑ 22°   ↓ 11°", 30, "#ffffff", 600, "middle", op=0.92))

    # почасовой
    o.append(RR(48, 700, 984, 260, 40, "#ffffff", 'opacity="0.22"'))
    hours = [("Сейчас", "sun", "18°"), ("15:00", "sun", "19°"), ("16:00", "cloudsun", "19°"),
             ("17:00", "cloudsun", "17°"), ("18:00", "cloud", "15°"), ("19:00", "rain", "13°")]
    for i, (hh, icon_name, tt) in enumerate(hours):
        x = 128 + i * 160
        if i == 0:
            o.append(RR(x - 68, 724, 136, 212, 34, "#ffffff", 'opacity="0.3"'))
        o.append(txt(x, 776, hh, 26, "#ffffff", 600, "middle", op=0.9))
        o.append(ic(icon_name, x, 846, 1.05, "#ffffff" if icon_name != "sun" else "#ffe066"))
        o.append(txt(x, 924, tt, 36, "#ffffff", 800, "middle"))

    # на неделю
    o.append(card(48, 1000, 984, 520, 40, "#ffffff", shadow=False, op=0.95))
    o.append(txt(88, 1070, "На неделю", 34, INK, 700))
    days = [("Чт", "sun", 11, 22, "#ffe066"), ("Пт", "cloudsun", 10, 20, "#8ab4ff"),
            ("Сб", "rain", 8, 15, "#5a8fd6"), ("Вс", "cloud", 7, 13, "#a7aec2"),
            ("Пн", "sun", 9, 17, "#ffe066")]
    for i, (d, icon_name, tmin, tmax, col) in enumerate(days):
        y = 1140 + i * 76
        o.append(txt(96, y + 12, d, 32, INK, 700))
        o.append(ic(icon_name, 220, y, 0.8, col if icon_name == "sun" else "#8ab4ff"))
        o.append(txt(330, y + 12, f"{tmin}°", 30, MUTE, 600))
        o.append(RR(400, y - 10, 460, 18, 9, "#eef1f8"))
        o.append(RR(400 + (tmin - 6) * 22, y - 10, (tmax - tmin) * 26, 18, 9,
                    lgrad("#8ad6ff", "#f0a500")))
        o.append(txt(920, y + 12, f"{tmax}°", 30, INK, 700))
    # детали
    det = [("Ветер", "4 м/с", "wind"), ("Влажность", "62%", "drop"),
           ("УФ-индекс", "3 низкий", "sun"), ("Давление", "748 мм", "chart")]
    for i, (lb, val, icon_name) in enumerate(det):
        x = 48 + (i % 2) * 514
        y = 1560 + (i // 2) * 180
        o.append(RR(x, y, 470, 156, 36, "#ffffff", 'opacity="0.22"'))
        o.append(ic(icon_name, x + 68, y + 56, 0.85, "#ffffff"))
        o.append(txt(x + 118, y + 66, lb, 28, "#ffffff", 600, op=0.9))
        o.append(txt(x + 40, y + 126, val, 40, "#ffffff", 800))
    return "".join(o)


# ----------------------------------------------------------------------------
# 6. ФИТНЕС — «Пульс»
# ----------------------------------------------------------------------------
def app_fitness():
    ACC, ACC2 = "#7cf2a8", "#2fa84f"
    BGD, CARD = "#10141f", "#1a2030"
    o = [RR(0, 0, W, H, 0, lgrad3("#141a2a", "#10141f", "#080b14"))]
    o.append(C(900, 220, 340, fade("#2fa84f", 0.3, 0.0)))
    o.append(C(140, 900, 300, fade("#3f7ae0", 0.2, 0.0)))

    o.append(txt(48, 96, "Среда, 29 октября", 28, "#8b93a7", 600))
    o.append(txt(48, 148, "Моя активность", 42, "#ffffff", 800))
    o.append(avatar(1000, 118, 46, "#7cf2a8", "#2fa84f"))

    # кольца
    o.append(RR(48, 206, 984, 420, 44, CARD))
    o.append(ring(268, 416, 150, 0.78, "#ff6b8a", "#d11149", 34, "#232b3e"))
    o.append(ring(268, 416, 108, 0.62, "#7cf2a8", "#2fa84f", 34, "#232b3e"))
    o.append(ring(268, 416, 66, 0.45, "#8ad6ff", "#2b74d6", 34, "#232b3e"))
    o.append(txt(268, 428, "78%", 44, "#ffffff", 800, "middle"))
    rows = [("Калории", "620", "800 ккал", "#ff6b8a", 0.78), ("Шаги", "8 420", "10 000", "#7cf2a8", 0.62),
            ("Минуты", "42", "60 мин", "#8ad6ff", 0.45)]
    for i, (lb, val, goal, col, frac) in enumerate(rows):
        y = 330 + i * 110
        o.append(C(500, y - 10, 12, col))
        o.append(txt(530, y, lb, 28, "#8b93a7", 600))
        o.append(txt(530, y + 48, val, 40, "#ffffff", 800))
        o.append(txt(660, y + 48, f"/ {goal}", 26, "#8b93a7", 600))
        o.append(RR(530, y + 66, 440, 12, 6, "#232b3e"))
        o.append(RR(530, y + 66, 440 * frac, 12, 6, col))

    # шаги
    o.append(RR(48, 660, 984, 360, 44, CARD))
    o.append(ic("steps", 100, 724, 0.9, "#7cf2a8"))
    o.append(txt(146, 736, "Шаги за неделю", 32, "#ffffff", 700))
    o.append(txt(992, 736, "+12%", 30, "#7cf2a8", 700, "end"))
    o.append(bars(96, 800, 880, 150, [6.2, 7.4, 5.1, 9.2, 8.4, 4.6, 8.4],
                  ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"], "#7cf2a8", "#2fa84f",
                  hi=6, lab_c="#8b93a7", val_fmt="%.1fк", track="#232b3e", inac="#3f8f66",
                  val_c="#ffffff"))

    # пульс
    o.append(RR(48, 1054, 470, 330, 44, CARD))
    o.append(ic("pulse", 100, 1118, 0.9, "#ff6b8a"))
    o.append(txt(146, 1130, "Пульс", 32, "#ffffff", 700))
    o.append(txt(88, 1222, "72", 68, "#ffffff", 800))
    o.append(txt(176, 1222, "уд/мин", 28, "#8b93a7", 600))
    o.append(line_chart(92, 1252, 380, 90, [68, 74, 71, 88, 76, 70, 72], "#ff6b8a", 0.2, False))

    # сон
    o.append(RR(562, 1054, 470, 330, 44, CARD))
    o.append(ic("moon", 614, 1118, 0.9, "#8ab4ff"))
    o.append(txt(660, 1130, "Сон", 32, "#ffffff", 700))
    o.append(txt(602, 1222, "7ч 20м", 60, "#ffffff", 800))
    o.append(txt(602, 1272, "Норма 8 часов", 26, "#8b93a7", 600))
    o.append(RR(602, 1300, 390, 16, 8, "#232b3e"))
    o.append(RR(602, 1300, 358, 16, 8, lgrad("#8ad6ff", "#2b74d6")))

    # тренировка
    o.append(RR(48, 1398, 984, 186, 44, CARD))
    o.append(RR(88, 1430, 122, 122, 34, lgrad("#2fa84f", "#176b31")))
    o.append(ic("fire", 149, 1491, 1.15, "#7cf2a8"))
    o.append(txt(242, 1482, "Вечерняя пробежка", 34, "#ffffff", 700))
    o.append(txt(242, 1526, "Запланировано на 19:00 · 5 км", 26, "#8b93a7", 600))
    o.append(pill_btn(48, 1602, 984, 92, "Начать тренировку", "#7cf2a8", "#2fa84f", 34, "#0d2a16"))

    o.append(tabbar([("Сводка", "home"), ("Тренировки", "fire"), ("Статистика", "chart"),
                     ("Профиль", "user")], 0, "#7cf2a8", y=1700, h=150, bg=CARD))
    return "".join(o)


# ----------------------------------------------------------------------------
# 7. ЕДА — «Вкусно Домой»
# ----------------------------------------------------------------------------
def app_food():
    ACC, ACC2 = "#f0620b", "#c43d00"
    o = [RR(0, 0, W, H, 0, "#fff8f1")]
    o.append(C(920, 80, 300, fade("#ffd1a8", 0.5, 0.0)))

    o.append(ic("pin", 76, 108, 0.95, ACC))
    o.append(txt(112, 98, "Доставка за 30 мин", 24, MUTE, 600))
    o.append(txt(112, 136, "ул. Гагарина, 7", 32, INK, 700))
    o.append(ic("chev_d", 396, 124, 0.7, MUTE))
    o.append(C(1000, 110, 46, "#ffffff", 'stroke="#f2e4d6" stroke-width="2"'))
    o.append(ic("cart", 1000, 110, 0.85, INK))
    o.append(C(1020, 90, 15, ACC, 'stroke="#ffffff" stroke-width="3"'))
    o.append(txt(1020, 99, "3", 20, "#ffffff", 800, "middle"))

    o.append(field(48, 196, 984, 96, "Пицца, роллы, бургеры…"))

    cats = [("Пицца", "pizza"), ("Суши", "sushi"), ("Бургеры", "burger"),
            ("Кофе", "coffee"), ("Десерты", "cake")]
    for i, (lb, kind) in enumerate(cats):
        x = 116 + i * 200
        o.append(C(x, 400, 68, "#ffffff", 'filter="url(#shs)"'))
        o.append(food_icon(kind, x, 400, 46))
        o.append(txt(x, 510, lb, 26, INK, 600, "middle"))

    # ресторан
    o.append(card(48, 560, 984, 300, 40, lgrad("#ff9a5c", "#e2470b")))
    o.append(C(940, 600, 190, "#ffffff", 'opacity="0.14"'))
    o.append(food_icon("pizza", 880, 740, 110))
    o.append(RR(88, 600, 192, 56, 28, "#ffffff", 'opacity="0.22"'))
    o.append(txt(184, 638, "Бесплатно", 26, "#ffffff", 700, "middle"))
    o.append(txt(88, 712, "Пицца Фреш", 52, "#ffffff", 800))
    o.append(star(104, 762, 20, "#ffe066", stroke="none", sw=0))
    o.append(txt(132, 774, "4,8  ·  25–35 мин  ·  от 600 ₽", 28, "#ffffff", 600, op=0.95))
    o.append(pill_btn(88, 798, 260, 62, "В меню", "#ffffff", "#ffe9d8", 28, ACC2))

    o.append(txt(48, 940, "Популярное", 38, INK, 800))
    o.append(txt(1032, 940, "Всё меню", 28, ACC, 700, "end"))
    dishes = [("Пепперони 30 см", "Пикантная колбаса, моцарелла", "690 ₽", "pizza", "Хит"),
              ("Филадельфия, 8 шт", "Лосось, сыр, огурец", "540 ₽", "sushi", None),
              ("Чизбургер XL", "Говядина, чеддер, соус", "420 ₽", "burger", "-20%"),
              ("Латте 0,4 л", "На кокосовом молоке", "210 ₽", "coffee", None)]
    for i, (name, sub, price, kind, tag) in enumerate(dishes):
        y = 990 + i * 178
        o.append(card(48, y, 984, 158, 36))
        o.append(RR(76, y + 20, 118, 118, 30, "#fff2e2"))
        o.append(food_icon(kind, 135, y + 79, 44))
        o.append(txt(220, y + 60, name, 32, INK, 700))
        o.append(txt(220, y + 102, sub, 25, MUTE, 600))
        o.append(txt(220, y + 136, price, 32, INK, 800))
        if tag:
            o.append(RR(352, y + 108, 104, 44, 22, "#ffeadb"))
            o.append(txt(404, y + 139, tag, 24, ACC, 700, "middle"))
        o.append(RR(924, y + 44, 76, 76, 26, lgrad(ACC, ACC2)))
        o.append(ic("plus", 962, y + 82, 0.8, "#ffffff"))

    o.append(pill_btn(48, 1716, 984, 108, "Корзина · 1 240 ₽", ACC, ACC2, 36))
    o.append(ic("cart", 180, 1770, 0.85, "#ffffff"))
    o.append(RR(W / 2 - 120, 1868, 240, 10, 5, "#e6d9c8"))
    return "".join(o)


# ----------------------------------------------------------------------------
# 8. УМНЫЙ ДОМ
# ----------------------------------------------------------------------------
def app_smarthome():
    ACC, ACC2 = "#3f6fd8", "#24449c"
    o = [RR(0, 0, W, H, 0, lgrad3("#eef2ff", "#f5f7fd", "#e9edfa"))]
    o.append(C(940, 120, 300, fade("#c9d8ff", 0.6, 0.0)))

    o.append(txt(48, 100, "Добрый вечер", 28, MUTE, 600))
    o.append(txt(48, 152, "Квартира", 44, INK, 800))
    o.append(C(1000, 118, 46, "#ffffff", 'stroke="#e0e5f2" stroke-width="2"'))
    o.append(ic("plus", 1000, 118, 0.85, INK))
    o.append(C(912, 118, 46, "#ffffff", 'stroke="#e0e5f2" stroke-width="2"'))
    o.append(ic("bell", 912, 118, 0.8, INK))

    sums = [("22°", "в доме", "sun", "#f0a500"), ("45%", "влажность", "drop", "#3f9ad8"),
            ("6", "устройств", "bolt", "#7c5ae0")]
    for i, (val, lb, icon_name, col) in enumerate(sums):
        x = 48 + i * 336
        o.append(card(x, 208, 312, 150, 36))
        o.append(C(x + 66, 284, 34, col, 'opacity="0.14"'))
        o.append(ic(icon_name, x + 66, 284, 0.7, col))
        o.append(txt(x + 118, 272, val, 36, INK, 800))
        o.append(txt(x + 118, 312, lb, 24, MUTE, 600))

    # термостат
    o.append(card(48, 394, 984, 470, 44))
    o.append(txt(88, 462, "Отопление", 34, INK, 700))
    o.append(txt(88, 504, "Гостиная · работает", 26, MUTE, 600))
    o.append(toggle(900, 440, True, "#f0a500"))
    cx, cy = 540, 680
    o.append(C(cx, cy, 160, "none", 'stroke="#eef1f8" stroke-width="30"'))
    circ = 2 * math.pi * 160
    o.append(f'<circle cx="{cx}" cy="{cy}" r="160" fill="none" stroke="{lgrad("#ffd166", "#f0620b")}" '
             f'stroke-width="30" stroke-linecap="round" stroke-dasharray="{circ*0.62:.0f} {circ:.0f}" '
             f'transform="rotate(130 {cx} {cy})"/>')
    for i in range(36):
        a = math.radians(130 + i * 7.8)
        o.append(f'<line x1="{cx+128*math.cos(a):.1f}" y1="{cy+128*math.sin(a):.1f}" '
                 f'x2="{cx+118*math.cos(a):.1f}" y2="{cy+118*math.sin(a):.1f}" stroke="#dfe4ee" '
                 f'stroke-width="4"/>')
    o.append(txt(cx, cy + 10, "22°", 110, INK, 800, "middle"))
    o.append(txt(cx, cy + 62, "цель 23°", 28, MUTE, 600, "middle"))
    o.append(C(cx - 250, cy, 54, "#f2f5fb"))
    o.append(ic("minus", cx - 250, cy, 0.8, INK))
    o.append(C(cx + 250, cy, 54, "#f2f5fb"))
    o.append(ic("plus", cx + 250, cy, 0.8, INK))

    rooms = [("Все", True), ("Гостиная", False), ("Кухня", False), ("Спальня", False)]
    x = 48
    for (lb, act) in rooms:
        w_ = 80 + len(lb) * 20
        o.append(chip(x, 900, w_, 72, lb, act, ACC, 28))
        x += w_ + 18

    devices = [("Свет", "Гостиная", "bulb", True, "#f0a500"),
               ("Кондиционер", "20° · авто", "ac", True, "#3f9ad8"),
               ("Шторы", "Открыты 60%", "curtain", False, "#7c5ae0"),
               ("Камера", "Прихожая", "cam", True, "#2fa84f"),
               ("Чайник", "Выключен", "kettle", False, "#e2543c"),
               ("Розетка", "ТВ · 86 Вт", "socket", True, "#5a6a85")]
    for i, (name, sub, icon_name, on, col) in enumerate(devices):
        x = 48 + (i % 2) * 514
        y = 1010 + (i // 2) * 232
        o.append(card(x, y, 470, 206, 38, "#ffffff" if on else "#f6f8fc"))
        o.append(C(x + 76, y + 70, 38, col, f'opacity="{0.16 if on else 0.08}"'))
        o.append(ic(icon_name, x + 76, y + 70, 0.8, col if on else "#a7aec2"))
        o.append(toggle(x + 310, y + 44, on, col, 92, 50))
        o.append(txt(x + 36, y + 150, name, 32, INK if on else MUTE, 700))
        o.append(txt(x + 36, y + 186, sub, 24, MUTE, 600))

    o.append(tabbar([("Дом", "home"), ("Сценарии", "bolt"), ("Энергия", "chart"),
                     ("Настройки", "gear")], 0, ACC))
    return "".join(o)


APPS = [("Flower_Shop", app_flowers, "Флора — доставка цветов"),
        ("Gas_Utility", app_gas, "МойГаз"),
        ("Taxi_Ride", app_taxi, "Поехали — такси"),
        ("Mobile_Bank", app_bank, "Капитал — банк"),
        ("Weather_Today", app_weather, "Погода"),
        ("Fitness_Tracker", app_fitness, "Пульс — фитнес"),
        ("Food_Delivery", app_food, "Вкусно Домой"),
        ("Smart_Home", app_smarthome, "Умный дом")]

if __name__ == "__main__":
    for name, fn, title in APPS:
        DEFS[:] = []
        CNT[0] = 0
        write(name, fn(), title)
