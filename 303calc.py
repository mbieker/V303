# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:41:26 2013

@author: martin
"""

from scipy import *
from matplotlib.pyplot import  *
from scipy.optimize import curve_fit
from uncertainties import *

data1 = loadtxt('Messwerte/aufg2', unpack='True')
data1[0] = data1[0]*pi/180
def cos_fit(phi,U_0,C):
    return 2*U_0*cos(phi)/pi+C
params , cov = curve_fit(cos_fit,data1[0],data1[1],(-5.3,0))
plot(data1[0],data1[1],'x')

phi = linspace(0,2*pi)

U_0 = ufloat(params[0],cov[0][0])
C = ufloat(params[1],cov[1][1])

print('Amplitude : %s und Eichfehler %s' % (U_0 , C))

plot(phi, cos_fit(phi, params[0],params[1]))
close()




## Aufg 4 LED Verlauf

data = loadtxt('Messwerte/aufg4', unpack='true')

distance = (data[0]-3.6)/100 # abstand der Lampen in m
output = data[1]/data[2] ## Out mit Gain normieren

def intensity_fit(dist, factor,  const):
    return factor*dist**-2+C

curve_fit(intensity_fit, distance, output)



plot(regression_distance,regression_distance**-2 *params[1]+params[2])
plot(distance,output,'x')

show()