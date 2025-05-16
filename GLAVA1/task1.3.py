try:
    number = float(input("Введите число: "))
    print(f"Вы ввели число {number}")
except ValueError:
    print("Ошибка! Вы ввели не число.")