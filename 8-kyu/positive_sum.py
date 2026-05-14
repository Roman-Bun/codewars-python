# Task: Sum of positive
# Link: https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
# Level: 8 kyu

nums = [1,-2,3,4,5]

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

print(positive_sum(nums))