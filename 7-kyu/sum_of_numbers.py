# Task: Beginner Series #3 Sum of Numbers
# Link: https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
# Level: 7 kyu

def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))
#    return (a + b) * (abs(a - b) + 1) // 2 # Формула Гаусса

num1 = 1
num2 = 4
print(get_sum(num1, num2))