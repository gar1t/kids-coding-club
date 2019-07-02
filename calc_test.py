""" calc.py tests

>>> import calc

Write prompt for variable:

>>> calc.write_var_prompt('x')
x:

Write answer:

>>> calc.write_answer(3, 2, 1)
2 + 1 = 3

Convert input to number:

>>> calc.input_to_number('1')
1

>>> calc.input_to_number('1.0')
1.0

>>> calc.input_to_number('1.1e-2')
0.011

>>> calc.input_to_number('a')
Traceback (most recent call last):
ValueError: could not convert string to float: a

"""

import doctest
import sys

result = doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
if result.failed:
    print("%i test(s) failed" % result.failed)
    sys.exit(1)
else:
    print("%i test(s) passed" % result.attempted)
