import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/auth_provider.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Главная'),
        actions: [
          // Кнопка настроек
          IconButton(
            icon: const Icon(Icons.settings),
            onPressed: () {
              Navigator.pushNamed(context, '/settings');
            },
          ),
           // Кнопка уведомлений
           IconButton(
              icon: const Icon(Icons.notifications),
              onPressed: () {
                // TODO: открыть уведомления
            },
          ),
          // Кнопка выхода
          IconButton(
            icon: const Icon(Icons.exit_to_app),
            onPressed: () {
              // Выход с очисткой данных
              Provider.of<AuthProvider>(context, listen: false).logout();
              Navigator.pushReplacementNamed(context, '/');
            },
          ),
        ],
      ),
      body: const Center(
        child: Text('Главный экран - скоро появится аналитика!'),
      ),
    );
  }
}