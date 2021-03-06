# Data Transfer Objects:


# DTO for Employees
class Employee:
    def __init__(self, id, name, salary, coffee_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand


# DTO for Suppliers
class Supplier:
    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information


# DTO for Products
class Product:
    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity


# DTO for Coffee_stands
class Coffee_stand:
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees


# DTO for Activities
# aid is Activities' primary key
class Activity:
    def __init__(self, aid, product_id, quantity, activator_id, date):
        self.aid = aid
        self.product_id = product_id
        self.quantity = int(quantity)
        self.activator_id = activator_id
        self.date = date



