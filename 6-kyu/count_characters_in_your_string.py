# Task: Count characters in your string
# Link: https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
# Level: 6 kyu

def count(s):
    count_dict = {}
    for char in s:
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict

text = 'aabb'
print(count(text))