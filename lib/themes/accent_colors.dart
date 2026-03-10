import 'package:flutter/material.dart';

class AccentColors {
  static const Map<String, Color> accents = {
    'Оранжевый': Color(0xFFFF9800),
    'Розовый': Color(0xFFE91E63),
    'Голубой': Color(0xFF03A9F4),
    'Зеленый': Color(0xFF4CAF50),
    'Желтый': Color(0xFFFFEB3B),
    'Фиолетовый': Color(0xFF9C27B0),
    'Красный': Color(0xFFF44336),
    'Бирюзовый': Color(0xFF00BCD4),
    'Лаймовый': Color(0xFFCDDC39),
    'Индиго': Color(0xFF3F51B5),
  };

  static Map<String, Map<int, Color>> get swatches {
    return {
      'Оранжевый': {
        50: const Color(0xFFFFF3E0),
        100: const Color(0xFFFFE0B2),
        200: const Color(0xFFFFCC80),
        300: const Color(0xFFFFB74D),
        400: const Color(0xFFFFA726),
        500: const Color(0xFFFF9800),
        600: const Color(0xFFFB8C00),
        700: const Color(0xFFF57C00),
        800: const Color(0xFFEF6C00),
        900: const Color(0xFFE65100),
      },
      'Розовый': {
        50: const Color(0xFFFCE4EC),
        100: const Color(0xFFF8BBD0),
        200: const Color(0xFFF48FB1),
        300: const Color(0xFFF06292),
        400: const Color(0xFFEC407A),
        500: const Color(0xFFE91E63),
        600: const Color(0xFFD81B60),
        700: const Color(0xFFC2185B),
        800: const Color(0xFFAD1457),
        900: const Color(0xFF880E4F),
      },
    };
  }

  static MaterialColor getMaterialColor(String colorName) {
    final swatch = swatches[colorName] ?? swatches['Оранжевый']!;
    return MaterialColor(swatch[500]!.value, swatch);
  }
}