"""Independent chapter practice, not the Assignment 3 PlanningRun solution.

PracticeHistory records string labels, not planning objects. Its simplified
contract accepts a string with at least one non-whitespace character, preserves
that label, and rejects invalid input without changing history.
"""

from dataclasses import dataclass, field


@dataclass
class PracticeHistory:
    _labels: list[str] = field(default_factory=list, init=False, repr=False)

    def record(self, label: str) -> None:
        if not isinstance(label, str) or not label.strip():
            raise ValueError("label must be a non-empty string")
        self._labels.append(label)

    @property
    def results(self) -> tuple[str, ...]:
        return tuple(self._labels)


def main():
    first = PracticeHistory()
    second = PracticeHistory()
    earlier_snapshot = first.results

    first.record("first attempt")
    print("first history:", first.results)
    print("second history:", second.results)
    print("earlier snapshot:", earlier_snapshot)

    before = first.results
    try:
        first.record("   ")
    except ValueError as error:
        print("invalid update rejected:", error)

    print("history unchanged:", first.results == before)


if __name__ == "__main__":
    main()
