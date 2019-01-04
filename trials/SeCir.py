<<<<<<< HEAD
=======
import math
>>>>>>> master
from math import cos
from math import sqrt
from math import radians

<<<<<<< HEAD

class shape ():

    pass


SeCir = shape()


def InterAngle():
    IntAng = input('Intersection angle? (degrees) ->')
    SeCir.IA = int(IntAng)


def Triangle():
    triag = input('How many Triangles? ->')
=======
class shape ():
    pass

SeCir = shape()

def InterAngle():
    IntAng = input ('Intersection angle? (degrees) ->')
    SeCir.IA = int (IntAng)
    
def Triangle():
    triag = input ('How many Triangles? ->')
>>>>>>> master
    SeCir.Tri = int(triag)
    SeCir.AngA = SeCir.IA/SeCir.Tri
    SeCir.AngB = (180 - SeCir.AngA)/2
    SeCir.AngTwoB = 180 - SeCir.AngA

<<<<<<< HEAD

def HLen():
    radius = input('What size Radius? ->')
    SeCir.Rad = float(radius)
    RA = radians(SeCir.AngA)
=======
def HLen():
    radius = input ('What size Radius? ->')
    SeCir.Rad = float(radius)
    RA = radians (SeCir.AngA)
>>>>>>> master
    SqrLen = ((SeCir.Rad**2)*2) - (2 * SeCir.Rad * SeCir.Rad * cos(RA))
    Len = sqrt(SqrLen)
    SeCir.Len = Len

<<<<<<< HEAD

def Details():
    print ('initial Angle, ', SeCir.AngB)
    print ('Following Angles, ', SeCir.AngTwoB)
    print ('with a length of ', SeCir.Len)


=======
def Details():

##  print ('With an intersection angle of ',SeCir.IA,',',SeCir.Tri,' triangles and radius of ',SeCir.Rad) 
    print ('initial Angle, ',SeCir.AngB)
    print ('Following Angles, ',SeCir.AngTwoB)
    print ('with a length of ', SeCir.Len)
    
>>>>>>> master
def Again():
    print ('Again?')
    YN = input()
    if YN == 'y' or YN == 'Y':
        hump()
<<<<<<< HEAD
    elif YN != 'y' or YN != 'Y':
        quit()
    else:
        quit()


=======
    else:
        quit()

>>>>>>> master
def hump():
    InterAngle()
    Triangle()
    HLen()
    Details()
    Again()

<<<<<<< HEAD

hump()
=======
hump()    
    
>>>>>>> master
