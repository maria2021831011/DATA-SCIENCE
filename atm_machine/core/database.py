database = {
    "111": {"name": "Alice", "balance": 5000, "pin": "1234"},
    "222": {"name": "Bob", "balance": 3000, "pin": "2345"},
    "333": {"name": "Charlie", "balance": 7000, "pin": "3456"}
}

def get(card_number):
    return database.get(card_number)
