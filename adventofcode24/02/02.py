import os
from adventofcode24.utils import io
from itertools import combinations


reports = io.read_input_file(day='02', output_type='list')
reports = [list(map(int, report.split(' '))) for report in reports]


def is_valid(r):
    level_diff = [r[i-1] - r[i] for i in range(1, len(r))]
    signs = [x/abs(x) if x != 0 else 0 for x in level_diff]
    return all(1 <= x <= 3 for x in map(abs, level_diff)) and all(sign == signs[0] for sign in signs)


def part_one(reports):
    print(sum(map(is_valid, reports)))


def part_two(reports):
    problem_reports = [r for r in reports if not is_valid(r)]
    print(len(reports) - len(problem_reports) + sum(any(is_valid(r) for r in list(combinations(r, len(r) - 1))) for r in problem_reports))


part_one(reports)
part_two(reports)
