"""
Task:
Immediately before any instruction is executed a second time, what value is in the accumulator?

Time complexity: O(n)
"""


def read_input():
    with open("day8/input.txt", 'r') as f:
        commands = []
        for line in f.readlines():
            line = line.split(' ')
            commands.append([line[0], int(line[1])])

    return commands


def run_program(commands):
    accumulator = 0
    command_counter = 0
    visited_lines = set()

    while command_counter not in visited_lines and command_counter < len(commands):
        visited_lines.add(command_counter)
        command, argument = commands[command_counter]

        if command == "nop":
            command_counter += 1
        elif command == "acc":
            accumulator += argument
            command_counter += 1
        elif command == "jmp":
            command_counter += argument

    return accumulator, command_counter


if __name__ == "__main__":
    commands = read_input()
    accumulator, command_counter = run_program(commands)
    print(accumulator)




