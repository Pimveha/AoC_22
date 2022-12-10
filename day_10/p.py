from collections import defaultdict

def read_file():
	with open("input", "r") as f:
	# with open("input2", "r") as f:
	# with open("input3", "r") as f:
		full_file = f.read()
	return [i.split() for i in full_file.split("\n")]


def main():
	read_list_list = read_file()
	cycle_amount = sum(2 if read_list_list[i][0] == "addx" else 1 for i in range(len(read_list_list)))
	v = 1
	cycle_val_dict = defaultdict(int)
	cycle_count = 2
	for line in read_list_list:
		# if read_list_list[pos][0] == "noop":
		if line[0] == "noop":
			cycle_val_dict[cycle_count] = v
			cycle_count += 1
		else:
			val = int(line[1])
			cycle_val_dict[cycle_count] = v
			cycle_count += 1

			cycle_val_dict[cycle_count] = v + val
			v = cycle_val_dict[cycle_count]
			cycle_count += 1

	# p1
	sum_list = []
	for k, v in cycle_val_dict.items():
		# print(k, v)
		if k in [20, 60, 100, 140, 180, 220]:
			sum_list.append(k*v)
	print(sum(sum_list))

	# p2
	screen = ""
	for i in range(len(list(cycle_val_dict.values()))-1):
		if list(cycle_val_dict.values())[i-1] - 1 <= i % 40 <= list(cycle_val_dict.values())[i-1] + 1:
			screen += '#'
		else:
			screen += ' '
	print()
	for i in range(40,241,40):
		print(screen[i-40:i])

if __name__ == '__main__':
	main()