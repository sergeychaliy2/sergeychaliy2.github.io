import 'package:flutter/material.dart';

/// Общая палитра и мелкие хелперы оформления для всех макетов.
class Ink2 {
  static const ink = Color(0xFF1D2335);
  static const mute = Color(0xFF8B93A7);
  static const line = Color(0xFFE6E9F2);
  static const bg = Color(0xFFF3F5FA);
}

ThemeData buildTheme(Color seed,
    {Brightness brightness = Brightness.light, TextTheme Function(TextTheme)? font}) {
  final scheme = ColorScheme.fromSeed(seedColor: seed, brightness: brightness);
  final base = brightness == Brightness.light ? ThemeData.light() : ThemeData.dark();
  final text = (font == null ? base.textTheme : font(base.textTheme)).apply(
    bodyColor: brightness == Brightness.light ? Ink2.ink : Colors.white,
    displayColor: brightness == Brightness.light ? Ink2.ink : Colors.white,
  );
  return base.copyWith(
    colorScheme: scheme,
    scaffoldBackgroundColor:
        brightness == Brightness.light ? Ink2.bg : const Color(0xFF10141F),
    textTheme: text,
    splashFactory: NoSplash.splashFactory,
  );
}

/// Мягкая карточка со скруглением и тенью — базовый кирпич всех экранов.
class SoftCard extends StatelessWidget {
  const SoftCard({
    super.key,
    required this.child,
    this.padding = const EdgeInsets.all(16),
    this.radius = 22,
    this.color = Colors.white,
    this.gradient,
    this.border,
    this.shadow = true,
    this.width,
    this.height,
    this.margin,
  });

  final Widget child;
  final EdgeInsets padding;
  final double radius;
  final Color color;
  final Gradient? gradient;
  final BoxBorder? border;
  final bool shadow;
  final double? width;
  final double? height;
  final EdgeInsets? margin;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: width,
      height: height,
      margin: margin,
      padding: padding,
      decoration: BoxDecoration(
        color: gradient == null ? color : null,
        gradient: gradient,
        borderRadius: BorderRadius.circular(radius),
        border: border,
        boxShadow: shadow
            ? const [
                BoxShadow(
                  color: Color(0x141D2335),
                  blurRadius: 24,
                  offset: Offset(0, 8),
                ),
              ]
            : null,
      ),
      child: child,
    );
  }
}

class RoundIconButton extends StatelessWidget {
  const RoundIconButton(
    this.icon, {
    super.key,
    this.size = 40,
    this.color = Ink2.ink,
    this.background = Colors.white,
    this.border,
    this.badge,
  });

  final IconData icon;
  final double size;
  final Color color;
  final Color background;
  final Color? border;
  final Widget? badge;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: size,
      height: size,
      child: Stack(
        clipBehavior: Clip.none,
        children: [
          Container(
            decoration: BoxDecoration(
              color: background,
              shape: BoxShape.circle,
              border: border == null ? null : Border.all(color: border!, width: 1),
            ),
            child: Icon(icon, size: size * 0.5, color: color),
          ),
          if (badge != null) Positioned(right: -2, top: -2, child: badge!),
        ],
      ),
    );
  }
}

class CountBadge extends StatelessWidget {
  const CountBadge(this.text, {super.key, this.color = const Color(0xFFE2443C)});
  final String text;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 2),
      decoration: BoxDecoration(
        color: color,
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: Colors.white, width: 1.5),
      ),
      child: Text(text,
          style: const TextStyle(
              color: Colors.white, fontSize: 9, fontWeight: FontWeight.w800, height: 1.2)),
    );
  }
}

class GradientButton extends StatelessWidget {
  const GradientButton(
    this.label, {
    super.key,
    required this.colors,
    this.height = 48,
    this.radius = 24,
    this.textColor = Colors.white,
    this.fontSize = 15,
    this.icon,
    this.width,
  });

