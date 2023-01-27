import random

a = round(10*random.random(),0)
l=[]

#while loops

    #print "hi" 25 times
i=0
while(i<25):
    print("hi")
    i=i+1

    #make a loop that iterates until a = 8
    #use "round(10*random.random(),0)" to get a new value if a each iteration
    #put each value of a into l
while(a!=8):
    a=round(10*random.random(),0)
    l.append(a)

    #do the same thing with break()
while(True):
    a=round(10*random.random(),0)
    l.append(a)
    if(a==8):
        break

    #print l
print(l)

#for loops

    #print "hi" 25 times
for i in range(25):
    print("hi")

    #iterate through l printing half of each value

for t in l:
    print(t/2)