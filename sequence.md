# Sequence Diagram

Example: Adding an expense.

```text
Student          main.py          expense.py        storage.py
   |                |                 |                 |
   |--Select Add--->|                 |                 |
   |                |--add_expense--->|                 |
   |                |                 |--Create record  |
   |                |<--Updated list--|                 |
   |                |--save_data----------------------->|
   |                |                 |                 |
   |<---Success message--------------|                 |
```
