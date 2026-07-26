# Task: Basic Mathematical Operations
# Link: https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
# Level: 8 kyu

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
#   return eval(f"{value1} {operator} {value2}")

oper = "/"
val1 = 49
val2 = 7

print(basic_op(oper, val1, val2))