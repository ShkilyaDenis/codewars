# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.


def positive_sum(arr):
    # Инициализируем сумму
    total = 0
    for num in arr:
        # Если число положительное
        if num > 0:
            # Добавляем его к общей сумме
            total += num
    # Возвращаем результат после завершения цикла
    return total


# Тесты
print(positive_sum([1,2,3,4,5]))  # Вывод: 15
print(positive_sum([1,-2,3,4,5]))  # Вывод: 13
print(positive_sum([-1,2,3,4,-5]))     # Вывод: 9
print((positive_sum([])))  # Вывод: 0
print(positive_sum([-1,-2,-3,-4,-5]))  # Вывод: 0