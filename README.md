# Student Expense & Budget Tracker

## Overview

Student Expense & Budget Tracker is a Python-based console application designed to help students record and manage their daily expenses and monthly budget.

The project provides a simple menu-driven system where users can add, view, search, edit and delete expenses. It also provides total and category-wise spending information and allows users to set and check a monthly budget.

## Features

- Add a new expense
- View all expenses
- Search expenses by category
- View total spending
- View category-wise spending
- Set a monthly budget
- Check remaining budget
- Edit an existing expense
- Delete an expense
- Store expense data using JSON
- Basic input validation and error handling

## Technologies Used

- Python 3
- JSON
- File Handling
- Git and GitHub
- Pytest for basic testing

## Project Structure

```text
Student-Expense-Tracker/
│
├── README.md
├── statement.md
│
├── src/
│   ├── main.py
│   ├── expense.py
│   ├── budget.py
│   ├── storage.py
│   └── utils.py
│
├── data/
│   ├── expenses.json
│   └── budget.txt
│
├── tests/
│   └── test_expense.py
│
├── docs/
│   ├── architecture.md
│   ├── workflow.md
│   ├── use_case.md
│   └── sequence.md
│
└── screenshots/
```

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal inside the project folder.
4. Move into the source folder:

```bash
cd src
```

5. Run the program:

```bash
python main.py
```

## Testing

From the project root, run:

```bash
pytest
```

The test file checks the basic expense-total calculation and the empty-expense case.

## Data Storage

Expense information is stored in `data/expenses.json`.

The monthly budget is stored in `data/budget.txt`.

## Future Enhancements

- Monthly expense filtering
- Graphical user interface
- Exporting reports
- More detailed spending charts
- User login
