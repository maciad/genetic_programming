from sympy import simplify

def simp(problem):
    return simplify(problem)

problem_file = 'results/zad1/-1_1.txt'
with open(problem_file, 'r') as f:
    problem = f.read()

simplified = simp(problem)
print(problem ,'\n\n\n', simplified)