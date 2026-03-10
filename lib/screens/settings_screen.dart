import 'package:flutter/material.dart';
import '../widgets/theme_switch.dart';
import '../widgets/accent_color_picker.dart';

class SettingsScreen extends StatelessWidget {
  const SettingsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Настройки'),
      ),
      body: ListView(
        children: [
          const SizedBox(height: 16),
          const ThemeSwitch(),
          const Divider(),
          const AccentColorPicker(),
          const Divider(),
          ListTile(
            leading: const Icon(Icons.language),
            title: const Text('Язык'),
            subtitle: const Text('Русский'),
            trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            onTap: () {
              // TODO: смена языка
            },
          ),
          const Divider(),
          ListTile(
            leading: const Icon(Icons.currency_ruble),
            title: const Text('Основная валюта'),
            subtitle: const Text('RUB'),
            trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            onTap: () {
              // TODO: смена валюты
            },
          ),
          const Divider(),
          ListTile(
            leading: const Icon(Icons.notifications),
            title: const Text('Уведомления'),
            subtitle: const Text('Включены'),
            trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            onTap: () {
              // TODO: настройка уведомлений
            },
          ),
          const Divider(),
          ListTile(
            leading: const Icon(Icons.info),
            title: const Text('О приложении'),
            subtitle: const Text('Версия 1.0.0'),
            onTap: () {
              showAboutDialog(
                context: context,
                applicationName: 'Finance App',
                applicationVersion: '1.0.0',
                applicationIcon: const Icon(Icons.account_balance_wallet, size: 50),
                children: [
                  const Text('Приложение для управления личными финансами'),
                ],
              );
            },
          ),
        ],
      ),
    );
  }
}