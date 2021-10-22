
"""
f(x) = y
f(x) = x^2 + 2x + 1
cứ mỗi giá trị truyền vào của x -> f(x)

f(x, y) = x^2 + 2xy + y^2
cứ mỗi x, y truyền vào -> (return) f(x, y)

y = 1
"""


def tinh(x, y):
    return x * x + 2 * x * y + y * y


def test():
    return 1


ten = 'con cho'


def change_name(name):
    name = 'con chim'
    return name


ten = change_name(name = ten)
print(ten)

