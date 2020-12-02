

"""
Task:
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second
character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these
positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy
enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?

"""


def password_ok(lower, upper, char, password):
    first_match = len(password) >= lower and (password[lower - 1] == char)
    second_match = len(password) >= upper and (password[upper - 1] == char)
    return (first_match + second_match) == 1


if __name__ == "__main__":
    count = 0
    with open("day2/input.txt", 'r') as f:
        while line := f.readline():
            bounds, char, password = line.split(' ')
            char = char.strip(':')
            lower, upper = [int(b) for b in bounds.split('-')]

            count += password_ok(lower, upper, char, password)

    print(count)


