def get_row(boarding_pass):
    row = 0
    mult = 64
    for c in boarding_pass:
        if c == "B":
            row += mult

        mult /= 2

    return row


def get_col(boarding_pass):
    col = 0
    mult = 4
    for c in boarding_pass:
        if c == "R":
            col += mult

        mult /= 2

    return col


def get_seat_ID(boarding_pass):
    row = get_row(boarding_pass[:7])
    col = get_col(boarding_pass[-3:])

    return int(row * 8 + col)


if __name__ == '__main__':
    passes = []
    with open("input.txt", "r") as f:
        passes = [l.replace("\n", "") for l in f.readlines()]

    
    seat_IDs = [get_seat_ID(p) for p in passes]

    print("Part 1:")
    print(max(seat_IDs))

    print("Part 2:")
    seat_IDs = sorted(seat_IDs)
    expected_ID = seat_IDs[0]
    for ID in seat_IDs:
        if not ID == expected_ID:
            print(expected_ID)
            break

        expected_ID += 1 


