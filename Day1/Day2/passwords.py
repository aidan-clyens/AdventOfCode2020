import re


if __name__ == '__main__':
    passwords = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            l = re.sub("\n|:", "", l)
            data = re.split("-|\s", l)
            data[0] = int(data[0])
            data[1] = int(data[1])
            passwords.append(data)

    valid_count = 0
    for p in passwords:
        min_count = p[0]
        max_count = p[1]
        char = p[2]
        pswd = p[3]

        c = pswd.count(char)
        if c >= min_count and c <= max_count:
            valid_count += 1

    print("Part 1:")
    print(valid_count)
