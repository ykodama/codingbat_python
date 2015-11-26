def count_evens(nums):
	count = 0
	for ni in nums:
		if ni % 2 == 0:
			count += 1

	return count
