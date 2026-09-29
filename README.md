# Student Expense Tracker

A simple Python command-line application for managing and tracking student expenses. The program stores expenses in a JSON file and provides features for adding, viewing, searching, summarizing, budgeting, and deleting expenses.

## Features

- Add a new expense with:
  - Amount
  - Category
  - Description
  - Automatically generated date
- View all saved expenses
- Search expenses by category
- View total spending and category-wise spending
- Set a monthly budget
- Check total spending against the saved budget
- Delete an expense by its expense number
- Save expense data permanently in `expenses.json`
- Save the monthly budget in `budget.txt`

## Requirements

- Python 3.x
- No external Python packages are required.
- The program uses Python's built-in:
  - `json` module
  - `datetime` module

## Files Used

When the program runs, it creates/uses these files in the same folder:

```text
expenses.json   # Stores all expense records
budget.txt      # Stores the monthly budget
```

These files are created automatically when needed.

## How to Run

1. Save the Python code as:

```text
expense_tracker.py
```

2. Open a terminal/command prompt in the project folder.

3. Run:

```bash
python expense_tracker.py
```

If your system uses `python3`, run:

```bash
python3 expense_tracker.py
```

## Menu Options

After starting the program, the following menu is displayed:

```text
==============================
 STUDENT EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Search Expense
4. Expense Summary
5. Set Monthly Budget
6. Check Budget
7. Delete Expense
8. Exit
==============================
```

### 1. Add Expense

Enter the expense amount, category, and description. The current date is added automatically.

Example:

```text
Enter amount: 120
Enter category: Food
Enter description: Lunch
```

The expense is then saved to `expenses.json`.

### 2. View Expenses

Displays all saved expenses along with their:

- Expense number
- Amount
- Category
- Description
- Date

### 3. Search Expense

Searches for expenses using an exact category name. The search is case-insensitive.

Example:

```text
Enter category: food
```

The program displays all matching expenses.

### 4. Expense Summary

Calculates:

- Total spending
- Category-wise spending

For example:

```text
Total spending: ₹ 850.0

Category-wise spending:
Food : ₹ 500.0
Travel : ₹ 350.0
```

### 5. Set Monthly Budget

Allows the user to enter a monthly budget. The value is stored in `budget.txt`.

Example:

```text
Enter your monthly budget: 5000
```

### 6. Check Budget

Compares the saved monthly budget with the total expenses and displays:

- Monthly budget
- Total spent
- Remaining amount
- Budget status

The program reports whether the user is within the budget, has used the complete budget, or has exceeded it.

### 7. Delete Expense

Displays the saved expenses and asks for the expense number to delete.

Example:

```text
Enter expense number to delete: 2
```

The selected expense is removed and the updated data is saved to `expenses.json`.

### 8. Exit

Closes the program safely.

## Data Storage

### `expenses.json`

Expenses are stored as a list of dictionaries. Each expense contains:

```text
amount
category
description
date
```

Example:

```json
[
    {
        "amount": 120.0,
        "category": "Food",
        "description": "Lunch",
        "date": "29-09-2026"
    }
]
```

### `budget.txt`

The monthly budget is stored as a simple number, for example:

```text
5000
```

## Program Structure

The program is organized into separate functions:

| Function | Purpose |
|---|---|
| `load_data()` | Loads existing expenses from `expenses.json` |
| `save_data()` | Saves expenses to `expenses.json` |
| `add_expense()` | Adds a new expense |
| `show_expenses()` | Displays all expenses |
| `search_expense()` | Searches expenses by category |
| `show_summary()` | Calculates total and category-wise spending |
| `set_budget()` | Saves the monthly budget |
| `get_budget()` | Reads the saved budget |
| `check_budget()` | Compares spending with the budget |
| `delete_expense()` | Deletes a selected expense |
| `main()` | Controls the main menu and program flow |

## Error Handling

The program includes basic error handling for invalid user input.

For example:

- Invalid expense amount → asks the user to enter a valid amount
- Invalid budget amount → asks the user to enter a valid amount
- Invalid delete option → displays an error message
- Missing `expenses.json` → starts with an empty expense list
- Missing `budget.txt` → asks the user to set a budget first

## Technologies Used

- **Python 3**
- **JSON** for expense data storage
- **Text file** for budget storage
- **Datetime** for automatically recording the expense date

## Project Objective

The objective of this project is to create a simple and practical expense management system for students. It demonstrates basic Python programming concepts such as:

- Variables and data types
- Lists and dictionaries
- Functions
- Loops
- Conditional statements
- Exception handling
- File handling
- JSON data storage
- User input and menu-driven programming

## Limitations

- The budget and expense calculations currently use all stored expenses rather than filtering expenses by the current calendar month.
- Expenses can only be searched by category.
- The application is command-line based and does not have a graphical user interface.
- There is no user login or multiple-user support.

## Future Improvements

Possible future improvements include:

- Monthly expense filtering
- Expense editing
- Date-based search
- Graphs and charts
- CSV export
- User login and multiple accounts
- A graphical user interface
- Automatic warnings when spending approaches the budget

## Author

**Student Expense Tracker Project**

This project is intended for educational use and demonstrates fundamental Python programming and file-handling concepts.
