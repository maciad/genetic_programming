from sympy import symbols, sympify
import matplotlib.pyplot as plt
import glob
import numpy as np


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

files_to_run = []
# all files in data/zad1, data/zad4, data/zad6
# for filename in glob.glob('data/zad1/*'):
#     files_to_run.append(filename)
# for filename in glob.glob('data/zad4/*'):
#     files_to_run.append(filename)
# for filename in glob.glob('data/zad6/*'):
#     files_to_run.append(filename)
files_to_run.append('results/zad1/-1000_1000.txt')

for file in files_to_run:
    x_min, x_max = file.split('/')[-1].split('\\')[-1].split('.')[0].split('_')
    x_min = int(x_min)
    x_max = int(x_max)

    problem = file.split('/')[1][-1]
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

    # Definicja zmiennych symboli
    X1, X2 = symbols('X1 X2')
    
    # Wyrażenie matematyczne jako string
    with open ('results/zad1/-1000_1000.txt', 'r') as f:
        expression = f.read().strip()

    # Parsowanie wyrażenia do obiektu sympy
    expr = sympify(expression)

    X = np.linspace(x_min, x_max, 100)
    y = np.zeros(len(X))
    original_function = np.zeros(len(X))
    for i in range(len(X)):
        y[i] = expr.subs({X1: X[i], X2: X[i]})
        original_function[i] = func(X[i])
    # Wyświetlenie wykresu

    plt.plot(X, original_function, label='original function', color='blue')
    plt.plot(X, y, label='fitted function', color='orange', linestyle='dashed')
    plt.xlabel('X')  # Etykieta osi x
    plt.ylabel('Y')  # Etykieta osi y
    plt.title('Wykres funkcji')  # Tytuł wykresu
    plt.grid(True)  # Włączenie siatki na wykresie
    plt.savefig(f'results/zad1/-1000_1000.png')
    # plt.show()  # Wyświetlenie wykresu



# # Przykładowe wartości dla zmiennych X1 i X2
# X1_val = 2
# X2_val = 10

# # Podstawienie wartości zmiennych i obliczenie wyniku
# result = expr.subs({X1: X1_val, X2: X2_val})

# print(f"Wynik wyrażenia dla X1={X1_val} i X2={X2_val}: {result}")