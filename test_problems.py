import math



#%% DTLZ helpers
def g1(k, X_M):
    return 100 * (k + sum([(X_M[i]-0.5)**2 - math.cos(20*math.pi*(X_M[i]-0.5)) for i in range(len(X_M))]))

def g2(X_M):
    return sum([(X_M[i]-0.5)**2 for i in range(len(X_M))])

#%% dtlz1 https://pymoo.org/problems/many/dtlz.html

def dtlz1(n, M):
    k = n - M + 1
    
    def fx(x, o):
        gx = g1(k, x[-k:])
        if o == 0:
            product = 0.5
            for i in range(M-1):
                product *= x[i]
            return product*(1+fx)
        elif o == M-1: 
            return 0.5*(1-x[0])*(1+gx)
        else:
            product = 0.5
            for i in range(M-o-1):
                product *= x[i]
            product *= (1-x[M-o])
            return product * (1+gx)
    return fx


#%% dtlz2
def dtlz2(n, M):
    k = n - M + 1
    
    def fx(x, o):
        gx = g2(x[-k:])
        if o == 0:
            product = 1
            for i in range(M-1):
                product *= math.cos(x[i]*math.pi/2)
            return product * (1+gx)
        elif o == M-1:
            return math.sin(x[0]*math.pi/2)*(1+gx)
        else:
            product = 1
            for i in range(M-o-1):
                product *= math.cos(x[i]*math.pi/2)
            product *= math.sin(x[M-o]*math.pi/2)
            return product * (1+gx)
    return fx

#%% dtlz3

def dtlz3(n, M):
    k = n - M + 1
    
    def fx(x, o):
        gx = g1(k, x[-k:])
        if o == 0:
            product = 1
            for i in range(M-1):
                product *= math.cos(x[i]*math.pi/2)
            return product * (1+gx)
        elif o == M-1:
            return math.sin(x[0]*math.pi/2)*(1+gx)
        else:
            product = 1
            for i in range(M-o-1):
                product *= math.cos(x[i]*math.pi/2)
            product *= math.sin(x[M-o]*math.pi/2)
            return product * (1+gx)
    return fx

#%% dtlz4

def dtlz4(n, M):
    k = n - M + 1
    
    def fx(x, o):
        gx = g1(k, x[-k:])
        if o == 0:
            product = 1
            for i in range(M-1):
                product *= math.cos((x[i]**100)*math.pi/2)
            return product * (1+gx)
        elif o == M-1:
            return math.sin((x[0]**100)*math.pi/2)*(1+gx)
        else:
            product = 1
            for i in range(M-o-1):
                product *= math.cos((x[i]**100)*math.pi/2)
            product *= math.sin((x[M-o]**100)*math.pi/2)
            return product * (1+gx)
    return fx

#%% zdt1

def zdt1(n=30):
    def f1(x):
        return x[0]
    def g(x):
        sum_portion = sum([x[i] for i in range(1, n)])
        return 1 + (9.0/(n-1))*sum_portion
    def h(fx, gx):
        return 1 - math.sqrt(fx/gx)
    def f2(x):
        return g(x)*h(f1(x), g(x))
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
        return g(x)*h(f1(x), g(x))
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
        return g(x)*h(f1(x), g(x))
    return f1, f2
    
#%% zdt5

def zdt5(n=11):
    def u(x):
        return x
    def v(ux):
        if ux < 5: return 2 + ux
        elif ux == 5: return 1
    def f1(x):
        return 1 + u(x[0])
    def g(x):
        return sum([v(u(x[i])) for i in range(1, len(x))])
    def h(fx, gx):
        return 1/fx
    def f2(x):
        return g(x)*h(f1(x), g(x))
    return f1, f2

#%% zdt6

def zdt6(n=10):
    def f1(x):
        return 1-math.exp(-4*x[0])*(math.sin(6*math.pi*x[0])**6)
    
    def g(x):
        sum_portion = sum([x[i] for i in range(1, n)])
        return 1 + 9 * (sum_portion/9)**0.25
    def h(fx, gx):
        return 1 - (fx/gx)**2
    def f2(x):
        return g(x)*h(f1(x), g(x))
    
    return f1, f2









