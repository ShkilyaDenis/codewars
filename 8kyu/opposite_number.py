#Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

#Examples:
#1: -1
#14: -14
#-34: 34

def opposite(number):
    # Если число меньше 0
    if number < 0:
        # Меняем знак на положительный
        return number * -1
    # Если число больше 0
    elif number > 0:
        # #Меняем знак на отрицательный
        return number * -1
    # Если число равно 0
    else:
        # Возвращаем 0
        return number


print(opposite(-34))   # 34
print(opposite(14))    # -14
print(opposite(0))     # 0