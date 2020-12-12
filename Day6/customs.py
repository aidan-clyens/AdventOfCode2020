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
                group.append([c for c in line])
        groups.append(group)

    total_sum = 0
    common_sum = 0
    for group in groups: 
        answers_count = {}
        for person in group:
            for c in person:
                if c not in answers_count.keys():
                    answers_count[c] = 0
                answers_count[c] += 1

        common_answers = set()
        for [a, c] in answers_count.items():
            if c == len(group):
                common_answers.add(a)
        total_sum += len(answers_count)
        common_sum += len(common_answers)

    print("Part 1:")
    print(total_sum)

    print("Part 2:")
    print(common_sum)

