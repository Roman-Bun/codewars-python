# Task: Isograms
# Link: https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
# Level: 7 kyu

def is_isogram(string):
    return len(string.lower()) == len(set(string.lower()))

text = "Dermatoglyphics"

print(is_isogram(text))