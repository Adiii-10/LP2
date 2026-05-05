import heapq

def simple_a_star(graph, heuristic, start, goal):
    
    queue = [(heuristic[start], start, [start])]
    
    visited = set()

    while queue:
       
        f, current, path = heapq.heappop(queue)

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            
            for neighbor, cost in graph[current]:
               
                g_score = 0
                for i in range(len(path) - 1):
                    for nxt, w in graph[path[i]]:
                        if nxt == path[i + 1]:
                            g_score += w

                g_score += cost

               
                f_score = g_score + heuristic[neighbor]

               
                heapq.heappush(queue, (f_score, neighbor, path + [neighbor]))

    return None


v = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

graph = {}

for _ in range(v):
    node = input("Enter node name: ")
    graph[node] = []

print("Enter edges (u v weight):")
for _ in range(e):
    u, vtx, w = input().split()
    w = int(w)
    graph[u].append((vtx, w))

heuristic = {}
print("Enter heuristic values:")
for node in graph:
    heuristic[node] = int(input(f"h({node}) = "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = simple_a_star(graph, heuristic, start, goal)

if path:
    print("Best path:", " -> ".join(path))
else:
    print("No path found")
