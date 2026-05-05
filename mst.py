# Find function (with path compression)
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

# Union function
def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal_mst(vertices, edges):
    edges.sort(key=lambda x: x[2])  # Greedy step

    parent = list(range(len(vertices)))
    rank = [0] * len(vertices)

    mst = []
    total_cost = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, w))
            total_cost += w
            union(parent, rank, u, v)

        if len(mst) == len(vertices) - 1:
            break

    print("\nEdges in MST:")
    for u, v, w in mst:
        print(f"{vertices[u]} - {vertices[v]} : {w}")

    print("Total Cost of MST:", total_cost)


# 🔹 Step 1: Number of vertices
v = int(input("Enter number of vertices: "))

# 🔹 Step 2: Enter vertex names
vertices = input("Enter vertex names (e.g., A B C D): ").split()

# Validation (optional but good for viva)
if len(vertices) != v:
    print("Error: Number of names must match number of vertices!")
    exit()

# Mapping (A→0, B→1...)
vertex_map = {name: i for i, name in enumerate(vertices)}

# 🔹 Step 3: Number of edges
e = int(input("Enter number of edges: "))

# 🔹 Step 4: Input edges
edges = []
print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = input().split()
    edges.append((vertex_map[u], vertex_map[v], int(w)))

# 🔹 Run MST
kruskal_mst(vertices, edges)
