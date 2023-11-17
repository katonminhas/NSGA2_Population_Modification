
#%% Imports
import os, sys
if "C:/Users/katon/Documents/JHU/Evo_Swarm/Research_Paper/" not in sys.path:
    sys.path.append("C:/Users/katon/Documents/JHU/Evo_Swarm/Research_Paper/")
import func as fn
from initialization import initialize
from individual import Individual
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
    population, functions, params = initialize(problem_name=test_prob, 
                                             pop_size=pop_size, 
                                             n=solution_size, 
                                             M=problem_size)
    
    
    initial_pop_size = pop_size
    pop_tracker = []
    fitness_tracker = []
    min_lifetime, max_lifetime = 1, 10
    
    
   
    # Main Loop
    gen_no=0
    while (gen_no<max_gen) :
        if gen_no%100 ==0: print("Generation: ", gen_no)
        pop_tracker.append(len(population))      
        #print("Pop length: ", len(population))
        # for ind in population:
        #     ind.print()
        
        # Get fitness values of current solution
        if 'dtlz' not in test_prob:
            values = {o : [functions[o](population[i].solution) for i in range(len(population))] for o in range(len(functions))}      
        else:
            values = {o : [functions(population[i].solution, o) for i in range(len(population))] for o in range(problem_size)}
        
        
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
        
        population2 = population.copy()
        #Generating offsprings
        while(len(population2)!=2*len(population)):
            a1 = random.randint(0,len(population)-1)
            b1 = random.randint(0,len(population)-1)
            cross_solution = fn.crossover(population[a1].solution, population[b1].solution, crossover_rate)
            offspring_solution = fn.mutation(cross_solution, mutation_rate, params, test_prob)
            new_individual = Individual(solution=offspring_solution, age=0, lifetime=-1)
            population2.append(new_individual)
        
        if 'dtlz' not in test_prob:
            values2 = {o : [functions[o](population2[i].solution) for i in range(len(population2))] for o in range(len(functions))}
        else: 
            values2 = {o : [functions(population2[i].solution, o) for i in range(len(population2))] for o in range(problem_size)}
        
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
        new_population= []
        for i in range(0,len(non_dominated_sorted_solution2)):
            non_dominated_sorted_solution2_1 = [fn.index_of(non_dominated_sorted_solution2[i][j],non_dominated_sorted_solution2[i] ) for j in range(0,len(non_dominated_sorted_solution2[i]))]
            front22 = fn.sort_by_vals(non_dominated_sorted_solution2_1, crowding_distance_values2[i])
            front = [non_dominated_sorted_solution2[i][front22[j]] for j in range(0,len(non_dominated_sorted_solution2[i]))]
            front.reverse()
            for value in front:
                new_population.append(value)
                if(len(new_population)==pop_size):
                    break
            if (len(new_population) == pop_size):
                break
    
        new_population = list(set(new_population))
        #print("New solution: ", new_solution)
        population = [population2[i] for i in new_population]
        

        # Iterate to next gen
        gen_dist, min_dist, max_dist = evaluation.generational_distance(values , solution_size, problem_size, test_prob)
        gen_fitness = round(gen_dist, 3)
        fitness_tracker.append(gen_fitness)
        
        # Initialize lifetimes
        for ind in population:
            if ind.lifetime == -1:
                ind.set_lifetime(fitness_tracker, min_dist, max_dist, min_lifetime, max_lifetime, functions, solution_size, problem_size, len(population), test_prob)

        # Increase age
        for ind in population:
            ind.age += 1
            
        # remove based on age
        if modification == 'gavaps':
            keep_idx = []
            for i in range(len(population)):
                ind = population[i]
                if ind.age < ind.lifetime:
                    keep_idx.append(i)
            population = [population[i] for i in keep_idx]
        
        gen_no = gen_no + 1
    
    
    return population, values, pop_tracker, fitness_tracker