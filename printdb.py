from Repository import *

print("Activities")
rows = repo.activities.getTable()
for row in rows :
    print(row)

print("Coffee stands")
rows = repo.coffee_stands.getTable()
for row in rows :
    print(row)

print("Employees")
rows = repo.employees.getTable()
for row in rows :
    print(row)

print("Products")
rows = repo.products.getTable()
for row in rows :
    print(row)

print("Suppliers")
rows = repo.suppliers.getTable()
for row in rows :
    print(row)

print("Employees Report")
rows = repo.getEmployeesReport()
for row in rows :
    print(str(row[0]) + " " +str(row[1]) + " " +str(row[2]) + " "+str(row[3]) + " "  )

print("Activity Report")
rows = repo.getActivityReport()
for row in rows :
    print(row)