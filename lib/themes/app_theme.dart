import 'package:flutter/material.dart';
import 'dark_theme.dart';
import 'light_theme.dart';
import 'accent_colors.dart';

class AppTheme {
  // Текущие настройки темы
  static bool isDarkMode = false;
  static String currentAccentColor = 'Оранжевый';
  
  // Геттер для текущей темы
  static ThemeData get currentTheme {
    if (isDarkMode) {
      return DarkTheme.getTheme(currentAccentColor);
    } else {
      return LightTheme.getTheme(currentAccentColor);
    }
  }
  
  // Переключение темы
  static void toggleTheme() {
    isDarkMode = !isDarkMode;
  }
  
  // Смена акцентного цвета
  static void changeAccentColor(String colorName) {
    if (Accents.accents.containsKey(colorName)) {
      currentAccentColor = colorName;
    }
  }
  
  // Получить список всех доступных цветов
  static List<String> get availableColors => Accents.accents.keys.toList();
}