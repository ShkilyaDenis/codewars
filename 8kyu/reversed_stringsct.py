# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'


def reverse_string(s):
    #Мы используем срез[::-1], который позволяет пройти по строке в обратном порядке, создавая новую строку.
    return s[::-1]
    # В результате функция возвращает строку, но символы идут в обратном порядке.


# Тесты
print(reverse_string('world'))  # Вывод: 'dlrow'
print(reverse_string('Hello'))   # Вывод: 'olleH'