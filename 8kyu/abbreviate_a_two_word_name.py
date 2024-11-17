# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
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