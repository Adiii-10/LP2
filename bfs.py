from collections import deque

# BFS
def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])

    visited.add(start_vertex)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Input
graph = {}

n = int(input("Enter number of vertices: "))
for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges: "))
print("Enter edges (u v):")

for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # undirected

start = int(input("Enter starting vertex: "))

# BFS
print("\nBreadth First Search (BFS):")
bfs(graph, start)
