#make a function, sep, that takes a string and seperates it by spaces, returning a list
#ex. sep("hello, how are you doing?") returns ["hello", "how", "are", "you", "doing?"]

#make a function, rando, that takes a list of strings and randomized their order

#make a function, noPuncs, that takes a list of string, and removes any with 
# [".", ",", "!", "?"]

#make a function, noNums, that takes a list of strings and replaces any that contain
#  a number with "ERROR: Incorrect Characters"

#make a function, stringify, that takes a list of string and combines them into 1 string, 
# with spaces in between

#make a function that does the job of rando, noNums, noPuncs, and stringify 
# in one loops

#add your functions to this function, changing sentence with each one
def ruinSentence(sentence):
    #add here



    return sentence

#a function to test your work
def test():
    inp="c:/Users/jjb33/OneDrive/Desktop/Lessons/Lesson 3/tests/test1.txt"
    f=open(inp)
    for line in f:
        if(line[-1]=="\n"):
            line=line[:-1]
        print(line)
        print(ruinSentence(line))


#run your tests here
test()