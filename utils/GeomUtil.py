from math import cos, sin
from data.PosVars import Point


class GeomUtil:

    PI = 3.141592653589793
    toRADIANS = PI / 180
    toDEGREES = 180 / PI

    @staticmethod
    def degreesToRadians(degrees):
    
        return degrees * GeomUtil.toRADIANS
    
    @staticmethod
    def getPositionOnCircle(centerX, centerY, angleInDegrees, radiusX, radiusY):
        
        radians = GeomUtil.degreesToRadians(angleInDegrees)

        return Point(centerX + cos(radians) * radiusX, centerY + sin(radians) * radiusY)