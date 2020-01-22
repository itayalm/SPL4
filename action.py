import sys
import sqlite3
from DTO import *
from DAO import *
from Repository import *

actions_file = open(sys.argv[len(sys.argv) -1], "r")

actions_file_lines = actions_file.readlines()
curr_aid = 1
for line in actions_file_lines:
    # parse the current line
    product_id = line.split(', ')[0]
    quantity = line.split(', ')[1]
    activator_id = line.split(', ')[2]
    date = line.split(', ')[3]
    # create DTO activity instance
    activity = Activity(curr_aid, product_id, int(quantity), activator_id, date)
    # create a DTO for the product
    product = repo.products.find(product_id)
    # if action is arrival
    if activity.quantity > 0:
        repo.products.add_quantity(product, activity.quantity)
        repo.activities.insert(activity)
    elif activity.quantity < 0 and product.quantity >= abs(activity.quantity):
        repo.products.remove_quantity(product, activity.quantity)
        repo.activities.insert(activity)
    curr_aid = curr_aid + 1
import printdb
# if the action is arrival then we should update the correct product to add the quantity
