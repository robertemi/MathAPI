from typing import Optional
from models.User import User
from werkzeug.security import generate_password_hash

class UserController:
    def __init__(self):
        pass

    def handle_user_auth(self, conn, email, password):
        try:
            user_exists = User.get_user_by_email_and_password(conn, email, password)
            return user_exists
        
        except Exception as e:
            print(f'User auth exception controller: {e}')

    def handle_user_sign_up(self, conn, first_name, last_name, email, password, role: Optional[str]):
        try:
            hashed_password = generate_password_hash(password)
            success = User.add_user(conn, first_name, last_name, email, hashed_password, role)
            return success
        except Exception as e:
            print(f'User sign up exception controller: {e}')

