#coding = utf-8
import math 
import numpy

def EarlistTimeIndex(ArrivalTime):
 earliest = ArrivalTime[0]
 Index =  0   
 for iter in range(0,len(ArrivalTime)):
     temp = ArrivalTime[iter+1]
     if(earliest > temp):
         earlist = temp
         Index = iter + 1
     else:
         continue
 return Index
     
    

        
  