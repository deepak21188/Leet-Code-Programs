class Queue:
    def __init__(self):
           self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)


q= Queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(6)
q.enqueue(9)
print(q.dequeue())
print(q.dequeue())


