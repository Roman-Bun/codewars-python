# Task: Square Every Digit
# Link: https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
# Level: 7 kyu

def square_digits(num):
    square = []
    num = str(num)
    for n in num:
        square.append(int(n) ** 2)
    return int(''.join(map(str, square)))

    #square = [str(int(n) ** 2) for n in str(num)]
    #return int("".join(square))

nums = 9119

print(square_digits(nums))