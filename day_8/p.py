
def read_file():
	# with open("input", "r") as f:
	with open("input", "r") as f:
		full_file = f.read()
	return [list(map(int, list(i))) for i in full_file.split("\n")]


def main():
	score_list = []
	read_list = read_file()
	c = 0
	for x in range(len(read_list)):
		for y in range(len(read_list[x])):

			# p1
			left_view = right_view = top_view = bottom_view = False
			t = read_list[x][y]

			if all(read_list[x][i] < t for i in range(y)):
				left_view = True
				# print("left view", [read_list[x][i] for i in range(y)], t)

			if all(read_list[x][i] < t for i in range(y + 1, len(read_list[x]))):
				right_view = True
				# print("right view", [read_list[x][i] for i in range(y + 1, len(read_list[x]))], t)

			if all(read_list[i][y] < t for i in range(x)):

				top_view = True
				# print("top view", [read_list[i][y] for i in range(x)], t)

			if all(read_list[i][y] < t for i in range(x + 1, len(read_list))):
				bottom_view = True
				# print("bottom view", [read_list[i][y] for i in range(x + 1, len(read_list))], t)
			
			if left_view or right_view or top_view or bottom_view:
				c += 1

			# print(f"x: {x},  y: {y}\n")



			# p2
			trees_to_the_left = read_list[x][:y]
			trees_to_the_right = read_list[x][y:][1:]
			trees_to_the_top = [read_list[i][y] for i in range(x)]
			trees_to_the_bottom = [read_list[i][y] for i in range(x + 1, len(read_list))]

			left_cnt = right_cnt = top_cnt = bottom_cnt = 0
			# for i, tree in enumerate(trees_to_the_left[::-1], start=1):
			# 	print(i)
			# 	if tree >= t:
			# 		left_cnt = i
			# 		break

			for tree in trees_to_the_left[::-1]:
				left_cnt += 1 
				if tree >= t:
					break
					
			for tree in trees_to_the_right:
				right_cnt += 1 
				if tree >= t:
					break
					
			for tree in trees_to_the_top[::-1]:
				top_cnt += 1 
				if tree >= t:
					break

			for tree in trees_to_the_bottom:
				bottom_cnt += 1 
				if tree >= t:
					break

			# for i in trees_to_the_top:
			# 	print(" "*len(trees_to_the_left), i)
			# print("".join([str(tree) for tree in trees_to_the_left]), t, "".join([str(tree) for tree in trees_to_the_right]))
			# for i in trees_to_the_bottom:
			# 	print(" "*len(trees_to_the_left), i)

			view_score = left_cnt * right_cnt * top_cnt * bottom_cnt
			score_list.append(view_score)

	print(c)
	print(max(score_list))


if __name__ == '__main__':
	main()
