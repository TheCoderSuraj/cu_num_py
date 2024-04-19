from pulp import *

# Create a LP maximization problem
prob = LpProblem("Portfolio Optimization", LpMaximize)

#  decision variable
x = LpVariable("x", lowBound=300000, upBound=600000)  # Investment in X
y = LpVariable("y", lowBound=200000, upBound=400000)  # Investment in Y
z = LpVariable("z", lowBound=100000, upBound=300000)  # Investment in Z

# objective function )
prob += 0.08 * x + 0.06 * y + 0.05 * z  # Adjust expected returns based on actual values

# Define constraints
prob += x + y + z == 1000000  # Total investment should equal $1,000,000

# constraints for minimum investment 
prob += x >= 300000
prob += y >= 200000
prob += z >= 100000

prob.solve()

print("Optimal Investment Strategy:")
for v in prob.variables():
    print(f"{v.name}: ${v.varValue:.2f}")

print(f"Expected Return: ${value(prob.objective):.2f}")