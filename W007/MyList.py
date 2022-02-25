import random
class MyList:

    def __init__(self, initial =[]):
        self.lst = initial

    def __len__(self):
        return len(self.lst)

    def append(self,item):
        self.lst.append(item)

    def choice(self):
        return random.choice(self.lst)

















