# Task: Sort the odd
# Link: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
# Level: 6 kyu

def sort_array(source_array):
    odds = sorted([x for x in source_array if x % 2 != 0])
    return [odds.pop(0) if x % 2 != 0 else x for x in source_array]

nums = [5, 8, 6, 3, 4]

print(sort_array(nums))