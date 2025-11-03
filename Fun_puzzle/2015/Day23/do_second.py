from command import Command
from register import Register

if __name__ == "__main__":
    reg_a = Register("a",1)
    reg_b = Register("b")
    # read input.txt into a list of lines
    with open(r"AdventOfCode\2015\Day23\input.txt") as f:
        lines = f.read().splitlines()

    current_line = 0
    while current_line < len(lines):
        command = Command(lines[current_line])
        offset = command.execute(reg_a, reg_b)
        current_line += offset

    print(f"Value in register b: {reg_b}")