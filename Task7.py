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