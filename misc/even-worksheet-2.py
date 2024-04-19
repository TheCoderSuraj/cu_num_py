def revenue(x):
    return -0.1 * x**3 + 5 * x**2 + 50

def cost(x):
    return 0.05 * x**3 - 2 * x**2 + 20 * x + 10

def profit(x):
    return revenue(x) - cost(x)

def derivative_profit(x):
    h = 1e-5
    return (profit(x + h) - profit(x)) / h

def newton_raphson_optimization(initial_guess, tolerance=1e-5, max_iterations=100):
    x = initial_guess

    for _ in range(max_iterations):
        x -= profit(x) / derivative_profit(x)

        if abs(profit(x)) < tolerance:
            break

    return x

initial_guess = 10.0

optimal_surface_area = newton_raphson_optimization(initial_guess)

print("Optimal Surface Area:", optimal_surface_area)