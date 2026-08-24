# Calculator Boilerplate Project

This project accompanies the "Building an Interactive Python Calculator" tutorial. It provides a function-based version of the calculator so that your work can be verified automatically using [pytest](https://docs.pytest.org/).

## Folder Structure

```text
CIS1702_Week3_calculator_project_Student/
    .gitignore
    README.md
    Variables_and_Operators/
        pyproject.toml          <- pytest configuration for module discovery
        requirements.txt        <- project dependencies (pytest)
        calculator/
            calculator.py       <- implement the TODO functions here
        tests/
            test_calculator.py  <- automated test suite; do not edit
```

Students should implement the required functions inside [`Variables_and_Operators/calculator/calculator.py`](Variables_and_Operators/calculator/calculator.py). The automated tests in [`Variables_and_Operators/tests/test_calculator.py`](Variables_and_Operators/tests/test_calculator.py) verify that each function behaves as expected.

## Setup

Navigate to the `Variables_and_Operators` folder and install the required dependencies:

```bash
cd Variables_and_Operators
pip install -r requirements.txt
```

## Running the Tests

From inside the `Variables_and_Operators` folder, run:

```bash
pytest -v
```

Alternatively, you can run pytest from the project root directory:

```bash
pytest -v Variables_and_Operators
```

You will see a list of tests, each marked `PASSED` or `FAILED`. In this starter project, every test will initially fail because each function raises `NotImplementedError`. As you implement each function in [`calculator/calculator.py`](Variables_and_Operators/calculator/calculator.py), re-run `pytest -v` to check your progress and watch the failures reduce one by one.

## Running the Interactive Calculator

Once your functions are implemented, you can run the interactive calculator itself from within the `Variables_and_Operators` directory:

```bash
python -m calculator.calculator
```

or:

```bash
python calculator/calculator.py
```

## How the Tests Map to the Tutorial

| Functions | Tutorial Section / Challenge |
| :--- | :--- |
| `add` / `subtract` / `multiply` | Building the Calculator, Adding Subtraction |
| `divide` | Challenge Activity A (divide-by-zero) |
| `modulo` | Modulo Division, Why Modulo Matters |
| `power` | Challenge Activity A (power operator) |
| `percentage_of` | Challenge Activity C (percentage calculator) |
| `convert_currency` | Challenge Activity D (currency converter) |

## Important Notes

- `divide` and `modulo` must raise a `ZeroDivisionError` when the divisor is `0`, giving a concrete, testable way to handle divide-by-zero behaviour.
- Remember to return the computed result from each function rather than printing it.
- The "Result Memory" challenge (Challenge Activity B) is deliberately not covered by an automated test here, as it depends on interactive terminal input and state rather than a pure function.
- Do not modify [`tests/test_calculator.py`](Variables_and_Operators/tests/test_calculator.py); test failures should be resolved by implementing or correcting the logic in [`calculator/calculator.py`](Variables_and_Operators/calculator/calculator.py).
