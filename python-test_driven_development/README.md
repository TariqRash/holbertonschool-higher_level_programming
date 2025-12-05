# Python - Test Driven Development

This project focuses on Test-Driven Development (TDD) principles in Python, emphasizing the importance of writing tests before implementing functionality.

## Learning Objectives

* Understanding the importance of interactive tests
* Writing comprehensive docstring tests
* Creating documentation for modules and functions
* Implementing unittest for complex test scenarios
* Finding and handling edge cases

## Project Structure
```
python-test_driven_development/
├── 0-add_integer.py
├── 2-matrix_divided.py
├── 3-say_my_name.py
├── 4-print_square.py
├── 5-text_indentation.py
├── 6-max_integer.py
└── tests/
    ├── 0-add_integer.txt
    ├── 2-matrix_divided.txt
    ├── 3-say_my_name.txt
    ├── 4-print_square.txt
    ├── 5-text_indentation.txt
    └── 6-max_integer_test.py
```

## Requirements

* Python 3.8.5
* pycodestyle 2.7.*
* All files must be executable
* All modules and functions must have documentation

## Testing

Run doctests:
```bash
python3 -m doctest ./tests/*.txt
```

Run unittests:
```bash
python3 -m unittest tests.6-max_integer_test
```

## Tasks

### 0. Integers addition
Function that adds two integers with type validation.

### 1. Divide a matrix
Function that divides all elements of a matrix with comprehensive validation.

### 2. Say my name
Function that prints formatted names with string validation.

### 3. Print square
Function that prints a square pattern with size validation.

### 4. Text indentation
Function that formats text with proper indentation after punctuation.

### 5. Max integer - Unittest
Comprehensive unittest suite for finding maximum integer in a list.

## Author

Created as part of Holberton School curriculum.
