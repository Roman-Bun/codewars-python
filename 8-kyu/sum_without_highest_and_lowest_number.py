# Task: Sum without highest and lowest number
# Link: https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
# Level: 8 kyu

def sum_array(arr):
    if not arr or len(arr) < 3:
        return 0
    return sum(arr) - min(arr) - max(arr)

numbers = [6, 2, 1, 8, 10]

print(sum_array(numbers))