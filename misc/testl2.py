import numpy as np

# Function to calculate profit
def profit(surface_area, cost, power_production):
    revenue_per_unit_energy = 0.12  # Revenue per kWh
    revenue = revenue_per_unit_energy * power_production
    return revenue - cost

# Derivative of the profit function with respect to surface area
def derivative_profit_surface_area(surface_area, cost, power_production):
    delta = 1e-5
    return (profit(surface_area + delta, cost, power_production) - profit(surface_area, cost, power_production)) / delta

# Newton-Raphson Method for finding root of a function
def newton_raphson(func, derivative_func, initial_guess, *args, tolerance=1e-5, max_iterations=100):
    x = initial_guess
    for _ in range(max_iterations):
        x_new = x - func(x, *args) / derivative_func(x, *args)
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    return None

# Historical data
historical_data = {
    10: (100, 500, 200),  # area: (cost, power_production)
    20: (200, 600, 400),
    30: (300, 700, 600),
    40: (400, 800, 800),
    50: (500, 900, 1000)
}

# Find the optimal surface area
# Find the optimal surface area
optimal_surface_area = None
max_profit = float('-inf')
for area, data in historical_data.items():
    cost, power_production = data
    profit_func = lambda surface_area: -profit(surface_area, cost, power_production)
    derivative_func = lambda surface_area: -derivative_profit_surface_area(surface_area, cost, power_production)
    root = newton_raphson(profit_func, derivative_func, initial_guess=area)
    if root is not None:
        current_profit = profit(root, cost, power_production)
        if current_profit > max_profit:
            max_profit = current_profit
            optimal_surface_area = root

print("Optimal surface area:", optimal_surface_area)

print("Optimal surface area:", optimal_surface_area)
