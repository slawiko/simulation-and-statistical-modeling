import random


class MultiplicativeCongruentialGenerator:
	def __init__(self):
		self.seq = []

	def generate(self, n, beta=78125, m=2 ** 31, start=78125, cache=False):
		if cache and len(self.seq) == n:
			return self.seq
		temp = list()
		temp.append(start)
		self.seq = list()
		for i in range(n):
			self.seq.append(temp[i] / m)
			temp.append((beta * temp[i]) % m)
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

	def generate(self, generator1, generator2, cache=False):
		if len(generator1) is not len(generator2):
			raise Exception('Generators must have the same len')
		if cache and len(self.seq) == len(generator1):
			return self.seq
		K = len(generator1)
		V = list(generator1)
		self.seq = list()
		for i in range(K):
			s = int(generator2[i] * K)
			self.seq.append(V[s])
			V[s] = generator1[i]
		return self.seq
