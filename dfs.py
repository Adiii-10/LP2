#DFS

def dfs(graph,vertex,visited):
    visited.add(vertex)
    print(vertex,end="")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)


graph={}
n=int(input("Enter the number of vertices: "))
for i in range(n):
    graph[i]=[]

e=int(input("enter the number of edges:"))

print("Enter edges(u,v):")
for i in range(e):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

start=int(input("enter starting vertex"))

print("\n Depth first search(DFS):")
visited=set()
dfs(graph,start,visited)
