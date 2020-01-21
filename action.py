import sys
import sqlite3
from DTO import *
from DAO import *

conn = sqlite3.connect('moncafe.db')

actions_file = open(sys.argv[1], "r")

actions_file_lines = actions_file.readlines()
curr_aid = 1
for line in actions_file_lines:
    # parse the current line
    product_id = line.split(', ')[0]
    quantity = line.split(', ')[1]
    activator_id = line.split(', ')[2]
    date = line.split(', ')[3]
    # create DAO activity instance
    activity = Activity(curr_aid, product_id, quantity, activator_id, date)
    print(activity)
    # create a DAO and DTO for the product
    products = Products(conn)
    product = products.find(product_id)
    # create a DAO for the activity
    activities = Activities(conn)
    # if action is arrival
    if activity.quantity > 0:
        products.add_quantity(product, quantity)
        activities.insert(activity)
    elif activity.quantity < 0 and product.quantity >= abs(activity.quantity):
        products.remove_quantity(products,activity.quantity)
        activities.insert(activity)
    curr_aid = curr_aid + 1
conn.commit()
# if the action is arrival then we should update the correct product to add the quantity
