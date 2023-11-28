from sympy import symbols, sympify
import matplotlib.pyplot as plt
import glob
import numpy as np
import os
from mpl_toolkits.mplot3d import Axes3D


def func1(x):
    return 5*x**3 - 2*x**2 + 3*x - 17

def func2(x):
    return np.sin(x) + np.cos(x)

def func3(x):
    return 2*np.log(x + 1)

def func4(x, y):
    return x + 2*y

def func5(x, y):
    return np.sin(x / 2) + 2*np.cos(y)

def func6(x, y):
    return x**2 + 3*x*y - 7*y + 1

def func7(x):
    return np.sin(x + np.pi/2)

def func8(x):
    return np.tan(2*x + 1)

files_to_run = []
# for filename in glob.glob('results2/zad1/*.txt'):
#     files_to_run.append(filename)
# for filename in glob.glob('results2/zad2/*.txt'):
#     files_to_run.append(filename)
# for filename in glob.glob('results2/zad3/*.txt'):
#     files_to_run.append(filename)
# for filename in glob.glob('results2/zad4/*.txt'):
#     files_to_run.append(filename)
for filename in glob.glob('results2/zad5/*.txt'):
    files_to_run.append(filename)
# for filename in glob.glob('results2/zad6/*.txt'):
#     files_to_run.append(filename)
# for filename in glob.glob('results2/zad7/*.txt'):
#     files_to_run.append(filename)
# for filename in glob.glob('results2/zad8/*.txt'):
#     files_to_run.append(filename)

print(files_to_run)

for file in files_to_run:
    savefile = file.replace('.txt', '.png')
    # x_min, x_max = file.split('/')[-1].split('\\')[-1].split('.')[0].split('_')
    # x_min, x_max = os.path.splitext(os.path.basename(file))[0].split('_')
    print(file.split('\\')[-1].replace('.txt', '').split('_'))
    x_min, x_max = file.split('\\')[-1].replace('.txt', '').split('_')
    print(x_min, x_max)
    x_min = float(x_min)
    x_max = float(x_max)


    problem = file.split('\\')[0][-1]
    print(problem)
    func = None
    if problem == '1':
        func = func1
    elif problem == '2':
        func = func2
    elif problem == '3':
        func = func3
    elif problem == '4':
        func = func4
    elif problem == '5':
        func = func5
    elif problem == '6':
        func = func6
    elif problem == '7':
        func = func7
    elif problem == '8':
        func = func8

    with open(file, 'r') as f:
        expression = f.read().strip()
        expr = sympify(expression)

    if problem in ['1', '2', '3', '7', '8']:
        X1 = symbols('X1')

        X = np.linspace(x_min, x_max, 100)
        result = np.zeros(len(X))
        original_function = np.zeros(len(X))
        for i in range(len(X)):
            # print(X[i])
            result[i] = expr.subs({X1: X[i]})
            # print(result[i])
            original_function[i] = func(X[i])

        plt.plot(X, original_function, label='original function', color='blue')
        plt.plot(X, result, label='fitted function', color='orange', linestyle='dashed')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Wykres funkcji')
        plt.grid(True)
        plt.legend()
        plt.savefig(savefile)
        plt.clf()  # Wyczyszczenie rysunku


    elif problem in ['4', '5', '6']:
        X1, X2 = symbols('X1 X2')

        x = np.linspace(x_min, x_max, 100)
        y = np.linspace(x_min, x_max, 100)
        X, Y = np.meshgrid(x, y)

        # original_function = func(X, Y)

        original_function = np.zeros((len(x), len(y)))
        result = np.zeros((len(x), len(y)))
        for i in range(len(x)):
            for j in range(len(y)):
                original_function[i][j] = func(x[i], y[j])
                result[i][j] = expr.subs({X1: x[i], X2: y[j]})

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, original_function, label='original function', color='blue')
        ax.plot_surface(X, Y, result, label='fitted function', color='orange', linestyle='dashed')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Wykres funkcji')
        # ax.legend()
        plt.savefig(savefile)
        plt.clf()
