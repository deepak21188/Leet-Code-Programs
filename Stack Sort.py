class stack:
    def __init__(self):
        self.st=[]

    def sortStack(self):
        rt=[]
        while(self.st.__len__()>0):
            temp= self.st.pop(-1)
            rl=rt.__len__()
            while(rl>0 and rt[rl-1]>temp):
                self.st.append(rt.pop(-1))
                rl = rt.__len__()
            rt.append(temp)
        return rt

s=stack()
s.st.append(2)
s.st.append(1)
s.st.append(4)
s.st.append(3)
s.st.append(5)
print(s.sortStack())






