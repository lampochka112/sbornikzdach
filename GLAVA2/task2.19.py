n = int(input("Введите натуральное число (>9): "))
units = n % 10
tens = (n // 10) % 10  

print(f"Число единиц: {units}")
print(f"Число десятков: {tens}")