# Task: [Code Golf] String to ASCII Character
# Link: https://www.codewars.com/kata/5abbb33396194245d5000161/train/python
# Level: 7 kyu

solution=lambda s:chr(sum(map(ord,s.upper()))//len(s))

s = "iamareallyreallylongstringthatiscompletelyworthlessandisheretostophardcoders"

print(solution(s))