from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

def fmap(n):
    return n * 10

def ffilter(n):
    return n > 10

def freduce(n, m):
    return n + m

l = [30, 90, 1, 4, 6]
for elem in ft_map(fmap, l):
    print(elem)

for elem in ft_filter(ffilter, l):
    print(elem)
    
for elem in ft_reduce(freduce, l):
    print(elem)
