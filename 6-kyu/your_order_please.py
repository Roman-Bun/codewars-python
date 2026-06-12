# Task: Your order, please
# Link: https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
# Level: 6 kyu

def order(sentence):
    sort_order = []
    order_list = sentence.split()
    for n in range(1, len(order_list) + 1):
        for char in order_list:
            if str(n) in char:
                sort_order.append(char)
    return " ".join(sort_order)
    #return " ".join(sorted(sentence.split(), key=lambda word: sorted(word)[0]))


text = "is2 Thi1s T4est 3a"
print(order(text))