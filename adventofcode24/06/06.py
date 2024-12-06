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


def parse_grid(grid):
    objs = set()
    x_max, y_max = len(grid[0]), len(grid)
    for y, line in enumerate(grid):
        for x, point in enumerate(line):
            if point == '#':
                objs.add((x, y))
            elif point in '^>v<':  # I thought the starting orientation was random, lol
                x0, y0 = x, y
                d = '^>v<'.index(point)
    return x_max, y_max, objs, x0, y0, d


def walk(x_max, y_max, objs, x, y, d, directions):
    seen = defaultdict(list, {(x, y): [d]})
    while 0 <= x <= x_max and 0 <= y <= y_max:
        dx, dy = directions[d]
        if (x + dx, y + dy) in objs:
            d = (d + 1) % len(directions)  # rotate right 90 degrees
            continue
        x, y = (x + dx, y + dy)
        # Check for loops, if we've seen this square in this direction already we're done
        if d in seen[(x, y)]:
            return
        seen[(x, y)].append(d)
    return seen


def part_one(grid, directions):
    x_max, y_max, objs, x, y, d = parse_grid(grid)
    seen = walk(x_max, y_max, objs, x, y, d, directions)
    return len(set(seen.keys())) - 1


def part_two(grid, directions):
    x_max, y_max, objs, x, y, d = parse_grid(grid)
    seen = walk(x_max, y_max, objs, x, y, d, directions)
    n = 0
    for square in seen.keys():
        objs.add(square)
        if walk(x_max, y_max, objs, x, y, d, directions) is None:
            n += 1
        objs.remove(square)
    return n


grid = read_input_file(day='06', output_type='list')
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # ^ > v <

print(f'Part one: {part_one(grid, directions)}')
print(f'Part two: {part_two(grid, directions)}')
