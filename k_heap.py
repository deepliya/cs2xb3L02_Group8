class k_heap:
    
    length = 0
    data = []
    k = 2

    def __init__(self, L, k):
        self.data = L
        self.length = len(L)
        self.build_heap(L)
        self.k = k

    def build_heap(self, values):

        for i in range(self.length - 1 // self.k, -1, -1):
            self.sink(i)

    def parent(self, i):
        return (i - 1) / self.k

    def children(self, i):

        children = []

        for _ in range(1, self.k+1):
            children.append(self.k * i + _)

        return children

    def sink(self, i):

        largest_known = i

        children = self.children(i)

        for _ in range(0, len(children)):

            if children[_] < self.length and self.data[children[_]] > self.data[largest_known]:
                largest_known = children[_]

        if largest_known != i:
            self.data[largest_known], self.data[i] = self.data[i], self.data[largest_known]

    def get_max(self):
        if len(self.data) > 0:
            return self.data[0]

L = [0, -1]
heap = k_heap(L, 2)

print(heap.get_max())