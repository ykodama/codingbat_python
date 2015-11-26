def sum13(nums):
	if not nums:
		return 0

	n_sum = 0
	is13back = False 
	for i, ni in enumerate(nums):
		if ni == 13:
			is13back = True
		elif is13back == True:
			is13back = False
		elif is13back == False:
			n_sum += ni
			is13back = False

	return n_sum