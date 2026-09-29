# Small helper functions


def show_title():
    print("\n==============================")
    print(" STUDENT EXPENSE TRACKER")
    print("==============================")


def show_menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Expense Summary")
    print("5. Set Monthly Budget")
    print("6. Check Budget")
    print("7. Edit Expense")
    print("8. Delete Expense")
    print("9. Exit")
    print("==============================")


def get_choice():
    return input("Enter your choice: ")
