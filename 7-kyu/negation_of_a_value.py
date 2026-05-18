# Task: Negation of a Value
# Link: https://www.codewars.com/kata/58f6f87a55d759439b000073/train/python
# Level: 7 kyu

def negation_value(s: str, val) -> bool:
    val = bool(val)
    
    if len(s) % 2 == 0:
        return val
    else:
        return not val

print(negation_value("!", False)) #=> True
print(negation_value("!!!!!", True)) #=> False
print(negation_value("!!", [])) #=> False