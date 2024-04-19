ERROR = 0.0001

def func(a):
    return a**2+a-1

def bisection(a,b):
    if func(a) * func(b) >= 0:
        return None
    prev = 0.0
    while(True):
        c = (a+b)/2
        sol = func(c)
        if sol == 0 or abs(sol - prev) < ERROR:
            return c
        elif sol > 0:
            b = c
        else:
            a = c
        prev = sol

print(f"the root is: {bisection(0,1)}")