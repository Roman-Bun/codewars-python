# Task: Sum of two lowest positive integers
# Link: https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
# Level: 7 kyu

def sum_two_smallest_numbers(numbers):
    sorted_nums = sorted(numbers)
    return sorted_nums[0] + sorted_nums[1]

nums = [5, 8, 12, 18, 22]

print(sum_two_smallest_numbers(nums))