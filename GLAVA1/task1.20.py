try:
    v1 = float(input("Скорость 1-го автомобиля (км/ч) > 0: "))
    v2 = float(input("Скорость 2-го автомобиля (км/ч) > 0: "))
    s = float(input("Расстояние между ними (км) > 0: "))
    
    if v1 <= 0 or v2 <= 0 or s <= 0:
        print("Ошибка: все значения должны быть положительными!")
    else:
        time = s / (v1 + v2)
        hours = int(time)
        minutes = int((time - hours) * 60)
        print(f"Время до встречи: {hours} ч {minutes} мин")
        
except ValueError:
    print("Ошибка! Вводите только числа.")