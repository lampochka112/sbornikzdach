n = int(input("Введите натуральное число (>999): "))
units = n % 100
tens = (n // 10) % 1000

print(f"Число единиц: {units}")
print(f"Число десятков: {tens}")