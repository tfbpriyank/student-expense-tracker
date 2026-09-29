# Functions related to monthly budget


def set_budget():
    print("\n--- Set Budget ---")

    try:
        budget = float(input("Enter your monthly budget: "))

        if budget <= 0:
            print("Budget should be greater than 0.")
            return

        with open("data/budget.txt", "w") as file:
            file.write(str(budget))

        print("Budget saved successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def get_budget():
    try:
        with open("data/budget.txt", "r") as file:
            budget = float(file.read())

        return budget

    except (FileNotFoundError, ValueError):
        return 0


def check_budget(expenses):
    print("\n--- Budget Status ---")

    budget = get_budget()

    if budget == 0:
        print("Please set your budget first.")
        return

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    remaining = budget - total

    print("Monthly budget :", budget)
    print("Total spent    :", total)
    print("Remaining      :", remaining)

    if remaining > 0:
        print("You are within your budget.")
    elif remaining == 0:
        print("You have used your complete budget.")
    else:
        print("You have exceeded your budget.")
