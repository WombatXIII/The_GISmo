from math import cos
from math import sqrt
from math import radians

from Calculator.Info.Parameter import Parameter


class SeCir:

    def __init__(self):
        self.Title = "Semi Circle Segments"
        self.IntAngle = Parameter("Intersection Angle (deg)")
        self.Triangles = Parameter("Amount of triangles")
        self.Radius = Parameter("Semi Circle radius (m)")
        self.ConvertedToDim = Parameter("Converted to dim (m)")
