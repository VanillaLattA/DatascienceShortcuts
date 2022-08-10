import math
import numpy as np
import collections 

#This snippet of code will take many user inputs and then insert into
#a file with the delimeters being , and then having a class that does things with the file 
#like giving word count, character count, and letter count for each letter

#get the number of data sets that are being used in the file 
try:
    textEntry= int(input("How many data sets do you want to read into the file? "))
except ValueError:
    print("The value that you entered cannot be processed")
    
#open the file 
fileOpen= open("testFile.txt", 'r+') #this will be cleared everytime per the first line

for i in range(textEntry):
    nameOfEntry= input("What is the name of the person? ")
    ageOfEntry= input("What is their age? ")
    grossIncomeOfEntry= input("What is their gross income? ") 
    finalString = str(nameOfEntry + ";" + ageOfEntry + ";"+ grossIncomeOfEntry)
    fileOpen.write(finalString)
