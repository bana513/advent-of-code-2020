

"""
Task:
How many bag colors can eventually contain at least one shiny gold bag?

Time complexity: O(n)
"""


def clean_key(str):
    return " ".join(str.strip().split(' ')[:2])


def clean_value(str):
    str = str.strip()
    value = int(str.split(' ')[0])
    name = " ".join(str.strip().split(' ')[1:3])
    return name, value


def read_hierarchy():
    hierarchy = {}
    invers_hierarchy = {}

    with open("day7/input.txt", 'r') as f:
        for line in f.readlines():
            key, values_str = line.split("contain")
            key = clean_key(key)

            values = {}
            for value_str in values_str.split(','):
                if "no other" not in value_str:
                    name, value = clean_value(value_str)
                    values[name] = value

            hierarchy[key] = values

            for name, _ in values.items():
                if name in invers_hierarchy:
                    invers_hierarchy[name].append(key)
                else:
                    invers_hierarchy[name] = [key]

    return hierarchy, invers_hierarchy


def find_all_parents(key, invers_hierarchy):
    parents = set()
    to_visit = [key]

    while len(to_visit) > 0:
        next_node = to_visit[0]
        del to_visit[0]

        if next_node in invers_hierarchy:
            for nn in invers_hierarchy[next_node]:
                if nn not in parents:
                    parents.add(nn)
                    to_visit.append(nn)
    return parents


if __name__ == "__main__":
    hierarchy, invers_hierarchy = read_hierarchy()
    parents = find_all_parents("shiny gold", invers_hierarchy)
    print(len(parents), parents)





