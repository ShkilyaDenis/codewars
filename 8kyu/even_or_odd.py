#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


def even_or_odd(number):
    # Если остаток от деления равен 0, число четное
    if number % 2 == 0:
        # Возвращаем "Even" для четного числа
        return "Even"
    else:
        # Возвращаем "Odd" для нечетного числа
        return "Odd"


# Тесты
print(even_or_odd(4))  # Even
print(even_or_odd(0))  # Even
print(even_or_odd(-3))  # Odd