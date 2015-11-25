def double_char(str):
	str_new = ""
	for i in range(len(str)):
		str_new += 2*str[i]
	return str_new

if __name__ == "__main__":
	print double_char("abc")
