import numpy as np
from utils import сombination


def negative_binomial(k, p, q, r):
    """

    :param k:
    :param p:
    :param q:
    :param r:
    :return:
    """
    result = 0
    for i in range(k):
        result += сombination(r + i - 1, i) * (p ** r) * (q ** i)
    return result


# TODO: refactor this method in style like negative_binomial
def uniform(a, b, n):
    result = list()
    for i in np.arange(a, b, 1/n):
        result.append(1)
    return result
