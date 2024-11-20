# Создайте функцию, которая отвечает на вопрос "Играешь ли ты на банжо?".
# Если ваше имя начинается с буквы "R" (большая или маленькая), значит, вы играете на банжо!
# Функция принимает имя в качестве единственного аргумента и возвращает одну из следующих строк:
# name + " plays banjo"
# name + " does not play banjo"
# Имена всегда будут допустимыми строками.


# Вариант решения:
def are_you_playing_banjo(name):
    # Проверяем, начинается ли имя с 'r' или 'R'
    if name[0].lower() == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


# Объяснение:
# name[0] — извлекает первый символ из строки name. Например, если имя — "Rachel", то name[0] будет равно 'R'.
# .lower() — приводит символ к нижнему регистру. Это важно, чтобы условие работало как для заглавной, так
# и для строчной буквы "R". Например, как для "Rachel", так и для "rachel".
# == "r" — проверяет, является ли первый символ имени (после приведения к нижнему регистру) буквой "r".
# Это условие вернет True, если имя начинается с "r" или "R".


# Тесты
print(are_you_playing_banjo("martin")) # martin does not play banjo
print(are_you_playing_banjo("Rikke")) # Rikke plays banjo
print(are_you_playing_banjo("bravo")) # bravo does not play banjo
print(are_you_playing_banjo("rolf")) # rolf plays banjo