import 'dart:math';

import 'package:flutter/material.dart';

/// «Умный дом» — системный сгруппированный стиль: серый фон, белые блоки
/// со скруглением 14, капслок-заголовки секций, плитки заливаются цветом,
/// когда устройство включено, и классический таб-бар снизу.
const _bg = Color(0xFFF2F2F7);
const _ink = Color(0xFF111114);
const _grey = Color(0xFF8A8A8E);
const _sep = Color(0xFFE3E3E8);
const _blue = Color(0xFF3F6FD8);

class SmartHomeScreen extends StatelessWidget {
  const SmartHomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: _bg,
      body: Column(
        children: [
          Expanded(
            child: ListView(
              padding: const EdgeInsets.fromLTRB(16, 0, 16, 10),
              physics: const NeverScrollableScrollPhysics(),
              children: [
                SafeArea(
                  bottom: false,
                  child: Padding(
                    padding: const EdgeInsets.only(top: 8, bottom: 10),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.end,
                      children: [
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: const [
                            Text('Добрый вечер',
                                style: TextStyle(fontSize: 12.5, color: _grey)),
                            Text('Квартира',
                                style: TextStyle(
                                    fontSize: 30,
                                    fontWeight: FontWeight.w700,
                                    color: _ink,
                                    height: 1.1)),
                          ],
                        ),
                        const Spacer(),
                        const Icon(Icons.add_circle_outline_rounded, size: 24, color: _blue),
                        const SizedBox(width: 14),
                        const Icon(Icons.more_horiz_rounded, size: 24, color: _blue),
                      ],
                    ),
                  ),
                ),
                // сегменты комнат
                Container(
                  height: 32,
                  padding: const EdgeInsets.all(3),
                  decoration: BoxDecoration(
                      color: const Color(0xFFE6E6EB),
                      borderRadius: BorderRadius.circular(9)),
                  child: Row(
                    children: const [
                      _Seg('Все', active: true),
                      _Seg('Гостиная'),
                      _Seg('Кухня'),
                      _Seg('Спальня'),
                    ],
                  ),
                ),
                const SizedBox(height: 18),
                const _Caption('КЛИМАТ'),
                Container(
                  decoration: BoxDecoration(
                      color: Colors.white, borderRadius: BorderRadius.circular(14)),
                  padding: const EdgeInsets.fromLTRB(16, 14, 16, 16),
                  child: Column(
                    children: [
                      Row(
                        children: [
                          const Text('Отопление · Гостиная',
                              style: TextStyle(
                                  fontSize: 14.5, fontWeight: FontWeight.w600, color: _ink)),
                          const Spacer(),
                          Transform.scale(
                            scale: 0.8,
                            child: Switch(
                              value: true,
                              onChanged: null,
                              activeThumbColor: Colors.white,
                              activeTrackColor: const Color(0xFF34C759),
                            ),
                          ),
                        ],
                      ),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          const _Round(Icons.remove_rounded),
                          SizedBox(
                            width: 128,
                            height: 128,
                            child: Stack(
                              alignment: Alignment.center,
                              children: [
                                CustomPaint(
                                  size: const Size(128, 128),
                                  painter: _Dial(0.62),
                                ),
                                Column(
                                  mainAxisSize: MainAxisSize.min,
                                  children: const [
                                    Text('22°',
                                        style: TextStyle(
                                            fontSize: 40,
                                            fontWeight: FontWeight.w600,
                                            color: _ink,
                                            height: 1)),
                                    SizedBox(height: 2),
                                    Text('цель 23°',
                                        style: TextStyle(fontSize: 11.5, color: _grey)),
                                  ],
                                ),
                              ],
                            ),
                          ),
                          const _Round(Icons.add_rounded),
                        ],
                      ),
                      const SizedBox(height: 6),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: const [
                          _Mode('Авто', active: true),
                          SizedBox(width: 8),
                          _Mode('Эко'),
                          SizedBox(width: 8),
                          _Mode('Ночь'),
                        ],
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 18),
                const _Caption('УСТРОЙСТВА'),
                Row(
                  children: const [
                    _Device('Свет', 'Гостиная · 60%', Icons.lightbulb_rounded,
                        Color(0xFFFFB200), true),
                    SizedBox(width: 12),
                    _Device('Кондиционер', '20° · авто', Icons.ac_unit_rounded,
                        Color(0xFF32ADE6), true),
                  ],
                ),
                const SizedBox(height: 12),
                Row(
                  children: const [
                    _Device('Шторы', 'Закрыты', Icons.blinds_closed_rounded,
                        Color(0xFF9C6ADE), false),
                    SizedBox(width: 12),
                    _Device('Камера', 'Прихожая', Icons.videocam_rounded,
                        Color(0xFF34C759), true),
                  ],
                ),
                const SizedBox(height: 18),
                const _Caption('СЦЕНАРИИ'),
                Container(
                  decoration: BoxDecoration(
                      color: Colors.white, borderRadius: BorderRadius.circular(14)),
                  child: Column(
                    children: const [
                      _Row('Доброе утро', 'в 07:00, будни', Icons.wb_twilight_rounded,
                          Color(0xFFFF9500)),
                      _Row('Ухожу из дома', 'по геолокации', Icons.lock_outline_rounded,
                          Color(0xFF007AFF), last: true),
                    ],
                  ),
                ),
              ],
            ),
          ),
          // классический таб-бар
          Container(
            padding: const EdgeInsets.only(top: 6, bottom: 6),
            decoration: const BoxDecoration(
              color: Color(0xFFF9F9FB),
              border: Border(top: BorderSide(color: _sep)),
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: const [
                _Tab('Дом', Icons.home_rounded, active: true),
                _Tab('Комнаты', Icons.grid_view_rounded),
                _Tab('Сценарии', Icons.bolt_rounded),
                _Tab('Энергия', Icons.insights_rounded),
                _Tab('Ещё', Icons.more_horiz_rounded),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _Caption extends StatelessWidget {
  const _Caption(this.text);
  final String text;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(left: 4, bottom: 7),
      child: Text(text,
          style: const TextStyle(
              fontSize: 10.5, letterSpacing: 0.9, color: _grey, fontWeight: FontWeight.w600)),
    );
  }
}

class _Seg extends StatelessWidget {
  const _Seg(this.label, {this.active = false});
  final String label;
  final bool active;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Container(
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: active ? Colors.white : Colors.transparent,
          borderRadius: BorderRadius.circular(7),
          boxShadow: active
              ? const [BoxShadow(color: Color(0x1A000000), blurRadius: 3, offset: Offset(0, 1))]
              : null,
        ),
        child: Text(label,
            style: TextStyle(
                fontSize: 12.5,
                color: _ink,
                fontWeight: active ? FontWeight.w600 : FontWeight.w400)),
      ),
    );
  }
}

