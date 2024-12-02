import os
from utils import io
from collections import Counter


lines = read_input_file(day='01', output_type='list')
l1, l2 = zip(*[line.split('  ') for line in lines])
l1, l2 = list(sorted(map(int, l1))), list(sorted(map(int, l2)))


def part_one(l1, l2):
    print(sum(abs(l1[i] - l2[i]) for i in range(len(l1))))


def part_two(l1, l2):
    def similarity(x, c):
        return x * c[x]

    cnt = Counter(l2)
    print(sum(similarity(x, cnt) for x in l1))


part_one(l1, l2)
part_two(l1, l2)