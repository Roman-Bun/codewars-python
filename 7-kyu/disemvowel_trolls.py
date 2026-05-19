# Task: Disemvowel Trolls
# Link: https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
# Level: 7 kyu

def disemvowel(string_):
    vowels = "aeiouAEIOU"
    return "".join([char for char in string_ if char not in vowels])

string = "This website is for losers LOL!"

print(disemvowel(string))