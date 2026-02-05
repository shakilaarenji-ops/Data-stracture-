class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]
        self.front = 0
        self.rear = -1
        self.count = 0

    def Enqueue(self, obj):
        if self.IsFull():
            print("Queue is full")
            return
        self.rear += 1
        self.queue[self.rear] = obj
        self.count += 1

    def Dequeue(self):
        if self.IsEmpty():
            print("Queue is empty")
            return None
        obj = self.queue[self.front]
        self.front += 1
        self.count -= 1
        return obj

    def Peek(self):
        if self.IsEmpty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def ReverseQueue(self):
        reversed_queue = Queue(self.size)
        temp = []

        while not self.IsEmpty():
            temp.append(self.Dequeue())

        while temp:
            reversed_queue.Enqueue(temp.pop())

        return reversed_queue

    def IsEmpty(self):
        return self.count == 0

    def IsFull(self):
        return self.count == self.size

    def Display(self):
        print(self.queue)



class CircularQueue:
    def init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def Enqueue(self, obj):
        if self.IsFull():
            print("Circular Queue is full")
            return
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = obj
        self.count += 1

    def Dequeue(self):
        if self.IsEmpty():
            print("Circular Queue is empty")
            return None
        obj = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return obj

    def Peek(self):
        if self.IsEmpty():
            print("Circular Queue is empty")
            return None
        return self.queue[self.front]

    def ReverseQueue(self):
        reversed_queue = CircularQueue(self.size)
        temp = []

        while not self.IsEmpty():
            temp.append(self.Dequeue())

        while temp:
            reversed_queue.Enqueue(temp.pop())

        return reversed_queue

    def IsEmpty(self):
        return self.count == 0

    def IsFull(self):
        return self.count == self.size

    def Display(self):
        print(self.queue)



if __name__ == "__main__":
    print("Normal Queue:")
    q = Queue(5)
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    q.Display()

    print("Dequeued:", q.Dequeue())
    print("Front element:", q.Peek())

    rq = q.ReverseQueue()
    print("Reversed Queue:")
    rq.Display()

    print("\nCircular Queue:")
    cq = CircularQueue(5)
    cq.Enqueue(1)
    cq.Enqueue(2)
    cq.Enqueue(3)
    cq.Display()

    print("Dequeued:", cq.Dequeue())
    cq.Enqueue(4)
    cq.Enqueue(5)
    cq.Display()
