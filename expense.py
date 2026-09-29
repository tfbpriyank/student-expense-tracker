# Functions related to expenses

from datetime import datetime


def add_expense(expenses):
    print("\n--- Add Expense ---")

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount should be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    if category == "":
        print("Category cannot be empty.")
        return

    if description == "":
        print("Description cannot be empty.")
        return

    date = datetime.now().strftime("%d-%m-%Y")

    new_expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(new_expense)
    print("Expense added successfully!")


def show_expenses(expenses):
    print("\n--- Your Expenses ---")

    if len(expenses) == 0:
        print("No expenses added yet.")
        return

    for i in range(len(expenses)):
        print("\nExpense", i + 1)
        print("Amount      :", expenses[i]["amount"])
        print("Category    :", expenses[i]["category"])
        print("Description :", expenses[i]["description"])
        print("Date        :", expenses[i]["date"])


def search_expense(expenses):
    print("\n--- Search Expense ---")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    category = input("Enter category: ").strip().lower()
    found = False

    for expense in expenses:
        if expense["category"].lower() == category:
            print(
                "₹", expense["amount"],
                "|", expense["description"],
                "|", expense["date"]
            )
            found = True

    if found == False:
        print("No expense found in this category.")


def show_summary(expenses):
    print("\n--- Expense Summary ---")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    total = 0
    category_total = {}

    for expense in expenses:
        total = total + expense["amount"]
        category = expense["category"]

        if category in category_total:
            category_total[category] = (
                category_total[category] + expense["amount"]
            )
        else:
            category_total[category] = expense["amount"]

    print("Total spending: ₹", total)
    print("\nCategory-wise spending:")

    for category in category_total:
        print(category, ": ₹", category_total[category])


def edit_expense(expenses):
    print("\n--- Edit Expense ---")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    show_expenses(expenses)

    try:
        number = int(input("\nEnter expense number to edit: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        expense = expenses[number - 1]

        print("\nLeave the input blank if you don't want to change it.")

        amount = input("Enter new amount: ")
        category = input("Enter new category: ")
        description = input("Enter new description: ")

        if amount != "":
            try:
                amount = float(amount)
                if amount > 0:
                    expense["amount"] = amount
                else:
                    print("Invalid amount. Old amount kept.")
            except ValueError:
                print("Invalid amount. Old amount kept.")

        if category != "":
            expense["category"] = category

        if description != "":
            expense["description"] = description

        print("Expense updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


def delete_expense(expenses):
    print("\n--- Delete Expense ---")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    show_expenses(expenses)

    try:
        number = int(input("\nEnter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        deleted = expenses.pop(number - 1)

        print(
            "Expense for ₹",
            deleted["amount"],
            "deleted successfully."
        )

    except ValueError:
        print("Please enter a valid number.")
