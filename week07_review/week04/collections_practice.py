from ap_week04_scene_data import Configuration, Obstacle, PlanningModelError

print("[1.2 Obstacle object]")
obstacle_b = Obstacle(
    obstacle_id="obstacle_b",
    center=Configuration((6.5, 4.0)),
    radius_m=0.6,
)
print("ID:", obstacle_b.obstacle_id)
print("centre:", obstacle_b.center.values)
print("radius (m):", obstacle_b.radius_m)

try:
    Obstacle("invalid", Configuration((6.5, 4.0)), 0.0)
except PlanningModelError as error:
    print(type(error).__name__ + ":", error)

print("[2.1 List]")
obstacle_a = Obstacle("obstacle_a", Configuration((3.0, 2.0)), 0.75)
obstacle_c = Obstacle("obstacle_c", Configuration((8.2, 6.2)), 0.45)
obstacles = [obstacle_a, obstacle_b, obstacle_c]

print(obstacles[0].obstacle_id)
print([item.obstacle_id for item in obstacles[1:]])
working = obstacles.copy()
working.append(obstacle_b)
print("original count:", len(obstacles))
print("copied count:", len(working))
print("same obstacle_b:", working[1] is obstacle_b)

print("[2.2 Dictionary]")
obstacle_by_id = {}
for item in obstacles:
    obstacle_by_id[item.obstacle_id] = item

print("radius (m):", obstacle_by_id["obstacle_b"].radius_m)
print("same obstacle_b:", obstacle_by_id["obstacle_b"] is obstacle_b)
print("missing ID present:", "missing_id" in obstacle_by_id)

print("[2.3 Set]")
sample = obstacles + [obstacles[0], obstacle_b]
seen = set()
duplicates = set()

for obstacle in sample:
    obstacle_id = obstacle.obstacle_id
    if obstacle_id in seen:
        duplicates.add(obstacle_id)
    else:
        seen.add(obstacle_id)

print(sorted(duplicates))

from ap_week04_scene_data import ConfigurationBounds, PlanningProblem

print("[2.4 Request objects]")
bounds = ConfigurationBounds(
    lower=Configuration((0.0, 0.0)),
    upper=Configuration((10.0, 8.0)),
)
request_1 = PlanningProblem(
    problem_id="request_1",
    start=Configuration((1.0, 1.0)),
    goal=Configuration((9.0, 7.0)),
    bounds=bounds,
)
request_2 = PlanningProblem(
    problem_id="request_2",
    start=Configuration((1.0, 7.0)),
    goal=Configuration((9.0, 1.0)),
    bounds=bounds,
)
requests = [request_1, request_2]
print("arrival order:", [item.problem_id for item in requests])

from collections import deque

print("[2.4 FIFO queue]")
request_queue = deque(requests)
current = request_queue.popleft()

print("returned:", current.problem_id)
print("remaining:", [item.problem_id for item in request_queue])
print("original:", [item.problem_id for item in requests])
print("same request:", current is request_1)

print("[2.4 LIFO stack]")
stack = deque(requests)
print("returned:", stack.pop().problem_id)
print("remaining:", [item.problem_id for item in stack])
