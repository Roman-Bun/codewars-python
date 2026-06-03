# Task: Does my number look big in this?
# Link: https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python
# Level: 6 kyu

def narcissistic(value):
    digits = [int(d) for d in str(value)]
    return sum(n ** len(digits) for n in digits) == value

num = 153

print(narcissistic(num))