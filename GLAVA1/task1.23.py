a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

choice = input("Выберите схему обмена (a/b): ")

if choice == 'a':
    a, b, c = b, c, a
elif choice == 'b':
    a, b, c = c, a, b
else:
    print("Неверный выбор схемы")

print(f"Результат: a = {a}, b = {b}, c = {c}")