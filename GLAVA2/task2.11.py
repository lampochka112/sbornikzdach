def main():
    num = int(input("Введите двузначное число (10-99): "))
    while num < 10 or num > 99:
        print("Ошибка: число должно быть двузначным (10-99)")
        num = int(input("Введите двузначное число (10-99): "))
    tens = num // 10  
    units = num % 10 
    
    reversed_num = units * 10 + tens

    print(f"Исходное число: {num}")
    print(f"Число после перестановки цифр: {reversed_num}")

if __name__ == "__main__":
    main()