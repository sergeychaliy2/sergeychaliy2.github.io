import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

import 'screens/bank_screen.dart';
import 'screens/fitness_screen.dart';
import 'screens/flowers_screen.dart';
import 'screens/food_screen.dart';
import 'screens/gas_screen.dart';
import 'screens/smart_home_screen.dart';
import 'screens/taxi_screen.dart';
import 'screens/weather_screen.dart';
import 'theme.dart';

/// У каждого приложения свой шрифт, своя тема и своя палитра —
/// экран выбирается фрагментом URL: index.html#/gas, #/taxi и так далее.
class AppSpec {
  const AppSpec(this.screen, this.seed, this.brightness, this.font);
  final Widget screen;
  final Color seed;
  final Brightness brightness;
  final TextTheme Function(TextTheme) font;
}

final Map<String, AppSpec> kScreens = {
  'flowers': AppSpec(const FlowersScreen(), const Color(0xFFA3374F), Brightness.light,
      (t) => GoogleFonts.interTextTheme(t)),
  'gas': AppSpec(const GasScreen(), const Color(0xFF0B63CE), Brightness.light,
      (t) => GoogleFonts.ptSansTextTheme(t)),
  'taxi': AppSpec(const TaxiScreen(), const Color(0xFFD6FF4B), Brightness.dark,
      (t) => GoogleFonts.manropeTextTheme(t)),
  'bank': AppSpec(const BankScreen(), const Color(0xFFD8B25F), Brightness.dark,
      (t) => GoogleFonts.montserratTextTheme(t)),
  'weather': AppSpec(const WeatherScreen(), const Color(0xFF3F93E8), Brightness.light,
      (t) => GoogleFonts.interTextTheme(t)),
  'fitness': AppSpec(const FitnessScreen(), const Color(0xFFC8FF4D), Brightness.dark,
      (t) => GoogleFonts.rubikTextTheme(t)),
  'food': AppSpec(const FoodScreen(), const Color(0xFFF0620B), Brightness.light,
      (t) => GoogleFonts.nunitoTextTheme(t)),
  'home': AppSpec(const SmartHomeScreen(), const Color(0xFF3F6FD8), Brightness.light,
      (t) => GoogleFonts.interTextTheme(t)),
};

void main() {
  final key = Uri.base.fragment.replaceAll('/', '').trim();
  runApp(MockApps(spec: kScreens[key] ?? kScreens['flowers']!));
}

class MockApps extends StatelessWidget {
  const MockApps({super.key, required this.spec});
  final AppSpec spec;

  /// Логический холст телефона: всё верстается в 360x640 и масштабируется
  /// в окно целиком — кадр получается ровно 1080x1920 при любом размере окна.
  static const canvas = Size(360, 640);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: buildTheme(spec.seed, brightness: spec.brightness, font: spec.font),
      home: SizedBox.expand(
        child: FittedBox(
          fit: BoxFit.contain,
          alignment: Alignment.center,
          child: SizedBox(
            width: canvas.width,
            height: canvas.height,
            child: MediaQuery(
              data: const MediaQueryData(size: canvas, devicePixelRatio: 3),
              child: spec.screen,
            ),
          ),
        ),
      ),
    );
  }
}
