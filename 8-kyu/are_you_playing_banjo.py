# Task: Are You Playing Banjo?
# Link: https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python
# Level: 8 kyu

def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

name_1 = "Rikke"
name_2 = "bravo"

print(are_you_playing_banjo(name_2))