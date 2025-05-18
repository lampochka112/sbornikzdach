def main():

    num = input("Введите трехзначное число с разными цифрами (100-999): ")

    while len(num) != 3 or not num.isdigit() or len(set(num)) != 3:
        print("Ошибка: число должно быть трехзначным и содержать три разные цифры")
        num = input("Введите трехзначное число с разными цифрами (100-999): ")
    
    digits = list(num)
    
    permutations = [
        digits[0] + digits[1] + digits[2],  # ABC
        digits[0] + digits[2] + digits[1],  # ACB
        digits[1] + digits[0] + digits[2],  # BAC
        digits[1] + digits[2] + digits[0],  # BCA
        digits[2] + digits[0] + digits[1],  # CAB
        digits[2] + digits[1] + digits[0]   # CBA
    ]
    
    print("\nВсе возможные перестановки цифр:")
    for i, perm in enumerate(permutations, 1):
        print(f"{i}. {perm}")

if __name__ == "__main__":
    main()