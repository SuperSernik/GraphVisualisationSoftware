class Queue:
    def __init__(self):
        self.queue = []

    def deQ(self):
        return self.queue.pop(0)
    
    def enQ(self, x):
        self.queue.append(x)
        return self.queue.index(x)
    
    def __len__(self):
        return len(self.queue)
    

class Stack:
    def __init__(self):
        self.__stack = []

    def pop(self):
        return self.__stack.pop()

    def push(self, x):
        self.__stack.append(x)
        return self.__stack.index(x)
    
    def __len__(self):
        return len(self.__stack)
    
    def __str__(self):
        return 'Stack: ' + str(self.__stack)
    