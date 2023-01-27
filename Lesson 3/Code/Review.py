import random


#make a function that returns a list of random length, with random elements between 0 and 20
#it should have arguments min and max

#make a function that returns the sum of a list
#if an element in the function is equal to 8.0, then print the index, and return None


def rand(min, max, dec):
    return round((max-min)*random.random(),dec) + min