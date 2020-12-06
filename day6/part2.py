

"""
Task:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to
which everyone answered "yes"!


Time complexity: O(n)
Note: The creation of intersection has a constant upper bound as there are constant characters
"""


if __name__ == "__main__":
    count = 0

    with open("day6/input.txt", 'r') as f:
        group_answers = set([chr(char) for char in range(ord('a'), ord('z')+1)])
        for line in f.readlines():
            if line == "\n":
                count += len(group_answers)
                group_answers = set([chr(char) for char in range(ord('a'), ord('z')+1)])
            else:
                group_answers = group_answers.intersection(set(line.strip()))

        count += len(group_answers)

    print(count)

