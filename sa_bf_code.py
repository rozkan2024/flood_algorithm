# Program Name: sa_code.py
# Description: This is a python implementation of simulated annealing
# Author: Ramazan ÖZKAN 
# Supervisor: Prof. Rüya ŞAMLI
import random
import math
import numpy as np

limitS=-100 #limits for solution variables
limitH=100 #limits for solution variables
def new_solution(solution1, dimension=2):
    solution=[]
    for i in solution1:
       solution.append(i)
    selected_dimension=random.randint(0, dimension-1)
    solution[selected_dimension]=random.uniform(limitS, limitH)
    return solution

def sa(fitnessFunction, nVars, neighborsCount, stopLimit=200):
    curr=[random.uniform(limitS, limitH) for j in range(nVars)]
    best=curr
    curr_value=fitnessFunction(curr)
    best_value=curr_value   
    temp=1
    nIteration=10000
    for j in range(nIteration):
        candidate=new_solution(curr,1)
        candidate_value=fitnessFunction(candidate)
        if candidate_value<best_value:
            best=candidate
            best_value=candidate_value
        diff=candidate_value-curr_value
        if diff<0:
            curr, curr_value=candidate,candidate_value
        else:
            t=temp/float(j+1)
            metropolis=math.exp(-diff/t)
            if np.random.rand()<metropolis:
                curr, curr_value=candidate,candidate_value
    return best, best_value