  final String label;
  final List<Color> colors;
  final double height;
  final double radius;
  final Color textColor;
  final double fontSize;
  final IconData? icon;
  final double? width;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: width,
      height: height,
      alignment: Alignment.center,
      decoration: BoxDecoration(
        gradient: LinearGradient(colors: colors),
        borderRadius: BorderRadius.circular(radius),
        boxShadow: [
          BoxShadow(color: colors.last.withValues(alpha: 0.35), blurRadius: 18, offset: const Offset(0, 8)),
        ],
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          if (icon != null) ...[
            Icon(icon, color: textColor, size: fontSize + 4),
            const SizedBox(width: 8),
          ],
          Text(label,
              style: TextStyle(
                  color: textColor, fontSize: fontSize, fontWeight: FontWeight.w700)),
        ],
      ),
    );
  }
}

class SectionHeader extends StatelessWidget {
  const SectionHeader(this.title, {super.key, this.action, this.actionColor});
  final String title;
  final String? action;
  final Color? actionColor;

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Text(title, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w800)),
        if (action != null)
          Text(action!,
              style: TextStyle(
                  fontSize: 13,
                  fontWeight: FontWeight.w700,
                  color: actionColor ?? Theme.of(context).colorScheme.primary)),
      ],
    );
  }
}

class Pill extends StatelessWidget {
  const Pill(this.label,
      {super.key,
      this.active = false,
      required this.accent,
      this.textColor,
      this.background});
  final String label;
  final bool active;
  final Color accent;
  final Color? textColor;
  final Color? background;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
      decoration: BoxDecoration(
        color: active ? accent : (background ?? Colors.white),
        borderRadius: BorderRadius.circular(20),
        border: active ? null : Border.all(color: Ink2.line),
      ),
      child: Text(label,
          style: TextStyle(
              fontSize: 12.5,
              fontWeight: FontWeight.w700,
              color: active ? Colors.white : (textColor ?? Ink2.mute))),
    );
  }
}

class SearchField extends StatelessWidget {
  const SearchField(this.hint, {super.key, this.trailing, this.fill = Colors.white});
  final String hint;
  final Widget? trailing;
  final Color fill;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Expanded(
          child: Container(
            height: 46,
            padding: const EdgeInsets.symmetric(horizontal: 14),
            decoration: BoxDecoration(
              color: fill,
              borderRadius: BorderRadius.circular(23),
              border: Border.all(color: Ink2.line),
            ),
            child: Row(
              children: [
                const Icon(Icons.search_rounded, color: Ink2.mute, size: 20),
                const SizedBox(width: 8),
                Text(hint,
                    style: const TextStyle(
                        fontSize: 13.5, color: Ink2.mute, fontWeight: FontWeight.w500)),
              ],
            ),
          ),
        ),
        if (trailing != null) ...[const SizedBox(width: 10), trailing!],
      ],
    );
  }
}

/// Нижняя панель навигации в едином стиле.
class AppTabBar extends StatelessWidget {
  const AppTabBar({
    super.key,
    required this.items,
    required this.active,
    required this.accent,
    this.background = Colors.white,
    this.inactive = const Color(0xFFA7AEC2),
  });

  final List<(String, IconData)> items;
  final int active;
  final Color accent;
  final Color background;
  final Color inactive;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.only(top: 10, bottom: 8),
      decoration: BoxDecoration(
        color: background,
        borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
        boxShadow: const [
          BoxShadow(color: Color(0x141D2335), blurRadius: 24, offset: Offset(0, -6)),
        ],
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Row(
            children: [
              for (var i = 0; i < items.length; i++)
                Expanded(
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
                        decoration: BoxDecoration(
                          color: i == active ? accent.withValues(alpha: 0.12) : Colors.transparent,
                          borderRadius: BorderRadius.circular(14),
                        ),
                        child: Icon(items[i].$2,
                            size: 21, color: i == active ? accent : inactive),
                      ),
                      const SizedBox(height: 3),
                      Text(items[i].$1,
                          maxLines: 1,
                          style: TextStyle(
                              fontSize: 9.5,
                              fontWeight: i == active ? FontWeight.w700 : FontWeight.w600,
                              color: i == active ? accent : inactive)),
                    ],
                  ),
                ),
            ],
          ),
          const SizedBox(height: 8),
          Container(
            width: 110,
            height: 4,
            decoration: BoxDecoration(
                color: const Color(0xFFD7DCED), borderRadius: BorderRadius.circular(2)),
          ),
        ],
      ),
    );
  }
}

