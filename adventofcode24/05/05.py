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


instructions = read_input_file(day='05', output_type='string')
rules, updates = instructions.split('\n\n')


def parse_rules(rules):
    rules_dict = defaultdict(list)
    for rule in rules.split('\n'):
        pre, post = rule.split('|')
        rules_dict[int(pre)].append(int(post))
    return rules_dict


def parse_updates(updates):
    return [[int(page) for page in update.split(',')] for update in updates.split('\n')]


def invalid_position(update, rules):
    for i in range(len(update)):
        if any(s in rules[update[i]] for s in update[:i]):
            return i
    return -1


def part_one(rules, updates):
    return sum(update[int(len(update) / 2)] for update in updates if invalid_position(update, rules) < 0)


def part_two(rules, updates):
    invalid_updates = [update for update in updates if invalid_position(update, rules) >= 0]
    total = 0
    for invalid_update in invalid_updates:
        update, valid = invalid_update.copy(), False
        while not valid:
            i = invalid_position(update, rules)
            for j in range(i, len(update)):
                a, b = update[j], update[j - 1]
                update[j], update[j - 1] = b, a
                if invalid_position(update, rules) < 0:
                    valid = True
                    break
        total += update[int(len(update) / 2)]
    return total


rules = parse_rules(rules)
print(rules)
updates = parse_updates(updates)
print(f'Part one: {part_one(rules, updates)}')
print(f'Part two: {part_two(rules, updates)}')
