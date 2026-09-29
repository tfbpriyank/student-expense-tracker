# System Architecture

The project follows a simple modular architecture.

```text
                +----------------+
                |    main.py     |
                | Main Program   |
                +-------+--------+
                        |
          +-------------+-------------+
          |             |             |
          v             v             v
   +------------+ +------------+ +------------+
   | expense.py | | budget.py  | |  utils.py  |
   +-----+------+ +-----+------+ +------------+
         |              |
         +------+-------+
                |
                v
         +--------------+
         | storage.py   |
         +------+-------+
                |
                v
        +---------------+
        | Local Files   |
        | JSON / TXT    |
        +---------------+
```

### Modules

- `main.py` controls the program flow and menu.
- `expense.py` handles expense operations.
- `budget.py` handles budget operations.
- `storage.py` handles saving and loading data.
- `utils.py` contains menu and display helpers.
