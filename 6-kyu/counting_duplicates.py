# Task: Counting Duplicates
# Link: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
# Level: 6 kyu

def duplicate_count(text):
    text_lower = text.lower()
    count = 0
    for char in set(text_lower):
        if text_lower.count(char) > 1:
            count += 1
    return count

text = "aabbcde"
print(duplicate_count(text))