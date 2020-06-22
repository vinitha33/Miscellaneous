class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.

        # Getter methods are better practice than just accessing an attribute directly

        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate

        return self.y

    def eq(self):
        if self.x == self.y:
            return True
        else:
            return False

    def repr(self, s):
        res = eval(s)
        print(res)

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

obj = Coordinate(2,2)
print(obj.eq())
obj.repr("10/2")