import random


#make a function that returns a list of random length, with random elements between 0 and 20
#it should have arguments min and max

def randList():
    l=[]
    for i in range(int(rand(5, 30, 0))):
        l.append(rand(0,20,0))
    return l
    

#make a function that returns the sum of a list
#if an element in the list is equal to 8.0, then print the "no", and return None

def sumList(l):
    s=0
    for i in l:
        s=i+s
        if(i==8.0):
            print("no")
            return None
    return s
    

def rand(min, max, dec):
    return round((max-min)*random.random(),dec) + min

#main
listy=randList()
print(listy)
print(sumList(listy))
print(sum(listy))