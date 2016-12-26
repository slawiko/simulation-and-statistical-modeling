from generators import Random


def calculate(h):
    A = [[0.6, -0.2], [0.3, 0.1]]
    f = [4, 6]
    p = [[0.5, 0.5], [0.5, 0.5]]
    pi = [0.5, 0.5]
    m = 1000
    N = 1000
    temp_ksi = 0
    i = []
    Q = []
    ksi = []
    r = Random()

    for j in range(m):
        bsv = r.generate(N)
        if bsv[0] < pi[0]:
            i.append(0)
        else:
            i.append(1)
        for k in range(1, N):
            if bsv[k] < pi[0]:
                i.append(0)
            else:
                i.append(1)

        if pi[i[0]] > 0:
            Q.append(h[i[0]] / pi[i[0]])
        else:
            Q.append(0)
        for k in range(1, N):
            if p[i[k-1]][i[k]] > 0:
                Q.append(Q[k - 1] * (A[i[k - 1]][i[k]] / p[i[k - 1]][i[k]]))
            else:
                Q.append(0)
        for k in range(N):
            temp_ksi += Q[k]*f[i[k]]
        ksi.append(temp_ksi)
        temp_ksi = 0
        i = []
        Q = []

    x = 0

    for k in range(m):
        x += ksi[k]
    return x / m

print("x = ", calculate([1, 0]))
print("y = ", calculate([0, 1]))
