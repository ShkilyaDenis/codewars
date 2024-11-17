# Make a function that will return a greeting statement that uses an input; your program should
# return, "Hello, <name> how are you doing today?".


def greet(name):
    # Возвращает строку приветствия, вставляя имя
    return f"Hello, {name} how are you doing today?"


# Тесты
print(greet("John")) # "Hello, John how are you doing today?"
print(greet(" Anna ")) # "Hello,  Anna  how are you doing today?" (пробелы сохраняются)
print(greet("John123")) # "Hello, John123 how are you doing today?"