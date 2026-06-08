# Task: Consecutive strings
# Link: https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python
# Level: 6 kyu

def longest_consec(strarr, k):
    longest = ""
    if k > 0 and len(strarr) >= k:
        for i in range(len(strarr) - k + 1):
            new_longest = "".join(strarr[i : i + k])
            if len(new_longest) > len(longest):
                longest = new_longest
    return longest
         
strarr = ["zone", "abigail", "theta", "form", "libe", "zas"]
k = 2

print(longest_consec(strarr, k))