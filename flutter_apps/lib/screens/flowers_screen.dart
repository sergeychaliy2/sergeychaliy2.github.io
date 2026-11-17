import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

/// «Флора» — бутиковая вёрстка: витрина-лукбук, засечный заголовок,
/// тонкие линейки вместо карточек, почти квадратные углы.
const _ink = Color(0xFF2A2420);
const _rose = Color(0xFFA3374F);
const _cream = Color(0xFFFBF7F3);
const _hair = Color(0xFFE4DCD3);

class FlowersScreen extends StatelessWidget {
  const FlowersScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: _cream,
      body: Stack(
        children: [
          ListView(
            padding: EdgeInsets.zero,
            physics: const NeverScrollableScrollPhysics(),
            children: [
              // обложка
              SizedBox(
                height: 194,
                child: Stack(
                  fit: StackFit.expand,
                  children: [
                    Container(
                      decoration: const BoxDecoration(
                        gradient: LinearGradient(
                          colors: [Color(0xFFE8C9CF), Color(0xFFC98E9B)],
                          begin: Alignment.topLeft,
                          end: Alignment.bottomRight,
                        ),
                      ),
                    ),
                    const Positioned(
                      right: -28,
                      top: 24,
                      child: Icon(Icons.local_florist_rounded,
                          size: 196, color: Color(0x33FFFFFF)),
                    ),
                    SafeArea(
                      child: Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 20),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Row(
                              children: [
                                const Icon(Icons.menu_rounded, color: Colors.white, size: 22),
                                const Spacer(),
                                Text('ФЛОРА',
                                    style: GoogleFonts.playfairDisplay(
                                        fontSize: 17,
                                        letterSpacing: 6,
                                        color: Colors.white,
                                        fontWeight: FontWeight.w600)),
                                const Spacer(),
                                const Icon(Icons.search_rounded, color: Colors.white, size: 22),
                              ],
                            ),
                            const Spacer(),
                            Text('Букеты,\nсобранные сегодня',
                                style: GoogleFonts.playfairDisplay(
                                    fontSize: 27,
                                    height: 1.2,
                                    color: Colors.white,
                                    fontWeight: FontWeight.w600)),
                            const SizedBox(height: 8),
                            Row(
                              children: [
                                Container(width: 22, height: 1, color: Colors.white70),
                                const SizedBox(width: 8),
                                const Text('ДОСТАВКА ЗА 2 ЧАСА ПО МОСКВЕ',
                                    style: TextStyle(
                                        fontSize: 9,
                                        letterSpacing: 1.6,
                                        color: Colors.white)),
                              ],
                            ),
                            const SizedBox(height: 18),
                          ],
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              // разделы — текстовые ссылки, без пилюль
              Padding(
                padding: const EdgeInsets.fromLTRB(20, 18, 20, 0),
                child: Row(
                  children: const [
                    _Tab('Все', active: true),
                    _Tab('Пионы'),
                    _Tab('Розы'),
                    _Tab('Авторские'),
                    _Tab('Сухоцветы'),
                  ],
                ),
              ),
              const SizedBox(height: 14),
              const Divider(height: 1, thickness: 1, color: _hair),
              // витрина
              Padding(
                padding: const EdgeInsets.fromLTRB(20, 16, 20, 0),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: const [
                    Expanded(
                      child: _Item(
                        name: 'Нежность',
                        sub: '15 пионов · ваза',
                        price: '4 290',
                        colors: [Color(0xFFF6E3EA), Color(0xFFE3C3CE)],
                        icon: Color(0xFFC98E9B),
                        tall: true,
                        liked: true,
                      ),
                    ),
                    SizedBox(width: 14),
                    Expanded(
                      child: _Item(
                        name: 'Рассвет',
                        sub: '25 роз',
                        price: '5 150',
                        colors: [Color(0xFFF7E6DC), Color(0xFFE6C3AE)],
                        icon: Color(0xFFCE7F52),
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 18),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: const [
                    Expanded(
                      child: _Item(
                        name: 'Лавандовый',
                        sub: 'Авторский',
                        price: '3 780',
                        colors: [Color(0xFFEAE4F5), Color(0xFFCFC2E6)],
                        icon: Color(0xFF8A6AD0),
                      ),
                    ),
                    SizedBox(width: 14),
                    Expanded(
                      child: _Item(
                        name: 'Солнечный',
                        sub: '19 гербер',
                        price: '4 650',
                        colors: [Color(0xFFFBF0D8), Color(0xFFEBD39A)],
                        icon: Color(0xFFC79A2E),
                        tall: true,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
          // нижняя строка заказа
          Positioned(
            left: 0,
            right: 0,
            bottom: 0,
            child: Container(
              padding: const EdgeInsets.fromLTRB(20, 14, 20, 18),
              decoration: const BoxDecoration(
                color: _cream,
                border: Border(top: BorderSide(color: _hair)),
              ),
              child: Row(
                children: [
                  Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text('В КОРЗИНЕ · 2 БУКЕТА',
                          style: TextStyle(
                              fontSize: 9, letterSpacing: 1.4, color: Color(0xFF9A8E84))),
                      const SizedBox(height: 2),
                      Text('8 470 ₽',
                          style: GoogleFonts.playfairDisplay(
                              fontSize: 22, fontWeight: FontWeight.w600, color: _ink)),
                    ],
                  ),
                  const Spacer(),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 22, vertical: 13),
                    decoration: BoxDecoration(
                        color: _rose, borderRadius: BorderRadius.circular(3)),
                    child: const Text('ОФОРМИТЬ',
                        style: TextStyle(
                            fontSize: 11,
                            letterSpacing: 1.8,
                            color: Colors.white,
                            fontWeight: FontWeight.w600)),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class _Tab extends StatelessWidget {
  const _Tab(this.label, {this.active = false});
  final String label;
  final bool active;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(right: 18),
      child: Column(
        children: [
          Text(label,
              style: TextStyle(
                  fontSize: 12.5,
                  letterSpacing: 0.3,
                  color: active ? _ink : const Color(0xFF9A8E84),
                  fontWeight: active ? FontWeight.w700 : FontWeight.w500)),
          const SizedBox(height: 5),
          Container(height: 1.6, width: active ? 18 : 0, color: _rose),
        ],
      ),
    );
  }
}

class _Item extends StatelessWidget {
  const _Item({
    required this.name,
    required this.sub,
    required this.price,
    required this.colors,
    required this.icon,
    this.tall = false,
    this.liked = false,
  });

  final String name;
  final String sub;
  final String price;
  final List<Color> colors;
  final Color icon;
  final bool tall;
  final bool liked;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Stack(
          children: [
            Container(
              height: tall ? 162 : 140,
              decoration: BoxDecoration(
                gradient: LinearGradient(
                    colors: colors, begin: Alignment.topLeft, end: Alignment.bottomRight),
                borderRadius: BorderRadius.circular(2),
              ),
              child: Icon(Icons.local_florist_rounded, size: tall ? 78 : 66, color: icon),
            ),
            Positioned(
              right: 8,
              top: 8,
              child: Icon(liked ? Icons.favorite : Icons.favorite_border,
                  size: 17, color: liked ? _rose : Colors.white),
            ),
          ],
        ),
        const SizedBox(height: 9),
        Text(name,
            style: GoogleFonts.playfairDisplay(
                fontSize: 16, fontWeight: FontWeight.w600, color: _ink)),
        const SizedBox(height: 2),
        Text(sub.toUpperCase(),
            style: const TextStyle(
                fontSize: 8.5, letterSpacing: 1.2, color: Color(0xFF9A8E84))),
        const SizedBox(height: 6),
        Row(
          children: [
            Text('$price ₽',
                style: const TextStyle(
                    fontSize: 13.5, fontWeight: FontWeight.w700, color: _ink)),
            const Spacer(),
            Container(
              width: 26,
              height: 26,
              decoration: BoxDecoration(
                border: Border.all(color: _ink, width: 1),
                borderRadius: BorderRadius.circular(2),
              ),
              child: const Icon(Icons.add_rounded, size: 15, color: _ink),
            ),
          ],
        ),
      ],
    );
  }
}
