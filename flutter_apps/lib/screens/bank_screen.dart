import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

/// «Капитал» — премиальный тёмный банк: глубокий синий, золотые акценты,
/// карусель карт, волосяные линии вместо карточек, плавающая пилюля навигации.
const _bg = Color(0xFF0D1330);
const _surface = Color(0xFF151C3D);
const _gold = Color(0xFFD8B25F);
const _dim = Color(0xFF8891B5);
const _hair = Color(0xFF232B52);

class BankScreen extends StatelessWidget {
  const BankScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: _bg,
      body: Stack(
        children: [
          ListView(
            padding: const EdgeInsets.only(bottom: 90),
            physics: const NeverScrollableScrollPhysics(),
            children: [
              SafeArea(
                bottom: false,
                child: Padding(
                  padding: const EdgeInsets.fromLTRB(18, 10, 18, 0),
                  child: Row(
                    children: [
                      Container(
                        width: 34,
                        height: 34,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          border: Border.all(color: _gold, width: 1),
                        ),
                        child: Center(
                          child: Text('СВ',
                              style: GoogleFonts.montserrat(
                                  fontSize: 11,
                                  color: _gold,
                                  fontWeight: FontWeight.w700)),
                        ),
                      ),
                      const SizedBox(width: 10),
                      Text('КАПИТАЛ',
                          style: GoogleFonts.montserrat(
                              fontSize: 13,
                              letterSpacing: 3.2,
                              color: Colors.white,
                              fontWeight: FontWeight.w600)),
                      const Spacer(),
                      const Icon(Icons.notifications_none_rounded,
                          size: 21, color: _dim),
                      const SizedBox(width: 16),
                      const Icon(Icons.qr_code_scanner_rounded, size: 21, color: _dim),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.only(left: 18),
                child: Text('ДОСТУПНО',
                    style: GoogleFonts.montserrat(
                        fontSize: 9.5, letterSpacing: 2, color: _dim)),
              ),
              const SizedBox(height: 6),
              Padding(
                padding: const EdgeInsets.only(left: 18),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.end,
                  children: [
                    Text('124 350',
                        style: GoogleFonts.montserrat(
                            fontSize: 38,
                            color: Colors.white,
                            fontWeight: FontWeight.w300,
                            height: 1)),
                    Text(',20 ₽',
                        style: GoogleFonts.montserrat(
                            fontSize: 20, color: _dim, fontWeight: FontWeight.w300)),
                  ],
                ),
              ),
              const SizedBox(height: 14),
              // карусель карт
              SizedBox(
                height: 112,
                child: ListView(
                  scrollDirection: Axis.horizontal,
                  padding: const EdgeInsets.symmetric(horizontal: 18),
                  physics: const NeverScrollableScrollPhysics(),
                  children: [
                    _Card(
                      title: 'Премиальная',
                      number: '•••• 4821',
                      value: '124 350,20 ₽',
                      gradient: const [Color(0xFF1E2A5E), Color(0xFF101737)],
                      accent: _gold,
                    ),
                    const SizedBox(width: 12),
                    _Card(
                      title: 'Накопительный',
                      number: '7,5% годовых',
                      value: '318 400,00 ₽',
                      gradient: const [Color(0xFF2A2140), Color(0xFF15102A)],
                      accent: const Color(0xFFB08BFF),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 16),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 18),
                child: Row(
                  children: const [
                    _Act('Перевод', Icons.north_east_rounded),
                    _Act('Пополнить', Icons.south_west_rounded),
                    _Act('Платежи', Icons.receipt_long_outlined),
                    _Act('Обмен', Icons.currency_exchange_rounded),
                  ],
                ),
              ),
              const SizedBox(height: 22),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 18),
                child: Row(
                  children: [
                    Text('РАСХОДЫ',
                        style: GoogleFonts.montserrat(
                            fontSize: 9.5, letterSpacing: 2, color: _dim)),
                    const Spacer(),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 3, vertical: 3),
                      decoration: BoxDecoration(
                          color: _surface, borderRadius: BorderRadius.circular(8)),
                      child: Row(
                        children: const [
                          _Seg('Нед'),
                          _Seg('Мес', active: true),
                          _Seg('Год'),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 14),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 18),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.end,
                  children: [
                    for (final (v, m, hi) in [
                      (0.45, 'июн', false),
                      (0.62, 'июл', false),
                      (0.38, 'авг', false),
                      (0.72, 'сен', false),
                      (0.95, 'окт', true),
                      (0.5, 'ноя', false),
                    ])
                      Expanded(
                        child: Column(
                          children: [
                            if (hi)
                              Text('48 200',
                                  style: GoogleFonts.montserrat(
                                      fontSize: 10,
                                      color: _gold,
                                      fontWeight: FontWeight.w700)),
                            const SizedBox(height: 4),
                            Container(
                              height: 54 * v,
                              margin: const EdgeInsets.symmetric(horizontal: 6),
                              decoration: BoxDecoration(
                                color: hi ? _gold : _hair,
                                borderRadius: BorderRadius.circular(3),
                              ),
                            ),
                            const SizedBox(height: 6),
                            Text(m,
                                style: GoogleFonts.montserrat(fontSize: 9.5, color: _dim)),
                          ],
                        ),
                      ),
                  ],
                ),
              ),
              const SizedBox(height: 18),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 18),
                child: Row(
                  children: [
                    Text('ПОСЛЕДНИЕ ОПЕРАЦИИ',
                        style: GoogleFonts.montserrat(
                            fontSize: 9.5, letterSpacing: 2, color: _dim)),
                    const Spacer(),
                    Text('все',
                        style: GoogleFonts.montserrat(fontSize: 11, color: _gold)),
                  ],
                ),
              ),
              const SizedBox(height: 6),
              const _Op('Пятёрочка', 'Продукты', '−840,00', Icons.shopping_basket_outlined),
              const _Op('Поехали Такси', 'Транспорт', '−310,00', Icons.local_taxi_rounded),
              const _Op('ООО «Ромашка»', 'Зарплата', '+95 000,00',
                  Icons.account_balance_rounded,
                  plus: true),
            ],
          ),
          // плавающая навигация
          Positioned(
            left: 60,
            right: 60,
            bottom: 18,
            child: Container(
              height: 56,
              decoration: BoxDecoration(
                color: _surface,
                borderRadius: BorderRadius.circular(28),
                border: Border.all(color: _hair),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Container(
                    width: 38,
                    height: 38,
                    decoration: BoxDecoration(
                        color: _gold, borderRadius: BorderRadius.circular(19)),
                    child: const Icon(Icons.pie_chart_rounded, size: 19, color: _bg),
                  ),
                  const Icon(Icons.credit_card_rounded, size: 21, color: _dim),
                  const Icon(Icons.swap_horiz_rounded, size: 21, color: _dim),
                  const Icon(Icons.person_outline_rounded, size: 21, color: _dim),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class _Card extends StatelessWidget {
  const _Card({
    required this.title,
    required this.number,
    required this.value,
    required this.gradient,
    required this.accent,
  });

  final String title;
  final String number;
  final String value;
  final List<Color> gradient;
  final Color accent;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 246,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        gradient: LinearGradient(
            colors: gradient, begin: Alignment.topLeft, end: Alignment.bottomRight),
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: accent.withValues(alpha: 0.35)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Text(title.toUpperCase(),
                  style: GoogleFonts.montserrat(
                      fontSize: 9, letterSpacing: 1.6, color: accent)),
              const Spacer(),
              Container(
                width: 26,
                height: 18,
                decoration: BoxDecoration(
                    color: accent.withValues(alpha: 0.22),
                    borderRadius: BorderRadius.circular(3)),
              ),
            ],
          ),
          const Spacer(),
          Text(value,
              style: GoogleFonts.montserrat(
                  fontSize: 19, color: Colors.white, fontWeight: FontWeight.w500)),
          const SizedBox(height: 4),
          Text(number,
              style: GoogleFonts.montserrat(fontSize: 11.5, color: _dim)),
        ],
      ),
    );
  }
}

