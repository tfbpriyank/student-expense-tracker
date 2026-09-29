# Basic tests for the expense calculations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    return total


def test_total_expense():
    expenses = [
        {"amount": 100, "category": "Food", "description": "Lunch"},
        {"amount": 200, "category": "Travel", "description": "Bus"}
    ]

    assert calculate_total(expenses) == 300


def test_empty_expenses():
    assert calculate_total([]) == 0
