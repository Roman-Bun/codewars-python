# Task: Break camelCase
# Link: https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
# Level: 6 kyu

def solution(s):
    return "".join(f" {char}" if char.isupper() else char for char in s)

text = "helloWorld"
print(solution(text))