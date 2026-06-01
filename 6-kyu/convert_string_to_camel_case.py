# Task: Convert string to camel case
# Link: https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
# Level: 6 kyu

def to_camel_case(text):
    if not text: 
        return ""
    
    clean_text = text.replace("-", "_")

    words = clean_text.split("_")

    camel_case_text = words[0]

    for word in words[1:]:
        camel_case_text += word.capitalize()
        
    return camel_case_text

text = "the_stealth_warrior"

print(to_camel_case(text))