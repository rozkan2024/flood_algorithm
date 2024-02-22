# Program Name: ga_code.py
# Description: This is a python implementation of genetic algorithm
# Author: Ramazan ÖZKAN 
# Supervisor: Prof. Rüya ŞAMLI
import math
import numpy as np
import random

limitS=-100 #limits for solution variables
limitH=100 #limits for solution variables
population=[]
population2=[]
function_values=[]

# tournament selection
def selection(popSize, k=3):
    # first random selection
    selection_ix = random.randint(0, popSize-1)
    for ix in np.random.permutation(popSize)[:k]:        
        if function_values[ix] < function_values[selection_ix]:
            selection_ix = ix
    return population[selection_ix]
#Function to carry out the crossover
def crossover(parent1,parent2, nVars):
    if nVars==2:
        child=[0 for i in range(nVars)]
        child[0]=parent2[1]
        child[1]=parent1[0]
    else:
        crossover_point=random.randint(0, nVars-2)
        child=[0 for i in range(nVars)]
        child[0:crossover_point]=parent2[0:crossover_point]
        child[crossover_point+1:]=parent1[crossover_point+1:]
    return child
#Function to carry out the mutation operator
def mutation(solution, nVars): 
    mutation_point=random.randint(0, nVars-1)
    solution[mutation_point]=random.uniform(limitS, limitH)
    return solution
#Function to carry out child production
def offspring(prnts, crossoverRate, mutationRate, nVars):
    popSize=len(prnts)
    nuCrossOver=0
    nuMutation=0
    c=[]
    for i in range(0, popSize, 2):
        p1, p2 = prnts[i], prnts[i+1]           
        if random.uniform(0, 1)<crossoverRate:
            c.append(crossover(p1, p2, nVars))
            c.append(crossover(p2, p1, nVars))
            nuCrossOver+=2
        else:
            c.append(p1)
            c.append(p2)
    for i in c:
        if random.uniform(0, 1)<(mutationRate):
            population2.append(mutation(i, nVars))
            nuMutation+=1
        else:
            population2.append(i)
def initial_population(popSize, nVars):
    population=[[random.uniform(limitS, limitH) for j in range(nVars)] for i in range(popSize)]
    return population

def genetic_algorithm(fitnessFunction, nVars=2, popSize=100, max_gen=100, migrationRate=0.1, crossoverRate=0.8, mutationRate=0.05):
    global population
    global population2
    global function_values
    population=initial_population(popSize, nVars)
    function_values = [fitnessFunction(population[m]) for m in range(0,popSize)]
    min_value=min(function_values)
    gen_no=0
    evol_control=100
    control=0
    while(gen_no<max_gen):
        parents=[]
        population2=[]
        for j in range(popSize):
            parents.append(selection(popSize))
        offspring(parents, crossoverRate, mutationRate, nVars)
        function_values2 = [fitnessFunction(population[k]) for k in range(0,popSize)]
        min_value2=min(function_values2)
        if min_value2>=min_value:
            control+=1
        else:
            min_value=min_value2
        if control==evol_control:
            break        
        population=population2
        function_values=function_values2
        gen_no+=1
    return min_value