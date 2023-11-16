import math

#%% dev_test
def function1(x):
    value = -x**2
    return value

#Second function to optimize
def function2(x):
    value = -(x-2)**2
    return value




#%%
def g1(k, X_M):
    return 100 * (k + sum([(X_M[i]-0.5)**2 - math.cos(20*math.pi*(X_M[i]-0.5)) for i in range(len(X_M))]))
                  
def g2(X_M):
    return sum([(X_M[i]-0.5)**2 for i in range(len(X_M))])


# def obj_func(self, X_, g):
#     f = []

#     for i in range(0, self.n_obj):
#         _f = 0.5 * (1 + g)
#         _f *= anp.prod(X_[:, :X_.shape[1] - i], axis=1)
#         if i > 0:
#             _f *= 1 - X_[:, X_.shape[1] - i]
#         f.append(_f)

#     return anp.column_stack(f)

#%% dtlz1 https://pymoo.org/problems/many/dtlz.html


# Create the oth function in a dtlz1 problem
# def dtlz1(n, M):
#     k = n - M + 1
    
#     # Define F_o(x) - this is the function that will be called in main
#     def fx(x, o):
#         final_term = (1 + g1(k, x[-k:]))
        
#         # Edge case o==0
#         if o==0:
#             product = 0.5
#             for i in range(0, M-1):
#                 product *= x[i]
#             return product * final_term
#         else:
#             product=0.5
#             for i in range(0, M-o):
#                 if i != (M-o-1):
#                     product *= x[i]
#                 else:
#                     product *= (1-x[i])
#             return product * final_term
        
#     return fx
    


#%% zdt1

def zdt1(n=30):
    def f1(x):
        return x[0]
    def g(x):
        sum_portion = sum([x[i] for i in range(1, n)])
        return 1 + (9/(n-1))*sum_portion
    def h(fx, gx):
        return 1 - math.sqrt(fx/gx)
    def f2(x):
        return h(f1(x), g(x))
    return f1, f2
    
#%% zdt2

def zdt2(n=30):
    def f1(x):
        return x[0]
    def g(x):
        sum_portion = sum([x[i] for i in range(1, n)])
        return 1 + (9/(n-1))*sum_portion
    def h(fx, gx):
        return 1 - (fx/gx)**2
    def f2(x):
        return h(f1(x), g(x))
    return f1, f2

#%% zdt3

def zdt3(n=30):
    def f1(x):
        return x[0]
    def g(x):
        sum_portion = sum([x[i] for i in range(1, n)])
        return 1 + (9/(n-1))*sum_portion
    def h(fx, gx):
        return 1 - math.sqrt(fx/gx) - (fx/gx)*math.sin(10*math.pi*fx)
    def f2(x):
        return h(f1(x), g(x))
    return f1, f2

#%% zdt4

def zdt4(n=10):
    def f1(x):
        return x[0]
    def g(x):
        sum_portion = sum([x[i]**2 - 10*math.cos(4*math.pi*x[i]) for i in range(1, n)])
        return 1 + 10*(n-1) + sum_portion
    def h(fx, gx):
        return 1 - math.sqrt(fx/gx)
    def f2(x):
        return h(f1(x), g(x))
    return f1, f2
    

#%% zdt6

def zdt6(n=10):
    def f1(x):
        return 1-math.exp(-4*x[0])*math.sin(6*math.pi*x[0])**6
    
    def g(x):
        sum_portion = sum([x[i] for i in range(1, n)])
        return 1 + 9 * (sum_portion/9)**0.25
    def h(fx, gx):
        return 1 - (fx/gx)**2
    def f2(x):
        return h(f1(x), g(x))
    
    return f1, f2
