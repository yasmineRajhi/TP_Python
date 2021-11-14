import shape
import drawing

c = shape.Circle(1, 2, 2.5, "blue")
t = shape.Triangle(0, 0, 2, 2, 5, 7, "green")
c.move(1, -1)
t.move(2, 2)
d = drawing.Drawing()
d.add_shape(c)
d.add_shape(t)
d.display()