#from calculator import Calculator
from calculatorAnswers import CalculatorAnswers


def test(calc):
    inp="c:/Users/jjb33/OneDrive/Desktop/tiger/test/"+input()+".txt"
    f=open(inp)
    fails=[]
    for line in f:
        if(line[-1]=="\n"):
            line=line[:-1]
        lines=line.split("=")
        calc.calculateTest(lines[0])
        if(calc.result!=float(lines[1])):
            fails.append("\n"+line+"\nYou Got: "+str(calc.result))
    if(len(fails)>0):
        print("\n\nYou Failed "+ str(len(fails))+" tests")
        for i in fails:
            print(i)
    else:
        print("\n\nSuccess!!")
    print("\n")



    
if __name__ == "__main__":
    calc=CalculatorAnswers()
    test(calc)
    #calc.calculate()
    #while(inp!=""):
        #inp=input()