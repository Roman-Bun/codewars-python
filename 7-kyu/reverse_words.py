# Task: Reverse words
# Link: https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
# Level: 7 kyu

def reverse_words(text):
    # words = text.split(' ')
    # reversed_words_list = []
    
    # for word in words:
    #     reversed_words_list.append(word[::-1])
        
    # return " ".join(reversed_words_list)
    return " ".join(word[::-1] for word in text.split(' '))

text = "This is an example!"

print(reverse_words(text))