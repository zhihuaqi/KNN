class KNN():
    def __init__(self, k):
        self.k = k

    def fit(self, v, g):
        self.v = v
        self.g = g

    def pred(self, x):
        res = []
        for i, v in enumerate(self.v):
            res.append([i, abs(v - x)])
        res.sort(key=lambda x: x[1])
        g_info = [self.g[res[i][0]] for i in range(self.k)]
        dic = {}
        for g in g_info:
            if g not in dic:
                dic[g] = 1
            else:
                dic[g] += 1
        res1 = []
        for k, v in dic.items():
            res1.append([k, v])
        res1.sort(key=lambda x: x[1], reverse=True)
        return res1[0][0]


if __name__ == '__main__':
    v = [1, 2, 4, 5, 2, 6, 7, 2, 3, 9]
    g = ['A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A']
    model = KNN(3)
    model.fit(v,g)
    model.pred(5)