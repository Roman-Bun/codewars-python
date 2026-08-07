# Task: Count the smiley faces!
# Link: https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python
# Level: 6 kyu

def count_smileys(arr):
    valid = {":)", ":D", ":-)", ":-D", ":~)", ":~D", 
             ";)", ";D", ";-)", ";-D", ";~)", ";~D"}
    return sum(1 for smile in arr if smile in valid)

smiles = [';]', ':[', ';*', ':$', ';-D']
print(count_smileys(smiles))