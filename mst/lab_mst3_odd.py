"""
Even: Write a python program to implement the composite trapozidal rule for numerically evaluating the integral [-1,2] |(e^(-x^2))dx using n = 16 equal subintervals.
Print the approximate value of the integral
"""
import numpy as np
import math



def func(x):
    # return np.exp((-x)**2)
    return math.e ** ((-x) ** 2)

def trapozidal(func, a, b,n):
    h = (b - a)/n

    # h/2[(last + first) + 2 * rest]
    fx = []
    for i in range(0, n): 
        fx.append(func(a + h*i))


    sum = fx[0] + fx[-1]

    for i in range(1,n-1):
        sum = sum + 2 * fx[i]
        # print(i,sum)

    res = h/2 * sum 
    return res
    
    # print(fx)

ans = trapozidal(func,a=-1,b=2,n=16)
print("the trapozidal value is ",ans)

