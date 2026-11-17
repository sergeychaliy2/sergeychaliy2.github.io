import 'dart:math';

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

/// «Поехали» — ночная карта: тёмный интерфейс, крупная геометричная
/// типографика, тарифы горизонтальным рядом, широкая кнопка с малым радиусом.
const _lime = Color(0xFFD6FF4B);
const _panel = Color(0xFF15181F);
const _panel2 = Color(0xFF1E232D);
const _dim = Color(0xFF8A93A6);

class TaxiScreen extends StatelessWidget {
  const TaxiScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0E1116),
      body: Stack(
        children: [
          Positioned.fill(child: CustomPaint(painter: _NightMap())),
          // метки
          const Positioned(
            left: 62,
            top: 276,
            child: Icon(Icons.trip_origin, size: 20, color: _lime),
          ),
          const Positioned(
            left: 286,
            top: 150,
            child: Icon(Icons.place_rounded, size: 30, color: Color(0xFFFF5C5C)),
          ),
          Positioned(
            left: 178,
            top: 222,
            child: Container(
              padding: const EdgeInsets.all(6),
              decoration: BoxDecoration(
                  color: _lime, borderRadius: BorderRadius.circular(8)),
              child: const Icon(Icons.local_taxi_rounded, size: 17, color: Color(0xFF11141A)),
            ),
          ),
          // верхние кнопки и адреса
          SafeArea(
            bottom: false,
            child: Padding(
              padding: const EdgeInsets.fromLTRB(14, 10, 14, 0),
              child: Column(
                children: [
                  Row(
                    children: [
                      _Square(Icons.menu_rounded),
                      const Spacer(),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 7),
                        decoration: BoxDecoration(
                            color: _panel, borderRadius: BorderRadius.circular(10)),
                        child: Row(
                          children: [
                            const Icon(Icons.bolt_rounded, size: 15, color: _lime),
                            const SizedBox(width: 5),
                            Text('Спрос обычный',
                                style: GoogleFonts.manrope(
                                    fontSize: 11.5,
                                    color: Colors.white,
                                    fontWeight: FontWeight.w600)),
                          ],
                        ),
                      ),
                      const Spacer(),
                      _Square(Icons.my_location_rounded),
                    ],
                  ),
                  const SizedBox(height: 12),
                  Container(
                    padding: const EdgeInsets.fromLTRB(14, 12, 12, 12),
                    decoration: BoxDecoration(
                        color: _panel, borderRadius: BorderRadius.circular(16)),
                    child: Row(
                      children: [
                        Column(
                          children: [
                            Container(
                                width: 8,
                                height: 8,
                                decoration: const BoxDecoration(
                                    color: _lime, shape: BoxShape.circle)),
                            Container(width: 1.4, height: 26, color: const Color(0xFF39404E)),
                            Container(
                                width: 8,
                                height: 8,
                                decoration: const BoxDecoration(
                                    color: Color(0xFFFF5C5C), shape: BoxShape.circle)),
                          ],
                        ),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text('ул. Ленина, 14',
                                  style: GoogleFonts.manrope(
                                      fontSize: 14.5,
                                      color: Colors.white,
                                      fontWeight: FontWeight.w700)),
                              const SizedBox(height: 10),
                              Text('Шереметьево, терминал B',
                                  style: GoogleFonts.manrope(
                                      fontSize: 14.5,
                                      color: Colors.white,
                                      fontWeight: FontWeight.w700)),
                            ],
                          ),
                        ),
                        const Icon(Icons.swap_vert_rounded, size: 20, color: _dim),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
          // шторка
          Positioned(
            left: 0,
            right: 0,
            bottom: 0,
            child: Container(
              padding: const EdgeInsets.fromLTRB(14, 12, 14, 16),
              decoration: const BoxDecoration(
                color: _panel,
                borderRadius: BorderRadius.vertical(top: Radius.circular(28)),
              ),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Container(
                    width: 38,
                    height: 4,
                    decoration: BoxDecoration(
                        color: const Color(0xFF39404E),
                        borderRadius: BorderRadius.circular(2)),
                  ),
                  const SizedBox(height: 16),
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.end,
                    children: [
                      Text('Комфорт',
                          style: GoogleFonts.manrope(
                              fontSize: 26,
                              color: Colors.white,
                              fontWeight: FontWeight.w800,
                              height: 1)),
                      const SizedBox(width: 10),
                      Padding(
                        padding: const EdgeInsets.only(bottom: 3),
                        child: Text('через 3 мин',
                            style: GoogleFonts.manrope(fontSize: 12.5, color: _dim)),
                      ),
                      const Spacer(),
                      Text('610 ₽',
                          style: GoogleFonts.manrope(
                              fontSize: 26,
                              color: _lime,
                              fontWeight: FontWeight.w800,
                              height: 1)),
                    ],
                  ),
                  const SizedBox(height: 14),
                  Row(
                    children: const [
                      _Tariff('Эконом', '420 ₽', Icons.directions_car_filled_rounded),
                      SizedBox(width: 8),
                      _Tariff('Комфорт', '610 ₽', Icons.local_taxi_rounded, active: true),
                      SizedBox(width: 8),
                      _Tariff('Бизнес', '980 ₽', Icons.airport_shuttle_rounded),
                    ],
                  ),
                  const SizedBox(height: 14),
                  Row(
                    children: [
                      _Chip(Icons.credit_card_rounded, '•••• 4821'),
                      const SizedBox(width: 8),
                      _Chip(Icons.local_offer_outlined, 'Промокод'),
                      const Spacer(),
                      Text('4 мин · 2,8 км',
                          style: GoogleFonts.manrope(fontSize: 12, color: _dim)),
                    ],
                  ),
                  const SizedBox(height: 14),
                  Container(
                    height: 54,
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                        color: _lime, borderRadius: BorderRadius.circular(14)),
                    child: Text('Заказать',
                        style: GoogleFonts.manrope(
                            fontSize: 17,
                            color: const Color(0xFF11141A),
                            fontWeight: FontWeight.w800)),
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

class _Square extends StatelessWidget {
  const _Square(this.icon);
  final IconData icon;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 40,
      height: 40,
      decoration: BoxDecoration(color: _panel, borderRadius: BorderRadius.circular(12)),
      child: Icon(icon, size: 20, color: Colors.white),
    );
  }
}

class _Chip extends StatelessWidget {
  const _Chip(this.icon, this.label);
  final IconData icon;
  final String label;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 7),
      decoration: BoxDecoration(color: _panel2, borderRadius: BorderRadius.circular(10)),
      child: Row(
        children: [
          Icon(icon, size: 14, color: _dim),
          const SizedBox(width: 6),
          Text(label,
              style: GoogleFonts.manrope(
                  fontSize: 11.5, color: Colors.white, fontWeight: FontWeight.w600)),
        ],
      ),
    );
  }
}

