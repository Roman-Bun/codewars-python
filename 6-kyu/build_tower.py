# Task: Build Tower
# Link: https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
# Level: 6 kyu

def tower_builder(n_floors):
    tower = []
    for i in range(1, n_floors + 1):
        spaces = " " * (n_floors - i)
        stars = "*" * (i * 2 - 1)
        tower.append(spaces + stars + spaces)
    return tower

n = 3
print(*tower_builder(n), sep='\n')