#!/usr/bin/python
#!encoding: UTF-8

#import pylab as dibujo
import sys
from sympy import *
import math
import time
import timeit

import numpy as np 
import matplotlib.pyplot as plt
import calculotaylor


n=3



tiempo=[]
xtiempo=[]



graf1= plt.subplot(211)
print"Cargado el   0 por ciento de las Graficas"
i=0
for error in calculotaylor.Errores:
    start=time.time()
    i+=1
    n=calculotaylor.ErrorTaylor(calculotaylor.x,calculotaylor.c,error)
    x1=np.arange(-10,10,0.001)
    y=calculotaylor.graficaTaylor(calculotaylor.c,n)
    plt.plot(x1,y, label= 'n = %d' %(n-1))
    print"Cargado %3d por ciento de las Graficas" %(100*i/(len(calculotaylor.Errores))) # Calcula el % de los datos introducidos en el Grafica, así hace la espera mas amena.
    finish=time.time()-start
    tiempo=tiempo+[finish]
plt.plot(x1,np.cos(x1), label = 'cos(x)')    
plt.title('Series de Potencias de Taylor de grado n')
plt.legend(loc = 3) 
plt.ylim(-1.5,1.5)

for i in range (1,len(tiempo)+1):
  xtiempo=xtiempo+[i]
  
graf2=plt.subplot(212)
plt.title('Tiempo que tarda en calcular el Polinomio de Taylor')
plt.plot(xtiempo,tiempo, 'bo')
plt.xticks(xtiempo, size = 'small', color = 'b')
plt.yticks(tiempo, size = 'small', color = 'b')
plt.xlabel("Numero del error")
plt.ylabel("Tiempo")
plt.xlim(0,(len(tiempo)+1))

plt.savefig("Graficas.eps", dpi=100)
plt.show()



