import numpy as np
import os


def func7(x):
    return np.sin(x + np.pi/2)

def func8(x):
    return np.tan(2*x + 1)

def generate_data(n_variables , n_rand , min_rand, max_rand, n_fit_cases, min_range, max_range, func):
    func_name = func.__name__
    dir = f"data/zad{func_name[-1]}/"
    os.chdir(dir)
    filename = f"{min_range}_{max_range}.dat"
    with open(filename, 'w') as f:
        f.write(f'{n_variables} {n_rand} {min_rand} {max_rand} {n_fit_cases}\n')
        x = np.linspace(min_range, max_range, n_fit_cases)
        for num in x:
            f.write(f'{num} ')
            f_x = func(num)
            f.write(f'{f_x}\n')
    os.chdir("../../")

generate_data(1, 100, -5, 5, 300, -np.pi, np.pi, func7)
generate_data(1, 100, -5, 5, 300, -np.pi/2, np.pi/2, func8)