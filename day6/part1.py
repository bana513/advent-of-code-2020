

"""
Task:

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?


Time complexity: O(n)
Note: The creation unions has a constant upper bound as there are constant characters
"""


if __name__ == "__main__":
    count = 0

    with open("day6/input.txt", 'r') as f:
        group = ""
        for line in f.readlines():
            if line == "\n":
                count += len(set(group))
                group = ""
            else:
                group += line.strip()

        count += len(set(group))

    print(count)

