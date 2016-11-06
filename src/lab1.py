beta = 78125
M = 2**31
start = beta
n = 100

import math
import random

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

def pirson_criteria(generator, k):
    n = len(generator)
    size = 1/k
    down, up = 0, 0 + size
    exp_count = n/k
    real_count = 0
    hi2 = 0
    for i in range(k):
        for g in generator:
            if g >= down and g < up:
                real_count += 1
        hi2 += ((real_count - exp_count)**2) / exp_count;
        real_count = 0;
        down, up = up, round(up + size, 15) # bullshit
    return hi2

def kolmogorov_criteria(generator):
    generator = sorted(generator)
    n = len(generator)
    D = 0
    for i in range(n):
        diff = abs((i + 1) / n - generator[i])
        D = diff if D < diff else D
    return D * math.sqrt(n)

mkmp = pirson_criteria(multi_congruential(beta, M, start, n), n)
rp = pirson_criteria(rand(n), n)
mmp = pirson_criteria(maclaren_marsaglia(multi_congruential(beta, M, start, n), rand(n)), n)

mkmk = kolmogorov_criteria(multi_congruential(beta, M, start, n))
rk = kolmogorov_criteria(rand(n))
mmk = kolmogorov_criteria(maclaren_marsaglia(multi_congruential(beta, M, start, n), rand(n)))

print('Критерий согласия Пирсона для мультипликативного конгруэнтного метода: {0}'.format(mkmp))
print('Критерий согласия Пирсона для стандартного датчика: {0}'.format(rp))
print('Критерий согласия Пирсона для метода МакЛорена-Марсальи: {0}'.format(mmp))
print('Критерий согласия Колмогорова для мультипликативного конгруэнтного метода: {0}'.format(mkmk))
print('Критерий согласия Колмогорова для стандартного датчика: {0}'.format(rk))
print('Критерий согласия Колмогорова для метода МакЛорена-Марсальи: {0}'.format(mmk))
