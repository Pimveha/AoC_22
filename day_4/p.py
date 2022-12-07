
def read_file():
	with open("input", "r") as f:
		full_file = f.read()
	return full_file.split("\n")
	# return [i.split() for i in full_file.split("\n")]

def main():
	read_list = read_file()
	cnt = 0
	for item in read_list:
		aa = list(map(int, item.split(",")[0].split("-")))[0]
		ab = list(map(int, item.split(",")[0].split("-")))[1]
		map(int, item.split(",")[0].split("-"))
		if aa == ab:
			a = [aa]
		else:
			a = list(range(aa, ab))

		ba = list(map(int, item.split(",")[1].split("-")))[0]
		bb = list(map(int, item.split(",")[1].split("-")))[1]
		if ba == bb:
			b = [ba]
		else:
			b = list(range(ba, bb))


		# print(a, b)
		# print(a, b)
		tr1 = set(a).issubset(b) or set(b).issubset(a)
		# print(tr, a, b)


		aa = list(map(int, item.split(",")[0].split("-")))[0]
		ab = list(map(int, item.split(",")[0].split("-")))[1]

		ba = list(map(int, item.split(",")[1].split("-")))[0]
		bb = list(map(int, item.split(",")[1].split("-")))[1]

		tr2 = (ba <= aa <= ab <=bb) or (aa <= ba <= bb <= ab)

		
		# q2 = max(aa, ba) <= min(ab, bb)
		if tr1 != tr2:
			print(tr1, a, b)
			cnt += 1

	print(cnt)
		# true_list = [num in char for ]


if __name__ == '__main__':
	main()