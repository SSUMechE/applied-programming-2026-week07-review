# Week 7 review files

These files reuse the original Week 2–5 teaching examples. This is not a new
Assignment. No new package installation, private repository or LMS submission
is required for these review runs.

Use Anaconda Prompt and the existing `applied-programming-w06` environment.
Extract the ZIP outside your Assignment repositories. Start in `week07_review`.

```text
conda activate applied-programming-w06
```

## Functions and NumPy — Week 2

`learning_geometry.py` contains the original complete function definitions.
The small execution files collect the original Reading's code blocks without
changing their calculations or values. Running the definition file alone does
not print a demonstration.

```text
cd week02
python values_and_calls.py
python function_calls.py
python tolerance_examples.py
python array_examples.py
python -m pytest -q test_learning_geometry.py
cd ..
```

The original three tests should pass. `example_wrong_distance.py` is the
original deliberately incorrect example, not a broken supplied solution.

## Objects and history — Week 3

The ordinary `Configuration` class and frozen dataclass are in separate files,
as in the original practice. The ordinary example calls `dimension()`. The
dataclass example reads the `dimension` property without parentheses.

```text
cd week03
python 01_instances.py
python 02_dataclass_property.py
python array_aliasing.py
python practice_history.py
python -m pytest -q test_practice_history.py
cd ..
```

The original four history tests should pass. The Reading's `as_array()` excerpt
retains its original Week 3 Assignment context. It is not added to the simple
class in `02_dataclass_property.py`.

## Collections and JSON — Week 4

Keep `ap_week04_scene_data` beside these files. The supplied original domain
classes support the original practice calls.

```text
cd week04
python collections_practice.py
python json_practice.py
cd ..
```

## Sampling and acceptance — Week 5

Keep `ap_week05` beside the original example file. These two commands use the
provided calculations and do not require completing the Assignment TODOs in
the package. Do not edit those files for this review.

```text
cd week05
python compare_evaluations.py method
python compare_evaluations.py limits
cd ..
```

Week 6's grid, greedy and selection examples are reviewed in the Reading using
the original diagrams, tables and supplied interfaces. The ZIP does not add a
new completed implementation of the Week 6 Assignment functions.

On macOS/Linux, directory changes and these Python commands are the same.
Use `ls` instead of `dir` to list files. The initial full-path directory change
uses `cd "/your/folder/week07_review"`, not Windows `cd /d`.
