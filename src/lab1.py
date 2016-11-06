import random
from criterias import pirson, kolmogorov

beta = 78125
M = 2 ** 31
start = beta
n = 100


def multi_congruential(beta, M, start, n):
	temp = list()
	temp.append(start)
	generator = list()
	for i in range(n):
		generator.append(temp[i] / M)
		temp.append((beta * temp[i]) % M)
	return generator


def rand(n):
	generator = list()
	for i in range(n):
		generator.append(random.random())
	return generator


def maclaren_marsaglia(generator1, generator2):
	if len(generator1) is not len(generator2):
		raise Exception('Generators must have the same len')
	K = len(generator1)
	V = list(generator1)
	generator = list()
	for i in range(K):
		s = int(generator2[i] * K)
		generator.append(V[s])
		V[s] = generator1[i]
	return generator


mkmp = pirson.check(multi_congruential(beta, M, start, n), n)
rp = pirson.check(rand(n), n)
mmp = pirson.check(maclaren_marsaglia(multi_congruential(beta, M, start, n), rand(n)), n)

mkmk = kolmogorov.check(multi_congruential(beta, M, start, n))
rk = kolmogorov.check(rand(n))
mmk = kolmogorov.check(maclaren_marsaglia(multi_congruential(beta, M, start, n), rand(n)))

print('Критерий согласия Пирсона для мультипликативного конгруэнтного метода: {0}'.format(mkmp))
print('Критерий согласия Пирсона для стандартного датчика: {0}'.format(rp))
print('Критерий согласия Пирсона для метода МакЛорена-Марсальи: {0}'.format(mmp))
print('Критерий согласия Колмогорова для мультипликативного конгруэнтного метода: {0}'.format(mkmk))
print('Критерий согласия Колмогорова для стандартного датчика: {0}'.format(rk))
print('Критерий согласия Колмогорова для метода МакЛорена-Марсальи: {0}'.format(mmk))
