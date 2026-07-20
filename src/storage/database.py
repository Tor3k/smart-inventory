"""
Smart Inventory

SQLite database management.
"""

import sqlite3


class Database:
    """
    Handles the SQLite database connection
    and database initialization.
    """

    def __init__(self, database_path):

        self.database_path = database_path

        self.connection = sqlite3.connect(
            self.database_path
        )

        self.connection.row_factory = sqlite3.Row

        self.create_tables()


    def create_tables(self):
        """
        Creates all required database tables.
        """

        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                identifier TEXT UNIQUE,

                identification_type TEXT NOT NULL,

                name TEXT NOT NULL,

                brand TEXT,

                product_category TEXT NOT NULL,

                unit_type TEXT NOT NULL,

                cost REAL,

                price REAL NOT NULL,

                stock INTEGER NOT NULL,

                quick_entry INTEGER NOT NULL

            )
            """
        )

        self.connection.commit()


    def get_connection(self):

        return self.connection


    def close(self):

        self.connection.close()