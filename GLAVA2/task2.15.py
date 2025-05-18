def main():

    num = int(input("Введите трехзначное число (100-999): "))
    while num < 100 or num > 999:
        print("Ошибка: число должно быть трехзначным (100-999)")
        num = int(input("Введите трехзначное число (100-999): "))

    last_digit = num % 10          
    first_two_digits = num // 10  

    new_number = last_digit * 100 + first_two_digits

    print(f"Исходное число: {num}")
    print(f"Преобразованное число: {new_number}")

if __name__ == "__main__":
    main()