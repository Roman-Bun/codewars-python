# Task: Convert number to reversed array of digits
# Link: https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
# Level: 8 kyu

def digitize(n):
    return [int(char) for char in str(n)[::-1]]

num = 12345
print(digitize(num))
