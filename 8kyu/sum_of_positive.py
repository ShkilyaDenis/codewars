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


print(positive_sum([1,2,3,4,5]))  # Вывод: 15
print(positive_sum([1,-2,3,4,5]))  # Вывод: 13
print(positive_sum([-1,2,3,4,-5]))     # Вывод: 9
print((positive_sum([])))  # Вывод: 0
print(positive_sum([-1,-2,-3,-4,-5]))  # Вывод: 0