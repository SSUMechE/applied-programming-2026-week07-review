# Week 7: Review

Review the concepts and coding skills already taught in **Weeks 1–6**.
Reading V20 uses the original teaching examples, values and terminology.
The supplied files collect the original Week 2–5 examples for execution.
Week 6 is reviewed through its original diagrams, tables and interfaces in
the Reading, without a new completed Assignment solution.

This is **not a new graded Assignment or the examination starter**.

- [Reading V20 (PDF)](docs/week_07_review_reading_v20.pdf)
- [Download the examples ZIP](https://github.com/SSUMechE/applied-programming-2026-week07-review/raw/refs/heads/main/downloads/week07_review_examples.zip)
- [Example files and execution commands](week07_review/README.md)

## 1. Get the files

Choose **one** method. Keep these files outside earlier Assignment repositories.

**ZIP:** download the examples ZIP and extract it. It contains the
`week07_review` folder used in the Reading.

**Git:** open **Anaconda Prompt** and run these commands from your course folder.
Replace `C:\your-course-folder` with your own folder.

```bat
cd /d "C:\your-course-folder"
git clone https://github.com/SSUMechE/applied-programming-2026-week07-review.git
cd applied-programming-2026-week07-review
cd week07_review
```

This source repository is public. Cloning or downloading does not require an
invitation or personal access token. No new private repository is required.

If you have the earlier review files, extract the new ZIP into a separate folder
to keep any work you have already saved. The current examples are organized
under `week02`, `week03`, `week04` and `week05`.

## 2. Use the existing environment

Keep the Week 6 environment. No extra installation, GPU or simulator is needed.
From `week07_review`:

```bat
conda activate applied-programming-w06
python -c "import sys, numpy, pytest; print(sys.executable); print(numpy.__version__, pytest.__version__)"
dir
```

The interpreter path should point to `applied-programming-w06`. The existing
Week 6 environment uses Python 3.12.13, NumPy 2.4.6 and pytest 9.1.1.
The listing should show the four week folders above.
If the environment is missing, follow the existing
[Week 6 setup instructions](https://github.com/SSUMechE/applied-programming-2026-week06-starter#2-prepare-repository-and-environment).
Do not replace a working environment to run this review.

On macOS/Linux, use your terminal, `cd "/your/course/folder"` instead of
`cd /d`, and `ls` instead of `dir`. The Conda and Python commands are the same.
Enter commands in the terminal, not after Python's `>>>` prompt.

## 3. Run in Reading order

The [example README](week07_review/README.md) lists the directory changes and
commands in order. It explains which files are complete demonstrations.

- **Section 2:** original functions and tests in `week02`. Expected: `3 passed`.
- **Section 3:** original NumPy, view/copy, interpolation and batch examples in `week02`.
- **Section 4:** original classes, dataclass and history in `week03`. Expected: `4 passed`.
- **Sections 5–6:** original collections and JSON examples in `week04`.
- **Section 7:** supplied Week 5 `method` and `limits` comparisons in `week05`.
- **Section 8:** original Week 6 grid, greedy and selection examples in the Reading.
- **Section 9:** optional reconstruction of the already taught Week 3 examples.

`week02/example_wrong_distance.py` is the original deliberately incorrect
example. Its test is expected to fail. It is not part of the three passing
function tests.

`week04/json_practice.py` writes and reads
`week04/practice/obstacle_practice.json`. This is a generated example file, not
an extra submission item.

The supplied Week 5 comparisons do not call the unfinished Assignment TODOs
in `ap_week05/model.py`. Leave those package files unchanged for this review.
The Reading's Week 3 `as_array()` excerpt keeps its original Assignment context.
It is not a method added to the simple review dataclass.

No new report, screenshot collection, wheel, private repository or mandatory
LMS submission is required. Earlier Assignment requirements are unchanged.
