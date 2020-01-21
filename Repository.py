import atexit
import sqlite3
import DTO
import os
# The Repository
from DAO import *


class _Repository:
    def __init__(self):
        if os.path.exists("moncafe.db"):
            os.remove("moncafe.db")
        self._conn = sqlite3.connect('moncafe.db')
        self.employee = Employees(self._conn)
        self.supplier = Suppliers(self._conn)
        self.product = Products(self._conn)
        self.coffee_stands = Coffee_stands(self._conn)
        self.activity = Activities(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()




    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE Employees (
            id      INT         PRIMARY KEY,
            name    TEXT        NOT NULL,
            salary  REAL        NOT NULL,
            coffee_stand INTEGER REFERENCES Coffee_stand(id)
        );

        CREATE TABLE Suppliers (
            id      INT         PRIMARY KEY,
            name    TEXT        NOT NULL,
            contact_information  TEXT    
        );

        CREATE TABLE Products (
            id      INT     PRIMARY KEY
            description  REAL     NOT NULL,
            quantity           INT     NOT NULL
        );
        CREATE TABLE Coffee_stands (
            id  INT     PRIMARY KEY,
            location    TEXT        NOT NULL,
            number_of_employees INT
        );
        CREATE TABLE Activities (
            aid INT PRIMARY KEY,
            product_id INT REFERENCES Product(id),
            quantity INT NOT NULL.
            activator_id INT NOT NULL 
            date DATE NOT NULL
        );
    """)
    def insertList(self, rowsToInsert):
        for row in rowsToInsert:
            if row[]

# the repository singleton
repo = _Repository()
atexit.register(repo._close)