
#%% Main.py
# Run a set of NSGA-II experiments with population modifications
import sys
if "C:/Users/katon/Documents/JHU/Evo_Swarm/Research_Paper/" not in sys.path:
    sys.path.append("C:/Users/katon/Documents/JHU/Evo_Swarm/Research_Paper/")
import nsga2_mod
import evaluation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%% Globals
pop_size = 100
max_gen = 100
solution_size = 5
problem_size=3
crossover_rate=0.1
mutation_rate=1/solution_size

test_problems = ['zdt1', 'zdt2', 'zdt3', 'zdt4', 'zdt6']

population_mods = ['base',
                   'proportional', 'inverse_proportional',
                   'gavaps',
                   'naive_linear', 'naive_power']

test_problem = 'zdt1'

sol, val, pop_tracker, fitness_tracker = nsga2_mod.run(test_prob=test_problem, 
                                          modification='base', 
                                          pop_size=pop_size, 
                                          pop_min = round(pop_size/10),
                                          max_gen=max_gen, 
                                          solution_size=solution_size, 
                                          problem_size=problem_size,
                                          crossover_rate=crossover_rate,
                                          mutation_rate=mutation_rate)

# Generational Distance
gen_dist, min_dist, max_dist = evaluation.generational_distance(val, test_problem)


if len(val) == 2:
    function1 = [i  for i in val[0]]
    function2 = [j  for j in val[1]]
    plt.xlabel('Function 1', fontsize=15)
    plt.ylabel('Function 2', fontsize=15)
    plt.scatter(function1, function2)
    plt.show()
else:
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    function1 = [i for i in val[0]]
    function2 = [j for j in val[1]]
    function3 = [k for k in val[2]]
    ax.scatter(function1, function2, function3)
    ax.view_init(45, 135)
    plt.show()
    