# Task: Odd or Even?
# Link: https://www.codewars.com/kata/5949481f86420f59480000e7/train/python
# Level: 7 kyu

def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"

a = [0, 1, 2]
b = [0, 1, 3]

print(odd_or_even(b))