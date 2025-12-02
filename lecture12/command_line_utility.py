import argparse
import sys
def calculator(arguments):
    a = arguments.a
    b = arguments.b
    operation = arguments.operation

    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Unknown operation"
parser=argparse.ArgumentParser(description='Simple command-line calculator')
parser.add_argument('a', type=float, help='First number')
parser.add_argument('b', type=float, help='Second number')
parser.add_argument('operation', type=str, choices=['add', 'subtract', 'multiply','divide'],help='operation')
args=parser.parse_args()  
res=calculator(args)
print(res)  