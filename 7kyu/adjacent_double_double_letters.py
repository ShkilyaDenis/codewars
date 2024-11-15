# Given a string which is a word, return True if the word has adjacent double double letters, like in 'balloon'.
# For example,
# 'balloon' -> True, 'lloo' are adjacent double double letters
# 'baaloon' -> False, because even though there are two double letters, they are not adjacent
# 'baboonn' -> True, here 'oonn' are adjacent double double letters
# 'matte'   -> False, because there is only one pair of double letters
# 'aaaaaaah'  -> True, any substring 'aaaa' makes it a word with adjacent double double letters
# Note: all the words will be lowercase, without any symbols or spaces


def adjacent_double_double_letters(word):
    # Идем до len(word) - 3, чтобы избежать выхода за границы
    for i in range(len(word) - 3):
        # Проверяем, что пара букв одинаковая
        if word[i] == word[i + 1] and word[i + 2] == word[i + 3]:
            return True
    return False


# Тесты
print(adjacent_double_double_letters('balloon'))  # True
print(adjacent_double_double_letters('baaloon'))  # False