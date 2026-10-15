"""Independent chapter practice, not the Assignment 3 Configuration solution.

This small class demonstrates initialization and method calls only.
It does not implement the assignment's input-validation contract.
"""


class Configuration:
    def __init__(self, values):
        self.values = tuple(values)

    def dimension(self):
        return len(self.values)


q_start = Configuration((0.0, 0.0))
q_goal = Configuration((3.2, 2.0))

print(q_start.values)
print(q_start.dimension())
print(q_start is q_goal)
