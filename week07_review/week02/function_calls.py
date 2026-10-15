from learning_geometry import distance_example

print(distance_example((0.0, 0.0), (3.0, 4.0)))
print(distance_example(goal_xy=(3.0, 4.0), start_xy=(0.0, 0.0)))
pair = ((0.0, 0.0), (3.0, 4.0))
print(distance_example(*pair))

from learning_geometry import distance_example, PathInputError

for goal in [(3.0, 4.0), (True, 4.0), (3.0,), (float("nan"), 4.0)]:
    try:
        print(distance_example((0.0, 0.0), goal))
    except PathInputError as error:
        print(error)
