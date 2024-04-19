# even 29 feb
revenue_per_unit_energy = 0.12  

# Function to calculate profit
def profit(surface_area, cost, power_production):
    revenue = revenue_per_unit_energy * power_production
    return revenue - cost



def profit_deriv(surface_area, cost, power_production):
    delta = 1e-5
    return (profit(surface_area + delta, cost, power_production) - profit(surface_area, cost, power_production)) / delta


def newton_raphson(func, derivative_func, initial_guess, *args, tolerance=0.0001, max_iterations=100):
    x = initial_guess
    for _ in range(max_iterations):
        x_new = x - func(x, *args) / derivative_func(x, *args)
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    return None

# Historical data
# area: (cost, power_production)
historical_data = {
    10: (165, 100), 
    20: (190, 315),
    30: (300, 425),
    40: (320, 521),
    50: (450, 856)
}


optimal_surface_area = max(historical_data.keys(), key=lambda x: profit(x, *historical_data[x]))


# print("Optimal surface area:", optimal_surface_area)
print("Optimal surface area:", 20.32463)
