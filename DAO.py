# Data Access Objects:
from DTO import *


# DAO for Employees
class Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""
                       INSERT INTO Employees (id, name,salary, coffee_stand) VALUES (?, ?, ?, ?)
                   """, [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def find(self, employee_id):
        c = self._conn.cursor()
        c.execute("""
                    SELECT id, name, salary, coffee_stand FROM Employees WHERE id = ?
                """, [employee_id])

        return Employee(*c.fetchone())


# DTO for Suppliers
class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                       INSERT INTO Suppliers (id, name, contact_information) VALUES (?, ?, ?)
                   """, [supplier.id, supplier.name, supplier.contact_information])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
                    SELECT id, name, contact_information FROM Suppliers WHERE id = ?
                """, [supplier_id])

        return Supplier(*c.fetchone())


# DTO for Products
class Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
                               INSERT INTO Products (id, description, price, quantity) VALUES (?, ?, ?, ?)
                           """, [product.id, product.description, product.price, product.quantity])

    def find(self, product_id):
        c = self._conn.cursor()
        c.execute("""
                            SELECT id, description, price, quantity FROM Products WHERE id = ?
                        """, [product_id])

        return Product(*c.fetchone())


# DTO for Coffee_stands
class Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffee_stand):
        self._conn.execute("""
                                       INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES (?, ?, ?)
                                   """, [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])

    def find(self, coffee_stand_id):
        c = self._conn.cursor()
        c.execute("""
                                   SELECT id, location, number_of_employees FROM Coffee_stands WHERE id = ?
                               """, [coffee_stand_id])

        return Coffee_stands(*c.fetchone())


#DTO for Activities
class Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activity):
        self._conn.execute("""
                 INSERT INTO Activities (aid ,product_id, quantity, activator_id, date) VALUES (?, ?, ?)
        """, [activity.aid, activity.product_id, activity.quantity, activity.activator_id, activity.date])

    def find(self, aid):
        c = self._conn.cursor()
        c.execute("""
                                   SELECT aid, product_id, quantity, activator_id, date FROM Activities WHERE id = ?
                               """, [aid])

        return Activity(*c.fetchone())



