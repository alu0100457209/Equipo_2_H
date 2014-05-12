#!/usr/bin/python
import random, sys
from sympy import *
import numpy as np 
import math
import time
import timeit

Errores=[0.4789, 0.0456, 0.00005, 0.000000005, 0.000000000007]
x=2.0
c=0.0
f=(x+c)/2

valor_c = Symbol('c')
valor_a = Symbol('f')
funcion = cos(valor_c)
funcion_ = cos (valor_a)


def fac(n):
  if n == 0:
    return 1
  else:
    return n * fac(n-1)

def MostrarTaylor(c,n):
  for i in range(n + 1):
    derivada = eval(str(diff(funcion,valor_c,i)))
    if (i<1):
     sys.stdout.write((str(derivada)))
    if(i>=1):
     x=Symbol('x')
     a=(derivada*((x-c)**i))
     if (derivada != 0):
       if (derivada<0):	 
        a=-a
        sys.stdout.write((' - '+str(a) +' / '+str (i)+'!'))
       else: 
        sys.stdout.write((' + '+str(a) +' / '+str (i)+'!'))
  print '\n' 
  return 1
  
def graficaTaylor(c,n):
  v=0
  for i in range(n + 1):
    derivada = eval(str(diff(funcion,valor_c,i)))
    if (i<1):
     v=v+derivada
    if(i>=1):
     x=np.arange(-10,10,0.001)
     a=(derivada*((x-c)**i))
     if (derivada != 0):
       v=v+derivada*((x-c)**i)/fac(i) 
  return v

  
def ErrorTaylor(x,c,error):
  i=0
  derivada = eval(str(diff(funcion_,valor_a,i)))
  polinomio = ((derivada/(fac(i)))*((x - c)**i))
  while (abs(polinomio)>=error):
    i+=1
    derivada = eval(str(diff(funcion_,valor_a,i)))
    polinomio = ((derivada/(fac(i)))*((x - c)**i))
  return i

 
if __name__=='__main__':
  for error in Errores:
    n=ErrorTaylor(x,c,error)
    print ('\n %3i iteraciones para dar un error <= %.15f') %(n,error)
    MostrarTaylor(c,n-1)
#    dibujargraficas(2,3)
    
  
