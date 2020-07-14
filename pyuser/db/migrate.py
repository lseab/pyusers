import sys
import os.path

path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
sys.path.append(path)

from sqlite3 import OperationalError
from pyuser.clients import db_client

def create_tables():
    with open('pyuser/db/schema.sql', 'r') as file:
        tables_file = file.read()
        commands = tables_file.split(';')

        for command in commands:
            try:
                db_client.query(command)
            except OperationalError as e:
                print(f"Skipped command: {e.message}")

if __name__ == '__main__':
    create_tables()
