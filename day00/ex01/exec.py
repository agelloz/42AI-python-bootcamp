import sys

j = len(sys.argv) - 1
while (j > 0):
    if (j >= 1):
        i = len(sys.argv[j]) - 1
        while (i >= 0):
            sys.stdout.write(sys.argv[j][i].swapcase())
            i = i - 1
        if (j > 1):
            sys.stdout.write(' ')
    j = j - 1
if (len(sys.argv) > 1):
    sys.stdout.write('\n')
