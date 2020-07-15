import json
import os
import pathlib

# 'PYUSERS_ENV' is an env variable allowing to switch environments
# e.g PYUSERS_ENV=test in our test suite 
config = os.environ
env = config.get('PYUSERS_ENV')

if env:
    # There must be a corresponding {env_name}.json in the same folder for a given {env_name}
    # e.g test.json for our test suite 
    this_file = pathlib.Path(__file__)
    this_dir = this_file.parent
    env_file = this_dir.joinpath(f'{env}.json')
    with open(env_file, 'r') as fd:
        settings_json = fd.read()
        settings_dict = json.loads(settings_json)
        config.update(settings_dict)

SMTP_USER = config.get('PYUSERS_SMTP_USER')
SMTP_PASSWORD = config.get('PYUSERS_SMTP_PASSWORD')
SMTP_PORT = config.get('PYUSERS_SMTP_PORT', 465)

CONFIRM_EMAIL_SUBJECT = config.get('PYUSERS_CONFIRM_EMAIL_SUBJECT', "Welcome to Ableton")
CONFIRM_EMAIL_CONTENT = config.get('PYUSERS_CONFIRM_EMAIL_CONTENT', "You have successfully signed up to Ableton.")

# number of authorised authentication attempts before a user is locked out
PASSWORD_ATTEMPTS = config.get('PYUSERS_PASSWORD_ATTEMPTS', 3)
# time users are locked out of their account after $PASSWORD_ATTEMPTS failed attempts
EMAIL_LOCK_TIME = config.get('PYUSERS_EMAIL_LOCK_TIME', 30)

DB_NAME = config.get('PYUSERS_DB_NAME')
