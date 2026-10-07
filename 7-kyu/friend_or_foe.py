# Task: Friend or Foe?
# Link: https://www.codewars.com/kata/55b42574ff091733d900002f/train/python
# Level: 7 kyu

def friend(x):
    return [name for name in x if len(name) == 4]

friend_list = ["Ryan", "Kieran", "Jason", "Yous"]
print(friend(friend_list))