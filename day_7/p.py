
def read_file():
	with open("input", "r") as f:
		full_file = f.read()
	return [i.split() for i in full_file.split("\n")]

def main():
	tot_pat_list = []
	size_dict = {}
	file_size = 0
	read_list = read_file()
	for item in read_list:
		if item[0] == "$":
			if item[1] == "cd":
				if item[2] == "..":
					tot_pat_list.pop()
				else:
					tot_pat_list.append(item[2])
			elif item[1] == "ls":
				continue
		elif item[0] == "dir":
			continue
		else:
			dirfilsize = int(item[0])
			for i in range(1, len(tot_pat_list)+1):
				# could've used a defaultdict
				if '/'.join(tot_pat_list[:i]) in size_dict.keys():
					size_dict['/'.join(tot_pat_list[:i])] += dirfilsize
				else:
					size_dict['/'.join(tot_pat_list[:i])] = dirfilsize
	# print(size_dict)	
	v1 = 0
	for k,v in size_dict.items():
		print(k, v) #:)
		if v <= 100000:
			v1 += v
	print("q1:", v1)


	root_total_size = size_dict["/"]
	# print(root_total_size)
	wanted_size = 40000000

	posib_values = []
	for k,v in size_dict.items():
		if v >= root_total_size - wanted_size:
			posib_values.append(v)
	# print(posib_values)
	# print(min(posib_values))
	print("q2:", min(posib_values))


if __name__ == '__main__':
	main()