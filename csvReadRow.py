import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

with open('addresses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    row1=next(csv_reader)
    print(row1)
