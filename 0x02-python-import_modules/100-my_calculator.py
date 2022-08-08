#!/usr/bin/python3
import calculator_1


def calculator(argv):
    n = len(argv) - 1
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    finalcomp = 0
    if n < 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        break
        return False
    else:
        if operator == "+":
            finalcomp = calculator_1.add(a, b)
        elif operator == "-":
            finalcomp = calculator_1.sub(a, b)
        elif operator == "*":
            finalcomp = calculator_1.mul(a, b)
        elif operator == "/":
            finalcomp = calculator_1.div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            return 1
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, finalcomp))
    return False
if __name__ == "__main__":
    """import sys"""
    """calculator(sys.argv)"""
    return False