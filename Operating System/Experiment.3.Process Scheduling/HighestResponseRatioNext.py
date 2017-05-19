#Process Scheduling:Highest Response Ratio Next
#Chen XingLei
#2017/5/19
#Python 2.7 64bit
import numpy as np

def HRRN_beta():
  #parameter
  MaxNum = 1000
  process_num = 5           #test data from homework   
  ArrivalTime = [0,1,2,3,4]
  ServiceTime = [6,2,5,9,8]
  value_Q = 2 # set q default value = 2 time 
  timer = 0  #time clock
  
  
  tempA = []  #temp set for arrivltime
  Priority = [] #(waittime + servicetime)/ servicetime
  WaitTime = []
  temp_set_S = []
  temp_set_I = []
 
  #answer
  FinishTime = []
  WholeTime = []
  WeightWholeTime = []
 
  for iter in range(process_num):
     tempA.append(ArrivalTime[iter])
  for iter in range(0,process_num):
     FinishTime.append(0)
  for iter in range(0,process_num):
     Priority.append(0) 
  for iter in range(0,process_num):
     WaitTime.append(0)
  for iter in range(0,process_num):
      WholeTime.append(0)
  for iter in range(0,process_num):
      WeightWholeTime.append(0)
  
  #refresh the priority
  for iter in range(0,process_num):
     Priority[iter] = float((WaitTime[iter] + ServiceTime[iter])/ServiceTime[iter])
  
  for iter1 in range(0,process_num):
     #find the earliest 
     for iter2 in range(0,process_num):  #1.ArivalTime avaiable for timer and store them in temp_set
      if(tempA[iter2]<=timer):
              temp_set_S.append(ServiceTime[iter2])  
              temp_set_I.append(iter2)
     for iter in range(0,len(temp_set_I)): #2.Get these process 's Priority
              index0 = temp_set_I[iter]
              Priority[index0] = float((WaitTime[index0] + ServiceTime[index0])/ServiceTime[index0])
     priority_min = min(Priority) 
     for iter in range(0,len(temp_set_I)):
         if Priority[iter] == priority_min:
              index1 = temp_set_I[iter] 
     tempA[index1] = MaxNum #process index1 finished

     ## test error :list index out of range 
     #print 'index1,len(temp_set_S):',index1,len(temp_set_S),'\n'

     FinishTime[index1] = ServiceTime[index1] + timer
     timer =  ServiceTime[index1] + timer
     #refresh the WaitTime
     for iter in range(0,len(temp_set_I)):
        if  temp_set_I[iter] != index1:
         WaitTime[temp_set_I[iter]]  =  WaitTime[temp_set_I[iter]] + ServiceTime[index1]
            
     #clean the temp_set
     temp_set_S = [] 
     temp_set_I = []

  #for iter in range(0,process_num):
  #   print 'FinishTime',iter,':',FinishTime[iter],'\n'   
  for iter in range(0,process_num):
      #WholeTime.insert(0,"WholeTime")
      WholeTime[iter] = FinishTime[iter] - ArrivalTime[iter] 
      #WeightWholeTime.insert(0,"WeightWholeTime")
      WeightWholeTime[iter] =round( float(WholeTime[iter])/float(ServiceTime[iter]),2) #float make sure division makes decimal,round controls the accuracy
  AverageWT = round(np.mean(WholeTime),2)
  AverageWWT = round(np.mean(WeightWholeTime),2)
  answer = (FinishTime,WholeTime,WeightWholeTime)
  return (answer,AverageWT,AverageWWT,process_num)

def HRRN_release():
  #parameter
  MaxNum = 1000
  process_num = 5           #test data from homework   
  ArrivalTime = [0,1,2,3,4]
  ServiceTime = [6,2,5,9,8]
  value_Q = 2 # set q default value = 2 time 
  timer = 0  #time clock
  
  
  tempA = []  #temp set for arrivltime
  Priority = [] #(waittime + servicetime)/ servicetime
  WaitTime = []
  temp_set_S = []
  temp_set_I = []
 
  #answer
  FinishTime = []
  WholeTime = []
  WeightWholeTime = []
 
  for iter in range(process_num):
     tempA.append(ArrivalTime[iter])
  for iter in range(0,process_num):
     FinishTime.append(0)
  for iter in range(0,process_num):
     Priority.append(0) 
  for iter in range(0,process_num):
     WaitTime.append(0)
  for iter in range(0,process_num):
      WholeTime.append(0)
  for iter in range(0,process_num):
      WeightWholeTime.append(0)
  
  #refresh the priority
  for iter in range(0,process_num):
     Priority[iter] = float((WaitTime[iter] + ServiceTime[iter])/ServiceTime[iter])
  
  for iter1 in range(0,process_num):
     #find the earliest 
     for iter2 in range(0,process_num):  #1.ArivalTime avaiable for timer and store them in temp_set
      if(tempA[iter2]<=timer):
              temp_set_S.append(ServiceTime[iter2])  
              temp_set_I.append(iter2)
     for iter in range(0,len(temp_set_I)): #2.Get these process 's Priority
              index0 = temp_set_I[iter]
              Priority[index0] = float((WaitTime[index0] + ServiceTime[index0])/ServiceTime[index0])
     priority_min = min(Priority) 
     for iter in range(0,len(temp_set_I)):
         if Priority[iter] == priority_min:
              index1 = temp_set_I[iter] 
     tempA[index1] = MaxNum #process index1 finished

     ## test error :list index out of range 
     #print 'index1,len(temp_set_S):',index1,len(temp_set_S),'\n'

     FinishTime[index1] = ServiceTime[index1] + timer
     timer =  ServiceTime[index1] + timer
     #refresh the WaitTime
     for iter in range(0,len(temp_set_I)):
        if  temp_set_I[iter] != index1:
         WaitTime[temp_set_I[iter]]  =  WaitTime[temp_set_I[iter]] + ServiceTime[index1]
            
     #clean the temp_set
     temp_set_S = [] 
     temp_set_I = []

  #for iter in range(0,process_num):
  #   print 'FinishTime',iter,':',FinishTime[iter],'\n'   
  for iter in range(0,process_num):
      #WholeTime.insert(0,"WholeTime")
      WholeTime[iter] = FinishTime[iter] - ArrivalTime[iter] 
      #WeightWholeTime.insert(0,"WeightWholeTime")
      WeightWholeTime[iter] =round( float(WholeTime[iter])/float(ServiceTime[iter]),2) #float make sure division makes decimal,round controls the accuracy
  AverageWT = round(np.mean(WholeTime),2)
  AverageWWT = round(np.mean(WeightWholeTime),2)
  answer = (FinishTime,WholeTime,WeightWholeTime)
  return (answer,AverageWT,AverageWWT,process_num)
      
 #find the running process 's index
  #temp0 = min(ArrivalTime)
  #for iter in range(0,process_num):
  #    if ArrivalTime[iter] == temp0:
  #         index = iter
  #ServiceTime[index] = 0 #process index finished
  #timer = timer + ServiceTime[index]
  #for iter in range(process_num):
  #    WaitTime[iter] = timer + ServiceTime[index]
  ##refresh the priority
  #for iter in range(0,process_num):
  #   Priority[iter] = float((WaitTime[iter] + ServiceTime[iter])/ServiceTime[iter])
  
  
  

  
 