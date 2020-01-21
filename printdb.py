from Repository import *

print("Activity")
rows = repo.activities.getTable()
for row in rows :
    print(row)

print("Coffee_stand")
rows = repo.coffee_stands.getTable()
for row in rows :
    print(row)

print("Employee")
rows = repo.employees.getTable()
for row in rows :
    print(row)

print("Product")
rows = repo.products.getTable()
for row in rows :
    print(row)

print("Supplier")
rows = repo.suppliers.getTable()
for row in rows :
    print(row)
