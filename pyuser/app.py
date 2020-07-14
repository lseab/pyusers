from pyuser.user import User
from pyuser.exceptions import EmailInUse, InvalidPassword, AccountLocked
from pyuser.settings import config
from email.message import EmailMessage
import smtplib
import time


class Application:

    def register_user(self, user: User) -> None:
        """
        Takes a User object as an argument, controls if the email is available then adds the user to the database.
        """
        if user.email_available():
            user.register_to_db()
            self.send_registration_email(user.email)
        else:
            raise EmailInUse(f'{user.email} is already in use.')

    def delete_user(self, user: User) -> None:
        """
        Takes a User object as an argument and deletes it from the database.
        """
        user.remove_from_db()

    def login_user(self, user: User, password: str) -> None:
        """
        If a user enters a wrong password $PASSWORD_ATTEMPTS times, their account is locked.
        This is done by recording the time.time() of the last failed attempt in the db (LOCK_TIME 
        in the schema) and checking on each consequent attempt checking if the time elapsed 
        (time.time() - user.lock_time) is greater that the configured EMAIL_LOCK_TIME.

        Parameters:
            user(User): user object that the password will be controlled against
            password (str): password entered by the client
        """
        if user.lock_time == -1 or (time.time() - user.lock_time) > config.EMAIL_LOCK_TIME:
            user.lock_time = -1 # lock_time value stored in db when the user isn't locked out
            if not user.valid_password(password):
                user.login_attempts += 1
                if user.login_attempts >= config.PASSWORD_ATTEMPTS:
                    user.lock_time = time.time()
                    user.login_attempts = 0
                raise InvalidPassword("Wrong password. Try again")
            else:
                print(f'User {user.full_name} successfully logged in.')
        else:
            time_to_wait = int(config.EMAIL_LOCK_TIME - (time.time() - user.lock_time))
            raise AccountLocked(f'Your account is currently locked. Try again in {time_to_wait} seconds.')

    def send_registration_email(self, user_email: str) -> None:
        """
        Send registration email to user on successful login.
        """
        msg = EmailMessage()
        msg['Subject'] = config.CONFIRM_EMAIL_SUBJECT
        msg['From'] = config.SMTP_USER
        msg['To'] = user_email
        msg.set_content(config.CONFIRM_EMAIL_CONTENT)

        with smtplib.SMTP_SSL('smtp.gmail.com', config.SMTP_PORT) as smtp:
            smtp.login(config.SMTP_USER, config.SMTP_PASSWORD)
            smtp.send_message(msg)