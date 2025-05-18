def main():
    # Ввод количества секунд
    n = int(input("Введите количество секунд, прошедших с начала суток: "))
    
    # a) Полные часы
    full_hours = n // 3600
    
    # b) Полные минуты с начала текущего часа
    remaining_seconds = n % 3600
    full_minutes = remaining_seconds // 60
    
    # c) Полные секунды с начала текущей минуты
    full_seconds = remaining_seconds % 60
    
    # Вывод результатов
    print(f"a) Полных часов: {full_hours}")
    print(f"б) Полных минут с начала часа: {full_minutes}")
    print(f"в) Полных секунд с начала минуты: {full_seconds}")

# Запуск программы
if __name__ == "__main__":
    main()