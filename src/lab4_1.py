import math
from generators import Random

n = 100
r = Random()
bsv = r.generate(n)
sequence = list()

for i in range(n):
    sequence.append(- math.log(1 - bsv[i]))


def calculate(x):
    n = len(x)
    result = 0
    for i in range(n):
        result += (x[i] * math.log(x[i]) / ((1 + math.pow(x[i], 3)) * math.exp(-x[i])))
    return result / n


print(calculate(sequence))
