# Introduction
# The first century spans from the year 1 up to and including the year 100,
# the second century - from the year 101 up to and including the year 200, etc.
# Task
# Given a year, return the century it is in.
# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# 2742 --> 28


def century(year):
    # Проверяем, делится ли год нацело на 100
    if year % 100 == 0:
        century = year // 100
    else:
        # Если остаток не равен 0, прибавляем 1 к результату деления
        century = year // 100+1
    # Возвращаем вычисленный век
    return century


#Тесты
print(century(1705)) # 18
print(century(1900)) # 19
print(century(1601)) # 17
print(century(2000)) # 20
print(century(356)) # 4
print(century(89)) # 1
