def single_root_words(root_words,*other_words):
    sample_words = []
    for i in other_words:
        if root_words.upper() in i.upper() or i.upper() in root_words.upper() :
            sample_words.append(i)
    return sample_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)

