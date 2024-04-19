import numpy as np

# Define function to integrate
def f(x):
    return np.sin(x)

# Implementing trapezoidal method
def trapezoidal(func,x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    integration = func(x0) + func(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integration = integration + 2 * func(k)
    
    # Finding final integration value
    integration = integration * h/2
    
    return integration
    

print(trapezoidal(f, 0,np.pi,11))

def f2(x):
    return np.log(x)

print(trapezoidal(f2, 4,5.2,6))
