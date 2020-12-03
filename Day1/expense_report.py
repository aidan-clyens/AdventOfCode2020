data = []
with open("input.txt", "r") as f:
    data = [int(l.replace("\n", "")) for l in f.readlines()]


for a in data:
    for b in data:
        for c in data:
            if a + b + c== 2020:
                print(f"{a} * {b} * {c} = {a*b*c}")
                exit()
