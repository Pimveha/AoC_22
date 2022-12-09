
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
	with open("input_test", "r") as f:
	# with open("input", "r") as f:
		full_file = f.read()
	return [(i.split()[0], i.split()[1]) for i in full_file.split("\n")]

def allowed_tail_positions(h_p):
	allowed_tuple_list = [tuple(map(sum,zip(h_p, i))) for i in allowed_tail_list]
	# print(allowed_tuple_list)
	return allowed_tuple_list

def main():
	read_list = read_file()
	tail9_postitions_visited = []

	start_post = (0, 0)
	# position = (x, y)
	tail_length = 9
	head_position = start_post
	tail_positions = [start_post] * tail_length
	for item in read_list:
		# move head --> tail follows
		move_amount = int(item[1])
		move_direction = item[0]
		print(f"\n\n\n=={move_amount}, {move_direction}")
		for step in range(move_amount):
			head_position = tuple(map(sum,zip(head_position, move_dir_dict[move_direction])))
			print("\n\n\nmain Head:", head_position)
			for indx, tail_p_move in enumerate(tail_positions):
				snake = [head_position] + tail_positions
				# tail position
				print("\n(temp)head:", tail_positions[indx], "\t\ttail:", snake[indx])
				if tail_positions[indx] in allowed_tail_positions(snake[indx]):
					print("allowed: H:", head_position, "\tT:", tail_positions)
					# tail_postitions_visited.append(tail_position)
				else:
					#move tail posoition accordingly
					if indx == 0:
						if move_direction == "U":
							sp = tail_positions[indx]
							tail_positions[indx] = tuple(map(sum,zip(snake[indx], (0, -1))))
							ep = tail_positions[indx]
							d_tuple = (ep[0]-sp[0], ep[1]-sp[1])

							# tail_position = tuple(map(sum,zip(head_position, (0, -1))))
							# print("H:", head_position, "\tT:", tail_position)
						elif move_direction == "D":
							# tail_position = tuple(map(sum,zip(head_position, (0, 1))))
							sp = tail_positions[indx]
							tail_positions[indx] = tuple(map(sum,zip(snake[indx], (0, 1))))
							ep = tail_positions[indx]
							d_tuple = (ep[0]-sp[0], ep[1]-sp[1])
							# print("H:", head_position, "\tT:", tail_position)
						elif move_direction == "L":
							# tail_position = tuple(map(sum,zip(head_position, (1, 0))))
							sp = tail_positions[indx]
							tail_positions[indx] = tuple(map(sum,zip(snake[indx], (1, 0))))
							ep = tail_positions[indx]
							d_tuple = (ep[0]-sp[0], ep[1]-sp[1])
							# print("H:", head_position, "\tT:", tail_position)
						elif move_direction == "R":
							# tail_position = tuple(map(sum,zip(head_position, (-1, 0))))
							sp = tail_positions[indx]
							tail_positions[indx] = tuple(map(sum,zip(snake[indx], (-1, 0))))
							ep = tail_positions[indx]
							d_tuple = (ep[0]-sp[0], ep[1]-sp[1])
					else:
						tail_positions[indx] = tuple(map(sum,zip(tail_positions[indx], d_tuple)))



					print("tail moves: H:", head_position, "\tT:", tail_positions)
					tail9_postitions_visited.append(tail_positions[-1])


	# print(tail_postitions_visited)
	# print(len(tail_postitions_visited))
	print(len(set(tail9_postitions_visited)))

	# print(postitions_visited)




if __name__ == '__main__':
	main()