

"""
Task:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

Count the number of valid passports - those that have all required fields. Treat cid as optional.
In your batch file, how many passports are valid?


Time complexity: O(n)
"""


def is_valid_pass(info, keys):
    key_value_pairs = info.split(' ')
    key_count = 0

    for pair in key_value_pairs:

        key, value = pair.split(':')

        if key in keys:
            key_count += 1

    return key_count >= 7


if __name__ == "__main__":
    keys = set(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))  # ignore cid
    count = 0

    with open("day4/input.txt", 'r') as f:
        info = ""

        for line in f.readlines():
            if line == "\n":
                if is_valid_pass(info.strip(), keys):
                    count += 1
                info = ""
            else:
                info += " " + line.strip()

        if is_valid_pass(info.strip(), keys):
            count += 1

    print(count)

