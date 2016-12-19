import random
from methods import brakovki_for_negative_binomial


class MultiplicativeCongruential:
    def __init__(self, beta=78125, m=2 ** 31, start=78125):
        self.seq = []
        self.beta = beta
        self.m = m
        self.start = start

    def generate(self, n, cache=False):
        if cache and len(self.seq) == n:
            return self.seq
        temp = list()
        temp.append(self.start)
        self.seq = list()
        for i in range(n):
            self.seq.append(temp[i] / self.m)
            temp.append((self.beta * temp[i]) % self.m)
        return self.seq


class Random:
    def __init__(self):
        self.seq = []

    def generate(self, n, cache=False):
        if cache and len(self.seq) == n:
            return self.seq
        self.seq = list()
        for i in range(n):
            self.seq.append(random.random())
        return self.seq


class MacLarenMarsaglia:
    def __init__(self):
        self.seq = []

    def generate(self, generator1, generator2, n, cache=False):
        seq1 = generator1.generate(n)
        seq2 = generator2.generate(n)
        if cache and len(self.seq) == len(seq1):
            return self.seq
        K = len(seq1)
        V = list(seq1)
        self.seq = list()
        for i in range(K):
            s = int(seq2[i] * K)
            self.seq.append(V[s])
            V[s] = seq1[i]
        return self.seq


class Brakovki:
    def __init__(self, p, r):
        self.seq = []
        self.p = p
        self.r = r

    def generate(self, n, generator, cache=False):
        if cache and len(self.seq) == n:
            return self.seq
        self.seq = list()
        while len(self.seq) < n:
            temp = brakovki_for_negative_binomial(self.p, self.r, generator.generate(n))
            if temp:
                self.seq.append(temp)
        return self.seq
