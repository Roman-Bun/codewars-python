# Task: Two Sum
# Link: https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
# Level: 6 kyu

def two_sum(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i

nums = [1, 2, 3]
target = 4
print(two_sum(nums, target))