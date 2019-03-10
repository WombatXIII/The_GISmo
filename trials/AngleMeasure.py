from math import tan
from math import radians
from math import degrees


class Angle ():
    pass


A = Angle()


def radi():
    A.X = input('1:')
    A.Y = input('2:')
    A.FX = float(A.X)
    A.FY = float(A.Y)
    A.RadX = radians(A.FX)
    A.RadY = radians(A.FY)
    IntersectA(A.RadY, A.RadX)


def IntersectA(x, y):
    theta = ((x-y)/(1+(x*y)))
    Ttheta = tan(theta)
    print(Ttheta)
    A.DegT = degrees(Ttheta)
    print(A.DegT)


radi()
