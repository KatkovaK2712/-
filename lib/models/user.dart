class User {
  final int id;
  final String email;
  final String mainCurrency;

  User({
    required this.id,
    required this.email,
    required this.mainCurrency,
  });

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      id: json['id'],
      email: json['email'],
      mainCurrency: json['main_currency'] ?? 'RUB',
    );
  }
}