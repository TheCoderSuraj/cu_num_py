# # function
# def func(x):
#     return np.sin(x)


# import numpy as np

# def trap_2(func,a,b,n):
#     h = b-a/n
#     x = np.linspace(a,b,n + 1)
#     y = func(x)

#     return h * (np.sum(y[1:-1]) - 0.5 * (y[0] + y[-1]))


# # 0-pi integral sinXdx
# # a = 0, b = pi, n = 11

# print(trap_2(func,a=0,b=np.pi,n=11))

# def func2(x):
#     return np.log(x)

# print(trap_2(func2, a= 4,b = 5.2,n=6))