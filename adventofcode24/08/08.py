from collections import defaultdict
from itertools import combinations
import os


def read_input_file(day, output_type='string'):
    with open(os.path.join('{}/{}.in'.format(day, day)), 'r') as f:
        input_str = f.read()
    if output_type == 'string':
        return input_str[:-1]  # drop \n
    if output_type == 'list':
        return input_str.split('\n')[:-1]  # drop empty last line
    raise ValueError('Unknown output_type {}. Expected string or list.'.format(output_type))


def find_antinodes(grid, antennas, bounds, resonations):
    antinodes, lb, ub = [], *bounds
    for _, coords in antennas.items():
        for c1, c2 in combinations(coords, 2):
            for n in resonations:
                antinodes += [n * c1 - (n-1) * c2, n * c2 - (n-1) * c1]

    return len(set([a for a in antinodes if (lb.real <= a.real < ub.real) and (lb.imag <= a.imag < ub.imag)]))


def part_one(grid, antennas, bounds):
    return find_antinodes(grid, antennas, bounds, range(2, 3))


def part_two(grid, antennas, bounds):
    return find_antinodes(grid, antennas, bounds, range(1, len(grid)))


def parse_grid(grid):
    antennas = defaultdict(list)
    x_max, y_max = len(grid[0]), len(grid)
    for y in range(y_max):
        for x in range(x_max):
            antennas[grid[y][x]].append(x + y * 1j)
    del antennas["."]  # skip all empty squares
    return antennas, (0 + 0j, x_max + y_max * 1j)


grid = read_input_file(day='08', output_type='list')
antennas, bounds = parse_grid(grid)

print(f'Part one: {part_one(grid, antennas, bounds)}')
print(f'Part two: {part_two(grid, antennas, bounds)}')
