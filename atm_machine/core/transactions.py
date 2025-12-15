from core import database

def check_balance(card_number):
    return database.database[card_number]["balance"]

def deposit(card_number, amount):
    database.database[card_number]["balance"] += amount

def withdraw(card_number, amount):
    if database.database[card_number]["balance"] >= amount:
        database.database[card_number]["balance"] -= amount
        return True
    return False
