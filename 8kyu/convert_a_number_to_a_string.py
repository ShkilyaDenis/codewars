# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"


def number_to_string(num):
    # Функция str() преобразует любой объект в строку
    return str(num)
    # Возвращаем число преобразованное в строку

# Тесты
print(number_to_string(123))   # 123
print(number_to_string(999))   # 999
print(number_to_string(-100))  # -100
print(number_to_string(0))     # 0