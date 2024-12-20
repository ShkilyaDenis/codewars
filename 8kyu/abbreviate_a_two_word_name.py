# Напиши функцию, которая преобразует имя в инициалы. Задача строго предполагает, что входная строка содержит
# два слова, разделенных одним пробелом.
# Вывод должен быть в виде двух заглавных букв с точкой между ними.
# Пример:
# Sam Harris => S.H
# patrick feeney => P.F


def abbrev_name(name):
    # Разбиваем имя на слова
    first_name, last_name = name.split()
    # Берем первые буквы, делаем их заглавными и объединяем через точку
    return f"{first_name[0].upper()}.{last_name[0].upper()}"


# Тесты
print(abbrev_name("Sam Harris"))  # Вывод: S.H
print(abbrev_name("patrick feeney"))  # Вывод: P.F


# Метод split() используется для разделения строки на части (подстроки) по заданному
# разделителю и возвращает список этих частей.

# Метод upper() преобразует все символы в строке в заглавные буквы.











