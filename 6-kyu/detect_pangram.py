# Task: Detect Pangram
# Link: https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
# Level: 6 kyu

def is_pangram(st):
    letters = set(char.lower() for char in st if char.isalpha())
    
    return len(letters) == 26

text = "The quick brown fox jumps over the lazy dog."

print(is_pangram(text))