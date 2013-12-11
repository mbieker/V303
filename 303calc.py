# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:41:26 2013

@author: martin
"""

from scipy import *
from matplotlib.pyplot import  *
from scipy.optimize import curve_fit
from uncertainties import *



data = loadtxt('Messwerte/aufg2', unpack='True')
data[0] = data[0]*pi/180
data[1] = data[1]/2
def cos_fit(phi,A):
    return A*cos(phi)/pi
params , cov = curve_fit(cos_fit,data[0],data[1])
plot(data[0],data[1],'x')
xlabel("Phasenverschiebung [rad]")
ylabel(r"$U_{out} [V]$")
grid(True)
phi = linspace(0,2*pi)
A = ufloat(params[0],cov[0][0])




plot(phi, cos_fit(phi, params[0]))
show()
close()

#Verlauf bei verrasuchtem Signal
data = loadtxt("Messwerte/aufg3")
phase_shift = data[0]*pi/180.
output = data[1]/data[2]


params , cov = curve_fit(cos_fit,phase_shift,output)
phi = linspace(0,2*pi)
A = ufloat(params[0],cov[0][0])
plot(phi, cos_fit(phi, params[0]))


plot(phase_shift,output, 'x')
show()
close()


## Aufg 4 LED Verlauf

data = loadtxt('Messwerte/aufg4', unpack='true')

distance = (data[0]-3.6)/100 # abstand der Lampen in m
output = data[1]/data[2] ## Out mit Gain normieren

def fit(x,a,b):
    return a*x+b



regression_distance = linspace(0.024,1.4)


plot(distance,output,'x')
yscale('log')
xscale("log")
show()