class _Tariff extends StatelessWidget {
  const _Tariff(this.name, this.price, this.icon, {this.active = false});
  final String name;
  final String price;
  final IconData icon;
  final bool active;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 10),
        decoration: BoxDecoration(
          color: active ? _lime.withValues(alpha: 0.14) : _panel2,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(color: active ? _lime : Colors.transparent, width: 1.4),
        ),
        child: Column(
          children: [
            Icon(icon, size: 22, color: active ? _lime : _dim),
            const SizedBox(height: 6),
            Text(name,
                style: GoogleFonts.manrope(
                    fontSize: 11.5,
                    color: active ? Colors.white : _dim,
                    fontWeight: FontWeight.w700)),
            Text(price,
                style: GoogleFonts.manrope(
                    fontSize: 12.5,
                    color: active ? _lime : Colors.white,
                    fontWeight: FontWeight.w800)),
          ],
        ),
      ),
    );
  }
}

class _NightMap extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    canvas.drawRect(Offset.zero & size, Paint()..color = const Color(0xFF0E1116));
    final rnd = Random(5);
    final block = Paint()..color = const Color(0xFF171B23);
    for (var i = 0; i < 30; i++) {
      final w = 26.0 + rnd.nextDouble() * 36;
      final h = 24.0 + rnd.nextDouble() * 32;
      final x = rnd.nextDouble() * (size.width - w);
      final y = rnd.nextDouble() * (size.height * 0.74 - h);
      canvas.drawRRect(
          RRect.fromRectAndRadius(Rect.fromLTWH(x, y, w, h), const Radius.circular(4)), block);
    }
    final park = Paint()..color = const Color(0xFF13241B);
    canvas.drawRRect(
        RRect.fromRectAndRadius(
            Rect.fromLTWH(8, 30, 96, 72), const Radius.circular(22)), park);
    canvas.drawRRect(
        RRect.fromRectAndRadius(
            Rect.fromLTWH(size.width - 112, size.height * 0.46, 116, 80),
            const Radius.circular(26)),
        park);
    canvas.drawPath(
        Path()
          ..moveTo(size.width, 46)
          ..quadraticBezierTo(size.width * 0.68, 124, size.width * 0.64, 232)
          ..quadraticBezierTo(size.width * 0.6, 318, size.width * 0.32, 372),
        Paint()
          ..color = const Color(0xFF13202E)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 18
          ..strokeCap = StrokeCap.round);
    final road = Paint()
      ..color = const Color(0xFF232935)
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round;
    for (final (p1, p2, w) in [
      (const Offset(-10, 118), Offset(size.width + 10, 118), 13.0),
      (const Offset(-10, 266), Offset(size.width + 10, 266), 15.0),
      (const Offset(104, -10), Offset(104, size.height * 0.8), 14.0),
      (const Offset(258, -10), Offset(258, size.height * 0.8), 11.0),
    ]) {
      canvas.drawLine(p1, p2, road..strokeWidth = w);
    }
    final route = Path()
      ..moveTo(72, 286)
      ..lineTo(72, 266)
      ..lineTo(196, 266)
      ..lineTo(196, 196)
      ..lineTo(300, 196)
      ..lineTo(300, 180);
    canvas.drawPath(
        route,
        Paint()
          ..color = _lime.withValues(alpha: 0.22)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 12
          ..strokeJoin = StrokeJoin.round
          ..strokeCap = StrokeCap.round);
    canvas.drawPath(
        route,
        Paint()
          ..color = _lime
          ..style = PaintingStyle.stroke
          ..strokeWidth = 4.5
          ..strokeJoin = StrokeJoin.round
          ..strokeCap = StrokeCap.round);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}
