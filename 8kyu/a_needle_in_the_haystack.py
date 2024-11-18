# Можешь найти иголку в стоге сена?
# Напиши функцию findNeedle(), которая принимает массив, полный мусора, но содержащий одну строку "needle".
# После того, как твоя функция найдет "needle", она должна вернуть сообщение (в виде строки), которое говорит:
# "found the needle at position " плюс индекс, на котором найдена "needle". Например:
# Пример (Ввод --> Вывод):
# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"
# Примечание: сообщение должно возвращать "found the needle at position 6" (нумерация начинается с 1).


def find_needle(haystack):
    #Перебор всех индексов массива haystack
    for index in range(len(haystack)):
        #Если текущий элемент массива равен "needle"
        if haystack[index] == "needle":
            #Сообщение с позицией иголки (индекса), найденной в массиве
            return f"found the needle at position {index}"


# Тесты
print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
# found the needle at position 3

# Функция range() в Python используется для создания последовательности чисел.
# Это очень удобный способ для перебора чисел в цикле, например, с помощью for.








