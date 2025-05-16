# Ввод двух целых чисел
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))

arithmetic_mean = (a + b) / 2
geometric_mean = (a * b) ** 0.5

print(f"Среднее арифметическое: {arithmetic_mean}")
print(f"Среднее геометрическое: {geometric_mean}")