#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.


def bool_to_word(boolean):
    # Проверяем, является ли boolean True
    if boolean:
        # Если True, возвращаем "Yes"
        return "Yes"
    else:
        # Если False, возвращаем "No"
        return "No"


# Тесты
print(bool_to_word(True))  # Yes
print(bool_to_word(False))  # No
