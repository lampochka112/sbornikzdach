
def main():
    
    num = int(input("Введите трехзначное число (100-999): "))
    while num < 100 or num > 999:
        print("Ошибка: число должно быть трехзначным (100-999)")
        num = int(input("Введите трехзначное число (100-999): "))

    hundreds = num // 100      
    tens = (num // 10) % 10     
    units = num % 10         
    new_number = hundreds * 100 + units * 10 + tens

    print(f"Исходное число: {num}")
    print(f"Число после перестановки второй и третьей цифр: {new_number}")

if __name__ == "__main__":
    main()