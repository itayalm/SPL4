import atexit
import sqlite3
import DTO
import os
# The Repository
from DAO import *


class _Repository:
    def __init__(self):

        self._conn = sqlite3.connect('moncafe.db')
        self.employees = Employees(self._conn)
        self.suppliers = Suppliers(self._conn)
        self.products = Products(self._conn)
        self.coffee_stands = Coffee_stands(self._conn)
        self.activities = Activities(self._conn)

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
            id      INT     PRIMARY KEY,
            description  REAL     NOT NULL,
            price REAL NOT NULL,
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
            quantity INT NOT NULL,
            activator_id INT NOT NULL ,
            date DATE NOT NULL
                
        );
        SELECT name, salary, coffee_stand ,MAX(0,(SELECT SUM(quantity* price ) FROM Employees NATURAL JOIN Activities 
            NATURAL  JOIN Products) )FROM Employees
        
    """)

    def getEmployeesReport(self):
        c = self._conn.cursor()
        c.execute("""
        SELECT name, salary, coffee_stand ,ifnull((SELECT SUM(a.quantity* price ) FROM Employees as e INNER JOIN
        (Products as p INNER JOIN Activities as a ON id= product_id AND a.quantity < 0) as sub ON e.id = sub.activator_id),0)FROM Employees 
               """)

        #"""SUM(A.quantity * P.price) FROM Employees as e INNER JOIN Activities as a ON e.id = a.activator_id INNER JOIN Products as P ON P.id = A.product_id;"""

        return c.fetchall()

    def getActivityReport(self):
        c = self._conn.cursor()
        c.execute("""
        SELECT A.date, P.description, A.quantity, 'NONE',  S.name FROM Activities as A INNER JOIN Products as P ON A.product_id = P.id INNER JOIN Suppliers as S ON S.id = A.activator_id WHERE A.quantity > 0 
        UNION
        SELECT  A.date, P.description, A.quantity,  E.name , 'NONE' FROM Activities as A INNER JOIN Products as P ON A.product_id = P.id INNER JOIN Employees as E ON E.id = A.activator_id WHERE A.quantity < 0 ORDER BY date ASC
               """)

        #"""SUM(A.quantity * P.price) FROM Employees as e INNER JOIN Activities as a ON e.id = a.activator_id INNER JOIN Products as P ON P.id = A.product_id;"""

        return c.fetchall()

# the repository singleton
repo = _Repository()
atexit.register(repo._close)