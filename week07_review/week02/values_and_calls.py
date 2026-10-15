start = (0.0, 0.0)
goal = (3.0, 4.0)

dx = goal[0] - start[0]
dy = goal[1] - start[1]
squared_length = dx * dx + dy * dy

def finish_distance(value):
    return value**0.5

distance = finish_distance(squared_length)
print(distance)

start = (0.0, 0.0)
corner = (3.0, 0.0)
goal = (3.0, 4.0)
waypoints = [start, corner]
waypoints.append(goal)

x_goal, y_goal = goal
first_two = waypoints[:2]
print(waypoints[1], first_two, x_goal, y_goal)

segments = []
for p0, p1 in zip(waypoints[:-1], waypoints[1:]):
    displacement = (p1[0] - p0[0], p1[1] - p0[1])
    segments.append(displacement)

for index, displacement in enumerate(segments):
    print(index, displacement)

segments_comp = [
    (p1[0] - p0[0], p1[1] - p0[1])
    for p0, p1 in zip(waypoints[:-1], waypoints[1:])
]
