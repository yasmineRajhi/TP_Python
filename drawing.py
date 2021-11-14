class Drawing:
    def __init__(self):
        self.shapes = []

    def add_shape(self, s):
        self.shapes.append(s)

    def display(self):
        for s in self.shapes:
            print(s)