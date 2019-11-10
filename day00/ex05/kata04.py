import sys

t = (0, 4, 132.42222, 10000, 12345.67)

sys.stdout.write("day_" + format(t[0], "02d") + ", ex_" + format(t[1], "02d"))
sys.stdout.write(" : " + format(t[2], ".2f") + ", " + format(t[3], ".2e"))
sys.stdout.write(", " + format(t[4], ".2e") + "\n")
