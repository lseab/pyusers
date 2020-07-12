import sqlite3
from sqlite3 import OperationalError


class Database:
    
    def __init__(self):
        self._db_connexion = sqlite3.connect('Auth.db')
        self._db_cursor = self._db_connexion.cursor()
        self.create_tables()

    def query(self, query, params={}):
        with self._db_connexion:
            return self._db_cursor.execute(query, params)

    def __del__(self):
        self._db_connexion.close()

    def create_tables(self):
        with open('user_app/tables.sql', 'r') as file:
            tables_file = file.read()
            commands = tables_file.split(';')

            for command in commands:
                try:
                    self.query(command)
                except OperationalError as e:
                    print(f"Skipped command: {e.message}")

    def update_field(self, table, field, condition):
        query = f"UPDATE {table} SET {field[0]} = :field_value WHERE {condition[0]} = :condition_value;"
        params = {
            "field_value": field[1],
            "condition_value": condition[1],
        }
        self.query(query, params)


db_client = Database()