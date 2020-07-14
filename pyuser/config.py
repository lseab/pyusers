import os

SMTP_USER = os.environ.get('EMAIL_USER')
SMTP_PASSWORD = os.environ.get('EMAIL_PASS')
SMTP_PORT = 465

CONFIRM_EMAIL_SUBJECT = "Welcome to Ableton"
CONFIRM_EMAIL_CONTENT = "You have successfully signed up to Ableton."

PASSWORD_ATTEMPTS = 3 # number of authorised authentication attempts before a user is locked out
EMAIL_LOCK_TIME = 30 # time users are locked out of their account after $PASSWORD_ATTEMPTS failed attempts

TEST_DB_NAME = 'Test.db'