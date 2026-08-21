# Task: Mumbling
# Link: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
# Level: 7 kyu

def accum(st):
    st = st.upper()
    result = []
    for i, char in enumerate(st):
        result.append(char + (char.lower() * i))
    return "-".join(result)

text = "aBcD"
print(accum(text))