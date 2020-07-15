import sqlite3
from pyuser.settings.config import DB_NAME
from sqlite3.dbapi2 import Cursor


class Database:
    
    def __init__(self, db_name: str):
        self._db_connexion = sqlite3.connect(db_name)
        self._db_cursor = self._db_connexion.cursor()

    def query(self, query: str, params: dict = {}) -> Cursor:
        """
        Perform a query on the database.

        Parameters:
            query (str): SQL statement
            params (dict): parameters to be passed to the SQL string
        """
        with self._db_connexion:
            return self._db_cursor.execute(query, params)

    def update_field(self, table: str, field: tuple, condition: tuple) -> Cursor:
        """
        Perform updates for a given table in the database.

        Parameters:
            table (str): name of the table to update
            field (tuple): two-element tuple, the first is the field name, the second the updated value
            condition (tuple): two-element tuple, the first is the field name, the second is the field constraint
        """
        query = f"UPDATE {table} SET {field[0]} = :field_value WHERE {condition[0]} = :condition_value;"
        params = {
            "field_value": field[1],
            "condition_value": condition[1],
        }
        return self.query(query, params)

    def __del__(self):
        """
        Ensure the connexion is closed when the object falls out of scope.
        """
        self._db_connexion.close()