# Task: Duplicate Encoder
# Link: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
# Level: 6 kyu

def duplicate_encode(word):
    word = word.lower()
    encode = ""
    for char in word:
        if word.count(char) > 1:
            encode += ")"
        else:
            encode += "(" 
    return encode
#   return "".join(")" if word.count(char) > 1 else "(" for char in word)

word = "recede" #"()()()"
print(duplicate_encode(word))