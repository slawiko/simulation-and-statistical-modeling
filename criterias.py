import math


def kolmogorov(sequence):
    sequence = sorted(sequence)
    n = len(sequence)
    D = 0
    for i in range(n):
        diff = abs((i + 1) / n - sequence[i])
        D = diff if D < diff else D
    return D * math.sqrt(n)


# TODO: сделать образцовое распределение
def pirson(sequence, k, interval=1):
    n = len(sequence)
    size = interval / k
    down, up = 0, 0 + size
    exp_count = n / k
    real_count = 0
    hi2 = 0
    for i in range(k):
        for g in sequence:
            if down <= g < up:
                real_count += 1
        hi2 += ((real_count - exp_count) ** 2) / exp_count
        real_count = 0
        down, up = up, round(up + size, 15)  # bullshit
    return hi2
