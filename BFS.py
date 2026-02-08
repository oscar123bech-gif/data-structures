class graph:
    def __init__(self, n):
        self.node = n
        self.a = [[] for _ in range(n)]

    def edges(self, x, y):
        self.a[x-1].append(y-1)
        self.a[y-1].append(x-1)


tree = graph(5)

tree.edges(1, 2)
tree.edges(1, 3)
tree.edges(2, 4)
tree.edges(2, 5)



