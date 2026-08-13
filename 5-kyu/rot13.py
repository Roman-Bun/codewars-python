# Task: Rot13
# Link: https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
# Level: 5 kyu

def rot13(message):
    result = []
    
    for char in message:
        if 'a' <= char <= 'z':
            shifted = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= char <= 'Z':
            shifted = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            result.append(shifted)
        else:
            result.append(char)
            
    return "".join(result)

text = "test 123!"
print(rot13(text))