# Task: Equal Sides Of An Array
# Link: https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python
# Level: 6 kyu

def find_even_index(arr):
    for i, _ in enumerate(arr):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i+1:])
        
        if left_sum == right_sum:
          return i 
                  
    return -1
#   return next((i for i, _ in enumerate(arr) if sum(arr[:i]) == sum(arr[i+1:])), -1)

nums = [1,2,3,4,3,2,1]

print(find_even_index(nums))