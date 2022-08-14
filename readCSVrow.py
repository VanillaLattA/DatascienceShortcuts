import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
with open('addresses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[1]) #prints row #1 of the CSV
