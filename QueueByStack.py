class queuebystacks:
    def __init__(self):
        self.st=[]
        self.rt=[]

    def enqueue(self,item):
        self.st.append(item)

    def dequeue(self):
        rl=self.rt.__len__()
        sl= self.st.__len__()
        if(rl>0):
            return self.rt.pop(-1)

        if(sl>0):
            while(sl>0):
                self.rt.append(self.st.pop(-1))
                sl=self.st.__len__()
            return self.rt.pop(-1)
        else:
            return "Empty queue"


q= queuebystacks()
q.enqueue(1)
q.enqueue(4)
q.enqueue(6)
q.enqueue(7)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())