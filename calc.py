import operator
import sys

operations = [
    ('add', '+', operator.add),
    ('subtract', '-', operator.sub),
    ('multiply', '*', operator.mul),
    ('divide', '/', operator.div),
]

def main():
    while True:
        try:
            calculate()
        except StopIteration:
            break

def calculate():
    operation = read_operation()
    if operation == 'q':
        raise StopIteration()
    dispatch_operation(operation)

def read_operation():
    write_operation_prompt()
    return input_to_operation(read_input())

def write_operation_prompt():
    sys.stdout.write('What would you like to do?\n')
    for name, _, _ in operations:
        sys.stdout.write(' [{}]{}\n'.format(name[0], name[1:]))
    sys.stdout.write(' [q]uit\n')
    sys.stdout.write('> ')
    sys.stdout.flush()

def input_to_operation(s):
    op = s.strip()
    valid = [name[0] for name, _, _ in operations] + ['q']
    if op not in valid:
        raise ValueError('invalid operation - must be in {}'.format(valid))
    return op

def dispatch_operation(op):
    for name, symbol, f in operations:
        if name[0] == op:
            apply_operation(f, symbol)
            break
    else:
        assert False, op

def apply_operation(f, symbol):
    x = read_var('x')
    y = read_var('y')
    answer = f(x, y)
    write_answer(answer, x, y, symbol)

def read_var(var_name):
    write_var_prompt(var_name)
    user_input = read_input()
    return input_to_number(user_input)

def read_input():
    return sys.stdin.readline()

def input_to_number(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def write_var_prompt(var_name):
    sys.stdout.write('Enter a value for {}:\n'.format(var_name))
    sys.stdout.write('> ')
    sys.stdout.flush()

def write_answer(answer, x, y, symbol):
    fmt = '\n  {} {} {} = {}\n\n'
    sys.stdout.write(fmt.format(x, symbol, y, answer))

if __name__ == '__main__':
    main()
