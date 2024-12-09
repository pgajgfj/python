#1
fruits = ("apple", "banana", "orange", "banana", "apple", "grape", "banana")
fruit_name = input("Введіть назву фрукта: ").strip().lower()

count = fruits.count(fruit_name)
print(f"Фрукт '{fruit_name}' зустрічається {count} раз(и).")
#2
fruits = ("apple", "banana", "orange", "bananamango", "mango", "strawberry-banana")
fruit_name = input("Введіть назву фрукта: ").strip().lower()

count_exact = fruits.count(fruit_name)
count_partial = sum(1 for fruit in fruits if fruit_name in fruit)

print(f"Фрукт '{fruit_name}' точно зустрічається {count_exact} раз(и).")
print(f"Фрукт '{fruit_name}' входить до складу елементів {count_partial} раз(и).")
#3
manufacturers = ("Toyota", "Ford", "BMW", "Ford", "Toyota", "Nissan", "Ford")
manufacturer_to_replace = input("Введіть назву виробника, яку потрібно замінити: ").strip()
replacement = input("Введіть слово для заміни: ").strip()

new_tuple = tuple(replacement if manufacturer == manufacturer_to_replace else manufacturer for manufacturer in manufacturers)
print("Оновлений кортеж:", new_tuple)

#4
numbers = (1, 23, 456, 7, 89, 101, 22, 3456, 78, 90, 12345)

digit_count = {}
for number in numbers:
    num_digits = len(str(abs(number)))
    digit_count[num_digits] = digit_count.get(num_digits, 0) + 1

for digits, count in sorted(digit_count.items()):
    print(f"{digits} цифра(и) — {count} елемент(ів)")
