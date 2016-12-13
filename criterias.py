import math


def kolmogorov(sequence):
    sequence = sorted(sequence)
    n = len(sequence)
    D = 0
    for i in range(n):
        diff = abs((i + 1) / n - sequence[i])
        D = diff if D < diff else D
    return D * math.sqrt(n)


# TODO: make for lab1
def pirson(sequence, distribution_sequence, interval=1):
    n = len(sequence)
    k = len(distribution_sequence) - 1
    size = interval / k
    down, up = 0, 0 + size
    real_count = 0
    hi2 = 0
    for i in range(k):
        exp_count = (distribution_sequence[i+1] - distribution_sequence[i]) * n
        for g in sequence:
            if down <= g < up:
                real_count += 1
        hi2 += ((real_count - exp_count) ** 2) / exp_count
        real_count = 0
        down, up = up, round(up + size, 15)  # bullshit
    return hi2
