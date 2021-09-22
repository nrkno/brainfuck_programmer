import sys


def read(filename):
    with open(filename) as f:
        lines = f.read()
    return lines


def parse(inputString):
    return ''.join(filter(lambda x: x in "<>+-.,[]", inputString))


def interpret(raw_program):
    program, jumps = build_jumps(raw_program)

    program_pointer = 0
    memory_pointer = 0
    memory = [0]
    printed = ""

    while program_pointer < len(program):
        instruction = program[program_pointer]

        if instruction == '>':
            memory_pointer += 1
            if memory_pointer == len(memory):
                memory.append(0)
        elif instruction == '<':
            memory_pointer -= 1
        elif instruction == '+':
            memory[memory_pointer] += 1
        elif instruction == '-':
            memory[memory_pointer] -= 1
        elif instruction == '.':
            printed += chr(memory[memory_pointer])
        elif instruction == ',':
            # memory[memory_pointer] = ord(sys.stdin.read(1))
            print("unsupported operation ','")
            exit(1)
        elif instruction == '[':
            if memory[memory_pointer] == 0:
                program_pointer = jumps[program_pointer]
        elif instruction == ']':
            if memory[memory_pointer] != 0:
                program_pointer = jumps[program_pointer]
        else:
            print("invalid character:", instruction)
            exit(1)

        program_pointer += 1

    return printed, memory, memory_pointer


def build_jumps(program):
    jump_map = {}
    bracket_stack = []
    for pos, instruction in enumerate(program):
        if instruction == '[':
            bracket_stack.append(pos)
        elif instruction == ']':
            partner = bracket_stack.pop()
            jump_map[partner] = pos
            jump_map[pos] = partner

    # add missing closing brackets
    while bracket_stack:
        open_bracket_pos = bracket_stack.pop()
        appended_closing_bracket_pos = len(program)
        jump_map[open_bracket_pos] = appended_closing_bracket_pos
        jump_map[appended_closing_bracket_pos] = open_bracket_pos
        program += "]"

    return program, jump_map


def execute(program):
    p, memory, memory_pointer = interpret(program)
    print(p)


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        program = parse(read(filename))
        execute(program)


if __name__ == "__main__":
    main()
