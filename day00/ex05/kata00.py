import sys

t = (19, 42, 21)
if (len(t) > 1):
    sys.stdout.write("The " + str(len(t)) + " numbers are: ")
    sys.stdout.write(str(t[0]))
    for n in t[1:]:
        sys.stdout.write(", " + str(n))
    sys.stdout.write("\n")
