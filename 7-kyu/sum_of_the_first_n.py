# Task: Sum of the first nth term of Series
# Link: https://www.codewars.com/kata/555eded1ad94b00403000071/train/python
# Level: 7 kyu

def series_sum(n):
    return f"{sum(1 / (1 + 3 * i) for i in range(n)):.2f}"

print(series_sum(5))