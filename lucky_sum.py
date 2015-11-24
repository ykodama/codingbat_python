def lucky_sum(a, b, c):
	n_sum = 0
	nums = [a, b, c]
	for ni in nums:
		if ni != 13:
			n_sum += ni
		else:
			break
	return n_sum
