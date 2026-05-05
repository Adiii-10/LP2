import heapq

n, e = map(int, input("Vertices & Edges: ").split())

g = {i: [] for i in range(n)}

for _ in range(e):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))   # undirected graph

start = int(input("Start vertex: "))

visited = set()
pq = [(0, start)]   # (weight, vertex)
cost = 0

while pq:
    w, u = heapq.heappop(pq)

    if u in visited:
        continue

    visited.add(u)
    cost += w

    for v, wt in g[u]:
        if v not in visited:
            heapq.heappush(pq, (wt, v))

print("MST cost:", cost)
