
import math
import random
import numpy as np


#%% Find index of list
def index_of(a,list_):
    if a in list_:
        return list_.index(a)
    else:
        return -1


#%% Fast Dominated Sort
def dominates(ind1, ind2, values):
    dominates_ind1 = False
    for obj in values.keys():
        value1_obj = values[obj][ind1]
        value2_obj = values[obj][ind2]
        
        if value1_obj < value2_obj:
            return False
        elif value1_obj > value2_obj:
            dominates_ind1 = True
    return dominates_ind1


def fast_non_dominated_sort(values):
    num_solutions = len(values[0])
    
    S = [[] for i in range(num_solutions)]
    front = [[]]
    n = [0 for i in range(num_solutions)]
    rank = [0 for i in range(num_solutions)]
    
    for p in range(num_solutions):
        S[p] = []
        n[p] = 0
        for q in range(num_solutions):
            if dominates(p, q, values):
                if q not in S[p]:
                    S[p].append(q)
            elif dominates(q, p, values):
                n[p] = n[p] + 1
        if n[p]==0:
            rank[p] = 0
            if p not in front[0]:
                front[0].append(p)
    
    i=0
    while front[i] != []:
        Q=[]
        for p in front[i]:
            for q in S[p]:
                n[q] = n[q]-1
                if n[q] == 0:
                    rank[q] = i + 1
                    if q not in Q:
                        Q.append(q)
        i = i + 1
        front.append(Q)
    del front[len(front) - 1]
    return front
    


#%% Calculate Crowding Distance
def sort_by_vals(list1, vals):
    sorted_list = []
    while(len(sorted_list)!=len(list1)):
        if index_of(min(vals),vals) in list1:
            sorted_list.append(index_of(min(vals),vals))
        vals[index_of(min(vals),vals)] = math.inf
    return sorted_list


def crowding_distance(values, front):
    if len(front) > 0:
        solutions_num = len(front)
        num_objectives = len(values)
        individual_crowding_distance = [0 for individual in front]
        for m in range(num_objectives):
            # Sort Front
            sorted_front = sort_by_vals(front, values[m].copy())
            individual_crowding_distance[0] = np.inf
            individual_crowding_distance[-1] = np.inf
            m_values = [values[m][individual] for individual in sorted_front]
            scale = max(m_values) - min(m_values)
            if scale == 0:
                scale = 1
            for i in range(1, solutions_num-1):
                individual_crowding_distance[i] += (values[m][sorted_front[i+1]] - values[m][sorted_front[i-1]]) / scale
        return individual_crowding_distance


#%% Crossover

def crossover(a, b, crossover_rate):
    crossed = []
    for i in range(len(a)):
        r = random.random()
        if r < crossover_rate:
            crossed.append((a[i] + b[i]) / 2)
        else:
            crossed.append(a[i])
    return crossed

#%% Mutation
def mutation(solution, mutation_rate, params):
    mutated_solution = []
    for s in solution:
        r = random.random()
        if r < mutation_rate:
            mutated_solution.append(params['min_x'] + (params['max_x'] - params['min_x']) * random.random())
        else:
            mutated_solution.append(s)
    return mutated_solution





