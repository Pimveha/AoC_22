

# A for A, B for B, and C for C.
# X for A, Y for B, and Z for C

def read_file():
    with open("input", "r") as f:
        games = f.read().split("\n")
    games = """A Z
B Y
C Z""".split("\n")
    return games

def main():
    games = read_file()
    op_list = ["A", "B", "C"]
    me_list = ["X", "Y", "Z"]
    score = 0
    for game in games:
    	p1 = game[-1]
        p2 = game[0]
        p2_real = me_list[op_list.index(p2)]
        print(f"{p1}, {p2}")
 
        if p1 == p2_real:
            score += me_list.index(p1) +1 + 3
        elif p1 == "X":
            if p2_real == "Y":
                score += me_list.index(p1) + 1
            else:
                score += me_list.index(p1) + 1 + 6
        elif p1 == "Y":
            if p2_real == "Z":
                score += me_list.index(p1) +1
            else:
                score += me_list.index(p1) +1 + 6
        elif p1 == "Z":
            if p2_real == "X":
                score += me_list.index(p1) + 1
            else:
                score += me_list.index(p1) +1 + 6
    print(score)


if __name__ == '__main__':
    main()