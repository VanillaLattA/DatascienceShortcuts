import math
import numpy as np
import collections 

#This snippet of code will take many user inputs and then insert into
#a file with the delimeters being , and then having a class that does things with the file 
#like giving word count, character count, and letter count for each letter


textEntry= int(input("How many data sets do you want to read into the file? "))
fileOpen= open("UserDataEnterBasics.txt") #this will be cleared everytime 
for i in range(textEntry):
    nameOfEntry= input("What is the name of the person? ")
    ageOfEntry= int(input("What is their age? "))
    grossIncomeOfEntry= int(input("What is their gross income? "))
    finalString = str(nameOfEntry + ageOfEntry + grossIncomeOfEntry)
    print(finalString)
