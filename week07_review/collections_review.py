"""Reuse complete objects to inspect containers and a JSON round trip."""

from collections import deque
import json
from pathlib import Path

from objects_review import ReviewObstacle


def main():
    # BEGIN SNIPPET collections_list
    post = ReviewObstacle("post", (0.0, 0.0), 0.5)
    second = ReviewObstacle("second", (1.0, 0.0), 0.4)
    marker = ReviewObstacle("marker", (2.0, 0.0), 0.25)
    obstacles = [post, second]
    copied = list(obstacles)
    print("new list:", copied is not obstacles)
    print("same first object:", copied[0] is obstacles[0])
    copied[0].resize(0.75)
    copied.append(marker)
    print("list lengths:", len(obstacles), len(copied))
    print("original first radius:", obstacles[0].radius)
    # END SNIPPET collections_list

    # BEGIN SNIPPET collections_lookup
    by_name = {item.name: item for item in obstacles}
    print("lookup second:", by_name["second"].center)
    names = ["post", "second", "post"]
    seen = set()
    duplicates = []
    for name in names:
        if name in seen:
            duplicates.append(name)
        seen.add(name)
    print("duplicates:", duplicates)
    # END SNIPPET collections_lookup

    # BEGIN SNIPPET collections_deque
    fifo = deque(["inspect", "place", "reset"])
    lifo = deque(["inspect", "place", "reset"])
    print("FIFO removed:", fifo.popleft())
    print("FIFO remaining:", list(fifo))
    print("LIFO removed:", lifo.pop())
    print("LIFO remaining:", list(lifo))
    # END SNIPPET collections_deque

    # BEGIN SNIPPET json_roundtrip
    record = {"name": marker.name,
              "center": list(marker.center), "radius": marker.radius}
    text = json.dumps(record, allow_nan=False)
    print("JSON text:", text)
    output = Path("outputs/obstacle.json")
    output.parent.mkdir(exist_ok=True)
    output.write_text(text, encoding="utf-8")
    loaded = json.loads(output.read_text(encoding="utf-8"))
    restored = ReviewObstacle(
        loaded["name"], loaded["center"], loaded["radius"]
    )
    print("loaded type:", type(loaded).__name__)
    print("restored:", restored.name, restored.center, restored.radius)
    # END SNIPPET json_roundtrip


if __name__ == "__main__":
    main()
