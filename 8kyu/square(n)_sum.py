# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because


def square_sum(numbers):
    # Начинаем с 0 для суммы
    total = 0
    # Проходим по каждому числу в списке
    for number in numbers:
        # Возводим число в квадрат и добавляем к общей сумме
        total += number ** 2
    # Возвращаем результат
    return total


numbers = [1, 2, 2]
result = square_sum(numbers)
print(result)  # 9