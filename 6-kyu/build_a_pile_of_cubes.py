# Task: Build a pile of Cubes
# Link: https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python
# Level: 6 kyu

def find_nb(m):
    total_volume = 0
    n = 0
    
    while total_volume < m:
        n += 1
        total_volume += n**3
        
    if total_volume == m:
        return n
    else:
        return -1

m = 4183059834009
print(find_nb(m))