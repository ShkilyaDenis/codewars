# Напишите функцию, которая принимает массив чисел и возвращает сумму чисел.
# Числа могут быть отрицательными или нецелыми. Если в массиве нет чисел, нужно вернуть 0.
# Примеры: Ввод: [1, 5.2, 4, 0, -1]
# Вывод: 9.2
# Ввод: []
# Вывод: 0
# Ввод: [-2.398]
# Вывод: -2.398
# Предположения:
# Можно предположить, что в массиве будут только числа.
# Нельзя предположить размер массива.
# Массив обязательно будет передан, и если он пустой, нужно вернуть 0.
# Что мы тестируем:
# Мы тестируем базовые циклы и математические операции.
# Это задача для начинающих, которые только начинают изучать циклы и математические операции.
# Опытные пользователи могут посчитать эту задачу очень легкой и решить ее в одну строку.


# Вариант решения:
def sum_array(a):
    # Проверка на пустой массив
    if len(a) == 0:
        return 0
    # Используем встроенную функцию sum()
    return sum(a)

# Разбор кода:
# Определяется функция sum_array, которая принимает один аргумент a. Предполагается, что это массив чисел.
# Проверка:
# Здесь используется len(a) для проверки длины массива.
# Если длина равна 0 (т.е. массив пустой), функция сразу возвращает 0, как указано в условии задачи.
# Это важно, чтобы избежать ненужных вычислений и ошибок при передаче пустого массива.
# Суммирование элементов массива:
# Если массив не пуст, используется встроенная функция sum(a), которая
# суммирует все элементы массива a и возвращает результат.
# Например, если a = [1, 2, 3], то sum(a) вернет 1 + 2 + 3 = 6.


# Тесты
print(sum_array([])) # 0
print(sum_array([1, 2, 3])) # 6
print(sum_array([1.1, 2.2, 3.3])) # 6.6
print(sum_array([4, 5, 6])) # 15
print(sum_array(range(101))) # 5050