a = float(input("Введите длину ребра куба: "))

объём = a ** 3
площадь_боковой_поверхности = 6 * a ** 2  # или 4 * a**2 для только боковых граней без основания

print(f"Объём куба: {объём:.2f}")
print(f"Площадь полной поверхности куба: {площадь_боковой_поверхности:.2f}")