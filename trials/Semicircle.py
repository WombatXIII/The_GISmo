import math
from math import cos
from math import sqrt
from math import degrees
from math import radians

def HumpAngle(triangles):
    AngleA = 180/triangles
    AngleB = (180 - AngleA)/2
    AngleTwoB = AngleB * 2
    print (AngleA,',',AngleB,',',AngleTwoB)

HumpAngle(5)

#def cosine(a):
#    print(cos(a))

#cosine(100)


def HumpLen(radius,AngA):
    RA = radians (AngA)
    ASqr = ((radius**2)*2) - (2 * radius * radius * cos(RA))
    A = sqrt(ASqr)
    print (A)
    
HumpLen(.75,36)

##    RadSqu = radius * radius
##    RAngA = radians(AngA)
##    CosRAngA = cos(RAngA)
##    form1 = RadSqu * 2
##    form2 = 2 * radius * radius * CosRAngA
##    Len = form1-form2
##    LenSqu = sqrt(Len)
##    print(LenSqu)

##RA = radians (36)
##
##ASqr = ((0.75**2)+(0.75**2)) - (2 * 0.75 * 0.75 * (cos(RA)))
##
##A = sqrt(ASqr)
##
##print (A)

    
#HumpLen(5,36)


    
