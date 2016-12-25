import math
from generators import Random
from distributions import ravn_reverse

r = Random()
n = 100
sequence_x = list()
sequence_y = list()
bsv_x = r.generate(n)
bsv_y = r.generate(n)
a_x = 0
b_x = 2
a_y = 0
b_y = 2 * math.pi

for i in range(n):
    sequence_x.append(ravn_reverse(a_x, b_x, bsv_x[i]))
    sequence_y.append(ravn_reverse(a_y, b_y, bsv_y[i]))


def calculate(seq_x, seq_y):
    n = len(seq_x)
    result = 0
    for i in range(n):
        result += math.sqrt(math.fabs(seq_x[i] * math.sin(seq_y[i]) - seq_y[i] * math.cos(seq_x[i])) ** 2) * 4 * math.pi
    return result / n


print(calculate(sequence_x, sequence_y))
