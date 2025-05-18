n = int(input("Введите натуральное число (>99): "))
units = n % 104
tens = (n // 10) % 100

print(f"Число единиц: {units}")
print(f"Число десятков: {tens}")