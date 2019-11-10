from vector import Vector

v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector(3)
v3 = Vector((10, 15))
v4 = Vector(5)
v5 = Vector([5.0])
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(repr(v5))
print("\nadd")
v6 = v1 + v2
v6 = v3 + v4
v6 = v5 + 4
v6 = 7 + v5
v6 = v2 + 5
v6 = 12 + v1
print("\nsub")
v6 = v1 - v2
v6 = v3 - v4
v6 = v5 - 4
v6 = 7 - v5
v6 = v2 - 5
v6 = 12 - v1
print("\ndiv")
v6 = v1 / v2
v6 = v3 / v4
v6 = v5 / 4
v6 = 7 / v5
v6 = v2 / 5
v6 = 12 / v1
print("\nmul")
print(str(v1 * v2))
print(str(v3 * v4))
v6 = v5 * 4
v6 = 7 * v5
v6 = v2 * 5
v6 = 12 * v1
#print(v2)
