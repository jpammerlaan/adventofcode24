import os


def read_input_file(day, output_type='string'):
    with open(os.path.join('{}/{}.in'.format(day, day)), 'r') as f:
        input_str = f.read()
    if output_type == 'string':
        return input_str[:-1]  # drop \n
    if output_type == 'list':
        return input_str.split('\n')[:-1]  # drop empty last line
    raise ValueError('Unknown output_type {}. Expected string or list.'.format(output_type))


def print_stones(stones):
    print(' '.join(stones))


def blink(stones, N):
    todo = stones.copy()
    done = []
    rules = {0: [1]}
    for _ in range(N):
        while todo:
            s = todo.pop()
            if s not in rules:
                c = str(s)
                if len(c) % 2 == 0:
                    s1, s2 = c[:len(c) // 2], c[len(c) // 2:]
                    rules[s] = [int(s1), int(s2)]
                else:
                    rules[s] = [s * 2024]
            done += rules[s]
        todo = done
        done = []
    return todo


def compute(s):
    if s == 0:
        return [1]
    c = str(s)
    if len(c) % 2 == 0:
        i = len(c) // 2
        return [int(c[:i]), int(c[i:])]
    else:
        return [s * 2024]


# use recursion with a heap (har har) of seen states
# state format is (stone_id, number_of_blinks): number_of_stones
def recurse(states, s, N):
    if (s, N) in states:
        return states[(s, N)]
    elif N == 1:
        states[(s, N)] = len(compute(s))
    else: 
        states[(s, N)] = sum([recurse(states, s2, N-1) for s2 in compute(s)])

    return states[(s, N)]


def part_one(stones):
    stones = blink(stones.copy(), 25)
    return len(stones)


def part_two(stones):
    states = {}
    return sum([recurse(states, s, 75) for s in stones])


stones = read_input_file(day='11', output_type='string')
stones = [int(s) for s in stones.split(' ')]

print(f'Part one: {part_one(stones)}')
print(f'Part two: {part_two(stones)}')
