#!/usr/bin/python3

class Tree:
    def __init__(self, parent):
        self.parent = parent
        self.n = len(self.parent)
        self.child = [[] for _ in range(self.n)]
        for v in range(self.n):
            assert isinstance(v, int)
            if v == 0:
                assert self.parent[v] == -1
                continue
            assert 0 <= self.parent[v] < v
            self.child[self.parent[v]] += [v]

    def _euler_dfs(self, v, dep):
        self.euler_tour += [(v, dep)]
        for u in self.child[v]:
            self._euler_dfs(u, dep + 1)
            self.euler_tour += [(v, dep)]

    def build_euler_tour(self):
        self.euler_tour = []
        self._euler_dfs(0, 0)


def __main__():
    parent = list(map(int, input().split()))
    t = Tree(parent)
    t.build_euler_tour()
