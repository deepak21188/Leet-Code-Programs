class MinStack:
    def __init__(self):
        self.top=None
        self.min=1000000
        self.stack=[]

    def push(self, x):
        a=[]
        l=self.stack.__len__()
        if(l>0 and self.stack[l-1][1] < x):
            a=[x,self.stack[l-1][1]]
        else:
            a=[x,x]
        self.stack.append(a)

    def pop(self):
        self.stack.pop()

    def ttop(self):
      l = self.stack.__len__()
      return self.stack[l - 1][0]

    def getMin(self):
        l = self.stack.__len__()
        return self.stack[l - 1][1]

