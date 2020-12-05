from day5.part1 import get_id

"""
Task:

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a
catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing
from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

Time complexity: O(n)
"""


if __name__ == "__main__":
    ids = set()

    with open("day5/input.txt", 'r') as f:
        for line in f.readlines():
            id = get_id(line.strip())
            ids.add(id)

    for id in range(min(ids), max(ids)):
        if id + 1 not in ids:
            print(id + 1)

