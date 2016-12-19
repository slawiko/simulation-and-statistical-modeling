from generators import Brakovki, Random
from criterias import pirson
from distributions import negative_binomial

p, q, r = 0.25, 0.75, 10


b = Brakovki(p, r)
sequence = b.generate(100, Random())
distribution_sequence = list()
for k in range(0, 100, 10):
    distribution_sequence.append(negative_binomial(k, p, q, r))

print('Сто ДСВ распределенных по Отрицательному биномиальному закону: {0}'.format(sequence))
print('Критерий Пирсона для ДСВ: {0}'.format(pirson(sequence, distribution_sequence, 100)))
