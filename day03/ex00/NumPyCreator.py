import numpy as np


class NumPyCreator:
    
    @staticmethod
    def from_list(lst, dtype=None):
        return np.array(lst, dtype=dtype)

    @staticmethod
    def from_tuple(tpl, dtype=None):
        return np.array(tpl, dtype=dtype)

    @staticmethod
    def from_iterable(itr, dtype=None):
        return (np.array([x for x in itr], dtype=dtype))

    @staticmethod
    def from_shape(shape, value=0, dtype=None):
        return np.full(shape, value, dtype=dtype)

    @staticmethod
    def random(shape):
        return np.random.random(size=shape)

    @staticmethod
    def identity(n, dtype=None):
        return np.identity(n, dtype=dtype)
    

if __name__ == '__main__':
    npc = NumPyCreator()
    print(npc.from_list([[1,2,3],[6,3,4]]))
    print(npc.from_tuple(("a", "b", "c")))
    print(npc.from_iterable(range(5)))
    shape=(3,5)
    print(npc.from_shape(shape))
    print(npc.random(shape))
    print(npc.identity(4))
