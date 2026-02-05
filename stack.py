
class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
    
    
    def Push(self, item):
        if self.IsFull():
            print("Stack is full")
            return
        self.stack.append(item)

    
    def Pop(self):
        if self.IsEmpty():
            print("Stack is empty")
            return None
        return self.stack.pop()

    
    def Peek(self):
        if self.IsEmpty():
            print("Stack is empty")
            return None
        return self.stack[-1]

    
    def IsEmpty(self):
        return len(self.stack) == 0

    
    def IsFull(self):
        return len(self.stack) == self.size

    
    def Display(self):
        print(self.stack)



if __name__ == "__main__":
    s = Stack(5)

    s.Push(10)
    s.Push(20)
    s.Push(30)

    print("Stack elements:")
    s.Display()

    print("Top element:", s.Peek())

    print("Popped element:", s.Pop())
    print("Stack after pop:")
    s.Display()
