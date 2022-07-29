import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
import math as m

class stack():
    def __init__(self):
        self.items=[] #initialize empty stack
    def push(self, data):
        self.items.append(data)
    def printStack(self):
        print(self.items[::-1])
    def pop(self):
        self.items.pop()
    def peek(self):
        print(self.items[0])
    def printReverse(self):
        print(self.items)
    def peekMiddle(self):
        halfLength= m.floor(len(self.items)/2)
        print(self.items[halfLength])
        
        

testStack=stack() #Tests to see it works
testStack.push(1)
testStack.push(3)
testStack.push(5)
testStack.printStack()
testStack.pop()
testStack.pop()
testStack.printStack()
testStack.peek()
testStack.push("hello")
testStack.push(133)
testStack.printStack()
testStack.peekMiddle()

