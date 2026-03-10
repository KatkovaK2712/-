import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../themes/accent_colors.dart';

class ThemeProvider extends ChangeNotifier {
  bool _isDarkMode = false;
  String _accentColor = 'Оранжевый';
  
  bool get isDarkMode => _isDarkMode;
  String get currentAccentColor => _accentColor;
  List<String> get availableColors => AccentColors.accents.keys.toList();
  
  ThemeProvider() {
    _loadThemePreferences();
  }
  
  Future<void> _loadThemePreferences() async {
    final prefs = await SharedPreferences.getInstance();
    _isDarkMode = prefs.getBool('isDarkMode') ?? false;
    _accentColor = prefs.getString('accentColor') ?? 'Оранжевый';
    notifyListeners();
  }
  
  Future<void> _saveThemePreferences() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool('isDarkMode', _isDarkMode);
    await prefs.setString('accentColor', _accentColor);
  }
  
  Future<void> toggleTheme() async {
    _isDarkMode = !_isDarkMode;
    await _saveThemePreferences();
    notifyListeners();
  }
  
  Future<void> changeAccentColor(String colorName) async {
    if (AccentColors.accents.containsKey(colorName)) {
      _accentColor = colorName;
      await _saveThemePreferences();
      notifyListeners();
    }
  }
  
  ThemeData get currentTheme {
    if (_isDarkMode) {
      return _getDarkTheme();
    } else {
      return _getLightTheme();
    }
  }
  
  ThemeData _getDarkTheme() {
    final accentSwatch = AccentColors.getMaterialColor(_accentColor);
    
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.dark,
      colorScheme: ColorScheme.dark(
        primary: accentSwatch,
        secondary: accentSwatch.shade300,
        tertiary: accentSwatch.shade100,
        surface: const Color(0xFF1E1E1E),
        background: const Color(0xFF121212),
        error: Colors.red.shade400,
        onPrimary: Colors.white,
        onSecondary: Colors.black,
        onSurface: Colors.white,
        onBackground: Colors.white,
      ),
      
      appBarTheme: const AppBarTheme(
        backgroundColor: Color(0xFF1E1E1E),
        foregroundColor: Colors.white,
        elevation: 0,
        centerTitle: true,
      ),
      
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: accentSwatch,
          foregroundColor: Colors.white,
          minimumSize: const Size(double.infinity, 45),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
        ),
      ),
      
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: const Color(0xFF2C2C2C),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: BorderSide.none,
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: BorderSide(color: accentSwatch, width: 2),
        ),
      ),
    );
  }
  
  ThemeData _getLightTheme() {
    final accentSwatch = AccentColors.getMaterialColor(_accentColor);
    
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.light,
      colorScheme: ColorScheme.light(
        primary: accentSwatch,
        secondary: accentSwatch.shade300,
        tertiary: accentSwatch.shade100,
        surface: Colors.white,
        background: const Color(0xFFF5F5F5),
        error: Colors.red.shade400,
        onPrimary: Colors.white,
        onSecondary: Colors.black,
        onSurface: Colors.black,
        onBackground: Colors.black,
      ),
      
      appBarTheme: const AppBarTheme(
        backgroundColor: Colors.white,
        foregroundColor: Colors.black,
        elevation: 0,
        centerTitle: true,
      ),
      
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: accentSwatch,
          foregroundColor: Colors.white,
          minimumSize: const Size(double.infinity, 45),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
        ),
      ),
      
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: Colors.grey.shade100,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: BorderSide.none,
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: BorderSide(color: accentSwatch, width: 2),
        ),
      ),
    );
  }
}