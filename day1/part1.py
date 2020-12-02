from utils.io import read_number
import numpy as np

"""
Task:
Find the two entries that sum to 2020; what do you get if you multiply them together?

Time comlexity: O(n*log(n))
"""


def find_pair(numbers, sum):
    """
    :param numbers: Have to be a sorted numpy array
    """

    start_idx = 0
    end_idx = numbers.size - 1

    while start_idx < end_idx:
        s = numbers[start_idx] + numbers[end_idx]

        if s == sum:
            return numbers[start_idx], numbers[end_idx]
        elif s < sum:
            start_idx += 1
        else:
            end_idx -= 1

    return None


if __name__ == "__main__":
    numbers = read_number("day1/input.txt")

    numbers.sort()

    # For O(1) indexing
    numbers = np.array(numbers)

    num1, num2 = find_pair(numbers, 2020)

    print(num1, num2, num1 * num2)

