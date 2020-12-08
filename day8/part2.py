"""
Task:
Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
What is the value of the accumulator after the program terminates?

Time complexity: O(n^2)
Note: I guess this can be improved to a linear solution
"""

from day8.part1 import read_input, run_program


if __name__ == "__main__":
    commands = read_input()

    for i in range(len(commands)):
        command = commands[i][0]
        if command in ("nop", "jmp"):
            commands[i][0] = "nop" if command == "jmp" else "jmp"
            accumulator, command_counter = run_program(commands)
            if command_counter >= len(commands):
                print(accumulator)
                break
            commands[i][0] = command




