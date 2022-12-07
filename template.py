
def read_file():
	with open("input", "r") as f:
		full_file = f.read()
	# return full_file.split("\n")
	return [i.split() for i in full_file.split("\n")]

def main():
	read_list = read_file()
	for item in read_list:
		...


if __name__ == '__main__':
	main()
