from typing import Optional
from werkzeug.security import check_password_hash


class User:
    def __init__(self, id, first_name, last_name, email, password, role):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role = role

    # for the sign up functionality
    @classmethod
    def add_user(self, conn, first_name, last_name, email, password, role: Optional[str] = None):
        try:
            with conn.cursor() as cur:
                if role:
                    cur.execute(
                        'INSERT INTO users '
                        '(first_name, last_name, email, password, role)'
                        'VALUES (%s, %s, %s, %s, %s) RETURNING id',
                        (
                            first_name,
                            last_name,
                            email,
                            password,
                            role
                        )
                    )
                else:
                    cur.execute(
                        'INSERT INTO users '
                        '(first_name, last_name, email, password)'
                        'VALUES (%s, %s, %s, %s) RETURNING id',
                        (
                            first_name,
                            last_name,
                            email,
                            password,
                        )
                    )                
                result = cur.fetchone()
                conn.commit()
                if not result:
                    print("No ID returned from INSERT")
                    return False
                else:
                    return True

        except Exception as e:
            conn.rollback()
            print(f"General error in User.add_user(): {e}")

    @classmethod
    def get_user_by_email_and_password(self, conn, email, password):
        try:
            with conn.cursor() as cur:
                cur.execute(
                    'SELECT password FROM users WHERE email = %s',
                    (email,)
                )
                user_hashed_password = cur.fetchone()[0]

                if not check_password_hash(user_hashed_password, password):
                    return False
                else:
                    return True
                
        except Exception as e:
            print(f'User auth exception: {e}')


    def to_dict(self) -> dict:
        """Convert to API-friendly format"""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'role': self.role if self.role else None
        }
