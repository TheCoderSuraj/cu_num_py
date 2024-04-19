from sympy import *
 
ERROR = 0.0001
x = symbols('x')
expr = x**2 + x - 1

def func(a):
    # return a**2+a-1
    return expr.subs(x,a)


def funcDif(a):
    expr_diff = Derivative(expr, x) 
    return expr_diff.subs(x,a)
  


def newtonRaphson(x1):
    if func(x1) > 0:
        return None
    
    while(True):
        x2 = x1 - func(x1)/funcDif(x1)
        if func(x2) == 0 or abs(func(x2) - func(x1)) < ERROR:
            return x2
        x1 = x2


print(f"the root is: {newtonRaphson(0)}")