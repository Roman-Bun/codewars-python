# Task: String ends with?
# Link: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
# Level: 7 kyu

def solution(text, ending):
    ending_text = text[-len(ending):]
    if (len(ending) > len(text)) or (ending_text != ending):
        return False
    else:
        return True
    # return text.endswith(ending) -- вбудований метод python

a, b = "samurai", "ai" 

print(solution(a, b))