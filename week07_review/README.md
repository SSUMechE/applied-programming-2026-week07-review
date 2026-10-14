# Week 7 review examples and short OOP practice

These files accompany the Week 7 Reading. The five demonstration scripts and
test_review.py are complete. The separate practice/ folder contains two optional
writing exercises from Sections 9.1–9.2, not a graded Assignment or examination
starter. No previous student TODO is imported. No new installation is required.

Extract these files together to a separate `week07_review` folder. Keep them out
of earlier assignment repositories. In Anaconda Prompt, activate the existing
Week 6 environment, then enter the extracted folder:

```text
conda activate applied-programming-w06
cd /d "C:\your-course-folder\week07_review"
```

Replace the example directory with your actual extracted directory. Run these
commands in that folder, not at Python's `>>>` prompt:

```text
python functions_review.py
python arrays_review.py
python objects_review.py
python collections_review.py
python models_review.py
python -m pytest -q test_review.py
```

- `functions_review.py`: arguments, returned values, validation and containers.
- `arrays_review.py`: shape, axis, translation, view/copy and batch.
- `objects_review.py`: initialization, property, state changes, dataclass,
  composition and exception inheritance.
- `collections_review.py`: list, dictionary, set, deque and a JSON round trip.
- `models_review.py`: sampled clearance, threshold margins and Cartesian grids.
- `test_review.py`: supplied checks that can be read and run as provided.

The files print their observations. Only `collections_review.py` also writes
`outputs/obstacle.json`, relative to the current folder. It reads the same file
back and explicitly constructs a `ReviewObstacle` from the resulting dictionary.
Rerunning the file replaces this small demonstration output. The output is not
a new submission item.

The snippets marked in comments are exact parts used in the Reading. Run the
complete files so their imports and earlier definitions are available. Importing
a module does not run its `main()` demonstration.
Each complete demonstration prints several sections in order. Each Reading
Output box shows the part produced by the adjacent code, not the entire run.

The small objects have deliberately narrow teaching contracts. `ReviewObstacle`
is a separate teaching type, not the frozen Week 4 `Obstacle` public API. Its names
and centres are supplied valid values. The radius must be a finite positive
Python integer or float, excluding Boolean. `Point` illustrates a nonempty owned
tuple of supplied numeric coordinates, not all of the Week 3 validation rules.
Coordinates and radii in the object/model examples are in metres. The separate
inspection-point arrays in `arrays_review.py` are in millimetres.

Sampled clearance is a geometric observation at selected points, not a continuous
collision check or a safety guarantee. This review does not run a robot or a
physics simulator. It adds no required report or test-writing quota and does
not alter earlier assignment or submission instructions.

## Two optional writing exercises

Use Reading Sections 9.1–9.2 for the exact tasks. Work in the practice folder:

```text
cd practice
```

1. In calibration.py, complete E1_CLASS and E1_APPLY. Keep the supplied return.

```text
python calibration.py 1
python -m pytest check_calibration.py -q -k calibration_case
```

After Exercise 1: 2 passed, 4 deselected. MeasurementSet may still be unfinished.

2. In calibration.py, complete E2_INIT and E2_VALUES. In
   check_my_measurements.py, write the E2_ASSERT checks specified in the Reading.

```text
python calibration.py 2
python -m pytest check_calibration.py check_my_measurements.py -q
```

After both exercises: 7 passed. The unchanged practice starter has 7 expected
NotImplementedError failures. These checks are separate from the 27 complete
demonstration tests. The explicit check_ filenames keep unfinished practice out
of the demonstration test command. Do not edit check_calibration.py.

Use cd .. to return to week07_review. No new report, repository or submission
is required. Raw readings use sensor units. Gain is mm per sensor unit, while
offset_mm and corrected values use mm. No fitting or device access is involved.
