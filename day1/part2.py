from utils.io import read_number
import numpy as np
from day1.part1 import find_pair

"""
Task:
What is the product of the three entries that sum to 2020?

Time comlexity: O(n^2)
"""
if __name__ == "__main__":
    numbers = read_number("day1/input.txt")

    numbers.sort()

    # For O(1) indexing
    numbers = np.array(numbers)

    for start_idx in range(numbers.size-2):
        pair = find_pair(numbers[start_idx+1:], 2020-numbers[start_idx])
        if pair is not None:
            print(numbers[start_idx], pair[0], pair[1],
                  numbers[start_idx] * pair[0] * pair[1])
            break


