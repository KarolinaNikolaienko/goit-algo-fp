# Завдання 7: Використання методу Монте-Карло

# Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, 
# які випадають на кубиках, і визначає ймовірність кожної можливої суми.

# Створіть симуляцію, де два кубики кидаються велику кількість разів. 
# Для кожного кидка визначте суму чисел, які випали на обох кубиках. 
# Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. 
# Використовуючи ці дані, обчисліть імовірність кожної суми.

# На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, 
# виявлені за допомогою методу Монте-Карло.

# Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

# Сума	Імовірність
# 2	    2.78% (1/36)
# 3	    5.56% (2/36)
# 4	    8.33% (3/36)
# 5	    11.11% (4/36)
# 6	    13.89% (5/36)
# 7	    16.67% (6/36)
# 8	    13.89% (5/36)
# 9	    11.11% (4/36)
# 10	8.33% (3/36)
# 11	5.56% (2/36)
# 12	2.78% (1/36)

# Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, 
# наведеними в таблиці вище.

import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np
import random

def monte_carlo(experiments):
    avr_entries = { i : 0 for i in range(2,13)}
    avr_probabilities = { i : 0 for i in range(2,13)}
    for i in range(experiments):
        sums = [random.randint(1, 6) + random.randint(1, 6) for _ in range(15000)]
        entries = {}
        probabilities = {}
        for i in range(2,13):
            entries[i] = sums.count(i)
            avr_entries[i] += entries[i]

            probabilities[i] = entries[i] / 15000
            avr_probabilities[i] += probabilities[i]
    
    for i in range(2,13):
        avr_entries[i] /= experiments 
        avr_probabilities[i] = avr_probabilities[i] * 100 / experiments

    return avr_probabilities


def main():
    probabilities = monte_carlo(100)
    print(" {:^10} | {:^15} ".format("Сума", "Ймовірність"))
    print("-" * 30)
    for key, value in probabilities.items():
        print(" {:^10} | {:^15} ".format(key, round(value, 2)))

if __name__ == "__main__":
    main()