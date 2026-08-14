# Task: Grasshopper - Grade book
# Link: https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python
# Level: 8 kyu

def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

print(get_grade(70, 70, 100))