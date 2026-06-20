# Task: Mexican Wave
# Link: https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
# Level: 6 kyu

def wave(people):
    result = []
    for i in range(len(people)):
        if people[i] == " ":
            continue      
        wave_word = people[:i] + people[i].upper() + people[i + 1:]
        result.append(wave_word)
    return result

# word = "codewars"
# result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
word = " c o d e w a r s "

print(wave(word))