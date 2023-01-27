import random

def hi(a,b,c):
    print(a)
    print(b+c)

l=[round(10*random.random(),0), 
round(10*random.random(),0),
round(10*random.random(),0),
round(10*random.random(),0),
round(10*random.random(),0),
round(10*random.random(),0)]

var1=round(10*random.random(),0)
var2=round(10*random.random(),0)
#functions

    #make a function called hello that prints "Hello, World!"
def hello():
    print("Hello, World!")

    #make a function called add that takes two paramters, 
    # a and b, and returns their sum
def add(a, b):
    return a+b
    
    #make a recursive factorial function

def factorial(g):
    fact=1
    while(g>0):
        fact=fact*g
        g=g-1
    return fact

def fact(f):
    if(f==0):
        return 1
    return f*fact(f-1)
    #make a function sum that takes a list, listy, and sums its elements
def sum(listy):
    s=0
    for i in listy:
        s=i+s

    return s


    #make a function foo that takes a function func as an arguments
    # as well as two others a and b
    #call func on a and b
    #return "hello" if that value is greater than 15
    #print "hello" if not
def foo(func,a,b):
    func(a,b)
    if(func(a,b)>15):
        return "hello"
    else:
        print("hi")
    

#main
    #call hello
print(hello())
    #print the result of add with 7 and 6
print(add(7, 6))
print(add(add(4,5), add(7,6)))
    #print the result of factorial of 10
print(factorial(10))

    #call sum on l
print(l)
print(sum(l))

    #call add on the result of sum(l) and round(10*random.random(),0)
add(sum(l), round(10*random.random(),0))
    #call factorial on var1
print(factorial(var1))
    #print the result of foo on add, var1 nd var2

print(foo(add, var1,var2))

