import 'package:flutter/material.dart';

/// «Вкусно Домой» — яркая доставка: крупный заголовок вместо шапки,
/// пастельные плитки категорий, большие скругления и тёмная плашка корзины.
const _orange = Color(0xFFFF6A00);
const _ink = Color(0xFF17120E);
const _mute = Color(0xFF9A8E86);

class FoodScreen extends StatelessWidget {
  const FoodScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: Stack(
        children: [
          ListView(
            padding: const EdgeInsets.fromLTRB(18, 0, 18, 96),
            physics: const NeverScrollableScrollPhysics(),
            children: [
              SafeArea(
                bottom: false,
                child: Padding(
                  padding: const EdgeInsets.only(top: 10),
                  child: Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const Text('Что закажем?',
                                style: TextStyle(
                                    fontSize: 28,
                                    fontWeight: FontWeight.w800,
                                    color: _ink,
                                    height: 1.1)),
                            const SizedBox(height: 8),
                            Container(
                              padding:
                                  const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                              decoration: BoxDecoration(
                                  color: const Color(0xFFFFF1E6),
                                  borderRadius: BorderRadius.circular(20)),
                              child: Row(
                                mainAxisSize: MainAxisSize.min,
                                children: const [
                                  Icon(Icons.place_rounded, size: 14, color: _orange),
                                  SizedBox(width: 4),
                                  Text('ул. Гагарина, 7 · 30 мин',
                                      style: TextStyle(
                                          fontSize: 11.5,
                                          color: _orange,
                                          fontWeight: FontWeight.w700)),
                                ],
                              ),
                            ),
                          ],
                        ),
                      ),
                      Container(
                        width: 44,
                        height: 44,
                        decoration: const BoxDecoration(
                            color: Color(0xFFF5F2F0), shape: BoxShape.circle),
                        child: const Icon(Icons.person_rounded, size: 22, color: _ink),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 16),
              Row(
                children: [
                  Expanded(
                    child: Container(
                      height: 46,
                      padding: const EdgeInsets.symmetric(horizontal: 14),
                      decoration: BoxDecoration(
                          color: const Color(0xFFF5F2F0),
                          borderRadius: BorderRadius.circular(16)),
                      child: Row(
                        children: const [
                          Icon(Icons.search_rounded, size: 19, color: _mute),
                          SizedBox(width: 8),
                          Text('Пицца, роллы, бургеры…',
                              style: TextStyle(fontSize: 13.5, color: _mute)),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(width: 10),
                  Container(
                    width: 46,
                    height: 46,
                    decoration: BoxDecoration(
                        color: _ink, borderRadius: BorderRadius.circular(16)),
                    child: const Icon(Icons.tune_rounded, size: 20, color: Colors.white),
                  ),
                ],
              ),
              const SizedBox(height: 18),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: const [
                  _Cat('Пицца', Icons.local_pizza_rounded, Color(0xFFFFEBD6), Color(0xFFE2740B)),
                  _Cat('Суши', Icons.set_meal_rounded, Color(0xFFFFE4E4), Color(0xFFD63B3B)),
                  _Cat('Бургеры', Icons.lunch_dining_rounded, Color(0xFFFDF0D0), Color(0xFFB4860C)),
                  _Cat('Кофе', Icons.local_cafe_rounded, Color(0xFFEFE6DE), Color(0xFF7A5134)),
                  _Cat('Десерт', Icons.cake_rounded, Color(0xFFFCE4F1), Color(0xFFD1489A)),
                ],
              ),
              const SizedBox(height: 20),
              // промо
              Container(
                height: 116,
                padding: const EdgeInsets.fromLTRB(18, 14, 18, 14),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(28),
                  gradient: const LinearGradient(
                      colors: [Color(0xFF2B1A10), Color(0xFF6B3A10)],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight),
                ),
                child: Stack(
                  children: [
                    const Positioned(
                      right: -16,
                      bottom: -26,
                      child: Icon(Icons.local_pizza_rounded,
                          size: 128, color: Color(0x33FFB27A)),
                    ),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Container(
                          padding:
                              const EdgeInsets.symmetric(horizontal: 9, vertical: 4),
                          decoration: BoxDecoration(
                              color: _orange, borderRadius: BorderRadius.circular(10)),
                          child: const Text('−40% ДО 23:00',
                              style: TextStyle(
                                  fontSize: 9.5,
                                  letterSpacing: 1,
                                  color: Colors.white,
                                  fontWeight: FontWeight.w800)),
                        ),
                        const Spacer(),
                        const Text('Вторая пицца\nв подарок',
                            style: TextStyle(
                                fontSize: 21,
                                color: Colors.white,
                                fontWeight: FontWeight.w800,
                                height: 1.15)),
                        const SizedBox(height: 4),
                        const Text('Пицца Фреш · 4,8 ★ · от 600 ₽',
                            style: TextStyle(fontSize: 11.5, color: Colors.white70)),
                      ],
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 16),
              Row(
                children: const [
                  Text('Популярное',
                      style: TextStyle(
                          fontSize: 19, fontWeight: FontWeight.w800, color: _ink)),
                  Spacer(),
                  Text('всё меню',
                      style: TextStyle(
                          fontSize: 12.5, color: _orange, fontWeight: FontWeight.w700)),
                ],
              ),
              const SizedBox(height: 12),
              const _Dish('Пепперони 30 см', 'Пикантная колбаса, моцарелла', '690',
                  Icons.local_pizza_rounded, Color(0xFFFFEBD6), Color(0xFFE2740B)),
              const _Dish('Филадельфия, 8 шт', 'Лосось, сыр, огурец', '540',
                  Icons.set_meal_rounded, Color(0xFFFFE4E4), Color(0xFFD63B3B)),
              const _Dish('Чизбургер XL', 'Говядина, чеддер, соус', '420',
                  Icons.lunch_dining_rounded, Color(0xFFFDF0D0), Color(0xFFB4860C)),
            ],
          ),
          // плашка корзины
          Positioned(
            left: 18,
            right: 18,
            bottom: 18,
            child: Container(
              height: 58,
              padding: const EdgeInsets.fromLTRB(8, 8, 18, 8),
              decoration: BoxDecoration(
                color: _ink,
                borderRadius: BorderRadius.circular(20),
                boxShadow: const [
                  BoxShadow(color: Color(0x3317120E), blurRadius: 20, offset: Offset(0, 8))
                ],
              ),
              child: Row(
                children: [
                  Container(
                    width: 42,
                    height: 42,
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                        color: _orange, borderRadius: BorderRadius.circular(14)),
                    child: const Text('3',
                        style: TextStyle(
                            fontSize: 16,
                            color: Colors.white,
                            fontWeight: FontWeight.w800)),
                  ),
                  const SizedBox(width: 12),
                  const Text('Корзина',
                      style: TextStyle(
                          fontSize: 15.5,
                          color: Colors.white,
                          fontWeight: FontWeight.w700)),
                  const Spacer(),
                  const Text('1 240 ₽',
                      style: TextStyle(
                          fontSize: 16,
                          color: Colors.white,
                          fontWeight: FontWeight.w800)),
                  const SizedBox(width: 6),
                  const Icon(Icons.arrow_forward_rounded, size: 18, color: _orange),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class _Cat extends StatelessWidget {
  const _Cat(this.label, this.icon, this.bg, this.fg);
  final String label;
  final IconData icon;
  final Color bg;
  final Color fg;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Container(
          width: 56,
          height: 56,
          decoration: BoxDecoration(color: bg, borderRadius: BorderRadius.circular(20)),
          child: Icon(icon, size: 27, color: fg),
        ),
        const SizedBox(height: 7),
        Text(label,
            style: const TextStyle(
                fontSize: 10.5, fontWeight: FontWeight.w700, color: _ink)),
      ],
    );
  }
}

class _Dish extends StatelessWidget {
  const _Dish(this.name, this.sub, this.price, this.icon, this.bg, this.fg);
  final String name;
  final String sub;
  final String price;
  final IconData icon;
  final Color bg;
  final Color fg;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 14),
      child: Row(
        children: [
          Stack(
            clipBehavior: Clip.none,
            children: [
              Container(
                width: 84,
                height: 84,
                decoration:
                    BoxDecoration(color: bg, borderRadius: BorderRadius.circular(22)),
                child: Icon(icon, size: 42, color: fg),
              ),
              Positioned(
                right: -8,
                bottom: -6,
                child: Container(
                  width: 30,
                  height: 30,
                  decoration: BoxDecoration(
                    color: _orange,
                    shape: BoxShape.circle,
                    border: Border.all(color: Colors.white, width: 2.5),
                  ),
                  child: const Icon(Icons.add_rounded, size: 17, color: Colors.white),
                ),
              ),
            ],
          ),
          const SizedBox(width: 18),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(name,
                    style: const TextStyle(
                        fontSize: 15, fontWeight: FontWeight.w800, color: _ink)),
                const SizedBox(height: 2),
                Text(sub, style: const TextStyle(fontSize: 11.5, color: _mute)),
                const SizedBox(height: 6),
                Text('$price ₽',
                    style: const TextStyle(
                        fontSize: 15, fontWeight: FontWeight.w800, color: _orange)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
