#prints
    #print "Hello, World!"
print("Hello, World!")

#vars
    #instantiate a varaible a that eqauls 5
a=5
    #multiply a by 4
a=a*4
    #set a to a%8
a=a%8
    #create a varaible b that eqauls 6, and swap the value of a and b
b=6

c=a
a=b
b=c
    #print a and b
print(a)
print(b)
print(str(a)+","+str(b))

#lists
    #make a list l that equals [1,2,3,[4,5,6,[7]], "hello"]
l=[1,2,3,[4,5,6,[7]], "hello"]

    #print the length of l
print("the length of "+str(l)+"="+str(len(l)))

    #print the element at index 3
print(l[3])

    #print the length of the element at index 3, multiplied by 2
print(len(l[3])*2)

    #add "hi" to the end of l
l.append("hi")

    #replace 7 with 8
l[3][3][0]=8

    #remove 2 from l
l.remove(2)

    #print l
print(l)