def big_diff(nums):
	v_min = nums[0]
	v_max = nums[0]
	for ni in nums:
		if ni < v_min:
			v_min = ni
		if ni > v_max:
			v_max = ni

	return v_max - v_min

if __name__ == "__main__":
	print big_diff([10, 3, 5, 6])