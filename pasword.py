import random
import string
import argparse
from datetime import datetime

class PasswordGenerator:
    def __init__(self):
        self.history = []
    
    def generate_password(self, length=12, use_digits=True, use_special=True):
        """Генерация пароля с заданными параметрами"""
        characters = string.ascii_letters
        
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        
        if not characters:
            return "Ошибка: необходимо выбрать хотя бы один тип символов"
        
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Сохраняем в историю
        self.history.append({
            'password': password,
            'length': length,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        return password
    
    def show_history(self):
        """Показать историю сгенерированных паролей"""
        if not self.history:
            print("История пуста")
            return
        
        print("\n--- История паролей ---")
        for i, item in enumerate(self.history, 1):
            print(f"{i}. Пароль: {item['password']} | Длина: {item['length']} | Время: {item['timestamp']}")

def main():
    parser = argparse.ArgumentParser(description='Генератор случайных паролей')
    parser.add_argument('-l', '--length', type=int, default=12, help='Длина пароля')
    parser.add_argument('-d', '--digits', action='store_true', help='Включать цифры')
    parser.add_argument('-s', '--special', action='store_true', help='Включать специальные символы')
    parser.add_argument('--history', action='store_true', help='Показать историю')
    
    args = parser.parse_args()
    
    generator = PasswordGenerator()
    
    if args.history:
        generator.show_history()
    else:
        password = generator.generate_password(
            length=args.length,
            use_digits=args.digits,
            use_special=args.special
        )
        print(f"Сгенерированный пароль: {password}")

if __name__ == "__main__":
    main()