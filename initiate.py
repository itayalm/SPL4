import sqlite3
import sys
import Repository
import csv


filename = sys.argv[len(sys.argv) - 1]
rowsToInsert =[]
file = open(filename, 'r')
rowsToInsert = file.readlines()
repo = Repository()
repo.insertList(rowsToInsert)