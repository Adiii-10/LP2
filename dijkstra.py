import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float("inf")] * n
    distances[start] = 0

    priority_queue = [(0, start)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Input
n, e = map(int, input("Enter number of vertices and edges: ").split())

graph = [[] for _ in range(n)]

print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # undirected

start_node = int(input("Enter the source node: "))

distances = dijkstra(graph, start_node)

print("\nShortest distances from node", start_node)
for i, dist in enumerate(distances):
    print(f"Node {i}: {dist}")
