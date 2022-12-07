
def read_file():
	with open("input2", "r") as f:
		full_file = f.read()
	return full_file.split("\n")
	

def main():
	score = 0
	read_list = read_file()
	for i in range(0, len(read_list), 3):
		print(read_list[i:i+3])
		match = [char for char in read_list[i] if char in read_list[i] and char in read_list[i+1] and char in read_list[i+2]][0]
		score_str = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		print(score_str.index(match))
		score += score_str.index(match)
		# match = [char for char in read_list[i] if char in all(read_list[i:i+3])]
		print(match)
	# for item in read_list:
	# 	# for char in a:
	# 	# 	if 
	# 	match = [char for char in a if char in b][0]
	# 	print(match)
	# 	# print(ord(str(match))-96)
	# 	score_str = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	# 	print(score_str.index(match))
	# 	score += score_str.index(match)
	print(score)



if __name__ == '__main__':
	main()