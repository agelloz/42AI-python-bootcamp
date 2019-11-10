import sys


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


error = False
if (len(sys.argv) == 1):
    error = True
elif (len(sys.argv) > 3):
    print("InputError: too many arguments")
    error = True
elif (check_int(sys.argv[1]) is False or check_int(sys.argv[2]) is False):
    print("InputError: only numbers")
    error = True
if (error is True):
    print("Usage: python operations.py")
    print("Example:")
    print("   python operations.py 10 3")
    exit()

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
try:
    print("Sum:        " + str(n1 + n2))
    print("Difference: " + str(n1 - n2))
    print("Product:    " + str(n1 * n2))
    print("Quotient:   " + str(n1 / n2))
    print("Remainder:  " + str(n1 % n2))
except ZeroDivisionError:
    print("Quotient:   ERROR (div by zero)")
    print("Remainder:  ERROR (modulo by zero)")
