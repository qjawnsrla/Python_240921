# 연산자 오버로딩 : 연산자의 기본기능을 사용자가 정의할 수 있게 한 것

"""
def over_sum(x, y):
    return x + y

print(over_sum(100, 200))
print(over_sum(1.11,  2.22))
print(over_sum("혜인", "하나"))
"""

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

v3 = v1 + v2
print(v3.x, v3.y)

v4 = 12 + 13
print(v4)

#v5 = v1 + 12