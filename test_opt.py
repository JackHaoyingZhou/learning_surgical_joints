

from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable


def opt(x,y):
    return x + 2 * y

model = LpProblem(name="small-problem", sense=LpMaximize)

# Initialize the decision variables
x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)

# Add the constraints to the model
model += (2 * x + y <= 20, "red_constraint")
model += (4 * x - 5 * y >= -10, "blue_constraint")
model += (-x + 2 * y >= -2, "yellow_constraint")
model += (-x + 5 * y == 15, "green_constraint")

model += opt(x,y)


status = model.solve()



model += lpSum([fat[f] * food_vars[f] for f in food_items]) >= 20.0, "FatMinimum"