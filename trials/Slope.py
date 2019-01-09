import math
from math import cos
from math import sqrt
from math import radians
from math import degrees


class Hill ():
    pass


AHill = Hill()


def GetLens():
    LaidLen = input('Laid Length? ->')
    AHill.Laid = float(LaidLen)
    CrowLen = input('2D Length? ->')
    AHill.Crow = float(CrowLen)


def CAH():
    CosAng = AHill.Crow/AHill.Laid
    Ang = cos(CosAng)
    AHill.Ang = degrees(Ang)


def LastAngle():
    AHill.LA = 180-AHill.Ang-90


def Radical():
    AHill.RA = radians(AHill.Ang)
    AHill.RLA = radians(AHill.LA)


def OppLen():
    formula1 = (AHill.Laid**2) * (AHill.Crow ** 2)
    formula2 = (2 * AHill.Laid * AHill.Crow * cos(AHill.RA))
    SqrLen = formula1 - formula2
    Len = sqrt(SqrLen)
    AHill.Len = Len

def grade():
    Grd = AHill.Len/AHill.Laid
    AHill.Grd = Grd
    AHill.PGrd = Grd*100

def Details():
    print ('Laid Length ', AHill.Laid, 'm')
    print ('2d Length ', AHill.Crow, 'm')
    print ('cos theta ', AHill.Ang, 'Rads')
    print ('LastAngle ', AHill.LA, 'Rads')
    print ('Length of c ', AHill.Len, 'm')
    print ('Percentage grade of slope is ', AHill.Grd, '%')


def Slope():
    GetLens()
    CAH()
    LastAngle()
    Radical()
    OppLen()
    grade()
    Details()


Slope()
