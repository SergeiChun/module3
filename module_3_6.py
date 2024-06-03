def single_root_words(root_world, *other_words):
    same_words = []
    root_word_lower = root_word.lower()  # переводим слово которое ищем в нижний регист
    for word in other_words:
        word_lower = word.lower()  # переводим слово из списка в нижний регист
        if root_word_lower in word_lower or word_lower in root_word_lower:  # условие что одно из слов должно
            # находиться в другом
            same_words.append(word)
    return same_words


# Подставляем значени и проверяем
root_word = 'Able'
other_words = 'Disablement', 'Able', 'Mable', 'Disable', 'Bagel'
same_words = single_root_words(root_word, *other_words)
print(f"Слова, содержащие '{root_word}' : {same_words}")

root_word = 'rich'
other_words = 'rich', 'richiest', 'orichalcum', 'cheers', 'richies'
same_words = single_root_words(root_word, *other_words)
print(f"Слова, содержащие '{root_word}' : {same_words}")