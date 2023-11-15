
#%% Imports
import os, sys
if "C:/Users/katon/Documents/JHU/Evo_Swarm/Research_Paper/" not in sys.path:
    sys.path.append("C:/Users/katon/Documents/JHU/Evo_Swarm/Research_Paper/")
import func as fn
from initialization import initialize
import population_modifications as mods
import evaluation
import random
import math
import matplotlib.pyplot as plt


def run(test_prob, 
        modification, 
        pop_size, 
        pop_min,
        max_gen, 
        solution_size, 
        problem_size,
        crossover_rate,
        mutation_rate):
    
    
    # Initialization
    solution, functions, params = initialize(problem_name=test_prob, 
                                             pop_size=pop_size, 
                                             n=solution_size, 
                                             M=problem_size)
    
    
    initial_pop_size = pop_size
    pop_tracker = []
    fitness_tracker = []
    
    
    # Main Loop
    gen_no=0
    while (gen_no<max_gen) :
        # Update trackers
        pop_tracker.append(len(solution))
        
        if gen_no%10 ==0: print(gen_no)
        
        if 'dtlz' not in test_prob:
            values = {o : [functions[o](solution[i]) for i in range(len(solution))] for o in range(len(functions))}      
        else:
            values = {o : [functions(solution[i], o) for i in range(len(solution))] for o in range(problem_size)}
        
        non_dominated_sorted_solution = fn.fast_non_dominated_sort(values)
        # print(len(non_dominated_sorted_solution[0]))
        # print("The best front for Generation number ",gen_no, " is")
        # for valuez in non_dominated_sorted_solution[0]:
        #     print(solution[valuez],end=" ")
        # print("\n")
        
        # Calculate crowding distance for all fronts
        crowding_distance_values=[]
        for i in range(len(non_dominated_sorted_solution)):
            crowding_distance_values.append(fn.crowding_distance(values, non_dominated_sorted_solution[i]))
        
        solution2 = solution.copy()
        #Generating offsprings
        while(len(solution2)!=2*len(solution)):
            a1 = random.randint(0,len(solution)-1)
            b1 = random.randint(0,len(solution)-1)
            cross = fn.crossover(solution[a1], solution[b1], crossover_rate)
            offspring = fn.mutation(cross, mutation_rate, params)
            solution2.append(offspring)
        
        if 'dtlz' not in test_prob:
            values2 = {o : [functions[o](solution2[i]) for i in range(len(solution2))] for o in range(len(functions))}
        else: 
            values2 = {o : [functions(solution2[i], o) for i in range(len(solution2))] for o in range(problem_size)}
        
        non_dominated_sorted_solution2 = fn.fast_non_dominated_sort(values2)
        
        crowding_distance_values2=[]
        for i in range(0,len(non_dominated_sorted_solution2)):
            crowding_distance_values2.append(fn.crowding_distance(values2, non_dominated_sorted_solution2[i]))
        
        
        # pop_size modifications
        if modification == 'base':
            pop_size = pop_size
        elif modification == 'proportional':
            pop_size = mods.proportional(pop_size, pop_min, gen_no, fitness_tracker)
        elif modification == 'gavaps':
            pop_size = 10*initial_pop_size # maximum value
        elif modification == 'naive_linear':
            pop_size = mods.naive_linear(initial_pop_size, pop_min, gen_no+1, max_gen)
        elif modification == 'naive_power':
            pop_size = mods.naive_power(initial_pop_size, pop_min, gen_no+1, max_gen)
        elif modification == 'naive_bell':
            pop_size = mods.naive_bell(initial_pop_size, pop_min, gen_no+1, max_gen)
        
        # Create new solution
        new_solution= []
        for i in range(0,len(non_dominated_sorted_solution2)):
            non_dominated_sorted_solution2_1 = [fn.index_of(non_dominated_sorted_solution2[i][j],non_dominated_sorted_solution2[i] ) for j in range(0,len(non_dominated_sorted_solution2[i]))]
            front22 = fn.sort_by_vals(non_dominated_sorted_solution2_1, crowding_distance_values2[i])
            front = [non_dominated_sorted_solution2[i][front22[j]] for j in range(0,len(non_dominated_sorted_solution2[i]))]
            front.reverse()
            for value in front:
                new_solution.append(value)
                if(len(new_solution)==pop_size):
                    break
            if (len(new_solution) == pop_size):
                break
    
        new_solution = list(set(new_solution))
        
        solution = [solution2[i] for i in new_solution]
        
        # Iterate to next gen
        if 'dtlz' not in test_prob:
            fitness_tracker.append(evaluation.generational_distance(values, test_prob))
        
        gen_no = gen_no + 1
    
    return solution, values, pop_tracker, fitness_tracker


