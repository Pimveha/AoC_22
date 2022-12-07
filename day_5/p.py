import json

def read_file():
	with open("inputa", "r") as f:
		full_file = f.read()
	return full_file.split("\n")
	# return [i.split() for i in full_file.split("\n")]

#                 [B]     [L]     [S]
#         [Q] [J] [C]     [W]     [F]
#     [F] [T] [B] [D]     [P]     [P]
#     [S] [J] [Z] [T]     [B] [C] [H]
#     [L] [H] [H] [Z] [G] [Z] [G] [R]
# [R] [H] [D] [R] [F] [C] [V] [Q] [T]
# [C] [J] [M] [G] [P] [H] [N] [J] [D]
# [H] [B] [R] [S] [R] [T] [S] [R] [L]
#  1   2   3   4   5   6   7   8   9 

crate_dict = {"1": ["R", "C", "H"],
			"2": ["F", "S", "L", "H", "J", "B"],
			"3": ["Q", "T", "J", "H", "D", "M", "R"],
			"4": ["J", "B", "Z", "H", "R", "G", "S"], 
			"5": ["B", "C", "D", "T", "Z", "F", "P", "R"],
			"6": ["G", "C", "H", "T"],
			"7": ["L", "W", "P", "B", "Z", "V", "N", "S"],
			"8": ["C", "G", "Q", "J", "R"],
			"9": ["S", "F", "P", "H", "R", "T", "D", "L"]}

instructions = read_file()

#move 8 from 7 to 1

# 1
for line in instructions:
	move_amount = line.split()[1]
	move_from = line.split()[3]
	move_to = line.split()[5]
	crate_dict[move_to] += crate_dict[move_from][:-int(move_amount) - 1:-1]
	del crate_dict[move_from][-int(move_amount):]
	# print(move_amount, move_from, move_to)
	# items = crate_dict[move_from][:int(move_amount)]
	# items = items[::-1]
	# new_dict = crate_dict
	# new_dict[move_from] = crate_dict[move_from][int(move_amount):]
	# new_dict[move_to] += items
	# print(items)
	# print(json.dumps(new_dict, indent=1))
	# crate_dict = new_dict

for i in crate_dict.values():
	print(i[0], end= "")
print()



crate_dict = {"1": ["R", "C", "H"],
			"2": ["F", "S", "L", "H", "J", "B"],
			"3": ["Q", "T", "J", "H", "D", "M", "R"],
			"4": ["J", "B", "Z", "H", "R", "G", "S"], 
			"5": ["B", "C", "D", "T", "Z", "F", "P", "R"],
			"6": ["G", "C", "H", "T"],
			"7": ["L", "W", "P", "B", "Z", "V", "N", "S"],
			"8": ["C", "G", "Q", "J", "R"],
			"9": ["S", "F", "P", "H", "R", "T", "D", "L"]}
# 2
for line in instructions:
	move_amount = line.split()[1]
	move_from = line.split()[3]
	move_to = line.split()[5]
	# print(move_amount, move_from, move_to)
	items = crate_dict[move_from][:int(move_amount)]
	new_dict = crate_dict
	new_dict[move_from] = crate_dict[move_from][int(move_amount):]
	new_dict[move_to] += items
	# print(items)
	# print(json.dumps(new_dict, indent=1))
	crate_dict = new_dict

for i in crate_dict.values():
	print(i[0], end= "")
print()



