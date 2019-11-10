import sys


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


if (len(sys.argv) == 1):
    sys.exit()
if (len(sys.argv) > 2 or check_int(sys.argv[1]) is False):
    print("ERROR")
    sys.exit()
if (int(sys.argv[1]) == 0):
    print("I'm Zero.")
elif (int(sys.argv[1]) % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
