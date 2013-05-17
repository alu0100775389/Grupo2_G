# -*- coding: utf-8 -*-
import sys
from matplotlib.pylab import *
import time

def integralsimple(f,a,b, integral):   #Cálculo de la integral simple

  inicio = time.time() #Calcula el tiempo transcurrido hasta el momento
  
  h=(b-a)/2;
  x=a
  fa=eval(f)
  x=b
  fb=eval(f)
  x=a+h
  fab=eval(f)
  ftotal=(fa+fb+4*fab)
  integs=(h/3)*ftotal
  
  fin = time.time()  #Calcula el tiempo transcurrido hasta que finaliza este procedimiento
  errort = abs(integs - integral)  #Calcula el error absoluto de la aproximación
  tiempot = fin - inicio  #Calcula tiempo total invertido en el procedimiento
  
  return integs, errort, tiempot

def integralcomps(funcion,a,b,n, integral):

  inicial = time.time()  # Mide tiempo inicial
  
  h=(b-a)/(3*n)
  f1=0
  i=1
  while i<=(n-1):
    x=a+h*(2*i)
    f1=f1+eval(funcion)
    i+=1
  f2=0
  k=1
  while k<=n:
    x=a+h*(2*i-1)
    f2=f2+eval(funcion)
    k+=1
  f=2*f1+4*f2
  x=a
  fa=f+eval(funcion)
  x=b
  fb=fa+eval(funcion)
  integc=(h/3)*fb
  
  final = time.time()  #Mide tiempo final, calcula la diferencia final - inicial e imprimir
  error = abs(integc - integral)  #Calcula error absoluto producido con la aproximación
  tiempo = final - inicial  # Calcula tiempo total
  return integc, error, tiempo

def representacionerrortiempo(funcion, a, b, X, integral):

  # Reserva memoria para los valores de Y
  Ye = zeros(len(X))
  Yt = zeros(len(X))
  
  # Da valores a Y
  for w in range(len(X)):
    integc, error, tiempo = integralcomps(funcion, a, b, X[w], integral)
    Ye[w] = error
    Yt[w] = tiempo
  
  # En una misma figura, se representan dos gráficas 
  figure(1) 
  title('Representacion errores y tiempo')
  
  # Primera gráfica
  subplot(211)
  xlabel('Subintervalos')
  ylabel('Error')
  errorplot, = plot(range(len(X)),Ye,'ro')
  xticks(range(len(X)), X)
  legend([errorplot], ('error'), 'best')
  
  #Segunda gráfica
  subplot(212)
  xlabel('Subintervalos')
  ylabel('Tiempo')
  tiempoplot, = plot(range(len(X)),Yt,'bo')
  xticks(range(len(X)), X)
  legend([tiempoplot], ('tiempo'), 'best')
  
  # Devuelve la gráfica como imagen .eps
  savefig('errortiemp.eps')
  
  #Muestra la gráfica
  show()
  
def representacionfuncion(funcion, a, b):

  # Valores de X y reserva memoria para Y
  X = linspace(a, b, 5)  
  Y = zeros(len(X))   
  
  # Da valores a Y
  for i in xrange(len(X)):
    x=X[i]
    Y[i] = eval(funcion)

  plot(X,Y)
  title('Representacion funcion') 
  xlabel('Valores entre el intervalo [1,2]')
  ylabel('Valores de la funcion en [1,2]')
  legend(['x**3/(1 + X**(1/2))'])
  xlim(0.9, 2.1)
  ylim(0.0, 4.5)
  
  # Devuelve imagen con la gráfica
  savefig('tmp2.eps')
  # Muestra gráfica
  show()
  
if __name__=='__main__':
  if len(sys.argv)==5:
    funcion = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    n = int(sys.argv[4])
    X = [10, 100, 1000, 10000, 100000]
    integral = 1.647
    print "Resultados finales colocados en: (Integral, error, tiempo)"
    print "Cálculo integral mediante fórmula simple:", integralsimple(funcion,a,b, integral)
    print "Cálculo integral mediante fórmula compuesta:", integralcomps(funcion,a,b,n, integral)
    print "Representación gráfica de la función:", representacionfuncion(funcion, a, b)
    print "Representación gráfica de la integral y los errores", representacionerrortiempo(funcion, a, b, X, integral)
    