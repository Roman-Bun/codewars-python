# Task: Testing 1-2-3
# Link: https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python
# Level: 7 kyu

def number(lines):
    return [f"{i}: {line}" for i, line in enumerate(lines, start=1)]

lines = ["a", "b", "c"]

print(number(lines))