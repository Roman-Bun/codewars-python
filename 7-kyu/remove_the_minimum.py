# Task: Remove the minimum
# Link: https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
# Level: 7 kyu

def remove_smallest(numbers):
    if not numbers:
        return []
        
    min_i = numbers.index(min(numbers))
    return [val for i, val in enumerate(numbers) if i != min_i]

ex = [5, 3, 2, 1, 4]
print(remove_smallest(ex))