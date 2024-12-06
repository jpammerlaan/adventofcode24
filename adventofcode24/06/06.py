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


grid = read_input_file(day='06', output_type='list')
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # ^ > v <

def parse_grid(grid):
    objs = {}
    x_max, y_max = len(grid[0]), len(grid)
    for y, line in enumerate(grid):
        for x, point in enumerate(line):
            if point == '#':
                objs[(x, y)] = 1
            elif point in '^>v<':  # I thought the starting orientation was random, lol
                pos = (x, y)
                d = '^>v<'.index(point)
    return x_max, y_max, objs, pos, d


def walk(x_max, y_max, objs, pos, d, directions):
    seen = defaultdict(list, {pos: [d]})
    loop = False
    while 0 <= pos[0] <= x_max and 0 <= pos[1] <= y_max:
        new_pos = (pos[0] + directions[d][0], pos[1] + directions[d][1])
        if new_pos in objs.keys():
            d = (d + 1) % len(directions)
        else:
            pos = new_pos
        if d in seen[pos]:
            loop = True
            break
        seen[pos].append(d)
    return seen, loop


def part_one(grid, directions):
    x_max, y_max, objs, pos, d = parse_grid(grid)
    seen, _ = walk(x_max, y_max, objs, pos, d, directions)
    return len(set(seen.keys())) - 1


def part_two(grid, directions):
    x_max, y_max, objs, pos, d = parse_grid(grid)
    seen, _ = walk(x_max, y_max, objs, pos, d, directions)
    n = 0
    for square in seen.keys():
        objs[square] = 1
        _, loop = walk(x_max, y_max, objs, pos, d, directions)
        n += loop
        del objs[square]
    return n


print(f'Part one: {part_one(grid, directions)}')
print(f'Part two: {part_two(grid, directions)}')
