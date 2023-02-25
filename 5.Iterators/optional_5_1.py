class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x , y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MAX_COORD <= x <= self.MIN_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("Access denied.")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError("Invalid attribute name.")
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        """Runs when you call non-existent item"""
        return f"Class 'Point' has no attribute '{item}'"

    def __delattr__(self, item):
        object.__delattr__(self, item)

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left


point_1 = Point(1, 2)
point_2 = Point(10, 20)
point_1.set_bound(-10)
print(point_1.__dict__)
print(Point.__dict__)