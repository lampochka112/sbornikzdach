def calculate_function_a(x):
    return 7 * x**2 + 3 * x + 6

def calculate_function_b(a):
    return 12 * a**2 + 7 * a + 16

x = float(input("Введите x для функции y = 7x² + 3x + 6: "))
print(f"Результат: {calculate_function_a(x)}")

a = float(input("Введите a для функции y = 12a² + 7a + 16: "))
print(f"Результат: {calculate_function_b(a)}")