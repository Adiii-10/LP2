class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal_mst(n, edges):
    edges.sort(key=lambda x: x[2])  # sort by weight

    ds = DisjointSet(n)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):  # no cycle
            mst.append((u, v, weight))
            total_cost += weight
            ds.union(u, v)

    return mst, total_cost


# Input
n, e = map(int, input("Vertices & Edges: ").split())

edges = []
print("Enter edges (u v weight):")

for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

mst, cost = kruskal_mst(n, edges)

print("\nEdges in MST:")
for u, v, w in mst:
    print(f"{u} - {v} (weight: {w})")

print("Total cost of MST:", cost)
