# Task: Jaden Casing Strings
# Link: https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
# Level: 7 kyu

def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())

text = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(text))