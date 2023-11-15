import test_problems
import random


def initialize(problem_name, pop_size, n=10, M=10):
    # Simple 2-function problem for testing
    if problem_name == 'dev_test':
        params = {'min_x' : -55, 'max_x' : 55}
        solutions = [params['min_x']+(params['max_x']-params['min_x'])*random.random() for i in range(pop_size)] # solutions is a list of floats
        functions = [test_problems.function1, test_problems.function2]
        return solutions, functions, params
    
    
    # DTLZ
    if problem_name=='dtlz1':
        params = {'min_x' : 0, 'max_x' : 1}
        solutions = [[random.random() for ind in range(n)] for i in range(pop_size)] # solutions is a list of dicts of floats
        functions = test_problems.dtlz1(n, M) # return list of test problems 
        return solutions, functions, params
    
    
    # ZDT
    if problem_name=='zdt1':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : 30}
        n=params['n']
        solutions = [[random.random() for ind in range(n)] for i in range(pop_size)]
        functions = test_problems.zdt1(n)
        return solutions, functions, params
    if problem_name=='zdt2':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : 30}
        n=params['n']
        solutions = [[random.random() for ind in range(n)] for i in range(pop_size)]
        functions = test_problems.zdt2(n)
        return solutions, functions, params
    if problem_name=='zdt3':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : 30}
        n=params['n']
        solutions = [[random.random() for ind in range(n)] for i in range(pop_size)]
        functions = test_problems.zdt3(n)
        return solutions, functions, params
    if problem_name=='zdt4':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : 10}
        n=params['n']
        solutions = [[random.random() for ind in range(n)] for i in range(pop_size)]
        functions = test_problems.zdt4(n)
        return solutions, functions, params
    if problem_name=='zdt5':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : 11}
        n=params['n']
        def create_solution(n):
            x1 = int(''.join(str(random.randint(0, 1)) for _ in range(30)))
            x_other = [int(''.join(str(random.randint(0, 1)) for _ in range(5))) for i in range(n-1)]
            return [x1]+x_other
        solutions = [create_solution(n) for i in range(pop_size)]
        functions = test_problems.zdt5(n)
        return solutions, functions, params
    if problem_name=='zdt6':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : 10}
        n=params['n']
        solutions = [[random.random() for ind in range(n)] for i in range(pop_size)]
        functions = test_problems.zdt6(n)
        return solutions, functions, params
    
    
    
    
    