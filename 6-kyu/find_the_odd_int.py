# Task: Find the odd int
# Link: https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
# Level: 6 kyu

def find_it(seq):
    # for n in seq:
    #     if seq.count(n) % 2 != 0:
    #         return n
    return next(n for n in seq if seq.count(n) % 2 != 0)

nums = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

print(find_it(nums))