/// Простой столбчатый график.
class MiniBars extends StatelessWidget {
  const MiniBars({
    super.key,
    required this.values,
    required this.labels,
    required this.accent,
    this.highlight,
    this.height = 90,
    this.track = const Color(0xFFEEF1F8),
    this.inactive = const Color(0xFFBFD2F5),
    this.labelColor = Ink2.mute,
    this.valueLabel,
  });

  final List<double> values;
  final List<String> labels;
  final Color accent;
  final int? highlight;
  final double height;
  final Color track;
  final Color inactive;
  final Color labelColor;
  final String Function(double)? valueLabel;

  @override
  Widget build(BuildContext context) {
    final max = values.reduce((a, b) => a > b ? a : b) * 1.15;
    return SizedBox(
      height: height + 34,
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.end,
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          for (var i = 0; i < values.length; i++)
            Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                if (valueLabel != null && highlight == i)
                  Text(valueLabel!(values[i]),
                      style: const TextStyle(fontSize: 11, fontWeight: FontWeight.w700)),
                const SizedBox(height: 2),
                Container(
                  width: 22,
                  height: height,
                  alignment: Alignment.bottomCenter,
                  decoration: BoxDecoration(
                      color: track, borderRadius: BorderRadius.circular(11)),
                  child: Container(
                    width: 22,
                    height: (height * values[i] / max).clamp(8, height),
                    decoration: BoxDecoration(
                      color: (highlight == null || highlight == i) ? null : inactive,
                      gradient: (highlight == null || highlight == i)
                          ? LinearGradient(
                              colors: [accent.withValues(alpha: 0.85), accent],
                              begin: Alignment.topCenter,
                              end: Alignment.bottomCenter)
                          : null,
                      borderRadius: BorderRadius.circular(11),
                    ),
                  ),
                ),
                const SizedBox(height: 6),
                Text(labels[i],
                    style: TextStyle(
                        fontSize: 10.5, color: labelColor, fontWeight: FontWeight.w600)),
              ],
            ),
        ],
      ),
    );
  }
}

/// Кольцевой индикатор (активность, прогресс).
class RingPainter extends CustomPainter {
  RingPainter(this.rings, {this.trackColor = const Color(0xFF232B3E), this.stroke = 11});
  final List<(double, Color)> rings; // доля, цвет
  final Color trackColor;
  final double stroke;

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    var radius = size.width / 2 - stroke / 2;
    for (final (frac, color) in rings) {
      final track = Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = stroke
        ..color = trackColor;
      canvas.drawCircle(center, radius, track);
      final arc = Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = stroke
        ..strokeCap = StrokeCap.round
        ..color = color;
      canvas.drawArc(Rect.fromCircle(center: center, radius: radius), -1.5708,
          6.2832 * frac, false, arc);
      radius -= stroke + 4;
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

/// Пончиковая диаграмма.
class DonutPainter extends CustomPainter {
  DonutPainter(this.segments, {this.stroke = 18});
  final List<(double, Color)> segments;
  final double stroke;

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final radius = size.width / 2 - stroke / 2;
    var start = -1.5708;
    for (final (frac, color) in segments) {
      final p = Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = stroke
        ..color = color;
      canvas.drawArc(Rect.fromCircle(center: center, radius: radius), start + 0.03,
          6.2832 * frac - 0.06, false, p);
      start += 6.2832 * frac;
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

/// Линейный график с заливкой.
class SparkPainter extends CustomPainter {
  SparkPainter(this.values, this.color);
  final List<double> values;
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    final min = values.reduce((a, b) => a < b ? a : b) * 0.92;
    final max = values.reduce((a, b) => a > b ? a : b) * 1.05;
    final path = Path();
    for (var i = 0; i < values.length; i++) {
      final x = size.width * i / (values.length - 1);
      final y = size.height - size.height * (values[i] - min) / (max - min);
      i == 0 ? path.moveTo(x, y) : path.lineTo(x, y);
    }
    final fill = Path.from(path)
      ..lineTo(size.width, size.height)
      ..lineTo(0, size.height)
      ..close();
    canvas.drawPath(fill, Paint()..color = color.withValues(alpha: 0.18));
    canvas.drawPath(
        path,
        Paint()
          ..style = PaintingStyle.stroke
          ..strokeWidth = 3
          ..strokeCap = StrokeCap.round
          ..strokeJoin = StrokeJoin.round
          ..color = color);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}
