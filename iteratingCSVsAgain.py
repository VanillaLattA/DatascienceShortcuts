import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
from csv import DictReader
# Python program to read CSV file line by line
# import necessary packages
import csv

with open('CSGOskinsCSV.csv', 'r') as read_obj: #add these two lines whenever iterating 
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        print(row['Type'])
    read_obj.seek(0)
    for row in csv_dict_reader:
        print(row['Skin'])
