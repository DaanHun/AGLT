from math import *
import cmath


#put the values of the x and y position of the target such that x and y are on a plane that cuts trough the AGLT (0,0) and the target such that x is parallel to the direction of the target.
XPOS_TARGET = 0
YPOS_TARGET = 0
BULLET_VELOCITY = 0
TARGET_VELOCITY = 0

p = (BULLET_VELOCITY**2-TARGET_VELOCITY**2)
q = 2*TARGET_VELOCITY*sqrt(XPOS_TARGET**2+YPOS_TARGET**2)*cos(atan2(YPOS_TARGET, XPOS_TARGET))
n = -XPOS_TARGET**2-YPOS_TARGET**2

s = (-q+sqrt(q**2-(4*p*n)))/(2*p)

cgamma = ((BULLET_VELOCITY**2-TARGET_VELOCITY**2)*s**2+XPOS_TARGET**2+YPOS_TARGET**2)/(2*BULLET_VELOCITY*s*sqrt(XPOS_TARGET**2+YPOS_TARGET**2))
try:
    print(acos(cgamma))
except:
    print("error, outside of domain.")

