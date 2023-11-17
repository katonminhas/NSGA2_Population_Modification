
import numpy as np
import math
from dtlz import DTLZ1, DTLZ2, DTLZ3, DTLZ4

# Return the actual pareto fronts of each problem
def get_actual_solution(problem_name, n_var, n_obj, n_pareto_points):
    if problem_name=='zdt1':
        x = np.linspace(0, 1, n_pareto_points)
        return np.array([x, 1 - np.sqrt(x)]).T
    if problem_name=='zdt2':
        x = np.linspace(0, 1, n_pareto_points)
        return np.array([x, 1 - np.power(x, 2)]).T
    if problem_name=='zdt3':
        regions = [[0, 0.0830015349],
                   [0.182228780, 0.2577623634],
                   [0.4093136748, 0.4538821041],
                   [0.6183967944, 0.6525117038],
                   [0.8233317983, 0.8518328654]]

        pf = []
        for r in regions:
            x1 = np.linspace(r[0], r[1], int(n_pareto_points / len(regions)))
            x2 = 1 - np.sqrt(x1) - x1 * np.sin(10 * np.pi * x1)
            pf.append(np.array([x1, x2]).T)
        pf = np.row_stack(pf)
        return pf
    if problem_name=='zdt4':
        x = np.linspace(0, 1, n_pareto_points)
        return np.array([x, 1 - np.sqrt(x)]).T
    if problem_name=='zdt5':
        x = 1 + np.linspace(0,1, n_pareto_points)*30
        pf = np.column_stack([x, 10/x])
        return pf
    if problem_name=='zdt6':
        x = np.linspace(0.2807753191, 1, n_pareto_points)
        return np.array([x, 1 - np.power(x, 2)]).T
    if problem_name=='dtlz1':
        return DTLZ1(n_var, n_obj)._calc_pareto_front()
    if problem_name=='dtlz2':
        return DTLZ2(n_var, n_obj)._calc_pareto_front()
    if problem_name=='dtlz3':
        return DTLZ3(n_var, n_obj)._calc_pareto_front()
    if problem_name=='dtlz4':
        return DTLZ4(n_var, n_obj)._calc_pareto_front()
    

def euclidean_dist(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    distance = np.sqrt(np.sum((point1 - point2) ** 2))
    return distance


def get_closest_dist(point, n_var, n_obj, current_pop, problem_name):
    front = get_actual_solution(problem_name, n_var, n_obj, current_pop)
    closest_dist = np.inf
    for actual_point in front:
        dist = euclidean_dist(point, actual_point)
        if dist < closest_dist:
            closest_dist = dist
    return closest_dist


# Takes values object
def generational_distance(front, n_var, n_obj, problem_name):
    closest_distances = []
    min_dist, max_dist = np.inf, -1
    front_length = len(front[0])
    for i in range(front_length):
        point = [front[o][i] for o in range(n_obj)]
        closest_dist = get_closest_dist(point, n_var, n_obj, front_length, problem_name)
        closest_distances.append(closest_dist)
        if closest_dist < min_dist:
            min_dist = closest_dist
        if closest_dist > max_dist:
            max_dist = closest_dist
    gen_dist = (sum([dist**2 for dist in closest_distances])**(1/2))/front_length
    avg_dist = np.mean(closest_distances)
    return gen_dist, avg_dist, min_dist, max_dist
    
    
    
    





