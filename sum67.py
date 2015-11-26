def sum67(nums):
	n_sum = 0

	is67seq = False
	for ni in nums:
		if ni == 6:
			is67seq = True
		elif ni == 7:
			is67seq = False
		elif is67seq:
			continue
		else:
			n_sum += ni

	return ni