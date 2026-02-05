
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    
    def HashFunction(self, key):
        return hash(key) % self.size
    
    def Insert(self, key, value):
        index = self.HashFunction(key)

        for item in self.table[index]:
            if item[0] == key:
                item[1] = value  
                return

        self.table[index].append([key, value])

    
    def Remove(self, key):
        index = self.HashFunction(key)

        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                return item[1]

        return None

    
    def Search(self, key):
        index = self.HashFunction(key)

        for item in self.table[index]:
            if item[0] == key:
                return item[1]

        return None

    
    def Display(self):
        for i in range(self.size):
            print(f"{i}: {self.table[i]}")



if __name__ == "__main__":
    ht = HashTable()

    ht.Insert("Ali", 20)
    ht.Insert("Reza", 25)
    ht.Insert("Sara", 30)

    print("Search Ali:", ht.Search("Ali"))
    print("Remove Reza:", ht.Remove("Reza"))

    ht.Display()
