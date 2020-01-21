import sys
import os

if os.path.isfile("moncafe.db"):
    os.remove("moncafe.db")

from Repository import *
import csv


filename = sys.argv[len(sys.argv) - 1]
rowsToInsert =[]
file = open(filename, 'r')
rowsToInsert = file.readlines()
repo.create_tables()
for row in rowsToInsert :
    split = row.split(", ")
    tableName = split[0]
    if tableName == 'E':
        employeeId = split[1]
        name = split[2]
        salary = split[3]
        coffee_stand = split[4]
        E = Employee(employeeId, name, salary, coffee_stand)
        repo.employees.insert(E)
    if tableName == 'S' :
        Id = split[1]
        name = split[2]
        contactInfo = split[3]
        S = Supplier(Id,name,contactInfo)
        repo.suppliers.insert(S)
    if tableName == 'P' :
        Id = split[1]
        description = split[2]
        price = split[3]
        P = Product(Id,description,price, 0)
        repo.products.insert(P)
    if tableName == 'C' :
        Id = split[1]
        location = split[2]
        employees = split[3]
        C = Coffee_stand(Id,location,employees)
        repo.coffee_stands.insert(C)

