import re


def is_valid_count(password_data):
    min_count = password_data[0]
    max_count = password_data[1]
    char = password_data[2]
    pswd = password_data[3]

    c = pswd.count(char)
    return c >= min_count and c <= max_count


def is_valid_pos(password_data):
    pos1 = password_data[0]
    pos2 = password_data[1]
    char = password_data[2]
    pswd = password_data[3]

    pos1_equal = (pswd[pos1-1] == char)
    pos2_equal = (pswd[pos2-1] == char)

    return (pos1_equal and not pos2_equal) or (not pos1_equal and pos2_equal)


if __name__ == '__main__':
    passwords = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            l = re.sub("\n|:", "", l)
            data = re.split("-|\s", l)
            data[0] = int(data[0])
            data[1] = int(data[1])
            passwords.append(data)

    valid_count_1 = 0
    valid_count_2 = 0
    for p in passwords:
        if is_valid_count(p):
            valid_count_1 += 1

        if is_valid_pos(p):
            valid_count_2 += 1

    print("Part 1:")
    print(valid_count_1)

    print("Part 2:")
    print(valid_count_2)
