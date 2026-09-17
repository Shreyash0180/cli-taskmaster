import hashlib
from src.storage import load_users, save_users
from src.models import User

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    users = load_users()
    if username in users:
        return False, "Username already exists."
    
    users[username] = User(username, hash_password(password)).to_dict()
    save_users(users)
    return True, "Registration successful."

def login(username, password):
    users = load_users()
    if username not in users:
        return False, "Invalid username or password."
    
    if users[username]['password'] == hash_password(password):
        return True, "Login successful."
    return False, "Invalid username or password."
