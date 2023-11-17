import numpy as np
import math
import evaluation 

#%%

# Proportional population decline (Salgotra et al)
def proportional(pop_size, pop_min, gen_no, fitness_tracker):
    
    def get_delta_t_best(fitness_tracker, gen_no):
        return (fitness_tracker[gen_no-2]-fitness_tracker[gen_no-1]) / np.abs(fitness_tracker[gen_no-1])
    if gen_no > 2:
        # Calculate delfa_t_best
        delta_t_best = get_delta_t_best(fitness_tracker, gen_no)
        new_pop_size = (1-delta_t_best)*pop_size
        return round(max(new_pop_size, pop_min))
    else:
        return pop_size

def inverse_proportional(pop_size, pop_min, gen_no, fitness_tracker):
    
    def get_delta_t_best(fitness_tracker, gen_no):
        return (fitness_tracker[gen_no-1]-fitness_tracker[gen_no-2]) / np.abs(fitness_tracker[gen_no-2])
    if gen_no > 2:
        # Calculate delfa_t_best
        delta_t_best = get_delta_t_best(fitness_tracker, gen_no)
        new_pop_size = (1-delta_t_best)*pop_size
        return round(max(new_pop_size, pop_min))
    else:
        return pop_size

    
# Decrease the population linearly between the starting population and pop_min
def naive_linear(initial_pop_size, pop_min, gen_no, max_gen):
    slope = (initial_pop_size - pop_min) / max_gen
    new_population = initial_pop_size - slope * gen_no
    new_population = max(new_population, pop_min)
    return round(new_population)


def naive_power(initial_pop_size, pop_min, gen_no, max_gen):
    # Calculate the population decrease using a power function
    exponent = 2  # Adjust the exponent for the desired effect
    decrease_factor = (initial_pop_size - pop_min) / (max_gen ** exponent)
    new_population = initial_pop_size - (decrease_factor * (gen_no ** exponent))
    return round(max(new_population, pop_min))

def naive_bell(initial_pop_size, pop_min, gen_no, max_gen):
    if gen_no <= max_gen / 2:  # Logarithmic increase phase
        target_pop_size = 2 * initial_pop_size
        # Applying a logarithmic growth formula
        increase_factor = math.log(gen_no+1) / math.log(max_gen / 2 + 1)
        new_population = initial_pop_size + (target_pop_size - initial_pop_size) * increase_factor
    else:  # Exponential decrease phase
        target_pop_size = pop_min
        decrease_factor = math.log(gen_no + 1) / math.log(max_gen/4 + 1 )
        new_population = 2*initial_pop_size - (gen_no-max_gen/2)**decrease_factor

    # Ensure the population size doesn't exceed the limits
    new_population = max(new_population, pop_min)
    return round(new_population)
    
    
    
    
