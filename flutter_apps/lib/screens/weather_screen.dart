import 'package:flutter/material.dart';

/// «Погода» — иммерсивный экран без карточек: контент лежит прямо на градиенте,
/// разделители — волосяные линии, сверхтонкая крупная температура.
const _line = Color(0x33FFFFFF);

class WeatherScreen extends StatelessWidget {
  const WeatherScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Color(0xFF1B2A74), Color(0xFF5C4C9E), Color(0xFFD98E6B)],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            stops: [0, 0.55, 1],
          ),
        ),
        child: SafeArea(
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const SizedBox(height: 6),
                Row(
                  children: const [
                    Text('МОСКВА',
                        style: TextStyle(
                            fontSize: 13,
                            letterSpacing: 4,
                            color: Colors.white,
                            fontWeight: FontWeight.w600)),
                    SizedBox(width: 4),
                    Icon(Icons.keyboard_arrow_down_rounded, size: 18, color: Colors.white70),
                    Spacer(),
                    Icon(Icons.format_list_bulleted_rounded, size: 19, color: Colors.white70),
                  ],
                ),
                const SizedBox(height: 26),
                Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: const [
                    Text('18',
                        style: TextStyle(
                            fontSize: 104,
                            height: 0.92,
                            color: Colors.white,
                            fontWeight: FontWeight.w100)),
                    Text('°',
                        style: TextStyle(
                            fontSize: 52, color: Colors.white54, fontWeight: FontWeight.w100)),
                  ],
                ),
                const SizedBox(height: 2),
                const Text('Малооблачно',
                    style: TextStyle(
                        fontSize: 17, color: Colors.white, fontWeight: FontWeight.w500)),
                const SizedBox(height: 4),
                const Text('Ощущается как 16°   ·   днём 22°   ·   ночью 11°',
                    style: TextStyle(fontSize: 12, color: Colors.white70)),
                const SizedBox(height: 22),
                const Divider(height: 1, color: _line),
                SizedBox(
                  height: 92,
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: const [
                      _Hour('сейчас', Icons.wb_sunny_rounded, '18°', now: true),
                      _Hour('15', Icons.wb_sunny_rounded, '19°'),
                      _Hour('16', Icons.wb_cloudy_rounded, '19°'),
                      _Hour('17', Icons.wb_cloudy_rounded, '17°'),
                      _Hour('18', Icons.cloud_rounded, '15°'),
                      _Hour('19', Icons.grain_rounded, '13°'),
                    ],
                  ),
                ),
                const Divider(height: 1, color: _line),
                const SizedBox(height: 10),
                const Text('ПРОГНОЗ НА НЕДЕЛЮ',
                    style: TextStyle(
                        fontSize: 9.5, letterSpacing: 2.4, color: Colors.white70)),
                const SizedBox(height: 4),
                const _Day('Четверг', Icons.wb_sunny_rounded, 11, 22, 0.1, 0.72),
                const _Day('Пятница', Icons.wb_cloudy_rounded, 10, 20, 0.06, 0.62),
                const _Day('Суббота', Icons.grain_rounded, 8, 15, 0.0, 0.38),
                const _Day('Воскресенье', Icons.cloud_rounded, 7, 13, 0.0, 0.3),
                const Spacer(),
                Row(
                  children: const [
                    _Detail('ВЕТЕР', '4 м/с', 'юго-западный'),
                    _Detail('ВЛАЖНОСТЬ', '62%', 'комфортно'),
                  ],
                ),
                const Divider(height: 22, color: _line),
                Row(
                  children: const [
                    _Detail('ЗАКАТ', '17:42', 'через 3 ч 20 мин'),
                    _Detail('УФ-ИНДЕКС', '3', 'низкий'),
                  ],
                ),
                const SizedBox(height: 18),
                Center(
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      for (var i = 0; i < 3; i++)
                        Container(
                          width: i == 0 ? 16 : 5,
                          height: 5,
                          margin: const EdgeInsets.symmetric(horizontal: 3),
                          decoration: BoxDecoration(
                            color: i == 0 ? Colors.white : Colors.white38,
                            borderRadius: BorderRadius.circular(3),
                          ),
                        ),
                    ],
                  ),
                ),
                const SizedBox(height: 10),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _Hour extends StatelessWidget {
  const _Hour(this.time, this.icon, this.temp, {this.now = false});
  final String time;
  final IconData icon;
  final String temp;
  final bool now;

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text(time,
            style: TextStyle(
                fontSize: 10.5,
                color: now ? Colors.white : Colors.white70,
                fontWeight: now ? FontWeight.w700 : FontWeight.w400)),
        const SizedBox(height: 9),
        Icon(icon, size: 19, color: Colors.white),
        const SizedBox(height: 9),
        Text(temp,
            style: const TextStyle(
                fontSize: 14.5, color: Colors.white, fontWeight: FontWeight.w500)),
      ],
    );
  }
}

class _Day extends StatelessWidget {
  const _Day(this.day, this.icon, this.tmin, this.tmax, this.start, this.end);
  final String day;
  final IconData icon;
  final int tmin;
  final int tmax;
  final double start;
  final double end;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 7),
      child: Row(
        children: [
          SizedBox(
              width: 92,
              child: Text(day,
                  style: const TextStyle(
                      fontSize: 13, color: Colors.white, fontWeight: FontWeight.w500))),
          Icon(icon, size: 16, color: Colors.white70),
          const SizedBox(width: 10),
          Text('$tmin°',
              style: const TextStyle(fontSize: 12.5, color: Colors.white54)),
          const SizedBox(width: 8),
          Expanded(
            child: SizedBox(
              height: 4,
              child: Stack(
                children: [
                  Container(
                    decoration: BoxDecoration(
                        color: Colors.white24, borderRadius: BorderRadius.circular(2)),
                  ),
                  FractionallySizedBox(
                    alignment: Alignment.centerLeft,
                    widthFactor: end,
                    child: Padding(
                      padding: EdgeInsets.only(left: start * 60),
                      child: Container(
                        decoration: BoxDecoration(
                          gradient: const LinearGradient(
                              colors: [Color(0xFF9FD4FF), Color(0xFFFFD28A)]),
                          borderRadius: BorderRadius.circular(2),
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(width: 8),
          Text('$tmax°',
              style: const TextStyle(
                  fontSize: 13, color: Colors.white, fontWeight: FontWeight.w600)),
        ],
      ),
    );
  }
}

class _Detail extends StatelessWidget {
  const _Detail(this.label, this.value, this.note);
  final String label;
  final String value;
  final String note;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(label,
              style: const TextStyle(
                  fontSize: 9, letterSpacing: 1.8, color: Colors.white60)),
          const SizedBox(height: 3),
          Text(value,
              style: const TextStyle(
                  fontSize: 22, color: Colors.white, fontWeight: FontWeight.w300)),
          Text(note, style: const TextStyle(fontSize: 10.5, color: Colors.white54)),
        ],
      ),
    );
  }
}
