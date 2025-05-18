result = 237

for x in range(100, 1000):
    c = x % 10               # Последняя цифра числа x
    step1 = x - c            # Вычитаем последнюю цифру
    step2 = step1 // 10      # Делим на 10
    step3 = int(f"{c}{step2}")  # Приписываем c слева
    
    if step3 == result:
        print(f"Искомое число x: {x}")
        break