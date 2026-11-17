import 'package:flutter/material.dart';

import '../theme.dart';

/// «Пульс» — неоновые плитки на почти чёрном: крупная сетка блоков,
/// капслок-микроподписи, плавающий островок навигации.
const _bg = Color(0xFF07090F);
const _tile = Color(0xFF12161F);
const _lime = Color(0xFFC8FF4D);
const _cyan = Color(0xFF4DE2FF);
const _pink = Color(0xFFFF4D9A);
const _dim = Color(0xFF7A8296);

class FitnessScreen extends StatelessWidget {
  const FitnessScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: _bg,
      body: Stack(
        children: [
          ListView(
            padding: const EdgeInsets.fromLTRB(16, 0, 16, 96),
            physics: const NeverScrollableScrollPhysics(),
            children: [
              SafeArea(
                bottom: false,
                child: Padding(
                  padding: const EdgeInsets.only(top: 8, bottom: 14),
                  child: Row(
                    children: [
                      Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: const [
                          Text('СРЕДА, 29 ОКТЯБРЯ',
                              style: TextStyle(
                                  fontSize: 9, letterSpacing: 2.2, color: _dim)),
                          SizedBox(height: 3),
                          Text('Активность',
                              style: TextStyle(
                                  fontSize: 24,
                                  color: Colors.white,
                                  fontWeight: FontWeight.w700,
                                  height: 1)),
                        ],
                      ),
                      const Spacer(),
                      Container(
                        width: 38,
                        height: 38,
                        decoration: BoxDecoration(
                            color: _tile, borderRadius: BorderRadius.circular(13)),
                        child: const Icon(Icons.tune_rounded, size: 18, color: _dim),
                      ),
                    ],
                  ),
                ),
              ),
              // герой: кольца + две плитки
              SizedBox(
                height: 196,
                child: Row(
                  children: [
                    Expanded(
                      flex: 5,
                      child: Container(
                        padding: const EdgeInsets.all(14),
                        decoration: BoxDecoration(
                            color: _tile, borderRadius: BorderRadius.circular(26)),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const Text('ЦЕЛЬ ДНЯ',
                                style: TextStyle(
                                    fontSize: 9, letterSpacing: 2, color: _dim)),
                            const Spacer(),
                            Center(
                              child: SizedBox(
                                width: 110,
                                height: 110,
                                child: Stack(
                                  alignment: Alignment.center,
                                  children: [
                                    CustomPaint(
                                      size: const Size(110, 110),
                                      painter: RingPainter(const [
                                        (0.78, _lime),
                                        (0.62, _cyan),
                                        (0.45, _pink),
                                      ], trackColor: const Color(0xFF1C2230), stroke: 10),
                                    ),
                                    Column(
                                      mainAxisSize: MainAxisSize.min,
                                      children: const [
                                        Text('78',
                                            style: TextStyle(
                                                fontSize: 30,
                                                color: Colors.white,
                                                fontWeight: FontWeight.w700,
                                                height: 1)),
                                        Text('%',
                                            style: TextStyle(fontSize: 11, color: _dim)),
                                      ],
                                    ),
                                  ],
                                ),
                              ),
                            ),
                            const Spacer(),
                          ],
                        ),
                      ),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      flex: 4,
                      child: Column(
                        children: const [
                          Expanded(
                              child: _Tile(
                                  label: 'ШАГИ',
                                  value: '8 420',
                                  note: 'из 10 000',
                                  color: _lime,
                                  icon: Icons.directions_walk_rounded)),
                          SizedBox(height: 12),
                          Expanded(
                              child: _Tile(
                                  label: 'КАЛОРИИ',
                                  value: '620',
                                  note: 'из 800 ккал',
                                  color: _pink,
                                  icon: Icons.local_fire_department_rounded)),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 12),
              // неделя
              Container(
                padding: const EdgeInsets.fromLTRB(16, 14, 16, 10),
                decoration:
                    BoxDecoration(color: _tile, borderRadius: BorderRadius.circular(26)),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        const Text('НЕДЕЛЯ',
                            style:
                                TextStyle(fontSize: 9, letterSpacing: 2, color: _dim)),
                        const Spacer(),
                        Container(
                          padding:
                              const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                          decoration: BoxDecoration(
                              color: _lime.withValues(alpha: 0.16),
                              borderRadius: BorderRadius.circular(8)),
                          child: const Text('+12%',
                              style: TextStyle(
                                  fontSize: 10,
                                  color: _lime,
                                  fontWeight: FontWeight.w700)),
                        ),
                      ],
                    ),
                    const SizedBox(height: 12),
                    Row(
                      crossAxisAlignment: CrossAxisAlignment.end,
                      children: [
                        for (final (v, d, hi) in [
                          (0.55, 'пн', false),
                          (0.7, 'вт', false),
                          (0.44, 'ср', false),
                          (0.92, 'чт', false),
                          (0.82, 'пт', false),
                          (0.38, 'сб', false),
                          (0.82, 'вс', true),
                        ])
                          Expanded(
                            child: Column(
                              children: [
                                Container(
                                  height: 72 * v,
                                  margin: const EdgeInsets.symmetric(horizontal: 5),
                                  decoration: BoxDecoration(
                                    color: hi ? _lime : const Color(0xFF232B3B),
                                    borderRadius: BorderRadius.circular(8),
                                  ),
                                ),
                                const SizedBox(height: 7),
                                Text(d,
                                    style: TextStyle(
                                        fontSize: 10,
                                        color: hi ? Colors.white : _dim,
                                        fontWeight:
                                            hi ? FontWeight.w700 : FontWeight.w400)),
                              ],
                            ),
                          ),
                      ],
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 12),
              Row(
                children: [
                  Expanded(
                    child: Container(
                      height: 118,
                      padding: const EdgeInsets.all(14),
                      decoration: BoxDecoration(
                          color: _tile, borderRadius: BorderRadius.circular(26)),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          const Text('ПУЛЬС',
                              style:
                                  TextStyle(fontSize: 9, letterSpacing: 2, color: _dim)),
                          const SizedBox(height: 6),
                          Row(
                            crossAxisAlignment: CrossAxisAlignment.end,
                            children: const [
                              Text('72',
                                  style: TextStyle(
                                      fontSize: 28,
                                      color: Colors.white,
                                      fontWeight: FontWeight.w700,
                                      height: 1)),
                              SizedBox(width: 4),
                              Padding(
                                padding: EdgeInsets.only(bottom: 2),
                                child: Text('уд/мин',
                                    style: TextStyle(fontSize: 10, color: _dim)),
                              ),
                            ],
                          ),
                          const Spacer(),
                          CustomPaint(
                            size: const Size(double.infinity, 28),
                            painter: SparkPainter(
                                const [68, 74, 71, 88, 76, 70, 72], _pink),
                          ),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(width: 12),
                  const Expanded(
                    child: _Tile(
                      label: 'СОН',
                      value: '7:20',
                      note: 'норма 8:00',
                      color: _cyan,
                      icon: Icons.nightlight_round,
                      height: 118,
                      big: true,
                    ),
                  ),
                ],
              ),
            ],
          ),
          // островок навигации
          Positioned(
            left: 54,
            right: 54,
            bottom: 20,
            child: Container(
              height: 58,
              decoration: BoxDecoration(
                  color: _tile, borderRadius: BorderRadius.circular(29)),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Container(
                    width: 42,
                    height: 42,
                    decoration: const BoxDecoration(color: _lime, shape: BoxShape.circle),
                    child: const Icon(Icons.show_chart_rounded, size: 20, color: _bg),
                  ),
                  const Icon(Icons.fitness_center_rounded, size: 21, color: _dim),
                  const Icon(Icons.restaurant_rounded, size: 21, color: _dim),
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

class _Tile extends StatelessWidget {
  const _Tile({
    required this.label,
    required this.value,
    required this.note,
    required this.color,
    required this.icon,
    this.height,
    this.big = false,
  });

  final String label;
  final String value;
  final String note;
  final Color color;
  final IconData icon;
  final double? height;
  final bool big;

  @override
  Widget build(BuildContext context) {
    return Container(
      height: height,
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(color: _tile, borderRadius: BorderRadius.circular(26)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Text(label,
                  style: const TextStyle(fontSize: 9, letterSpacing: 2, color: _dim)),
              const Spacer(),
              Icon(icon, size: 15, color: color),
            ],
          ),
          const Spacer(),
          Text(value,
              style: TextStyle(
                  fontSize: big ? 28 : 22,
                  color: Colors.white,
                  fontWeight: FontWeight.w700,
                  height: 1)),
          const SizedBox(height: 2),
          Text(note, style: const TextStyle(fontSize: 10, color: _dim)),
        ],
      ),
    );
  }
}
