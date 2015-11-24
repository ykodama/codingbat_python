def lone_sum(a, b, c):
	n_sum = 0
	nums = [a, b, c]
	for i,n1 in enumerate(nums):
		isSame = False
		for j,n2 in enumerate(nums):
			if i != j and n1 == n2:
				isSame = True
		if not isSame:
			n_sum += n1

	return n_sum