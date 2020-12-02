

"""
Task:
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number
of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must
contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but
needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of
their respective policies.

How many passwords are valid according to their policies?

"""


def password_ok(lower, upper, char, password):
    count = 0
    for c in password:
        if c == char:
            count += 1

    return lower <= count <= upper


if __name__ == "__main__":
    count = 0
    with open("day2/input.txt", 'r') as f:
        while line := f.readline():
            bounds, char, password = line.split(' ')
            char = char.strip(':')
            lower, upper = [int(b) for b in bounds.split('-')]

            count += password_ok(lower, upper, char, password)

    print(count)


