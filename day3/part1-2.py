

"""
Task:
Starting at the top-left corner of your map and following a slope of right 3 and down 1,
how many trees would you encounter?

"""

if __name__ == "__main__":
    steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]  # (right, left) pairs
    positions = [0] * len(steps)
    tree_counts = [0] * len(steps)

    with open("day3/input.txt", 'r') as f:
        for line_counter, line in enumerate(f.readlines()):
            line = line.strip()
            max_position = len(line)

            for i in range(len(steps)):
                if line_counter % steps[i][1] != 0:
                    continue

                while positions[i] >= max_position:
                    positions[i] -= max_position

                if line[positions[i]] == '#':
                    tree_counts[i] += 1

                positions[i] += steps[i][0]

    print(tree_counts)

    product = 1
    for tc in tree_counts:
        product *= tc
    print(product)
