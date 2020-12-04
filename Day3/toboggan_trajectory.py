def num_trees_hit(trees, right, down):
    height = len(trees)
    width = len(trees[0])

    x = 0
    y = 0
    trees_count = 0
    while y < height - 1:
        x = (x + right) % width
        y += down

        if trees[y][x]:
            trees_count += 1

    return trees_count


if __name__ == '__main__':
    trees = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            l = l.replace("\n", "")
            
            trees.append([(c == "#") for c in l])

    
    trees_count_1 = num_trees_hit(trees, 3, 1)
    print("Part 1")
    print(trees_count_1)

    trees_count_2 = num_trees_hit(trees, 1, 1)
    trees_count_3 = num_trees_hit(trees, 5, 1)
    trees_count_4 = num_trees_hit(trees, 7, 1)
    trees_count_5 = num_trees_hit(trees, 1, 2)
    print("Part 2")
    print(f"{trees_count_1} * \
{trees_count_2} * \
{trees_count_3} * \
{trees_count_4} * \
{trees_count_5} = \
{trees_count_1*trees_count_2*trees_count_3*trees_count_4*trees_count_5}"
    )
