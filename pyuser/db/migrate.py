import os
from sqlite3 import OperationalError
from pyuser.clients import db_client
from pyuser.settings.config import DB_NAME

def create_tables():
    with open('pyuser/db/schema.sql', 'r') as file:
        tables_file = file.read()
        commands = tables_file.split(';')

        for command in commands:
            try:
                db_client.query(command)
            except OperationalError as e:
                print(f"Skipped command: {e.message}")

def drop_tables():
    tables_query = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"    
    tables = db_client.query(tables_query).fetchall()

    for table in tables:
        db_client.query(f"DROP TABLE {table[0]};")

if __name__ == '__main__':
    create_tables()
