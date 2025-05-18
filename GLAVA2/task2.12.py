def main():
    num = int(input("Введите трехзначное число (100-999): "))
    while num < 100 or num > 999:
        print("Ошибка: число должно быть трехзначным (100-999)")
        num = int(input("Введите трехзначное число (100-999): "))

    hundreds = num // 100        
    tens = (num // 10) % 10     
    units = num % 10            

    sum_digits = hundreds + tens + units
    product_digits = hundreds * tens * units
    
    print(f"а) Число единиц: {units}")
    print(f"б) Число десятков: {tens}")
    print(f"в) Сумма цифр: {sum_digits}")
    print(f"г) Произведение цифр: {product_digits}")

if __name__ == "__main__":
    main()