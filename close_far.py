def close_far(a, b, c):
	diff_ab = abs(a-b) 
	diff_bc = abs(b-c)
	diff_ca = abs(c-a)

	if diff_ab <= 1 and (diff_bc >= 2 and diff_ca >= 2):
		return True
	elif diff_ca <= 1 and (diff_ab >= 2 and diff_bc >= 2):
		return True
	else:
		return False