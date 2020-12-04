if __name__ == '__main__':
    trees = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            l = l.replace("\n", "")
            
            trees.append([(c == "#") for c in l])

    height = len(trees)
    width = len(trees[0])

    x = 0
    y = 0
    trees_count = 0
    while y < height - 1:
        x = (x + 3) % width
        y += 1

        if trees[y][x]:
            trees_count += 1

    print("Part 1")
    print(trees_count)
