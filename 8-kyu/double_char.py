# Task: Double Char
# Link: https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
# Level: 8 kyu

def double_char(s):
    return "".join(c * 2 for c in s)

text = "String"
print(double_char(text))