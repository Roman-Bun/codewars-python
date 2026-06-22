# Task: Write Number in Expanded Form
# Link: https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python
# Level: 6 kyu

def expanded_form(num):
    str_num = str(num)
    parts = []
    for i in range(len(str_num)):
        if str_num[i] != "0":
            zeros = "0" * (len(str_num) - 1 - i)
            parts.append(str_num[i] + zeros)
    return " + ".join(parts)
# Рухаємось по ходу: для кожної цифри додаємо потрібну кількість нулів
#    return " + ".join(digit + "0" * (len(s) - 1 - i) for i, digit in enumerate(s) if digit != "0")
 
num = 70304  #70000 + 300 + 4
print(expanded_form(num))