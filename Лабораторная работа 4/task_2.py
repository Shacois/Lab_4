def get_count_char(str_):
    dict_ = {}
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for letter in str_:
        if letter.isalpha():
            if dict_.get(letter):
                dict_[letter] += 1
            else:
                dict_[letter] = 1
    return dict_

def dict_in_percent(dict_):  #Функция, которая заменяет количество на процентное отношение
    total_symbols = sum(dict_.values())
    for key in dict_:
        dict_[key] = dict_[key] / total_symbols * 100
    return dict_






main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
