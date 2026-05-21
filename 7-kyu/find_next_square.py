# Task: Find the next perfect square!
# Link: https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python
# Level: 7 kyu

def find_next_square(sq):
    result = sq ** 0.5
    if not result.is_integer():
        return -1
    return int((result + 1) ** 2)

number = 121

print(find_next_square(number))