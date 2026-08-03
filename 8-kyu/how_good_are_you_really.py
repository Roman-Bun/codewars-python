# Task: How good are you really?
# Link: https://www.codewars.com/kata/5601409514fc93442500010b/train/python
# Level: 8 kyu

def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)

nums = [100, 40, 34, 57, 29, 72, 57, 88]
you = 75
print(better_than_average(nums, you))
