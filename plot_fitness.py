import matplotlib.pyplot as plt
import numpy as np
import csv

def plot_fitness(file):
    avg_file = file.replace('.txt', '_avg.png')
    best_file = file.replace('.txt', '_best.png')
    with open(file, 'r') as f:
        reader = csv.reader(f)
        # skip header
        next(reader)
        data = list(reader)

    data = np.array(data)
    data = data.astype(np.float)

    plt.plot(data[:, 0])
    plt.xlabel('Iteration')
    plt.ylabel('avg Fitness')
    plt.title('avg Fitness over iterations')
    plt.savefig(avg_file)
    plt.clf()

    plt.plot(data[:, 1])
    plt.xlabel('Iteration')
    plt.ylabel('best Fitness')
    plt.title('best Fitness over iterations')
    plt.savefig(best_file)
    plt.clf()


plot_fitness('fitness/zad5/-3.14_3.14.txt')