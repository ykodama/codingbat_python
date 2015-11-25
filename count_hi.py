def count_hi(str):
	count = 0
	for i in range(len(str)-1):
		if str[i:i+2] == "hi":
			count += 1
	return count

if __name__ == "__main__":
	a = count_hi("abc hi ho")
	b = count_hi("ABChi hi")
	c = count_hi("hihi")
	print a, b, c