def check(generator, k):
	n = len(generator)
	size = 1 / k
	down, up = 0, 0 + size
	exp_count = n / k
	real_count = 0
	hi2 = 0
	for i in range(k):
		for g in generator:
			if down <= g < up:
				real_count += 1
		hi2 += ((real_count - exp_count) ** 2) / exp_count
		real_count = 0
		down, up = up, round(up + size, 15)  # bullshit
	return hi2
