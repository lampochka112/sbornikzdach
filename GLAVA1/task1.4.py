
try:
    number = float(input("Введите число: "))
    print(f"{number} - вот какое число Вы ввели")
except ValueError:
    print("Ошибка! Нужно ввести число.")
