def xyz_there(str):
	i_x_list = []
	for i in range(len(str)-2):
		if str[i:i+3] == "xyz":
			i_x_list.append(i)

	isThere = False
	for j in i_x_list:
		if j == 0:
			return True
		elif str[j-1] == ".":
			isThere = False
		else:
			isThere = True

	return isThere


if __name__ == "__main__":
	print xyz_there("abcxyz")