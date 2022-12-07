
def read_file():
	with open("input", "r") as f:
		full_file = f.read()
	return full_file

def main():
	read_list = read_file()
	act = 0
	for i in range(len(read_list)):
		if len(set(read_list[i:i+4])) == 4:
			print(f"{act}: {read_list[i:i+4]}")
			break
		act += 1
	print(act + 4)



if __name__ == '__main__':
	main()