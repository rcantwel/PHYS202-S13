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
