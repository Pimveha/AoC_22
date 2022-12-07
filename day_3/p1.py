
def read_file():
	with open("input", "r") as f:
		full_file = f.read()
	return full_file.split("\n")
	

def main():
	score = 0
	read_list = read_file()
	for item in read_list:
		a = item[:int(len(item)/2)]
		b = item[int(len(item)/2):]
		# for char in a:
		# 	if 
		match = [char for char in a if char in b][0]
		print(match)
		# print(ord(str(match))-96)
		score_str = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		print(score_str.index(match))
		score += score_str.index(match)
	print(score)



if __name__ == '__main__':
	main()