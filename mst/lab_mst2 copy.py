# even 29 feb
import sympy as sp

unit_price = 0.12  
cs = 16.5
eff = 10


# Function to calculate profit
def profit(surface_area):
    return eff * surface_area * unit_price - surface_area * cs

def profit_derivative(surface_area):
    # Define symbols
    surface_area_sym = sp.Symbol('surface_area')
    cs_sym = sp.Symbol('cs')
    eff_sym = sp.Symbol('eff')
    unit_price_sym = sp.Symbol('unit_price')

    # Define the profit function
    profit_func = eff_sym * surface_area_sym * unit_price_sym - surface_area_sym * cs_sym

    # Calculate the derivative
    derivative = sp.diff(profit_func, surface_area_sym)

    # Substitute the given values
    derivative = derivative.subs({cs_sym: cs, eff_sym: eff, unit_price_sym: unit_price, surface_area_sym: surface_area})

    return derivative


def newton_raphson(x1, tolerance=0.0001, max_iterations=100):
    itt = 0
    while(itt < max_iterations):
        x2 = x1 - profit(x1)/profit_derivative(x1)

        if profit(x2) == 0 or abs(profit(x2) - profit(x1)) < tolerance:
            return x2
        x1 = x2
        itt += 1

    return x1

# Historical data
# area: (cost, power_production)
historical_data = {
    10: (165, 100), 
    20: (190, 315),
    30: (300, 425),
    40: (320, 521),
    50: (450, 856)
}

# optimal_surface_area = max(historical_data.keys(), key=lambda x: profit(x, *historical_data[x]))
lis = []
# for key, values in historical_data.items():
#     cs = values[0]/key
#     eff = values[1]/key
#     lis.append(newton_raphson(10))


# print("Optimal surface area:", max(lis))

print(profit(0), profit_derivative(0),profit(0)/profit_derivative(0))
# print(newton_raphson(10))
