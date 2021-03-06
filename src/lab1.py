import criterias
from distributions import uniform
from generators import MacLarenMarsaglia, MultiplicativeCongruential, Random

r = Random()
mc = MultiplicativeCongruential()
mm = MacLarenMarsaglia()

mcp = criterias.pirson(mc.generate(100), uniform(0, 1, 100))
rp = criterias.pirson(r.generate(100), uniform(0, 1, 100))
mmp = criterias.pirson(mm.generate(mc, r, 100), uniform(0, 1, 100))

mck = criterias.kolmogorov(mc.generate(100))
rk = criterias.kolmogorov(r.generate(100))
mmk = criterias.kolmogorov(mm.generate(mc, r, 100))

print('Критерий согласия Пирсона для мультипликативного конгруэнтного метода: {0}'.format(mcp))
print('Критерий согласия Пирсона для стандартного датчика: {0}'.format(rp))
print('Критерий согласия Пирсона для метода МакЛорена-Марсальи: {0}'.format(mmp))
print('Критерий согласия Колмогорова для мультипликативного конгруэнтного метода: {0}'.format(mck))
print('Критерий согласия Колмогорова для стандартного датчика: {0}'.format(rk))
print('Критерий согласия Колмогорова для метода МакЛорена-Марсальи: {0}'.format(mmk))
