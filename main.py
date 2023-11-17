
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
import numpy as np

#%% Globals
pop_size = 100
max_gen = 10000
solution_size = 20
problem_size=2
crossover_rate=0.9
mutation_rate=1/solution_size

test_problems = ['zdt1', 'zdt2', 'zdt3', 'zdt4',
                 'dtlz1', 'dtlz2', 'dtlz3', 'dtlz4']


population_mods = ['no',
                   'proportional',
                   'gavaps',
                   'naive_linear', 'naive_power']


results_dict = {}
for prob in test_problems:
    if 'dtlz' in prob:
        prob_sizes = [3, 7, 11]
    else: prob_sizes = [2]
    for prob_size in prob_sizes:
        for mod in population_mods:
            print(f"Running {prob} with {mod} modification and prob_size {prob_size}")
            # run 10 experiments
            convergence_list = []
            fitness_list = []
            best_fitness, best_solution, best_val = np.inf, [], []
            best_fit_tracker, best_pop_tracker = [], []
            for i in range(10):
                # Run experiment
                sol, val, converge_gen, pop_tracker, fitness_tracker = nsga2_mod.run(test_prob=prob, 
                                                          modification=mod, 
                                                          pop_size=pop_size, 
                                                          pop_min = round(pop_size/10),
                                                          max_gen=max_gen, 
                                                          solution_size=20,  # only used for dtlz
                                                          problem_size=prob_size,
                                                          crossover_rate=crossover_rate,
                                                          mutation_rate=1/20)
                
                # Plot
                if len(val) == 2:
                    # plot front
                    fig1 = plt.figure()
                    ax = fig1.add_subplot()
                    function1 = [i  for i in val[0]]
                    function2 = [j  for j in val[1]]
                    ax.set_xlabel('Function 1', fontsize=15)
                    ax.set_ylabel('Function 2', fontsize=15)
                    ax.set_title(f'Converged Pareto Front: {prob} with {mod} population modification - experiment {i}')
                    ax.scatter(function1, function2)
                elif len(val) == 3:
                    # plot front
                    fig1 = plt.figure()
                    ax = fig1.add_subplot(projection='3d')
                    function1 = [i  for i in val[0]]
                    function2 = [j  for j in val[1]]
                    function2 = [j for j in val[2]]                                                                                                                                                                                                                                                 
                    ax.set_xlabel('Function 1', fontsize=15)
                    ax.set_ylabel('Function 2', fontsize=15)
                    ax.set_zlabel('Function 3', fontsize=15)
                    ax.set_title(f'Converged Pareto Front: {prob} with {mod} population modification - experiment {i}')
                    ax.scatter(function1, function2)
                # plot convergence
                fig2 = plt.figure()
                ax = fig2.add_subplot()
                ax.plot(fitness_tracker)
                ax.set_xlabel('Generation')
                ax.set_ylabel('GD')
                ax.set_title(f'Generational Fitness: {prob} with {mod} population modification - experiment {i}')
                plt.show()
                # plot population
                fig3 = plt.figure()
                ax = fig3.add_subplot()
                ax.plot(pop_tracker)
                ax.set_xlabel('Generation')
                ax.set_ylabel('Population Size')
                ax.set_title(f'Population Size: {prob} with {mod} population modification - experiment {i}')
                plt.show()
                
                # add to lists
                convergence_list.append(converge_gen)
                
                min_fitness = min(fitness_tracker)
                fitness_list.append(min_fitness)
                if min_fitness < best_fitness:
                    best_solution = sol
                    best_val = val
                    best_fitness = min_fitness
                    best_fit_tracker = fitness_tracker
                    best_pop_tracker = pop_tracker
                
                print(f"{i} experiments complete")
                print(f"Converged at {converge_gen}. Achieved {best_fitness} score")
                
            
            results_dict[f'{prob}_{prob_size}_{mod}'] = {'mean_convergence' : np.mean(convergence_list),
                                                         'std_convergence' : np.std(convergence_list),
                                                         'mean_fitness' : np.mean(fitness_list),
                                                         'std_fitness' : np.std(fitness_list),
                                                         'best_solution' : best_solution,
                                                         'best_values' : best_val,
                                                         'best_fitness_tracker' : best_fit_tracker,
                                                         'best_population_tracker' : best_pop_tracker}
            
            
            
# Write Results to CSV
def create_dataframe(results_dict):
    # Extract relevant fields from the dictionary
    data = {
        'Problem': [],
        'Size': [],
        'Model': [],
        'Mean_Convergence': [],
        'Std_Convergence': [],
        'Mean_Fitness': [],
        'Std_Fitness': []
    }

    for key, values in results_dict.items():
        # Split the key into components (e.g., 'prob_prob_size_mod')
        prob, prob_size, mod = key.split('_')

        data['Problem'].append(prob)
        data['Size'].append(prob_size)
        data['Model'].append(mod)
        data['Mean_Convergence'].append(values['mean_convergence'])
        data['Std_Convergence'].append(values['std_convergence'])
        data['Mean_Fitness'].append(values['mean_fitness'])
        data['Std_Fitness'].append(values['std_fitness'])

    # Create a DataFrame
    df = pd.DataFrame(data)
    return df

results_df = create_dataframe(results_dict)
results_df.to_excel("C:/Users/katon/Documents/JHU/Evo_Swarm/Research_Paper/results.xlsx")




                