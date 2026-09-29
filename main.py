# Main program for Student Expense Tracker

from expense import (
    add_expense,
    show_expenses,
    search_expense,
    show_summary,
    edit_expense,
    delete_expense
)
from budget import set_budget, check_budget
from storage import load_data, save_data
from utils import show_title, show_menu, get_choice


def main():
    expenses = load_data()

    while True:
        show_title()
        show_menu()

        choice = get_choice()

        if choice == "1":
            add_expense(expenses)
            save_data(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            search_expense(expenses)

        elif choice == "4":
            show_summary(expenses)

        elif choice == "5":
            set_budget()

        elif choice == "6":
            check_budget(expenses)

        elif choice == "7":
            edit_expense(expenses)
            save_data(expenses)

        elif choice == "8":
            delete_expense(expenses)
            save_data(expenses)

        elif choice == "9":
            print("Thank you for using the Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
