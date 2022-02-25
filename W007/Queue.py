class Queue:
    def __init__(self):
        self.q=[]

    def __eq__(self, other):
        return self.q == other.q

    def __len__(self):
        return len(self.q)

    def isEmpty(self):
        return (len(self.q)==0)

    def enqueue (self, item):
        return self.q.append(item)

    def dequeue(self):
        return self.q.pop(0)


a=Queue()
a.enqueue('apple')
a.enqueue('banana')
a.enqueue('coconut')
print(a.q)