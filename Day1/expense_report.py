data = []
with open("input.txt", "r") as f:
    data = [int(l.replace("\n", "")) for l in f.readlines()]

data = sorted(data)
S = 2020

i = 0
j = len(data) - 1

while i < j:
    if data[i] + data[j] == S:
        print(f"{data[i]} * {data[j]} = {data[i]*data[j]}")
        break
    elif data[i] + data[j] < S:
        i += 1
    else:
        j -= 1

