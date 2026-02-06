class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def InsertAtBegin(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def InsertAtEnd(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def InsertAtIndex(self, data, index):
        if index == 0:
            self.InsertAtBegin(data)
            return
        temp = self.head
        for _ in range(index - 1):
            if not temp:
                raise IndexError("Index out of range")
            temp = temp.next
        node = Node(data)
        node.next = temp.next
        temp.next = node

    def UpdateNode(self, data, index):
        temp = self.head
        for _ in range(index):
            if not temp:
                raise IndexError("Index out of range")
            temp = temp.next
        temp.data = data

    def RemoveNodeAtBegin(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def RemoveNodeAtEnd(self):
        if not self.head:
            return None
        if not self.head.next:
            data = self.head.data
            self.head = None
            return data
        temp = self.head
        while temp.next.next:
            temp = temp.next
        data = temp.next.data
        temp.next = None
        return data

    def RemoveNodeAtIndex(self, index):
        if index == 0:
            return self.RemoveNodeAtBegin()
        temp = self.head
        for _ in range(index - 1):
            if not temp.next:
                raise IndexError("Index out of range")
            temp = temp.next
        data = temp.next.data
        temp.next = temp.next.next
        return data

    def SizeOfList(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def Concatenate(self, other):
        if not self.head:
            self.head = other.head
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = other.head

    def Invert(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def Display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def InsertAtBegin(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            node.next = node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        node.next = self.head
        self.head = node
        temp.next = self.head

    def InsertAtEnd(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            node.next = node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = node
        node.next = self.head

    def InsertAtIndex(self, data, index):
        if index == 0:
            self.InsertAtBegin(data)
            return
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
            if temp == self.head:
                raise IndexError("Index out of range")
        node = Node(data)
        node.next = temp.next
        temp.next = node

    def UpdateNode(self, data, index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
            if temp == self.head:
                raise IndexError("Index out of range")
        temp.data = data

    def RemoveNodeAtBegin(self):
        if not self.head:
            return None
        data = self.head.data
        if self.head.next == self.head:
            self.head = None
            return data
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        self.head = self.head.next
        temp.next = self.head
        return data

    def RemoveNodeAtEnd(self):
        if not self.head:
            return None
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        data = temp.next.data
        temp.next = self.head
        return data

    def RemoveNodeAtIndex(self, index):
        if index == 0:
            return self.RemoveNodeAtBegin()
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
            if temp.next == self.head:
                raise IndexError("Index out of range")
        data = temp.next.data
        temp.next = temp.next.next
        return data

    def SizeOfList(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head.next
        while temp != self.head:
            count += 1
            temp = temp.next
        return count

    def Concatenate(self, other):
        if not self.head:
            self.head = other.head
            return
        t1 = self.head
        while t1.next != self.head:
            t1 = t1.next
        t2 = other.head
        while t2.next != other.head:
            t2 = t2.next
        t1.next = other.head
        t2.next = self.head

    def Invert(self):
        if not self.head:
            return
        prev = None
        curr = self.head
        start = self.head
        while True:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            if curr == start:
                break
        self.head.next = prev
        self.head = prev

    def Display(self):
        if not self.head:
            print("None")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")      


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def InsertAtBegin(self, data):
        node = Node(data)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

    def InsertAtEnd(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        node.prev = temp

    def InsertAtIndex(self, data, index):
        if index == 0:
            self.InsertAtBegin(data)
            return
        temp = self.head
        for _ in range(index - 1):
            if not temp.next:
                raise IndexError("Index out of range")
            temp = temp.next
        node = Node(data)
        node.next = temp.next
        node.prev = temp
        if temp.next:
            temp.next.prev = node
        temp.next = node

    def UpdateNode(self, data, index):
        temp = self.head
        for _ in range(index):
            if not temp:
                raise IndexError("Index out of range")
            temp = temp.next
        temp.data = data

    def RemoveNodeAtBegin(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return data

    def RemoveNodeAtEnd(self):
        if not self.head:
            return None
        temp = self.head
        while temp.next:
            temp = temp.next
        data = temp.data
        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None
        return data

    def RemoveNodeAtIndex(self, index):
        if index == 0:
            return self.RemoveNodeAtBegin()
        temp = self.head
        for _ in range(index):
            if not temp:
                raise IndexError("Index out of range")
            temp = temp.next
        data = temp.data
        temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        return data

    def SizeOfList(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def Concatenate(self, other):
        if not self.head:
            self.head = other.head
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = other.head
        if other.head:
            other.head.prev = temp

    def Invert(self):
        curr = self.head
        temp = None
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp:
            self.head = temp.prev

    def Display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    print(" Singly Linked List ")
    sll = SinglyLinkedList()
    sll.InsertAtEnd(10)
    sll.InsertAtEnd(20)
    sll.InsertAtBegin(5)
    sll.InsertAtIndex(15, 2)
    sll.Display()
    print("Size:", sll.SizeOfList())
    sll.UpdateNode(25, 2)
    sll.Display()
    print("Removed:", sll.RemoveNodeAtIndex(1))
    sll.Display()
    sll.Invert()
    print("After invert:")
    sll.Display()

    print("\n Circular Linked List ")
    cll = CircularLinkedList()
    cll.InsertAtEnd(1)
    cll.InsertAtEnd(2)
    cll.InsertAtEnd(3)
    cll.InsertAtBegin(0)
    cll.Display()
    cll.UpdateNode(5, 2)
    cll.Display()
    print("Removed:", cll.RemoveNodeAtIndex(1))
    cll.Display()
    cll.Invert()
    print("After invert:")
    cll.Display()

    print("\n Doubly Linked List ")
    dll = DoublyLinkedList()
    dll.InsertAtBegin(100)
    dll.InsertAtEnd(200)
    dll.InsertAtIndex(150, 1)
    dll.Display()
    dll.UpdateNode(175, 1)
    dll.Display()   
    print("Removed:", dll.RemoveNodeAtIndex(1))
    dll.Display()
    dll.Invert()
    print("After invert:")
    dll.Display()
