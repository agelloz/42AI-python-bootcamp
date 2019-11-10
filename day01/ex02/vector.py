import typing

class Vector:
    def __init__(self, arg):
        self.values = []
        self.length = 0

        if isinstance(arg, list):
            for val in arg:
                if isinstance(val, float) is False:
                    print("Error in initializing vector")
                    exit()
            self.values = arg
            self.length = len(arg)
        elif isinstance(arg, tuple):
            if len(arg) is not 2:
                print("Error in initializing vector")
                exit()
            for val in arg:
                if (isinstance(val, int) is False or arg[0] >= arg[1]):
                    print("Error in initializing vector")
                    exit()
            for i in range(arg[0], arg[1]):
                self.values.append(float(i))
            self.length = arg[1] - arg[0]
        elif isinstance(arg, int):
            if arg < 1:
                print("Error in initializing vector")
                exit()
            i = 0.0
            for n in range(arg):
                self.values.append(i)
                i += 1.0
            self.length = arg

    def __str__(self):
        return self.__class__.__name__ + str(self.values)

    def __repr__(self):
        return self.__class__.__name__ + str(self.values)

    def __add__(self, other):
        if isinstance(other, int) and len(self.values) is 1:
            res = [self.values[0] + other]
            return Vector(res)
        if isinstance(other, Vector) is False or len(self.values) != len(other.values):
            if isinstance(other, Vector):
                print("Error: impossible to add thoses objects: " + str(self.values) + " and " + str(other.values))
            else:
                print("Error: impossible to add thoses objects: " + str(self.values) + " and " + str(other))
            return
        res = []
        for i in range(len(self.values)):
            res.append(self.values[i] + other.values[i])
        return Vector(res)

    def __radd__(self, other):
        self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int) and len(self.values) is 1:
            res = [self.values[0] - other]
            return Vector(res)
        if isinstance(other, Vector) is False or len(self.values) != len(other.values):
            if isinstance(other, Vector):
                print("Error: impossible to sub thoses objects: " + str(self.values) + " and " + str(other.values))
            else:
                print("Error: impossible to sub thoses objects: " + str(self.values) + " and " + str(other))
            return
        res = []
        for i in range(len(self.values)):
            res.append(self.values[i] - other.values[i])
        return Vector(res)

    def __rsub__(self, other):
        self.__sub__(other)

    def __truediv__(self, other):
        if isinstance(other, Vector) is True:
            print("Error: impossible to div thoses objects: " + str(self.values) + " and " + str(other.values))
            return
        res = []
        for i in self.values:
            res.append(i / other)
        return Vector(res)

    def __rtruediv__(self, other):
        self.__truediv__(other)

    def __mul__(self, other):
        if isinstance(other, int):
            res = []
            for i in self.values:
                res.append(i * other)
            return Vector(res)
        if isinstance(other, Vector) is False or len(self.values) != len(other.values):
            if isinstance(other, Vector):
                print("Error: impossible to mul thoses objects: " + str(self.values) + " and " + str(other.values))
            else:
                print("Error: impossible to mul thoses objects: " + str(self.values) + " and " + str(other))
            return
        res = 0
        for i in range(len(self.values)):
            res += self.values[i] * other.values[i]
        return res

    def __rmul__(self, other):
        self.__mul__(other)
