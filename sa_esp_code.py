# Program Name: ga_code.py
# Description: This is a python implementation of simulated annealing for exam seat planning
# Author: Ramazan ÖZKAN 
# Supervisor: Prof. Rüya ŞAMLI
import pandas as pd
import numpy as np
import random
import math
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
    temp=1
    coolingRate=0.9
    nIteration=10000
    for j in range(nIteration):
        candidate=new_solution(curr,1)
        candidate_value=ff1(candidate)+ff2(candidate)
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
    print(i,"th session--Min_value=",best_value)
    
    
    
    
    
    
    