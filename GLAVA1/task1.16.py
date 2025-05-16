import math

a = float(input("Введите длину первой стороны прямоугольника: "))
b = float(input("Введите длину второй стороны прямоугольника: "))

perimeter = 2 * (a + b)           
diagonal = math.sqrt(a**2 + b**2)  

print(f"Периметр прямоугольника: {perimeter:.2f}")
print(f"Длина диагонали прямоугольника: {diagonal:.2f}")