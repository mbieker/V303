# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:41:26 2013

@author: martin
"""

from scipy import *
from matplotlib.pyplot import  *
from scipy.optimize import curve_fit
from uncertainties import *

def make_LaTeX_table(data,header, flip= 'false', onedim = 'false'):
    output = '\\begin{tabular}{'
    #Get dimensions
    if(onedim == 'true'):
        if(flip == 'false'):
        
            data = array([[i] for i in data])
        
        else:
            data = array([data])
        

    row_cnt, col_cnt = data.shape
    header_cnt = len(header)
    
    if(header_cnt == col_cnt and flip== 'false'):
        #Make Format
        output += '|'
        for i in range(col_cnt):
            output += 'c|'
        output += '}\n\\hline\n'+ header[0]
        for i in range (1,col_cnt):
            output += ' & ' + header[i]
        output += ' \\\\\n\\hline\n'
        for i in data:
            output += str(i[0])
            for j in range(1,col_cnt):
                output += ' & ' + str( i[j])
            output += '\\\\\n'
        output += '\\hline\n\\end{tabular}\n'
                            
        return output
    else:
        if(row_cnt == header_cnt):
            output += '|c|' + (col_cnt)*'c' + '|}\n\\hline\n'
            for i in range(row_cnt):
                output += header[i]
                for j in range(col_cnt):
                    output += ' & ' + str(data[i][j])
                output += '\\\\\n\\hline\n'
                
            output += '\\end{tabular}\n'
            return output
        else:
            return 'ERROR'


data = loadtxt('Messwerte/aufg2', unpack='True')
table_content = [[data[0][i], data[1][i], data[1][i]/2] for i in range(12)]
data[0] = data[0]*pi/180
data[1] = data[1]/2



print(make_LaTeX_table(array(table_content), [r'$\Delta \phi [^\cric]$','U_{out}','U_{out}^*']))
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
table_content = [[data[0][i], data[1][i], data[2][i] ,data[1][i]/data[2][i]] for i in range(13)]
print(make_LaTeX_table(array(table_content), [r'$\Delta \phi [^\circ]$','$U_{out}^*$', "Gain",'$U_{out}$']))
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

table_content = array([data[0]/100, distance, data[1] , data[2] , output]).T
print(make_LaTeX_table(array(table_content), [r'd^* [m]','d [m]','$U_{out}^*$', "Gain",'$U_{out}$']))
def fit(x,a,b):
    return a*x+b



regression_distance = linspace(0.024,1.4)


plot(distance,output,'x')
yscale('log')
xscale("log")
show()