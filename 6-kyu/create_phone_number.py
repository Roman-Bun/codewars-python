# Task: Create Phone Number
# Link: https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
# Level: 6 kyu

def create_phone_number(n):
    num = "".join([str(item) for item in n])
    return f"({(num[0:3])}) {(num[3:6])}-{(num[6:])}"

    # return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(create_phone_number(nums))