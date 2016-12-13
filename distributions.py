import numpy as np
from utils import сombination


def negative_binomial(x, p, q, r):
    """

    :param x:
    :param p:
    :param q:
    :param r:
    :return:
    """
    result = 0
    for i in range(x):
        result += сombination(r + i - 1, i) * (p ** r) * (q ** i)
    return result


def uniform(a, b, n):
    result = list()
    for i in np.arange(a, b, 1/n):
        result.append(1)
    return result
