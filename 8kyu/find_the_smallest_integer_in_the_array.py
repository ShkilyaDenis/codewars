# Given an array of integers your solution should find the smallest integer.
# For example:
# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.


def find_smallest_int(arr):
    min_value = arr[0]
    # #перебор элементов массива
    for num in arr:
        # проверка на минимальность
        if num < min_value:
            # выбор минимального значения
            min_value = num
            # возвращение результата
    return min_value


# Тесты
print(find_smallest_int([78, 56, 232, 12, 11, 43])) # 11
print(find_smallest_int([78, 56, -2, 12, 8, -33])) # -33