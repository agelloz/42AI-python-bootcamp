import sys
from time import sleep


def ft_progress(it, prefix="", size=40, file=sys.stdout):

    def show(j):
        count = len(it)
        x = int(size * j / count)
        file.write("%s[%s%s] %i/%i\r" %
                (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()

    show(0)
    for i, item in enumerate(it):
        yield item
    show(i + 1)
    file.write('\n')
    file.flush()
