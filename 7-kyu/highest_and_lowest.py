# Task: Highest and Lowest
# Link: https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
# Level: 7 kyu

def high_and_low(numbers):
    numbers = numbers.split()
    numbers = [int(n) for n in numbers]
    return f"{max(numbers)} {min(numbers)}"

nums = ("1 2 -3 4 5")

print(high_and_low(nums))