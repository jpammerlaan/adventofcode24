import os


def read_input_file(day, output_type='string'):
    with open(os.path.join('{}/{}.in'.format(day, day)), 'r') as f:
        input_str = f.read()
    if output_type == 'string':
        return input_str[:-1]  # drop \n
    if output_type == 'list':
        return input_str.split('\n')[:-1]  # drop empty last line
    raise ValueError('Unknown output_type {}. Expected string or list.'.format(output_type))


def find_neighbors(grid, node, seen, h, w):
    x, y = node
    neighbors = [(max(x - 1, 0), y), (min(x + 1, w - 1), y), (x, max(y - 1, 0)), (x, min(y + 1, h - 1))]
    return [(xn, yn) for xn, yn in neighbors if (xn, yn) not in seen and grid[yn][xn] - grid[y][x] == 1]


def bfs(grid, start, h, w):
    shortest_dist = {(x, y): 1e5 for y in range(h) for x in range(w)}
    paths = {(x, y): [] for x, y in shortest_dist.keys()}
    shortest_dist[start] = 0
    seen = set()

    q = [(start, [])]
    while len(q):
        current, path = q.pop(0)
        if current in seen and path in paths[current]:
            continue

        neighbors = find_neighbors(grid, current, seen, h, w)
        for n in neighbors:
            dist = shortest_dist[current] + 1
            shortest_dist[n] = min(shortest_dist[n], dist)
            q.append((n, path + [n]))

        seen.add(current)
        paths[current].append(path)

    return shortest_dist, paths


def part_one(grid):
    h, w = len(grid), len(grid[0])
    starts = [(x, y) for y in range(h) for x in range(w) if grid[y][x] == 0]
    ends = [(x, y) for y in range(h) for x in range(w) if grid[y][x] == 9]
    total = 0
    for start in starts:
        dists, _ = bfs(grid, start, h, w)
        total += sum(dists[e] < 1e5 for e in ends)
    return total


def part_two(grid):
    h, w = len(grid), len(grid[0])
    starts = [(x, y) for y in range(h) for x in range(w) if grid[y][x] == 0]
    ends = [(x, y) for y in range(h) for x in range(w) if grid[y][x] == 9]
    total = 0
    for start in starts:
        _, paths = bfs(grid, start, h, w)
        total += sum(len(paths[e]) for e in ends)
    return total


grid = read_input_file(day='10', output_type='list')
grid = [[int(i) for i in row] for row in grid]

print(f'Part one: {part_one(grid)}')
print(f'Part two: {part_two(grid)}')
