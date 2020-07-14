import pytest
import pyuser.settings.config as config
import time
from pyuser.app import Application
from pyuser.user import User
from pyuser.exceptions import EmailInUse, InvalidPassword, AccountLocked, InvalidEmail

app = Application()
email_address = 'luke.seabright@gmail.com'
password = 'AbletonRules'


def test_register_user():
    try:
        user = User.from_email(email_address)
        app.delete_user(user)
    except InvalidEmail:
        pass
    
    user = User(email_address, 'Luke', 'Seabright')
    user.set_password(password)
    app.register_user(user)

def test_user_login():
    user = User.from_email(email_address)
    app.login_user(user, password)

def test_email_in_use():
    user = User.from_email(email_address)
    with pytest.raises(EmailInUse):
        assert app.register_user(user)

def test_invalid_password():
    user = User.from_email(email_address)
    with pytest.raises(InvalidPassword):
        assert app.login_user(user, 'WrongPassword')

def test_invalid_email():
    with pytest.raises(InvalidEmail):
        assert User.from_email('non.existant@email.com')

def test_account_locked():
    user = User.from_email(email_address)
    user.login_attempts = 2
    with pytest.raises(InvalidPassword):
        assert app.login_user(user, 'WrongPassword')
    with pytest.raises(AccountLocked):
        app.login_user(user, "WrongPassword")

def test_account_unlocked():
    test_account_locked()
    time.sleep(config.EMAIL_LOCK_TIME + 1)
    test_user_login()

if __name__ == '__main__':
    test_register_user()