from generators import Random
from criterias import kolmogorov
from distributions import ravn_reverse

n = 10
r = Random()
seq = r.generate(n)
a = 3
b = 5


result = list()

for i in range(n):
    result.append(ravn_reverse(a, b, seq[i]))

print(result)
print(kolmogorov(result))
