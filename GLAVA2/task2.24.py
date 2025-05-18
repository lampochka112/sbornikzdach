result = 564
for a in range(1, 10):
    bc = (result - a) / 10

    if bc.is_integer() and 10 <= bc <= 99:
        bc = int(bc)
       
        x = a * 100 + bc

        if (x // 100) + (x % 100) * 10 == result:
            print(f"Искомое число x: {x}")
            break
else:
    print("Решение не найдено")