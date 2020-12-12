if __name__ == '__main__':
    groups = []
    with open("input.txt", "r") as f:
        group = []
        for line in f.readlines():
            line = line.replace("\n", "")
            if len(line) == 0:
                groups.append(group)
                group = []
            else:
                group.append(line)
        groups.append(group)

    total_sum = 0
    for group in groups: 
        answers = set()
        for person in group:
            for c in person:
                answers.add(c)

        total_sum += len(answers)

    print("Part 1:")
    print(total_sum)

