# Program Name: ga_code.py
# Description: This is a python implementation of genetic algorithm for exam seat planning
# Author: Ramazan ÖZKAN 
# Supervisor: Prof. Rüya ŞAMLI
import pandas as pd
import numpy as np
import random
#get student-course information from excel
def stdcourse_vector():    
    data = pd.read_excel('students.xlsx')
    formattedData=[[]]
    for i in data:
        tmp=[]
        for j in data[i]:
            tmp.append(j)
        formattedData.append(tmp)  
    return formattedData
#get sitting places from excel
def sitting_places():    
    data = pd.read_excel('AdjacencyMatrix.xlsx')
    sittingPlaces=[[] for i in range(data.size)]
    for index, row in data[:].iterrows():
        sittingPlaces[index]=row
    return sittingPlaces
#first part of the fitness function
def ff1(solution):
    sumSides=0
    for i in range(nVars):
        student=solution[i]
        course=students[student-1]#[0]
        side=sittingPlaces[i][3]
        if side!=-1 and side<nVars:
            sideStudent=solution[side-1]
            sideCourse=students[sideStudent-1]#[0]
            if course==sideCourse:
                sumSides+=1        
    return sumSides
#seconf part of the fitness function
def ff2(solution):
    sumBacks=0
    for i in range(nVars):
        student=solution[i]
        course=students[student-1]#[0]
        back=sittingPlaces[i][4]
        if back!=-1 and back<nVars:
            backStudent=solution[back-1]
            backCourse=students[backStudent-1]#[0]
            if course==backCourse:
                sumBacks+=1        
    return sumBacks
# tournament selection
def selection(k=3):
    # first random selection
    selection_ix = random.randint(0, popSize-1)
    for ix in np.random.permutation(popSize)[:k-1]:
        if function_values[ix] < function_values[selection_ix]:
            selection_ix = ix
    return population[selection_ix]
#Function to carry out the crossover
def crossover(parent1,parent2):
    crossover_points=np.random.permutation(nVars)[:2]
    crossover_points.sort()
    child=[-1 for i in range(nVars)]
    child[crossover_points[0]:crossover_points[1]]=parent2[crossover_points[0]:crossover_points[1]]
    k=0
    for i in parent1:
        if i not in child:
            if k==crossover_points[0]:
                k=crossover_points[1]
            child[k]=i
            k+=1
    return child
#Function to carry out the mutation operator
def mutation(solution): 
    nMutation=2
    mPoint1=np.random.permutation(nVars)[:nMutation]
    mPoint2=np.random.permutation(nVars)[:nMutation]
    for i in range(nMutation):
        temp=solution[mPoint1[i]]
        solution[mPoint1[i]]=solution[mPoint2[i]]
        solution[mPoint2[i]]=temp
    return solution
#Alternative mutation function - Reverse Sequence Mutation (RSM)
def mutation_rsm(solution):
    mPoints=[]
    mPoints.append(random.randint(0, nVars-1))
    mPoints.append(random.randint(0, nVars-1))
    mPoints.sort()
    reverseList=solution[mPoints[0]:mPoints[1]]
    solution[mPoints[0]:mPoints[1]]=reverseList[::-1]
    return solution
def offspring(prnts):
    nuCrossOver=0
    nuMutation=0
    c=[]
    for i in range(0, popSize, 2):
        p1, p2 = prnts[i], prnts[i+1]           
        if random.uniform(0, 1)<crossoverRate:
            c.append(crossover(p1, p2))
            c.append(crossover(p2, p1))
            nuCrossOver+=2
        else:
            c.append(p1)
            c.append(p2)
    for i in c:
        if random.uniform(0, 1)<(mutationRate):
            population2.append(mutation(i))
            #population2.append(mutation_rsm(i))
            nuMutation+=1
        else:
            population2.append(i)
def initial_population():
    population=[[] for i in range(popSize)]
    for i in range(popSize):
        population[i]=np.random.permutation(range(1,nVars+1))[:nVars]
    return population

students_=stdcourse_vector()
sittingPlaces=sitting_places()
popSize = 100
max_gen=100
migrationRate=0.1
crossoverRate=0.8
mutationRate=0.05
for i in range(1,len(students_)):
    students=[]   
    students=students_[i]    
    for j in range(len(students)-1,-1,-1):
        if students[j]==0:
            students.pop()
        else:
            break
    nVars=len(students)
    population=initial_population()
    function_values = [ff1(population[m])+ff2(population[m]) for m in range(0,popSize)]
    min_value=min(function_values)
    gen_no=0
    evol_control=100
    control=0
    while(gen_no<max_gen):
        print(gen_no)
        parents=[]
        population2=[]
        for j in range(popSize):
            parents.append(selection())
        offspring(parents)
        function_values2 = [ff1(population2[k])+ff2(population2[k]) for k in range(0,popSize)]
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
        print(i,"th session--Min_value=",min_value)
    
    
    
    
    
    
    