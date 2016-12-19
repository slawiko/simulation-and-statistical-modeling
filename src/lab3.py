from generators import Random
from criterias import kolmogorov

n = 10
r = Random()
seq = r.generate(n)


def func(x):
    return 2 * x + 3

result = list()

for i in range(n):
    result.append(func(seq[i]))

print(result)
print(kolmogorov(result))
