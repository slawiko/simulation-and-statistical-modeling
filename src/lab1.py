import criterias
from generators import MacLarenMarsaglia, MultiplicativeCongruentialGenerator, Random

r = Random()
mc = MultiplicativeCongruentialGenerator()
mm = MacLarenMarsaglia()

mcp = criterias.pirson(mc.generate(100), 100)
rp = criterias.pirson(r.generate(100), 10)
mmp = criterias.pirson(mm.generate(mc.generate(100), r.generate(100)), 100)

mck = criterias.kolmogorov(mc.generate(100))
rk = criterias.kolmogorov(r.generate(100))
mmk = criterias.kolmogorov(mm.generate(mc.generate(100), r.generate(100)))

print('Критерий согласия Пирсона для мультипликативного конгруэнтного метода: {0}'.format(mcp))
print('Критерий согласия Пирсона для стандартного датчика: {0}'.format(rp))
print('Критерий согласия Пирсона для метода МакЛорена-Марсальи: {0}'.format(mmp))
print('Критерий согласия Колмогорова для мультипликативного конгруэнтного метода: {0}'.format(mck))
print('Критерий согласия Колмогорова для стандартного датчика: {0}'.format(rk))
print('Критерий согласия Колмогорова для метода МакЛорена-Марсальи: {0}'.format(mmk))
