# Task: Grasshopper - Personalized Message
# Link: https://www.codewars.com/kata/5772da22b89313a4d50012f7/train/python
# Level: 8 kyu

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

name = "Roman"
owner = "Roman"
print(greet(name, owner))