import json
from ap_week04_scene_data import Configuration, Obstacle

print("[4.1 JSON text]")
obstacle_b = Obstacle("obstacle_b", Configuration((6.5, 4.0)), 0.6)
obstacle_record = {
    "obstacle_id": obstacle_b.obstacle_id,
    "center": list(obstacle_b.center.values),
    "radius_m": obstacle_b.radius_m,
}
text = json.dumps(obstacle_record)
loaded = json.loads(text)

print(text)
print("text type:", type(text).__name__)
print("loaded type:", type(loaded).__name__)
print("same values:", loaded == obstacle_record)

from pathlib import Path

print("[4.1 JSON file]")
path = Path("practice/obstacle_practice.json")
path.write_text(json.dumps(loaded, indent=2), encoding="utf-8")
reloaded = json.loads(path.read_text(encoding="utf-8"))

print("saved:", path.name)
print("same values:", reloaded == loaded)
