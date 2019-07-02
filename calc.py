import sys

def main():
    while True:
        calculate()

def calculate():
    operation = read_operation()
    x = read_var('x')
    y = read_var('y')
    answer = x + y
    write_answer(answer, x, y)

def read_operation():
    write_operation_prompt()
    return read_input()

def write_operation_prompt():
    sys.stdout.write('What would you like to do?\n')
    sys.stdout.write(' [a]dd\n')
    sys.stdout.write(' [s]ubtract\n')
    sys.stdout.write(' [m]ultiply\n')
    sys.stdout.write(' [d]ivide\n')
    sys.stdout.write(' [q]uit\n')
    sys.stdout.write('> ')
    sys.stdout.flush()

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

def write_answer(answer, x, y):
    sys.stdout.write('{} + {} = {}\n\n'.format(x, y, answer))

if __name__ == '__main__':
    main()
