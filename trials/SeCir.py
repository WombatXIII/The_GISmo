import math
from math import cos
from math import sqrt
from math import radians


class shape ():
    pass


SeCir = shape()


def InterAngle():
    IntAng = input('Intersection angle? (degrees) ->')
    SeCir.IA = int(IntAng)


def Triangle():
    triag = input('How many Triangles? ->')
    SeCir.Tri = int(triag)
    SeCir.AngA = SeCir.IA/SeCir.Tri
    SeCir.AngB = (180 - SeCir.AngA)/2
    SeCir.AngTwoB = 180 - SeCir.AngA


def HLen():
    radius = input('What size Radius? ->')
    SeCir.Rad = float(radius)
    RA = radians(SeCir.AngA)
    SqrLen = ((SeCir.Rad**2)*2) - (2 * SeCir.Rad * SeCir.Rad * cos(RA))
    Len = sqrt(SqrLen)
    SeCir.Len = Len


def Details():
    print ('initial Angle, ', SeCir.AngB)
    print ('Following Angles, ', SeCir.AngTwoB)
    print ('with a length of ', SeCir.Len)
    print (5/2)

def Again():
    print ('Again?')
    YN = input()
    if YN == 'y' or YN == 'Y':
        hump()
    elif YN != 'y' or YN != 'Y':
        quit()
    else:
        quit()

def hump():
    InterAngle()
    Triangle()
    HLen()
    Details()
    Again()

hump()
