import numpy as np 
k= 8.99*10**9
"""This function will tell you the voltage based upon the location of the charges""" 
def pointPotential(x,y,q, posx, posy):
    Vxy = (k*q/((x-posx)**2+(y-posy)**2)**(1/2.))
    return Vxy

def dipolePotential(x,y,q,d):
    V1 = pointPotential(x,y,q,-d/2,0)
    V2 = pointPotential(x,y,q,d/2,0)
    Vxy = V1 - V2	
    return Vxy

def pointField(x,y,q,Xq,Yq):
    Ex = (kq(x-Xq))/(((x-Xq)**2+(y-Yq)**2)**1/2)
    Ey = (kq(y-Yq))/(((x-Xq)**2+(y-Yq)**2)**1/2)
    Exy = Ex - Ey 
"""The function will return a value at a certain point for (x,y) that 
indicates a point charge part of an electric field"""

