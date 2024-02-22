# Program Name: ga_code.py
# Description: This is a python implementation of flood algorithm for exam seat planning
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
def initial_population():
    population=[[] for i in range(popSize)]
    for i in range(popSize):
        population[i]=np.random.permutation(range(1,nVars+1))[:nVars]
    return population
def rotateArray(t_array, rPoint):
    temp=[]
    n=len(t_array)
    for i in range(rPoint, n):
        temp.append(t_array[i])
    i=0
    for i in range(0,rPoint):
        temp.append(t_array[i])
    t_array=temp.copy()
    return t_array
    
def path_relinking(c_solution, t_solution, c_value, t_value, max_step):
    #rotate
    for i in range(nVars):
        if c_solution[i]==t_solution[0]:
            c_solution=rotateArray(c_solution,i)
            break
    #change
    key=1
    for j in range(max_step):
        for k in range(key, nVars):
            if t_solution[key]==c_solution[k]:
                temp=c_solution[key]
                c_solution[key]=c_solution[k]
                c_solution[k]=temp
                key+=1
                break                
        if (ff1(c_solution)+ff2(c_solution))<c_value or (ff1(c_solution)+ff2(c_solution))<t_value:
            break
    return c_solution
def new_solution(solution, max_step, c_value, t_value):
    for i in range(max_step):        
        sPoint1=random.randint(0, nVars-1)
        sPoint2=random.randint(0, nVars-1)
        tempPoint=solution[sPoint1]
        solution[sPoint1]=solution[sPoint2]
        solution[sPoint2]=tempPoint
        if (ff1(solution)+ff2(solution))<t_value:
            break
    return solution
students_=stdcourse_vector()
sittingPlaces=sitting_places()
popSize = 100
maxIteration = 100

for i in range(1,len(students_)):
    students=[]   
    students=students_[i]    
    for j in range(len(students)-1,-1,-1):
        if students[j]==0:
            students.pop()
        else:
            break
    nVars=len(students)
    mopsoPopulation=initial_population()
    values=[(ff1(item)+ff2(item)) for item in mopsoPopulation]
    pBestPositions=mopsoPopulation
    pBestValues = values
    qBestPosition = mopsoPopulation[0]
    qBestValue = min(values)
    for k in range(maxIteration):
        print(k)
        for m in range(popSize):
            v1=new_solution(mopsoPopulation[m], 3, values[m], qBestValue)
            currValue=ff1(v1)+ff2(v1)
            if currValue<pBestValues[m]:
                pBestPositions[m]=v1
                pBestValues[m]=currValue
            if currValue<qBestValue:
                qBestPosition=v1
                qBestValue=currValue
            v2=path_relinking(v1, pBestPositions[m], values[m], pBestValues[m], 3)
            currValue=ff1(v2)+ff2(v2)
            if currValue<pBestValues[m]:
                pBestPositions[m]=v2
                pBestValues[m]=currValue
            if currValue<qBestValue:
                qBestPosition=v2
                qBestValue=currValue
            v3=path_relinking(v1, qBestPosition, values[m], qBestValue, 3)
            currValue=ff1(v3)+ff2(v3)
            if currValue<pBestValues[m]:
                pBestPositions[m]=v3
                pBestValues[m]=currValue
            if currValue<qBestValue:
                qBestPosition=v3
                qBestValue=currValue
    print(i,"th session--Min_value=",qBestValue)