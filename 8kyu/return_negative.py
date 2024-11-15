def make_negative( number ):
    # Если число больше 0, делаем его отрицательным
    if number > 0:
        return -number
    # В остальных случаях возвращаем число без изменений
    return number

# Примеры использования
print(make_negative(1))   # Вывод: -1
print(make_negative(-5))  # Вывод: -5
print(make_negative(0))   # Вывод: 0