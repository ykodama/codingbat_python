def end_other(a, b):
	if len(a) >= len(b):
		str_long = a
		str_short = b
	else:
		str_long = b
		str_short = a

	str_long = str_long.lower()
	str_short = str_short.lower()

	if str_long.endswith(str_short):
		return True
	else:
		return False