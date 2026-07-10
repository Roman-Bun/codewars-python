# Task: Moving Zeros To The End
# Link: https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
# Level: 5 kyu

def move_zeros(lst):
    # Збираємо все, що НЕ нуль (або є булевим False)
    non_zeros = [x for x in lst if x != 0 or type(x) is bool]
    
    # Збираємо тільки чисті нулі
    zeros = [x for x in lst if x == 0 and type(x) is not bool]
    
    return non_zeros + zeros
    # return sorted(lst, key=lambda x: x == 0 and type(x) is not bool)

lst = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
print(move_zeros(lst))