from position import Position


class Shape:
    def __init__(self, c):
        self.color = c

    def __str__(self):
        return f"Color: {self.color}"


class Circle(Shape):
    def __init__(self, x, y, r, c):
        super().__init__(c)
        self.position = Position(x, y)
        self.radius = r

    def __str__(self):
        return f"Circle[Center: {self.position.__str__()}, Radius: {self.radius}," \
               f" {super().__str__()}]"

    def move(self, dx, dy):
        self.position.move(dx, dy)


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3, c):
        super().__init__(c)
        self.p1 = Position(x1, y1)
        self.p2 = Position(x2, y2)
        self.p3 = Position(x3, y3)

    def __str__(self):
        return f"Triangle[{self.p1.__str__()}, {self.p2.__str__()}, {self.p3.__str__()}, {super().__str__()}]"

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)
        self.p3.move(dx, dy)