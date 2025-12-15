```
atm_project/
├── main.py                 <-- The Screen/Keypad (User Interface)
└── core/                   <-- The "Bank Internals" Package
    ├── __init__.py         <-- Makes this a package
    ├── database.py         <-- Holds user account data
    ├── auth.py             <-- Handles PIN verification
    └── transactions.py     <-- Handles math (withdraw/deposit)
```
