
def sparse_matrix(matrix):
    n = len(matrix)
    sparse = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                sparse.append((i, j, matrix[i][j]))

    return sparse



class MyArray:
    def __init__(self):
        self.data = []

    
    def Insert(self, obj, index):
        self.data.insert(index, obj)

    
    def Delete(self, index):
        return self.data.pop(index)

    
    def Find(self, obj):
        if obj in self.data:
            return self.data.index(obj)
        else:
            return -1

    
    def Display(self):
        print(self.data)



if __name__ == "__main__":
    
    matrix = [
        [0, 0, 3],
        [4, 0, 0],
        [0, 5, 0]
    ]

    print("Sparse Matrix Representation:")
    print(sparse_matrix(matrix))

    
    arr = MyArray()
    arr.Insert(10, 0)
    arr.Insert(20, 1)
    arr.Insert(30, 2)

    print("\nArray after insertions:")
    arr.Display()

    print("\nIndex of 20:", arr.Find(20))

    print("\nDeleted element:", arr.Delete(1))
    print("Array after deletion:")
    arr.Display()
