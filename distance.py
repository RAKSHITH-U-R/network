router_matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0],
                 [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0],
                 [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0],
                 [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7],
                 [0, 0, 2, 0, 0, 0, 6, 7, 0]]
n = len(router_matrix)

distances = dict()
for i in range(n):
    dist = dict()
    for j in range(n):
        if i != j and router_matrix[i][j] != 0:
            dist[j] = router_matrix[i][j]
    distances[i] = dist

edges = list()
for u, dist in distances.items():
    for v, w in dist.items():
        edges.append((u, v, w))


def bellmanford(src):
    dist = [float("Inf")] * n
    dist[src] = 0
    nextHop = {node: None for node in range(n)}

    for i in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if not nextHop[u]:
                    nextHop[v] = v
                else:
                    nextHop[v] = nextHop[u]

    nextHop[src] = src
    # print('Router table for router ', src + 1)
    table = []
    for dest, hop in nextHop.items():
        # print(dest + 1, hop + 1, dist[dest])
        table.append((dest, hop, dist[dest]))

    return table


# print(distances)
# print(edges)

# for i in range(n):
#     bellmanford(i)

start = 5
end = 0

while (start != end):
    print(str(start) + '=>', end="")
    table = bellmanford(start)
    start = table[end][1]
    if start == end:
        print(str(start))
