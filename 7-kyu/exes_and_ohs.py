# Task: Exes and Ohs
# Link: https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
# Level: 7 kyu

def xo(s):
    s = s.lower()
    return s.count("x") == s.count("o")

text = "ooxXm"
print(xo(text))