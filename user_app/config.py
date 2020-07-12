import os

SMTP_USER = os.environ.get('EMAIL_USER')
SMTP_PASSWORD = os.environ.get('EMAIL_PASS')
SMTP_PORT = 465
CONFIRM_EMAIL_SUBJECT = "Welcome to Ableton"
CONFIRM_EMAIL_CONTENT = "You have successfully signed up to Ableton."
EMAIL_LOCK_TIME = 30