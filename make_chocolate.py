def make_chocolate(small, big, goal):
	big_max = goal // 5
	if big_max > big:
		a = goal - big*5
	else:
		a = goal - big_max*5

	if a > small:
		return -1
	else:
		return a