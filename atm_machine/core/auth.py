from core import database

def authenticate_user(card, pin):
    user = database.get(card)
    if user and user['pin'] == pin:
        return True
    return False
