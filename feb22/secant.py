ERROR = 0.0001

def func(a):
    return a**2+a-1

def secant(x0,x1):
    if func(x0) * func(x1) >= 0:
        return None
    
    while(True):
        num = (x0*func(x1) - x1 * func(x0))
        det = func(x1) - func(x0)
        x2 = num/det 
        if func(x2) == 0 or abs(func(x2) - func(x1)) < ERROR:
            return x2
        x0 = x1
        x1 = x2


print(f"the root is: {secant(0,1)}")