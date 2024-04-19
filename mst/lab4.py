'''
Even: 
You are planning to build a portfolio of investments consisting of three assets: Asset X, Asset Y, and Asset Z. Each asset has a certain expected return and risk associated with it. You have a total of $1,000,000 to invest. However, you also have the following constraints and Maximize the expected return on investment while minimizing the risk.

Ø  You want to invest at least $300,000 in Asset X.
Ø  You want to invest at least $200,000 in Asset Y.
Ø  You want to invest at least $100,000 in Asset Z.
Ø  You cannot invest more than $600,000 in Asset X.
Ø  You cannot invest more than $400,000 in Asset Y.
Ø  You cannot invest more than $300,000 in Asset Z.
'''

import numpy as np
from scipy.optimize import minimize


expected_returns = np.array([0.12, 0.09, 0.15])
covariance_matrix = np.array(
    [[0.015, 0.005, 0.008], [0.005, 0.009, 0.004], [0.008, 0.004, 0.020]]
)

# constraints based on question
cons = (
    {"type": "eq", "fun": lambda x: np.sum(x) - 1}, # sum of all amounts = 1
    # given constraints
    {"type": "ineq", "fun": lambda x: x[0] - 0.3},
    {"type": "ineq", "fun": lambda x: x[1] - 0.2},
    {"type": "ineq", "fun": lambda x: x[2] - 0.1},
    {"type": "ineq", "fun": lambda x: 0.6 - x[0]},
    {"type": "ineq", "fun": lambda x: 0.4 - x[1]},
    {"type": "ineq", "fun": lambda x: 0.3 - x[2]},
)

# objective function
def objective(amount):
    portfolio_return = amount.dot(expected_returns)
    portfolio_variance = amount.T.dot(covariance_matrix).dot(amount)
    return -(portfolio_return - 0.5 * portfolio_variance)

# initial guess
init_guess = np.array([0.33, 0.33, 0.34])


result = minimize(objective, init_guess, method="SLSQP", constraints=cons)

# results
rets = []
for prof, amt in zip(expected_returns, result.x * 1_000_000):
    rets.append(prof * amt)

optimal_amount = result.x
returns = optimal_amount.dot(expected_returns)
print("Optimal Amount: ", optimal_amount * 1_000_000)
print(returns * 1_000_000)
print(np.sum(rets))
