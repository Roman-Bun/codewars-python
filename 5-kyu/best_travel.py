# Task: Best travel
# Link: https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python
# Level: 5 kyu

from itertools import combinations

def choose_best_sum(t, k, ls):
    if len(ls) < k:
        return None

    all_sums = [sum(comb) for comb in combinations(ls, k)]
    valid_sums = [s for s in all_sums if s <= t]
    if valid_sums:
        return max(valid_sums)
    else:
        return None
    
ts = [50, 55, 56, 57, 58]
t = 163
k = 3

print(choose_best_sum(t, k, ts))


# from itertools import combinations

# def choose_all_best_sums(t, k, ls):
#     if len(ls) < k:
#         return None
    
#     all_combinations = list(combinations(ls, k))
    
#     # 1. Залишаємо тільки ті комбінації, які вписуються в ліміт t
#     valid_combinations = [c for c in all_combinations if sum(c) <= t]
    
#     if not valid_combinations:
#         return None
        
#     # 2. Знаходимо ОДНЕ число — саму максимальну суму серед усіх валідних
#     max_possible_sum = max(sum(c) for c in valid_combinations) # Це буде 163
    
#     # 3. Збираємо ВСІ комбінації, які мають саме таку суму
#     best_routes = [c for c in valid_combinations if sum(c) == max_possible_sum]
    
#     return max_possible_sum, best_routes

# ts = [50, 55, 56, 57, 58]
# max_km, routes = choose_all_best_sums(163, 3, ts)

# print(f"Найкраща відстань: {max_km} км")
# print("Всі ідеальні маршрути:")
# for r in routes:
#     print(r)