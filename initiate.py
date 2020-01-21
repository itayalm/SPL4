import sqlite3
import sys
from Repository import *
import csv


filename = sys.argv[len(sys.argv) - 1]
rowsToInsert =[]
file = open(filename, 'r')
rowsToInsert = file.readlines()
for row in rowsToInsert :
    split = row.split(", ")
    tableName = split[0]
    if tableName == 'E':
        employeeId = split[1]
        name = split[2]
        salary = split[3]
        coffee_stand = split[4]
        E = Employee(employeeId, name, salary, coffee_stand)
        print(E)
        repo.employees.insert(E)
    if tableName == 'S' :
        Id = split[1]
        name = split[2]
        contactInfo = split[3]
        S = Supplier(Id,name,contactInfo)
        print(S)
        repo.suppliers.insert(S)
    if tableName == 'P' :
        Id = split[1]
        description = split[2]
        price = split[3]
        P = Product(Id,description,price)
        print(P)
        repo.products.insert(P)
    if tableName == 'C' :
        Id = split[1]
        location = split[2]
        employees = split[3]
        C = Coffee_stand(Id,location,employees)
        print(C)
        repo.coffee_stands.insert(C)