class _Act extends StatelessWidget {
  const _Act(this.label, this.icon);
  final String label;
  final IconData icon;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Column(
        children: [
          Container(
            width: 46,
            height: 46,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              border: Border.all(color: _hair),
            ),
            child: Icon(icon, size: 19, color: Colors.white),
          ),
          const SizedBox(height: 7),
          Text(label,
              style: GoogleFonts.montserrat(fontSize: 10, color: _dim)),
        ],
      ),
    );
  }
}

class _Seg extends StatelessWidget {
  const _Seg(this.label, {this.active = false});
  final String label;
  final bool active;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 11, vertical: 5),
      decoration: BoxDecoration(
        color: active ? _gold : Colors.transparent,
        borderRadius: BorderRadius.circular(6),
      ),
      child: Text(label,
          style: GoogleFonts.montserrat(
              fontSize: 10.5,
              color: active ? _bg : _dim,
              fontWeight: FontWeight.w600)),
    );
  }
}

class _Op extends StatelessWidget {
  const _Op(this.name, this.cat, this.value, this.icon, {this.plus = false});
  final String name;
  final String cat;
  final String value;
  final IconData icon;
  final bool plus;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(18, 13, 18, 13),
      decoration: const BoxDecoration(
        border: Border(bottom: BorderSide(color: _hair)),
      ),
      child: Row(
        children: [
          Icon(icon, size: 19, color: _dim),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(name,
                    style: GoogleFonts.montserrat(
                        fontSize: 13.5, color: Colors.white, fontWeight: FontWeight.w500)),
                Text(cat, style: GoogleFonts.montserrat(fontSize: 10.5, color: _dim)),
              ],
            ),
          ),
          Text('$value ₽',
              style: GoogleFonts.montserrat(
                  fontSize: 13.5,
                  color: plus ? const Color(0xFF6FE39A) : Colors.white,
                  fontWeight: FontWeight.w600)),
        ],
      ),
    );
  }
}
