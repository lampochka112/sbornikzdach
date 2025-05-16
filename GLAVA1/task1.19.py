import math

a = float(input("Введите длину большего основания трапеции: "))
b = float(input("Введите длину меньшего основания трапеции: "))
angle_deg = float(input("Введите угол при большем основании (в градусах): "))

angle_rad = math.radians(angle_deg)

h = (a - b) / 2 * math.tan(angle_rad)

area = (a + b) / 2 * h

print(f"Площадь трапеции: {area:.2f}")
