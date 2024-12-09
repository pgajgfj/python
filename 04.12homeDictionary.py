import json

# Словник для зберігання користувачів
users = {}

# Завантаження даних з файлу
def load_users():
    global users
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
            print("Дані завантажено.")
    except FileNotFoundError:
        print("Файл не знайдено. Починаємо з порожнього списку.")

# Збереження даних у файл
def save_users():
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)
    print("Дані збережено.")

# Додавання нового користувача
def add_user():
    username = input("Введіть логін: ")
    if username in users:
        print("Користувач уже існує!")
        return
    password = input("Введіть пароль: ")
    users[username] = password
    print("Користувача додано.")

# Видалення користувача
def delete_user():
    username = input("Введіть логін для видалення: ")
    if username not in users:
        print("Користувача не знайдено!")
        return
    del users[username]
    print("Користувача видалено.")

# Зміна пароля
def update_password():
    username = input("Введіть логін: ")
    if username not in users:
        print("Користувача не знайдено!")
        return
    old_password = users[username]
    new_password = input("Введіть новий пароль: ")
    if new_password == old_password:
        print("Новий пароль має відрізнятись від попереднього!")
        return
    users[username] = new_password
    print("Пароль оновлено.")

# Перевірка паролів
def check_passwords():
    print("Незахищені паролі:")
    for user, password in users.items():
        if len(password) < 6 or password.isalpha():
            print(f"- {user}: {password}")

# Отримання пароля за логіном
def get_password():
    username = input("Введіть логін: ")
    if username not in users:
        print("Користувача не знайдено!")
        return
    print(f"Пароль користувача {username}: {users[username]}")


def menu():
    load_users()
    while True:
        print("\nМеню:")
        print("1. Додати користувача")
        print("2. Видалити користувача")
        print("3. Змінити пароль")
        print("4. Перевірити паролі")
        print("5. Отримати пароль за логіном")
        print("6. Зберегти список користувачів у файл")
        print("7. Вийти")
        choice = input("Ваш вибір: ")
        if choice == '1':
            add_user()
        elif choice == '2':
            delete_user()
        elif choice == '3':
            update_password()
        elif choice == '4':
            check_passwords()
        elif choice == '5':
            get_password()
        elif choice == '6':
            save_users()
        elif choice == '7':
            save_users()
            print("До побачення!")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз.")


if __name__ == '__main__':
    menu()
