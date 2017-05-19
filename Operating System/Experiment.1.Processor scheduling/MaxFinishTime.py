import math 

def MaxFinishTime(FinishTime):
    temp = FinishTime[0]
    for iter in range(0,len(FinishTime)):
        if temp < FinishTime[iter]:   
             temp = FinishTime[iter]
    return temp;   