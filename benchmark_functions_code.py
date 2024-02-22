import random
import numpy as np
import math
def beale(x):
    return (1.5-x[0]+x[0]*x[1])**2+(2.25-x[0]+x[0]*x[1]**2)**2+(2.625-x[0]+x[0]*x[1]**3)**2
def sixhumpcamelback(X):    
    return (4-2.1*X[0]**2+((X[0]**4)/3))*X[0]**2+X[0]*X[1]+(-4+4*X[1]**2)*X[1]**2 
def quatric(x):
    z=random.randint(0,1)
    s=0
    for i in range(1,len(x)+1):
        s+=i*x[i-1]**4
    return s+z
def easom(x):
    return -np.cos(x[0])*np.cos(x[1])*np.exp(-(x[0]-math.pi)**2-(x[1]-math.pi)**2) 
def michalewicz(X):
    toplam=0
    for i in range(1,len(X)+1):
        toplam+=np.sin(X[i-1])*pow(np.sin((i*X[i-1]**2)/math.pi),20)
    return -toplam
def sphere(x):
    sumX=0
    for i in range(len(x)):
        xi = x[i]
        sumX += xi ** 2
    return sumX
def ackley(x):
    s1=sum([k**2 for k in x])
    s2=sum([np.cos(2*math.pi*k) for k in x])
    return -20.0 * np.exp(-0.2 * np.sqrt((1/len(x)) * s1))-np.exp((1/len(x)) * s2) + math.e + 20
def rastrigin(X):
    A = 10
    return A*len(X) + sum([(x**2 - A * np.cos(2 * math.pi * x)) for x in X])
def shubert(X):
    result=1
    for i in range(len(X)):
        result*=((1*np.cos(2*X[i]+1))+(2*np.cos(3*X[i]+2))+(3*np.cos(4*X[i]+3))+(4*np.cos(5*X[i]+4))+(5*np.cos(6*X[i]+5)))
    return result