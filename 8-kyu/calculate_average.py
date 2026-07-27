# Task: Calculate average
# Link: https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python
# Level: 8 kyu

def find_average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0

num = [1, 2, 3]
print(find_average(num))