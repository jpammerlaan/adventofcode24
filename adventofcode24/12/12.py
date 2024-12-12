import os
from collections import defaultdict


def read_input_file(day, output_type='string'):
    with open(os.path.join('{}/{}.in'.format(day, day)), 'r') as f:
        input_str = f.read()
    if output_type == 'string':
        return input_str[:-1]  # drop \n
    if output_type == 'list':
        return input_str.split('\n')[:-1]  # drop empty last line
    raise ValueError('Unknown output_type {}. Expected string or list.'.format(output_type))


def calc(region, discount=False):
    a = len(region)
    p = 0
    neighbors = [1, -1, 1j, -1j]
    diag = [1+1j, 1-1j, -1+1j, -1-1j]
    if discount:  # count corners
        for r in region:
            diff = [r + n for n in neighbors if r + n not in region]

            # outside corners
            if len(diff) == 4:
                p += 4
            elif len(diff) == 3:
                p += 2
            elif len(diff) == 2:
                n1, n2 = diff
                # only check for outside corners here, inside corners handled separately below
                if n1.real != n2.real and n1.imag != n2.imag:
                    p += 1

            # inside corners
            # check if orthogonal neighbors are in region, but diagonal neighbors are not.
            for n in diag:
                orthog = [r + n.real, r + n.imag * 1j]
                if all(o in region for o in orthog) and r + n not in region:
                    p += 1
    else: # count edges
        for r in region:
            p += sum(r + n not in region for n in neighbors)
    
    return a * p


def find_regions(inp):
    # start with regions of size 1
    plant_regions = defaultdict(list)
    for y, row in enumerate(inp):
        for x in range(len(row)):
            plant_regions[row[x]].append([x + y*1j])

    # merge regions iteratively
    merged = True
    neighbors = [1, -1, 1j, -1j]
    while merged:
        merged = False
        for plant, regions in plant_regions.items():
            i = 0
            while i < len(regions):
                j = i + 1
                while j < len(regions):
                    # if any squares are neighbors, merge the regions
                    if any(r + n in regions[j] for n in neighbors for r in regions[i]):
                        regions[i] += regions[j]
                        del regions[j]
                        merged = True
                    j += 1
                i += 1
            plant_regions[plant] = regions

    return plant_regions


def part_one(regions):
    return sum(sum(calc(r) for r in plant_regions) for plant_regions in regions.values())


def part_two(grid):
    return sum(sum(calc(r, discount=True) for r in plant_regions) for plant_regions in regions.values())


inp = read_input_file(day='12', output_type='list')
regions = find_regions(inp)

print(f'Part one: {part_one(regions)}')
print(f'Part two: {part_two(regions)}')
