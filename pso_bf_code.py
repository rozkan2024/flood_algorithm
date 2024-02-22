# Program Name: ga_code.py
# Description: This is a python implementation of genetic algorithm
# Author: Ramazan ÖZKAN 
# Supervisor: Prof. Rüya ŞAMLI
import numpy as np
limitS=-100 #limits for solution variables
limitH=100 #limits for solution variables
def pso_algorithm(fitnessFunction, nVars=2, popSize=100, maxIteration=100, c1=2, c2=2, w=0.8):    
    X = np.random.rand(nVars, popSize)  * (limitH - limitS) + limitS
    V = np.random.randn(nVars, popSize) * 0.1
    pbest = X
    pbest_obj=[0 for i in range(popSize)]
    for l in range(popSize):
        a=[]
        for m in range(nVars):
            a.append(X[m][l])
        pbest_obj[l]=fitnessFunction(a)
    gbest = pbest[:, np.argmin(pbest_obj)]
    gbest_obj = np.min(pbest_obj)
    for k in range(maxIteration):
        r = np.random.rand(2)
        V = w * V + c1*r[0]*(pbest - X) + c2*r[1]*(gbest.reshape(-1,1)-X)
        X = X + V
        obj=[0 for i in range(popSize)]
        for l in range(popSize):
            a=[]
            for m in range(nVars):
                a.append(X[m][l])
            obj[l]=fitnessFunction(a)
        pbest[:, (pbest_obj >= obj)] = X[:, (pbest_obj >= obj)]
        pbest_obj = np.array([pbest_obj, obj]).min(axis=0)
        gbest = pbest[:, pbest_obj.argmin()]
        gbest_obj = pbest_obj.min()
    return gbest_obj