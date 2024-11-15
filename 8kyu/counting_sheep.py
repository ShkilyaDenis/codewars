# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
# For example,
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.
# Hint: Don't forget to check for bad values like null/undefined


def count_sheeps(sheep):
    # Инициализация счетчика
    count = 0
    #Цикл по списку овец
    for sheeps in sheep:
        # Проверка на присутствие овцы
        if sheeps == True:
            # Увеличиваем счетчик, если овца на месте
            count += 1
    # Возврат результата
    return count


# Тесты
sheep_list = [True, True, True, False, True, True, True, True,
              True, False, True, False, True, False, False, True,
              True, True, True, True, False, False, True, True]

print(count_sheep(sheep_list))  # 17