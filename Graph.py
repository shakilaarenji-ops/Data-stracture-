
class Graph:
    def __init__(self):
        
        self.graph = {}

    
    def AddVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    
    def AddEdge(self, firstVertex, secondVertex):
        if firstVertex not in self.graph:
            self.AddVertex(firstVertex)
        if secondVertex not in self.graph:
            self.AddVertex(secondVertex)

        if secondVertex not in self.graph[firstVertex]:
            self.graph[firstVertex].append(secondVertex)
            self.graph[secondVertex].append(firstVertex)

    
    def RemoveEdge(self, firstVertex, secondVertex):
        if firstVertex in self.graph and secondVertex in self.graph[firstVertex]:
            self.graph[firstVertex].remove(secondVertex)
            self.graph[secondVertex].remove(firstVertex)


    def RemoveVertex(self, vertex):
        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                self.graph[neighbor].remove(vertex)
            del self.graph[vertex]

    
    def BFS(self, start):
        visited = set()
        queue = [start]
        result = []

        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            result.append(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return " -> ".join(result)


    def DFS(self, start):
        visited = set()
        result = []

        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return " -> ".join(result)

    
    def Display(self):
        for vertex in self.graph:
            print(vertex, ":", self.graph[vertex])



if __name__ == "__main__":
    g = Graph()

    g.AddVertex("A")
    g.AddVertex("B")
    g.AddVertex("C")
    g.AddVertex("D")

    g.AddEdge("A", "B")
    g.AddEdge("A", "C")
    g.AddEdge("B", "D")
    g.AddEdge("C", "D")

    print("Graph:")
    g.Display()

    print("\nBFS from A:")
    print(g.BFS("A"))

    print("\nDFS from A:")
    print(g.DFS("A"))

    print("\nRemove Edge A-C")
    g.RemoveEdge("A", "C")
    g.Display()

    print("\nRemove Vertex D")
    g.RemoveVertex("D")
    g.Display()
