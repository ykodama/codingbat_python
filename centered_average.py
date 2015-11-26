def centered_average(nums):
	# n_min = nums[0]
	# n_max = nums[0]
	# i_min = 0
	# i_max = 0
	# for i, ni in enumerate(nums):
	# 	if ni < n_min:
	# 		n_min = ni
	# 		i_min = i
	# 	if ni > n_max:
	# 		n_max = ni
	# 		i_min = i

	nums.remove(max(nums))
	nums.remove(min(nums))

	return sum(nums)/len(nums)

if __name__ == "__main__":
	print centered_average([100, 0, 5, 3, 4])