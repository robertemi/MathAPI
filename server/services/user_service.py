from typing import Optional
from utils.password_utils import check_password, hash_password


class UserService:

    async def handle_user_auth(self, conn, email, password):
        try:
            row = await conn.fetchrow(
                "SELECT password FROM users WHERE email = $1",
                email
                )
            if not row:
                return False
            return check_password(password, row['password'])
        except Exception as e:
            print(f"Auth error: {e}")
            return False

    async def handle_user_sign_up(
            self,
            conn,
            first_name,
            last_name,
            email,
            password,
            role: Optional[str]
    ):
        hashed = hash_password(password)
        try:
            if role:
                result = await conn.fetchrow(
                    """INSERT INTO users (
                                        first_name,
                                        last_name,
                                        email,
                                        password,
                                        role
                                        )
                       VALUES ($1, $2, $3, $4, $5) RETURNING id""",
                    first_name, last_name, email, hashed, role
                )
            else:
                result = await conn.fetchrow(
                    """INSERT INTO users (
                                        first_name,
                                        last_name,
                                        email,
                                        password
                                        )
                       VALUES ($1, $2, $3, $4) RETURNING id""",
                    first_name, last_name, email, hashed
                )
            return result is not None
        except Exception as e:
            print(f"Sign-in error: {e}")
            return False
