def sum2(data, S):
    i = 0
    j = len(data) - 1

    while i < j:
        if data[i] + data[j] == S:
            return [data[i], data[j]]
        elif data[i] + data[j] < S:
            i += 1
        else:
            j -= 1


def sum3(data, S):
    for i in range(len(data)):
        d = sum2(data[i+1:], S - data[i])
        if d is not None:
            if data[i] + d[0] + d[1] == S:
                return d + [data[i]]


if __name__ == "__main__":
    data = []
    with open("input.txt", "r") as f:
        data = [int(l.replace("\n", "")) for l in f.readlines()]

    data = sorted(data)
    S = 2020

    print("Part 1:")
    [a, b] = sum2(data, S)
    print(f"{a} * {b} = {a*b}")
    
    print("Part 2:")
    [a, b, c] = sum3(data, S)
    print(f"{a} * {b} * {c} = {a*b*c}")
