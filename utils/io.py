

def read_lines(filename):
    with open(filename, 'r') as f:
        return f.readlines()


def read_number(filename):
    with open(filename, 'r') as f:
        return [int(line) for line in f.readlines()]
