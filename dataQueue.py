import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
import math as m

class queue():
    def __init__(self):
        self.items=[] #initialize empty queue
    def push(self, data):
        self.items.append(data)
    def printQueue(self):
        print(self.items)
    def remove(self):
        self.items.pop(0)
    def peekFront(self):
        print(self.items[0])
    def peekBack(self):
        lengthOfQueue=len(self.items)
        print(self.items[lengthOfQueue-1])

testStack=queue() #Tests to see it works
testStack.push(1)
testStack.push(3)
testStack.push(5)
testStack.push(2)
testStack.push(0)
testStack.printQueue()
testStack.remove()
testStack.peekFront()
testStack.peekBack()
#works as intended
