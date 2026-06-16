# Task: Simple Sentences
# Link: https://www.codewars.com/kata/5297bf69649be865e6000922/train/python
# Level: 6 kyu

def make_sentences(parts):
    # 1. Склеюємо всі елементи через звичайний пробіл
    sentence = " ".join(parts)
    # 2. Прибираємо пробіли перед комами заміною " ," на ","
    sentence = sentence.replace(" ,", ",")
    # 3. Видаляємо всі крапки та пробіли, які випадково опинилися в самому кінці
    sentence = sentence.rstrip(". ")
    # 4. Повертаємо рядок із красивою фінальною крапкою
    return sentence + "."  

parts = ['One', ',', 'two', 'two', ',', 'three', 'three', 'three', ',', '4', '4', '4', '4']
print(make_sentences(parts))