# Week 7: Review

Review the concepts and coding skills from Weeks 1–6. The five demonstration
scripts are complete. Sections 9.1–9.2 provide two short, optional exercises
for writing a class, connecting objects and checking results with assertions.
This is not a new graded Assignment or the examination starter.

- [Reading V16 (PDF)](docs/week_07_review_reading_v16.pdf)
- [Download the examples ZIP](https://github.com/SSUMechE/applied-programming-2026-week07-review/raw/refs/heads/main/downloads/week07_review_examples.zip)
- [Example files and practice instructions](week07_review/README.md)

## 1. Get the files

Choose **one** method. Do not put these files inside an earlier assignment repository.

**ZIP:** download the examples ZIP above and extract it. It contains the
`week07_review` folder used in the Reading.

**Git:** open **Anaconda Prompt** and run the following from your course folder.
Replace `C:\your-course-folder` with your own folder.

```bat
cd /d "C:\your-course-folder"
git clone https://github.com/SSUMechE/applied-programming-2026-week07-review.git
cd applied-programming-2026-week07-review
cd week07_review
```

The source repository is public. Downloading or cloning it does not require
an invitation or a personal access token. A new private repository is not
required for this review.

## 2. Use the existing environment

Keep the Week 6 environment. No additional package, GPU or simulator is needed.
From the `week07_review` folder:

```bat
conda activate applied-programming-w06
python -c "import sys, numpy, pytest; print(sys.executable); print(numpy.__version__, pytest.__version__)"
dir
```

The interpreter path should point to `applied-programming-w06`. The Week 6
environment uses Python 3.12.13, NumPy 2.4.6 and pytest 9.1.1. The directory
listing should contain `functions_review.py` and the other review files.
If the Week 6 environment has not been installed, use the existing
[Week 6 setup instructions](https://github.com/SSUMechE/applied-programming-2026-week06-starter#2-prepare-repository-and-environment).
Do not overwrite a working environment merely to run these examples.

On macOS or Linux, use your terminal, `cd "/your/course/folder"` instead of
`cd /d`, and `ls` instead of `dir`. The Conda and Python commands are the same.
Enter these commands in the terminal, not after Python's `>>>` prompt.

## 3. Run the supplied examples

Stay in `week07_review` and follow the Reading order:

```bat
python functions_review.py
python arrays_review.py
python objects_review.py
python collections_review.py
python models_review.py
python -m pytest -q
```

The unchanged supplied examples give **27 passed**. Each complete script
prints several sections. Each Output box in the Reading corresponds to the
adjacent code, not necessarily the entire script's output.

`collections_review.py` also writes `outputs/obstacle.json` and reads it back.
It is a generated demonstration file, not an extra submission item.

## 4. Optional object-oriented practice

Use Reading Sections **9.1–9.2** for the exact instructions and two cases per
exercise. Only the five marked regions need writing:

- `practice/calibration.py`: E1_CLASS, E1_APPLY, E2_INIT and E2_VALUES.
- `practice/check_my_measurements.py`: E2_ASSERT.

Keep the supplied returns and surrounding code. Do not edit
`practice/check_calibration.py`.

After completing Exercise 1:

```bat
cd practice
python calibration.py 1
python -m pytest check_calibration.py -q -k calibration_case
```

Expected test summary: **2 passed, 4 deselected**.

After completing Exercise 2, stay in `practice`:

```bat
python calibration.py 2
python -m pytest check_calibration.py check_my_measurements.py -q
```

Expected test summary: **7 passed**. Before editing, these seven checks fail
with `NotImplementedError` because the practice regions are unfinished.
They are separate from the 27 complete demonstration checks.
Use `cd ..` to return to `week07_review`.

There is no new report, screenshot collection, package build or mandatory
submission for these review exercises. Earlier assignments and their
submission requirements are unchanged.
