import hashlib
import os
from . import db_client
from .exceptions import EmailInUse, InvalidEmail


class User:

    def __init__(self, email: str, first_name: str, last_name: str, login_attempts: int = 0, lock_time: float = -1, salt: bytes = os.urandom(32)):
        self.table_name = 'users'
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.salt = salt
        self._login_attempts = login_attempts
        self._lock_time = -1

    def __repr__(self):
        return f"User('{self.last_name}', '{self.first_name}')"

    @property
    def lock_time(self):
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        db_client.update_field(self.table_name, ('lock_time', lock_time), ('email', self.email))
        self._lock_time = lock_time

    @property
    def login_attempts(self):
        return self._login_attempts

    @login_attempts.setter
    def login_attempts(self, login_attempts):
        db_client.update_field(self.table_name, ('login_attempts', login_attempts), ('email', self.email))
        self._login_attempts = login_attempts

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def set_password(self, password):
        self.password = self._encrypt_password(password)

    def _encrypt_password(self, password: str):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            self.salt,
            100000
        )

    def valid_password(self, password: str):
        encrypted_pw = self._encrypt_password(password)
        return encrypted_pw == self.password

    def register_to_db(self):
        db_client.query(
            "INSERT INTO users VALUES(:email, :first_n, :last_n, :lock_time, :log_attempts, :salt, :pwd)",
            {
                'email': self.email,
                'first_n': self.first_name,
                'last_n': self.last_name,
                'lock_time': self.lock_time,
                'log_attempts': self.login_attempts,
                'salt': self.salt,
                'pwd': self.password,
            }
        )

    def remove_from_db(self):
        db_client.query(
            "DELETE FROM users WHERE email = :email",
            {
                'email': self.email
            }
        )

    def email_available(self):
        result = User.get_user(self.email)
        if result.fetchall(): return False
        else: return True

    @staticmethod
    def get_user(email):
        return db_client.query(
            "SELECT * FROM users WHERE email = :email",
            {
                "email": email
            })

    @classmethod
    def from_email(cls, email):
        result = User.get_user(email).fetchone()
        if result is None:
            raise InvalidEmail("User not found")
        else:
            user = cls(*result[:-1])
            user.password = result[-1]
        return user