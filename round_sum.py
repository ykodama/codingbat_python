def round_sum(a, b, c):
	n_sum = 0
	nums = [a, b, c]
	for ni in nums:
		n_sum += round10(ni)
	return n_sum


def round10(num):
	rest = num % 10
	if rest >= 5:
		return (num // 10)*10 + 10
	else:
		return (num // 10)*10