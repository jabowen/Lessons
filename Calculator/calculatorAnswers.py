class CalculatorAnswers:
    result=None
    eq=[]
    input=""
    nums = ['0','1','2','3','4','5','6','7','8','9','.']
    ops = ['/','*','-','+']

    
    def __init__(self):
        self.eq=[]

    def calculateTest(self,inp):
        self.eq=[]
        self.result=None
        self.input=""
        self.scan(inp)
        self.eq=self.parse(self.eq)
        self.solve()

    def calculate(self):
        inp=input()
        while(inp!=""):
            self.calculateTest(inp)
            print(self.result)
            inp=input()

    def scan(self,inp):
        self.input=inp
        prevNum=0
        length=len(self.input)
        i=0
        while(i<length):
            if(i==' '):
                continue
            if(self.input[i] in self.nums):
                curr=0
                dec=False
                decVal=1
                while(i<length and (self.input[i] in self.nums)):
                    if(self.input[i]=='.'):
                        dec=True
                        i+=1
                    if(dec):
                        decVal*=10
                    curr=curr*10+int(self.input[i])
                    i+=1
                self.eq.append(curr/decVal)
            else:
                self.eq.append(self.input[i])
                i=i+1

        
    def parse(self, eq):
        ind=-1
        for j in self.ops:
            for i in range(len(eq)):
                if(eq[i]==j):
                    ind=i
                    break
        if(not(ind==-1)):
            left=self.parse(eq[:ind])
            right=self.parse(eq[ind+1:])
            eq=[left,eq[ind],right]
        return eq
        
    def add(self,x,y):
        return x+y
        
    def mult(self,x,y):
        return x*y
        
    def sub(self,x,y):
        return x-y
        
    def div(self,x,y):
        return x/y

    def solve(self):
        self.result=round(self.traverse(self.eq),4)
    
    def traverse(self,inp):
        if(len(inp)==1):
            if(type(inp[0])==list):
                return self.traverse(inp[0])
            else:
                return inp[0]
        else:
            if(inp[1]=='+'):
                return self.add(self.traverse(inp[0]), self.traverse(inp[2]))
            elif(inp[1]=='-'):
                return self.sub(self.traverse(inp[0]), self.traverse(inp[2]))
            elif(inp[1]=='*'):
                return self.mult(self.traverse(inp[0]), self.traverse(inp[2]))
            elif(inp[1]=='/'):
                return self.div(self.traverse(inp[0]), self.traverse(inp[2]))