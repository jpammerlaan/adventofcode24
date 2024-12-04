from adventofcode24.utils import io
import re


instructions = io.read_input_file(day='03', output_type='string')


def process_instructions(i):
    mul_pattern = r'mul\((-?\d+),(-?\d+)\)'
    return sum([int(x) * int(y) for x, y in re.findall(mul_pattern, i)])


def part_one(instructions):
    print(process_instructions(instructions))


def part_two(instructions):
    i = ""
    # Parse the instructions; read instructions until they tell you don't(), then start again when seeing do()
    while instructions:
        try:
            dont_ind = instructions.index("don't()") + len("don't()")
            i += instructions[:dont_ind]
        except ValueError:
            i += instructions
            break

        do_ind = instructions.index("do()", dont_ind) + len("do()")
        instructions = instructions[do_ind:]

    print(process_instructions(i))


print(f'Part one: {part_one(instructions)}')
print(f'Part two: {part_two(instructions)}')
