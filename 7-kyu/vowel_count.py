# Task: Vowel Count
# Link: https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
# Level: 7 kyu

def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count
    # return len([char for char in sentence if char in vowels])

text = "aeiou"
text2 = "bcdfghjklmnpqrstvwxz y"

print(get_count(text))
print(get_count(text2))