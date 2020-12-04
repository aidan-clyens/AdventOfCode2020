if __name__ == '__main__':
    trees = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            l = l.replace("\n", "")
            
            trees.append([(c == ".") for c in l])

    print(trees)
