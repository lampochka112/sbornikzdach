def main():
    
    num = int(input("Введите трехзначное число (100-999): "))
    while num < 100 or num > 999:
        print("Ошибка: число должно быть трехзначным (100-999)")
        num = int(input("Введите трехзначное число (100-999): "))

    units = num % 10        
    tens = (num // 10) % 10  
    hundreds = num // 100   

    reversed_num = units * 100 + tens * 10 + hundreds

    print(f"Исходное число: {num}")
    print(f"Число после перестановки цифр: {reversed_num}")

if __name__ == "__main__":
    main()