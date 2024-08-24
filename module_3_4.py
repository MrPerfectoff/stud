def single_root_words(root_word = str, *other_words):
    same_words = []
    root_word_low = root_word.lower()
    for i in other_words:
        i = i.lower()
        if root_word_low in i or i in root_word_low:
            same_words.append(i)
    return same_words


result = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable')
print(result2)
