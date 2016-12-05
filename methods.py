# Берется последовательность независимых случайных чисел,
# равномерно распределенных на [0,1]. Среди них подсчитывается количество чисел,
# меньших p, и количество чисел, больших p. В тот момент, когда количество y чисел,
# меньших p, впервые станет равным x, количество чисел, больших p, даст случайное число,
# подчиняющееся отрицательному биномиальному распределению


def brakovki_for_negative_binomial(p, r, generator):
    if r > len(generator):
        raise Exception('Parameter p must be smaller than generator length')

    count_smaller, count_bigger = 0, 0
    for x in generator:
        if x < p:
            count_smaller += 1
        else:
            count_bigger += 1
        if count_smaller == r:
            return count_bigger

    return None
