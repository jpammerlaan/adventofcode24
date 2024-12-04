# from adventofcode24.utils import io
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


field = read_input_file(day='04', output_type='list')


def part_one(field):
    # good luck reading all this, even I don't understand what I'm doing!
    rows = [row for row in field]
    rows += [row[::-1] for row in rows]
    rows += [row for row in zip(*field)]
    rows += [row[::-1] for row in zip(*field)]

    # get all diagonal lines within the map
    # thank god the grids are square
    n = len(field)
    diag = [[field[j][j] for j in range(n)]] + [[field[n-j-1][j] for j in range(n)]]
    for i in range(1, n):
        diag.append([field[j][j+i] for j in range(n-i)])
        diag.append([field[j+i][j] for j in range(n-i)])
        diag.append([field[n-j-1][j+i] for j in range(n-i)])
        diag.append([field[n-i-j-1][j] for j in range(n-i)])
    rows += diag + [row[::-1] for row in diag]

    return sum(map(lambda row: ''.join(row).count('XMAS'), rows))

def part_two(field):
    n = len(field)
    xmas = 0
    for i in range(1, n-1):
        for j in range(1, n-1):
            if field[i][j] == 'A':
                neighbors = field[i-1][j-1] + field[i+1][j+1], field[i-1][j+1] + field[i+1][j-1]
                if neighbors in [('SM', 'SM'), ('MS', 'SM'), ('SM', 'MS'), ('MS', 'MS')]:
                    xmas += 1

    return xmas


print(f'Part one: {part_one(field)}')
print(f'Part two: {part_two(field)}')
