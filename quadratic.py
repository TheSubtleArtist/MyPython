import math
import sys

class QuadraticError(ValueError):
    """Error raised when incorrect quadratic arguments are provided."""

def quadratic(a, b, c):
    """Solve quadratic equation ax² + bx + c = 0."""
    if a == 0:
        raise QuadraticError("Variable 'a' cannot be 0")
    x1 = -1 * b / (2 * a)
    try:
        x2 = math.sqrt(b ** 2 - 4 * a * c) / (2 * a)
    except ValueError as e:
        raise QuadraticError("Cannot take square root of negative number") from e
    return (x1 + x2), (x1 - x2)

def main(args):
    try:
        a, b, c = (float(x) for x in args)
    except ValueError:
        raise QuadraticError("Three numeric arguments required")
    solution1, solution2 = quadratic(a, b, c)
    print("x = {} or {}".format(solution1, solution2))

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except QuadraticError as error:
        print(error)
        exit(1)