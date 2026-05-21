# Task: Two to One
# Link: https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
# Level: 7 kyu

def longest(a1, a2):
    my_set = sorted(set(a1 + a2))
    return "".join(my_set)
    
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

print(longest(a, b))