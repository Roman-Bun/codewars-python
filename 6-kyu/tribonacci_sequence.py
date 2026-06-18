# Task: Tribonacci Sequence
# Link: https://www.codewars.com/kata/556deca17c58da83c00002db/train/python
# Level: 6 kyu

def tribonacci(signature, n):
    # Якщо просять повернути менше чисел, ніж є в старті
    if n < 3:
        return signature[:n]
    
    # Створюємо копію початкових трьох чисел
    res = signature[:]
    
    # Цикл працює, поки не наберемо потрібну кількість n чисел
    while len(res) < n:
        # Беремо суму трьох останніх елементів списку за допомогою зрізу [-3:]
        next_num = sum(res[-3:])
        res.append(next_num)
        
    return res

# Перевіряємо з початковими [1, 1, 1] для 10 елементів
print(tribonacci([1, 1, 1], 10)) 
# Виведе: [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]