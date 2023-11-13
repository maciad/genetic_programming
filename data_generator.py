import numpy as np
import os

def generate_data(n_variables , n_rand , min_rand, max_rand, n_fit_cases, min_range, max_range, func):
    func_name = func.__name__
    dir = f"data/zad{func_name[-1]}/"
    os.chdir(dir)
    filename = f"{min_range}_{max_range}.dat"
    with open(filename, 'w') as f:
        f.write(f'{n_variables} {n_rand} {min_rand} {max_rand} {n_fit_cases}\n')
        if n_variables == 1:
            x = np.linspace(min_range, max_range, n_fit_cases)
            for num in x:
                f.write(f'{num} ')
                f_x = func(num)
                f.write(f'{f_x}\n')
        elif n_variables == 2:
            x = np.linspace(min_range, max_range, n_fit_cases)
            y = np.linspace(min_range, max_range, n_fit_cases)
            for num1, num2 in zip(x, y):
                f.write(f'{num1} {num2} ')
                f_x = func(num1, num2)
                f.write(f'{f_x}\n')
    os.chdir("../../")

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
    

generate_data(1, 100, -5, 20, 300, -10, 10, func1)
generate_data(1, 100, -5, 20, 300, 0, 100, func1)
generate_data(1, 100, -5, 20, 300, -1, 1, func1)
generate_data(1, 100, -5, 20, 300, -1000, 1000, func1)

generate_data(1, 100, -5, 5, 300, -3.14, 3.14, func2)
generate_data(1, 100, -5, 5, 300, 0, 7, func2)
generate_data(1, 100, -5, 5, 300, -100, 100, func2)
generate_data(1, 100, -5, 5, 300, 0, 100, func2)

generate_data(1, 100, -5, 5, 300, 0, 4, func3)
generate_data(1, 100, -5, 5, 300, 0, 9, func3)
generate_data(1, 100, -5, 5, 300, 0, 99, func3)
generate_data(1, 100, -5, 5, 300, 0, 999, func3)

# [(0,1), (-10, 10), (0, 100), (-1000, 1000)]
generate_data(2, 100, -5, 5, 300, 0, 1, func4)
generate_data(2, 100, -5, 5, 300, -10, 10, func4)
generate_data(2, 100, -5, 5, 300, 0, 100, func4)
generate_data(2, 100, -5, 5, 300, -1000, 1000, func4)

# [-3.14, 3.14], [0, 7], [0, 100], [-100, 100]
generate_data(2, 100, -5, 5, 300, -3.14, 3.14, func5)
generate_data(2, 100, -5, 5, 300, 0, 7, func5)
generate_data(2, 100, -5, 5, 300, 0, 100, func5)
generate_data(2, 100, -5, 5, 300, -100, 100, func5)

# [-10, 10], [0, 100], [-1, 1], [-1000, 1000]
generate_data(2, 100, -5, 5, 300, -10, 10, func6)
generate_data(2, 100, -5, 5, 300, 0, 100, func6)
generate_data(2, 100, -5, 5, 300, -1, 1, func6)
generate_data(2, 100, -5, 5, 300, -1000, 1000, func6)