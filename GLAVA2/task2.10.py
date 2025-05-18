def main():
    # Ввод двузначного числа
    num = int(input("Введите двузначное число (10-99): "))
    while num < 10 or num > 99:
        print("Ошибка: число должно быть двузначным (10-99)")
        num = int(input("Введите двузначное число (10-99): "))

    # а) Число десятков
    tens = num // 10

    # б) Число единиц
    units = num % 10
    
    sum_digits = tens + units

    print(f"а) Число десятков: {tens}")
    print(f"б) Число единиц: {units}")
    print(f"в) Сумма цифр: {sum_digits}")

if __name__ == "__main__":
    main()