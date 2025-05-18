def main():
   
    num = int(input("Введите трехзначное число (100-999): "))
    while num < 100 or num > 999:
        print("Ошибка: число должно быть трехзначным (100-999)")
        num = int(input("Введите трехзначное число (100-999): "))

    first_digit = num // 100    
    last_two_digits = num % 100   

    new_number = last_two_digits * 10 + first_digit

    print(f"Исходное число: {num}")
    print(f"Преобразованное число: {new_number}")

if __name__ == "__main__":
    main()