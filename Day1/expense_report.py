data = []
with open("input.txt", "r") as f:
    data = [int(l.replace("\n", "")) for l in f.readlines()]


for a in data:
    for b in data:
        if a + b == 2020:
            print(a*b)
            exit()
