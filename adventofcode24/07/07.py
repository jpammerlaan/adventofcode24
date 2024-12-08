from collections import defaultdict
import os


def read_input_file(day, output_type='string'):
    with open(os.path.join('{}/{}.in'.format(day, day)), 'r') as f:
        input_str = f.read()
    if output_type == 'string':
        input_content = input_str[:-1]  # drop \n
    elif output_type == 'list':
        input_content = input_str.split('\n')[:-1]  # drop empty last line
    else:
        raise ValueError('Unknown output_type {}. Expected string or list.'.format(output_type))
    return input_content


def parse_equations(equations):
    parsed_equations = ()
    for eq in equations:
        t, numbers = eq.split(': ')
        numbers = list(map(int, numbers.split(' ')))
        parsed_equations += ((int(t), numbers),)
    return parsed_equations


def mul(a, b):
    return a * b


def add(a, b):
    return a + b


def concat(a, b):
    return int(str(a) + str(b))


def possible(target, current, numbers, functions):
    if not numbers:
        return target if current == target else 0
    return max(possible(target, fn(current, numbers[0]), numbers[1:], functions) for fn in functions)


def process(equations, functions):
    return sum(map(lambda eq: possible(eq[0], eq[1][0], eq[1][1:], functions), equations))


def part_one(equations):
    return process(equations, (mul, add))


def part_two(equations):
    return process(equations, (mul, add, concat))


equations = read_input_file(day='07', output_type='list')
equations = parse_equations(equations)

print(f'Part one: {part_one(equations)}')
print(f'Part two: {part_two(equations)}')
