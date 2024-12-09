from collections import defaultdict
from typing import List
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

def disk_map_to_mem(disk_map):
    mem = []
    for i in range(len(disk_map)):
        mem += [None if i % 2 == 1 else i//2] * disk_map[i]
    return mem


def print_mem(mem):
    print(' '.join('.' if m is None else str(m) for m in mem))


def remap_mem(mem):
    first_free, last_free = mem.index(None), len(mem) - 1
    while last_free >= first_free:
        m = mem[last_free]
        if m is not None:
            mem[first_free] = m
            mem[last_free] = None
        last_free -= 1
        first_free = mem.index(None)
    return mem


def remap_files(mem: List):
    first_free, f = mem.index(None), max(m for m in mem if m is not None)
    while f >= 0:
        start = mem.index(f)
        end = start
        while True:
            if end >= len(mem) or mem[end] != f:
                break
            end += 1
        length = end - start
        for i in range(first_free, start):
            # try to move
            if all(m is None for m in mem[i : i + length]): # if all are empty, we can move.
                mem[i : i + length] = [f] * length
                mem[start : start + length] = [None] * length
                break
        first_free = mem.index(None)
        f -= 1
    return mem


def checksum(mem):
    return sum([i * m for i, m in enumerate(mem) if m is not None])


def part_one(disk_map):
    mem = disk_map_to_mem(disk_map)
    mem = remap_mem(mem)
    return checksum(mem)


def part_two(disk_map):
    mem = disk_map_to_mem(disk_map)
    mem = remap_files(mem)
    return checksum(mem)


disk_map = read_input_file(day='09', output_type='string')
disk_map = list(map(int, disk_map))

print(f'Part one: {part_one(disk_map)}')
print(f'Part two: {part_two(disk_map)}')
