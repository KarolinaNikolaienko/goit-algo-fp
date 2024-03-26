# Завдання 6: Жадібні алгоритми та динамічне програмування

# Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та 
# алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю 
# в межах обмеженого бюджету.

# Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, 
# де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

# items = {
#     "pizza": {"cost": 50, "calories": 300},
#     "hamburger": {"cost": 40, "calories": 250},
#     "hot-dog": {"cost": 30, "calories": 200},
#     "pepsi": {"cost": 10, "calories": 100},
#     "cola": {"cost": 15, "calories": 220},
#     "potato": {"cost": 25, "calories": 350}
# }

# Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи 
# співвідношення калорій до вартості, не перевищуючи заданий бюджет.

# Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, 
# яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.

import timeit

def greedy_algorithm(budget, items):
    items = dict(sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True))
    res = {}
    if budget:
        for item, value in items.items():
            res[item] = budget // value["cost"]
            budget -= value["cost"] * res[item]
    calories = 0
    for key, value in res.items():
        calories += items[key]["calories"]
    return res, calories

def dynamic_programming(budget, items):
    items = dict(sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True))
    # створюємо таблицю K для зберігання оптимальних значень підзадач
    n = len(items)
    calories = []
    cost = []
    for key, value in items.items():
        calories.append(value["calories"])
        cost.append(value["cost"])

    K = [[0 for w in range(budget + 1)] for i in range(n + 1)]
    # будуємо таблицю K знизу вгору
    for i in range(n + 1):
        for b in range(budget + 1):
            if i == 0 or b == 0:
                K[i][b] = 0
            elif cost[i - 1] <= b:
                K[i][b] = max(calories[i - 1] + K[i - 1][b - cost[i - 1]], K[i - 1][b])
            else:
                K[i][b] = K[i - 1][b]

    res = K[n][budget] 
    b = budget
    items_to_buy = {key : 0 for key in items.keys()}
    items_cost_key = {value["cost"]: key for key, value in items.items()}
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][b]:
            continue
        else:
            items_to_buy[items_cost_key[cost[i - 1]]] += 1
            #print(cost[i - 1])
            res = res - calories[i - 1]
            b = b - cost[i - 1]
    return items_to_buy, K[n][budget]

def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
        }

    budget = 115

    starttime = timeit.default_timer()
    res, calories = greedy_algorithm(budget, items)
    time = timeit.default_timer() - starttime
    print(f"Greedy for:\n{res}\n{calories}\nTime: {time}\n")

    starttime = timeit.default_timer()
    res, calories = dynamic_programming(budget, items)
    time = timeit.default_timer() - starttime
    print(f"Dynamic:\n{res}\n{calories}\nTime: {time}\n\n")

if __name__ == "__main__":
    main()