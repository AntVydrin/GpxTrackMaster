from math import pi, sin, cos, sqrt, acos

def Dist( latit1, longit1, latit2, longit2):
    dSigma = 0.0
    try:
        # центральный угол
        value = sin(latit1/57.3)*sin(latit2/57.3)+cos(latit1/57.3)*cos(latit2/57.3)*cos(longit2/57.3-longit1/57.3)
        if abs(value) < 1:
            dSigma = acos(value)
        else:
            dSigma = 0

        # локальный радиус Земли
        r = cos(latit1/57.3)*(6378137.0-6356752.3142) + 6356752.3142 #6356752.3142 - полярный радиус; 6378137.0 -экваториальный

    except:
        return 0

    return r * dSigma #Расстояние между точками

#Dist(55.75, 37.616667 , 60.05, 30.25) = 645624.97


