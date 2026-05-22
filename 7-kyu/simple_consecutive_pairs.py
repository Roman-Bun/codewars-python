# Task: Simple consecutive pairs
# Link: https://www.codewars.com/kata/5a3e1319b6486ac96f000049/train/python
# Level: 7 kyu

def pairs(arr):
    count = 0
    
    for n in range(0, len(arr) - 1, 2):
        if abs(arr[n] - arr[n + 1]) == 1:
            count += 1

    return count

numbers = [1,2,5,8,-4,-3,7,6,5]

print(pairs(numbers))