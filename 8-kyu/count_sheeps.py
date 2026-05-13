# Task: Counting sheep...
# Link: https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
# Level: 8 kyu

sheeps = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

def count_sheeps(sheep):
    return sheep.count(True)

print(count_sheeps(sheeps))