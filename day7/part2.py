"""
Task:
How many individual bags are required inside your single shiny gold bag?

Time complexity: O(n^2)
"""

from day7.part1 import read_hierarchy


def bag_number(key, hierarchy, number_of_bags={}):
    if key in number_of_bags:
        return number_of_bags[key]

    values = hierarchy[key]

    count = 0
    for value_name, c in values.items():
        nob = bag_number(value_name, hierarchy, number_of_bags)
        number_of_bags[value_name] = nob
        count += c + c * nob

    number_of_bags[key] = count

    return count


if __name__ == "__main__":
    hierarchy, invers_hierarchy = read_hierarchy()
    print(hierarchy)
    number_of_bags = {}
    bag_number = bag_number("shiny gold", hierarchy, number_of_bags)
    print(bag_number, number_of_bags)
