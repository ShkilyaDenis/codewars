def number_to_string(num):
    # Функция str() преобразует любой объект в строку
    return str(num)
    # Возвращаем число преобразованное в строку

# Проверяем с разными числами
print(number_to_string(123))   # Ожидаемый вывод: '123'
print(number_to_string(999))   # Ожидаемый вывод: '999'
print(number_to_string(-100))  # Ожидаемый вывод: '-100'
print(number_to_string(0))     # Ожидаемый вывод: '0'