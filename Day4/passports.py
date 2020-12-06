def is_valid(passport):
    expected_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for k in expected_keys:
        if k not in passport.keys():
            return False

    return True


if __name__ == '__main__':
    passports = []
    passports.append({})
    i = 0
    with open("input.txt", "r") as f:
        for l in f.readlines():
            l = l.replace("\n", "").split()
            if len(l) == 0:
                i+= 1
                passports.append({})
            else:
                for entry in l:
                    entry = entry.split(":")
                    passports[i][entry[0]] = entry[1]

    valid_count = 0
    for p in passports:
        if is_valid(p):
            valid_count += 1

    print("Part 1:")
    print(valid_count)