class _Round extends StatelessWidget {
  const _Round(this.icon);
  final IconData icon;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 40,
      height: 40,
      decoration: const BoxDecoration(color: Color(0xFFF2F2F7), shape: BoxShape.circle),
      child: Icon(icon, size: 21, color: _ink),
    );
  }
}

class _Mode extends StatelessWidget {
  const _Mode(this.label, {this.active = false});
  final String label;
  final bool active;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
      decoration: BoxDecoration(
        color: active ? const Color(0xFFFFF1D6) : const Color(0xFFF2F2F7),
        borderRadius: BorderRadius.circular(14),
      ),
      child: Text(label,
          style: TextStyle(
              fontSize: 12,
              color: active ? const Color(0xFFB37400) : _grey,
              fontWeight: FontWeight.w600)),
    );
  }
}

class _Device extends StatelessWidget {
  const _Device(this.name, this.sub, this.icon, this.color, this.on);
  final String name;
  final String sub;
  final IconData icon;
  final Color color;
  final bool on;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.all(14),
        decoration: BoxDecoration(
          color: on ? color : Colors.white,
          borderRadius: BorderRadius.circular(14),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(icon, size: 22, color: on ? Colors.white : _grey),
                const Spacer(),
                Transform.scale(
                  scale: 0.72,
                  child: Switch(
                    value: on,
                    onChanged: null,
                    activeThumbColor: Colors.white,
                    activeTrackColor: Colors.white.withValues(alpha: 0.45),
                    inactiveThumbColor: Colors.white,
                    inactiveTrackColor: const Color(0xFFE3E3E8),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
            Text(name,
                style: TextStyle(
                    fontSize: 14.5,
                    fontWeight: FontWeight.w600,
                    color: on ? Colors.white : _ink)),
            Text(sub,
                style: TextStyle(
                    fontSize: 11.5,
                    color: on ? Colors.white70 : _grey)),
          ],
        ),
      ),
    );
  }
}

class _Row extends StatelessWidget {
  const _Row(this.title, this.sub, this.icon, this.color, {this.last = false});
  final String title;
  final String sub;
  final IconData icon;
  final Color color;
  final bool last;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(14, 11, 14, 11),
      decoration: BoxDecoration(
        border: last ? null : const Border(bottom: BorderSide(color: _sep)),
      ),
      child: Row(
        children: [
          Container(
            width: 32,
            height: 32,
            decoration: BoxDecoration(color: color, borderRadius: BorderRadius.circular(9)),
            child: Icon(icon, size: 18, color: Colors.white),
          ),
          const SizedBox(width: 12),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(title,
                  style: const TextStyle(
                      fontSize: 14.5, fontWeight: FontWeight.w500, color: _ink)),
              Text(sub, style: const TextStyle(fontSize: 11.5, color: _grey)),
            ],
          ),
          const Spacer(),
          const Icon(Icons.chevron_right_rounded, size: 20, color: Color(0xFFC4C4C9)),
        ],
      ),
    );
  }
}

class _Tab extends StatelessWidget {
  const _Tab(this.label, this.icon, {this.active = false});
  final String label;
  final IconData icon;
  final bool active;

  @override
  Widget build(BuildContext context) {
    final c = active ? _blue : _grey;
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Icon(icon, size: 22, color: c),
        const SizedBox(height: 2),
        Text(label, style: TextStyle(fontSize: 9.5, color: c)),
      ],
    );
  }
}

class _Dial extends CustomPainter {
  _Dial(this.frac);
  final double frac;

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final radius = size.width / 2 - 12;
    const start = 135 * pi / 180;
    const sweep = 270 * pi / 180;
    for (var i = 0; i <= 44; i++) {
      final a = start + sweep * i / 44;
      final on = i / 44 <= frac;
      canvas.drawLine(
        center + Offset(cos(a), sin(a)) * radius,
        center + Offset(cos(a), sin(a)) * (radius - (on ? 14 : 9)),
        Paint()
          ..color = on
              ? Color.lerp(const Color(0xFFFFB200), const Color(0xFFFF5E3A), i / 44)!
              : const Color(0xFFE3E3E8)
          ..strokeWidth = 2.6
          ..strokeCap = StrokeCap.round,
      );
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}
