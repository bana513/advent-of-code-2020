

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

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for
automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
Your job is to count the passports where all required fields are both present and valid according to the above rules.


Time complexity: O(n)
"""


def is_valid_pass(info, keys):
    key_value_pairs = info.split(' ')
    key_count = 0

    for pair in key_value_pairs:

        key, value = pair.split(':')

        if key in keys.keys() and keys[key](value):
            key_count += 1

    return key_count >= 7


def valid_height(str):
    try:
        if str.endswith('cm'):
            str = str[:-2]
            return 150 <= int(str) <= 193
        elif str.endswith('in'):
            str = str[:-2]
            return 59 <= int(str) <= 76
        return False
    except:
        return False


def valid_hair_color(str):
    try:
        if str.startswith('#') and len(str) == 7:
            str = str[1:]
            for char in str:
                if not ('0' <= char <= '9' or 'a' <= char <= 'f'):
                    return False
            return True
        return False
    except:
        return False


def valid_eye_color(str):
    return str in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def valid_pid(str):
    return len(str) == 9 and str.isnumeric()


if __name__ == "__main__":
    keys = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': valid_height,
        'hcl': valid_hair_color,
        'ecl': valid_eye_color,
        'pid': valid_pid,
    }  # ignore cid
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

