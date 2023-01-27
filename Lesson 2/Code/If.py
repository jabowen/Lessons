import random

str="hello there" #input("enter a string: ")
char="t"
a = round(10*random.random(),0)
print(a)
b=True
c=False
d=(a>10)

#if b print b
if(b):
    print(b)

#if c print c
if(c):
    print(c)

#if b and c print b
if(b and c):
    print(b)

#if b or c print c
if(b or c):
    print(c)
    
#if not c print c
if(not c):
    print(c)
    
#if char is in str print True
if(char in str):
    print("True")

#make an if statment with these parameters:
#if a is less than 3 print "hello"
#else if a is greater than or eqaul to 7 print "hi"
#else if a=5 print "hola"
#else if a between 3 and 7 but not 5, print "bonjour"
if(a<3):
    print("hello")
elif(a>=7):
    print("hi")
elif(a==5):
    print("hola")
else:
    print("bonjour")

#make an if statment with these parameters:
#if a is less than 8 and even print "sup"
#else if a is less than 8 or even print "hey"
#else if a is greater than eqaul to 4 and str contains char and str has a length of greater than 6 print "greetings"
if((a<8) and (a%2==0)):
    print("sup")
elif((a<8) or (a%2==0)):
    print("hey")
elif((a>=4) and (char in str) and (len(str)>6)):
    print("greetings")