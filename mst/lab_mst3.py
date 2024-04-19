"""
Even: Write a python program to implement the composite trapezoidal rule for numerically evaluating the integral [-1,2] f(x) = (e^(-x^2))dx using n = 16 equal sub-intervals.
Print the approximate value of the integral
"""
import numpy as np

def func(x):
    return np.exp(-(x**2))

def trapezoidal(func, a, b,n):
    h = (b - a)/n

    # h/2[(last + first) + 2 * rest]
    fx = []
    for i in range(0, n+1): 
        fx.append(func(a + h*i))
        # print(i, func(a + h*i))

    sum = fx[0] + fx[-1]

    for i in range(1,n):
        sum = sum + 2 * fx[i]
        # print(i,sum)

    res = h/2 * sum 
    return res
    
    # print(fx)

ans = trapezoidal(func,a=-1,b=2,n=16)
print("the trapezoidal value is ",ans)

