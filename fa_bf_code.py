# Program Name: fa_code.py
# Description: This is a python implementation of flood algorithm
# Author: Ramazan ÖZKAN 
# Supervisor: Prof. Rüya ŞAMLI
import random

limitS=-100 #limits for solution variables
limitH=100 #limits for solution variables
def new_solution(solution1, dimension=2):
    solution=[]
    for i in solution1:
       solution.append(i)
    selected_dimension=random.randint(0, dimension-1)
    solution[selected_dimension]=random.uniform(limitS, limitH)
    return solution

def flood_algorithm(fitnessFunction, nVars, neighborsCount, stopLimit=200):
    stopControl=0    
    vcurr=1
    vmin=0.1
    curr=[random.uniform(limitS, limitH) for j in range(nVars)]
    best=curr
    curr_value=fitnessFunction(curr)
    best_value=curr_value   
    while vcurr>vmin or stopControl<stopLimit:
        neighbors=[[] for k in range(neighborsCount)]
        neighborsValues=[0 for k in range(neighborsCount)]
        control=False
        for j in range(neighborsCount):
            neighbors[j]=new_solution(curr, nVars)
            neighborsValues[j]=fitnessFunction(neighbors[j])            
            if neighborsValues[j]<curr_value:
                curr=neighbors[j]
                curr_value=neighborsValues[j]                
                if neighborsValues[j]<best_value:
                    best=neighbors[j]
                    best_value=neighborsValues[j]
                    stopControl=0
                control=True
                break
        if control==False:
            stopControl+=1
            temp=[]
            tempValue=0
            difference=9999999
            for j in range(neighborsCount):
                temp_difference=neighborsValues[j]-curr_value
                if temp_difference<difference:
                    temp=neighbors[j]
                    tempValue=neighborsValues[j]
                    difference=temp_difference
            curr=temp
            curr_value=tempValue
    return best, best_value

