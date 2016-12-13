def сombination(n, k):
    result = 1
    for i in range(1, k+1):
        result = (result / i) * (n - k + i)
    return result
