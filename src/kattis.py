import math


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb

        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra

        else:
            self.parent[rb] = ra
            self.rank[ra] += 1

        return True


T = int(input())

for _ in range(T):

    S, P = map(int, input().split())

    points = []

    for _ in range(P):
        x, y = map(int, input().split())
        points.append((x, y))

    edges = []

    # cria todas as arestas
    for i in range(P):

        x1, y1 = points[i]

        for j in range(i + 1, P):

            x2, y2 = points[j]

            dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

            edges.append((dist, i, j))

    # ordena arestas
    edges.sort()

    dsu = DSU(P)

    used = 0
    answer = 0

    # Kruskal
    for dist, u, v in edges:

        if dsu.union(u, v):

            answer = dist
            used += 1

            # queremos S componentes
            if used == P - S:
                break

    print(f"{answer:.2f}")