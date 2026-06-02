# Task: Replace With Alphabet Position
# Link: https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
# Level: 6 kyu

def alphabet_position(text):
    eng_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    letters = "".join([char.upper() for char in text if char.isalpha()])
    
    positions_list = []
    for n in letters:
        pos = eng_alphabet.index(n) + 1
        positions_list.append(str(pos))
        
    return " ".join(positions_list)

    #return " ".join(str(ord(c) - 64) for c in text.upper() if c.isalpha())
    
text = "The sunset sets at twelve o' clock."

print(alphabet_position(text))