class Point:
    def __init__(self, x_coor, y_coor):
        self.x = x_coor
        self.y = y_coor

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)
