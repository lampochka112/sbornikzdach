num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

sum_result = num1 + num2       
difference = num1 - num2          
product = num1 * num2             

try:
    quotient = num1 / num2    
    print(f"Частное: {quotient:.2f}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")

print(f"Сумма: {sum_result:.2f}")
print(f"Разность: {difference:.2f}")
print(f"Произведение: {product:.2f}")