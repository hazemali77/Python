#!/usr/bin/python
class point:
    def __init__(self, x, y):
        self.move(x, y)
    def move(self, x, y):
        self.x=x
        self.y=y
    def reset(self):
        self.move(0, 0)
    def cal_dist(self, other_point):
        distance =((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return math.sqrt(distance)
