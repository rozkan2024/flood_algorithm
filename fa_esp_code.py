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
def new_solution(solution1, stepSize):
    solution=[]
    for i in solution1:
       solution.append(i) 
    for i in range(stepSize):        
        sPoint1=random.randint(0, nVars-1)
        sPoint2=random.randint(0, nVars-1)
        tempPoint=solution[sPoint1]
        solution[sPoint1]=solution[sPoint2]
        solution[sPoint2]=tempPoint
    return solution
students_=stdcourse_vector()
sittingPlaces=sitting_places()
for i in range(1,len(students_)):
    students=[]   
    students=students_[i]    
    for j in range(len(students)-1,-1,-1):
        if students[j]==0:
            students.pop()
        else:
            break
    nVars=len(students)
    curr=np.random.permutation(range(1,nVars+1))[:nVars]
    best=curr
    curr_value=ff1(curr)+ff2(curr)
    best_value=curr_value
    maxIteration=10000
    vmaxlimit=1.0
    vmax=1.0
    neighborsCount=30
    contIt=0
    while vmax>0.1 and contIt<maxIteration:
        neighbors=[[] for k in range(neighborsCount)]
        neighborsValues=[0 for k in range(neighborsCount)]
        oldCurr=curr
        oldCurrValue=curr_value
        control=False
        for j in range(neighborsCount):
            neighbors[j]=new_solution(curr, 1)
            contIt+=1
            neighborsValues[j]=ff1(neighbors[j])+ff2(neighbors[j])
            if neighborsValues[j]<curr_value:
                curr=neighbors[j]
                curr_value=neighborsValues[j]
                if neighborsValues[j]<best_value:
                    best=neighbors[j]
                    best_value=neighborsValues[j]
                control=True
                break
        if control==False:
            temp=[]
            tempValue=0
            difference=999999
            for j in range(neighborsCount):
                temp_difference=neighborsValues[j]-curr_value
                if temp_difference<difference:
                    temp=neighbors[j]
                    tempValue=neighborsValues[j]
                    difference=temp_difference
            curr=temp
            curr_value=tempValue
        vmax*=oldCurrValue/curr_value    
    print(i,"th session--Min_value=",best_value)
    
    
    
    
    
    
    