import math


def check(generator):
	generator = sorted(generator)
	n = len(generator)
	D = 0
	for i in range(n):
		diff = abs((i + 1) / n - generator[i])
		D = diff if D < diff else D
	return D * math.sqrt(n)
