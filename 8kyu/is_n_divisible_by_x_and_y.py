# Напишите функцию, которая проверяет, делится ли число n на два числа x и y.
# Все входные числа — положительные и не равны нулю.
# Примеры:
# n = 3, x = 1, y = 3 => true, потому что 3 делится на 1 и на 3.
# n = 12, x = 2, y = 6 => true, потому что 12 делится на 2 и на 6.
# n = 100, x = 5, y = 3 => false, потому что 100 не делится на 3.
# n = 12, x = 7, y = 5 => false, потому что 12 не делится ни на 7, ни на 5.


def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0
# n % x == 0 — проверяет, делится ли n на x без остатка.
# n % y == 0 — проверяет, делится ли n на y без остатка.
# Логический оператор and гарантирует, что оба условия должны быть выполнены для возврата True.

def is_divisible(n,x,y):
    #your code here
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False


#Тесты
print(is_divisible(3,2,2)) # False
print(is_divisible(3,3,4)) # False
print(is_divisible(12,3,4)) # True
print(is_divisible(8,3,4)) # False