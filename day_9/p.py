
move_dir_dict = {
	"L": (-1, 0),
	"R": (1, 0),
	"U": (0, 1),
	"D": (0, -1)
}

allowed_tail_list = [
(-1, 0),
(1, 0),
(0, 1),
(0, -1),
(1, 1),
(-1, 1),
(1, -1),
(-1, -1),
(0, 0)
]

def read_file():
	# with open("input_test", "r") as f:
	with open("input", "r") as f:
		full_file = f.read()
	return [(i.split()[0], i.split()[1]) for i in full_file.split("\n")]

def allowed_tail_positions(h_p):
	allowed_tuple_list = [tuple(map(sum,zip(h_p, i))) for i in allowed_tail_list]
	# print(allowed_tuple_list)
	return allowed_tuple_list

def main():
	read_list = read_file()
	tail_postitions_visited = []

	start_post = (0, 0)
	# position = (x, y)
	head_position = tail_position = start_post
	for item in read_list:
		# move head --> tail follows
		move_amount = int(item[1])
		move_direction = item[0]
		for step in range(move_amount):
			head_position = tuple(map(sum,zip(head_position, move_dir_dict[move_direction])))
			print("H:", head_position, "\tT:", tail_position)

			# tail position
			if tail_position in allowed_tail_positions(head_position):
				print("allowed: H:", head_position, "\tT:", tail_position)
				tail_postitions_visited.append(tail_position)
			else:
				#move tail posoition accordingly
				if move_direction == "U":
					tail_position = tuple(map(sum,zip(head_position, (0, -1))))
					# print("H:", head_position, "\tT:", tail_position)
				elif move_direction == "D":
					tail_position = tuple(map(sum,zip(head_position, (0, 1))))
					# print("H:", head_position, "\tT:", tail_position)
				elif move_direction == "L":
					tail_position = tuple(map(sum,zip(head_position, (1, 0))))
					# print("H:", head_position, "\tT:", tail_position)
				elif move_direction == "R":
					tail_position = tuple(map(sum,zip(head_position, (-1, 0))))

				print("tail moves: H:", head_position, "\tT:", tail_position)
				tail_postitions_visited.append(tail_position)

	# print(tail_postitions_visited)
	# print(len(tail_postitions_visited))
	print(len(set(tail_postitions_visited)))

	# print(postitions_visited)




if __name__ == '__main__':
	main()