# Task: A Needle in the Haystack
# Link: https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
# Level: 8 kyu

def find_needle(haystack):
        return f"found the needle at position {haystack.index('needle')}"

stack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

print(find_needle(stack))