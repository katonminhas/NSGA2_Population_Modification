
import numpy as np
import math

# Return the actual pareto fronts of each problem
def get_actual_solution(problem_name, n_pareto_points):
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
    if problem_name=='zdt6':
        x = np.linspace(0.2807753191, 1, n_pareto_points)
        return np.array([x, 1 - np.power(x, 2)]).T
    
    
    

def euclidean_dist(point1, point2):
    squared_distance = sum((p1-p2)**2 for p1, p2 in zip(point1, point2))
    distance = math.sqrt(squared_distance)
    return distance

# Takes values object
def generational_distance(front, problem_name):
    actual_front = get_actual_solution(problem_name, len(front)*100)
    
    # For point in front
    # calculate distance between each point in actual front, keeping track of the closest
    # append the closest to a list
    closest_distances = []
    for i in range(len(front[0])):
        front_point = [front[o][i] for o in front.keys()]
        closest_dist = np.inf
        for actual_point in actual_front:
            dist = euclidean_dist(front_point, actual_point)
            if dist < closest_dist:
                closest_dist = dist
        closest_distances.append(closest_dist)
    
    return (np.sum(closest_distances)**(1/len(front)))/len(front[0])



