import test_problems
import random
from individual import Individual
import evaluation


def initialize(problem_name, pop_size, n=10, M=10):
        
    # Simple 2-function problem for testing
    if problem_name == 'dev_test':
        params = {'min_x' : -55, 'max_x' : 55}
        solutions = [params['min_x']+(params['max_x']-params['min_x'])*random.random() for i in range(pop_size)] # solutions is a list of floats
        functions = [test_problems.function1, test_problems.function2]
        return solutions, functions, params
    
    
    # DTLZ
    if problem_name=='dtlz1':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : n}
        population = [Individual(solution=[random.random() for i in range(params['n'])],
                                 age=0,
                                 lifetime=-1)
                      for p in range(pop_size)]
        
        functions = test_problems.dtlz1(n, M)
        return population, functions, params
    if problem_name=='dtlz2':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : n}
        population = [Individual(solution=[random.random() for i in range(params['n'])],
                                 age=0,
                                 lifetime=-1)
                      for p in range(pop_size)]
        
        functions = test_problems.dtlz2(n, M)
        return population, functions, params
    if problem_name=='dtlz3':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : n}
        population = [Individual(solution=[random.random() for i in range(params['n'])],
                                 age=0,
                                 lifetime=-1)
                      for p in range(pop_size)]
        
        functions = test_problems.dtlz3(n, M)
        return population, functions, params
    if problem_name=='dtlz4':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : n}
        population = [Individual(solution=[random.random() for i in range(params['n'])],
                                 age=0,
                                 lifetime=-1)
                      for p in range(pop_size)]
        
        functions = test_problems.dtlz4(n, M)
        return population, functions, params
    
    # ZDT
    if problem_name=='zdt1':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : 30}
        population = [Individual(solution=[random.random() for i in range(params['n'])],
                                 age=0,
                                 lifetime=-1)
                      for p in range(pop_size)]
        
        functions = test_problems.zdt1(30)
        return population, functions, params
    
    if problem_name=='zdt2':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : 30}
        population = [Individual(solution=[random.random() for i in range(params['n'])],
                                 age=0,
                                 lifetime=-1)
                      for p in range(pop_size)]
        
        functions = test_problems.zdt2()
        return population, functions, params
    if problem_name=='zdt3':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : 30}
        population = [Individual(solution=[random.random() for i in range(params['n'])],
                                 age=0,
                                 lifetime=-1)
                      for p in range(pop_size)]
        
        functions = test_problems.zdt3()
        return population, functions, params
    if problem_name=='zdt4':
        params = {'min_x' : 0, 'max_x' : 1, 'n' : 10}
        population = [Individual(solution=[random.random() for i in range(params['n'])],
                                 age=0,
                                 lifetime=-1)
                      for p in range(pop_size)]
        
        functions = test_problems.zdt4()
        return population, functions, params
    
    
    
    