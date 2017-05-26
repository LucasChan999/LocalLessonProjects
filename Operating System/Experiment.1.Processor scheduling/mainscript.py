#Job Scheduling:main script
#Chen XingLei
#2017/5/5
#Python 2.7 64bit


import FirstComeFirstServe 
import ShortJobFirst as SJF
import math 
import InputFromKeyboard 
import numpy as np

#MaxNum = 100
#process_num = 5           test data from homework   
#ArrivalTime = [0,1,3,4,6]
#ServiceTime = [5,7,3,8,2]

#process_num = 5           test data from book
#ArrivalTime = [0,1,2,3,4]
#ServiceTime = [4,3,4,2,4]

#FinishTime = int[MaxNum]
#WholeTime = list[MaxNum]
#WeightWholeTime = list[MaxNum]
#AverageWT_FCFS,AverageWT_SJF
#AverageWWT_FCFS,AverageWWT_SJF

print "Welcome Use Processor Scheduling system.......\n"
process_num,ArrivalTime,ServiceTime,selection = InputFromKeyboard.InputFromKeyboard()


def SJF_release():
   import mainscript as main
   #ArrivalTime = [0,1,3,4,6]
   #ServiceTime = [5,7,3,8,2]
   ArrivalTime = main.ArrivalTime
   ServiceTime = main.ServiceTime  
   process_num = main.process_num
 
   FinishTime = []
   WholeTime = []
   WeightWholeTime = []
   temp0 = []
   #set origin set values = 0
   for iter in range(0,process_num):
      FinishTime.append(0)
   for iter in range(0,process_num):
      WholeTime.append(0)
   for iter in range(0,process_num):
      WeightWholeTime.append(0)
    
   for iter in range(process_num):
       temp0.append(ArrivalTime[iter])
   timer = 0
   index = 0
   temp_set_S = []#store time-available process's index    !note:temp_set shall not be assined original values!
   temp_set_I = []#store time-available process's arrival time
      
   for iter1 in range(0,process_num):
     #find the earliest 
     for iter2 in range(0,process_num): 
      if(temp0[iter2]<=timer):
              #print 'test:',iter1,'|',iter2,'\n' #for test
              temp_set_S.append(ServiceTime[iter2])  
              temp_set_I.append(iter2)
     #find the minnum Service time of avaiable process
     temp_set_min = min(temp_set_S)
     for iter3 in range(len(temp_set_S)):
        if(temp_set_min  == temp_set_S[iter3]):
             index = temp_set_I[iter3]#locate the index of this process
 
     timer = timer + temp_set_min
       
     #clean the temp_set
     temp_set_S = [] 
     temp_set_I = []
  
     temp2 = max(FinishTime)
     FinishTime[index] = temp_set_min + temp2 
     print "Time ",iter," Process ",index," start runnning..."
     temp0[index] = 100#make sure process used not available
   for iter in range(0,process_num):
      #WholeTime.insert(0,"WholeTime")
      WholeTime[iter] = FinishTime[iter] - ArrivalTime[iter] 
      #WeightWholeTime.insert(0,"WeightWholeTime")
      WeightWholeTime[iter] =round( float(WholeTime[iter])/float(ServiceTime[iter]),2) #float make sure division makes decimal,round controls the accuracy
   AverageWT = round(np.mean(WholeTime),2)
   AverageWWT = round(np.mean(WeightWholeTime),2)
   answer = (FinishTime,WholeTime,WeightWholeTime)
   return (answer,AverageWT,AverageWWT)

def FCFS_release():
   import mainscript as main
   #ArrivalTime = [0,1,3,4,6]
   #ServiceTime = [5,7,3,8,2]
   ArrivalTime = main.ArrivalTime
   ServiceTime = main.ServiceTime  
   process_num = main.process_num
 
   FinishTime = []
   WholeTime = []
   WeightWholeTime = []
   temp0 = []
   #set origin values 0
   for iter in range(0,process_num):
      FinishTime.append(0)
   for iter in range(0,process_num):
      WholeTime.append(0)
   for iter in range(0,process_num):
      WeightWholeTime.append(0)
  
   #if point to ArrivalTime,origin value will be affected
   for iter in range(process_num):
       temp0.append(ArrivalTime[iter])
   index =  0 
   temp2 = FinishTime[0]
   for iter in range(0,process_num):
      #get earliest arrvial time's index
      value = min(temp0)
      for iter in range(0,process_num):#[0,process_num)
       if(temp0[iter] == value):
         index = iter
         temp0[iter] = 100
      #print 'index:',index  just for test
     
     #max value of finish_time
      temp2 = max(FinishTime)
      #FinishTime.insert(0,"FinishTime")
      FinishTime[index] = ServiceTime[index] + temp2
      print "Time ",iter," Process ",index," start runnning..."
   for iter in range(0,process_num):
      #WholeTime.insert(0,"WholeTime")
      WholeTime[iter] = FinishTime[iter] - ArrivalTime[iter] 
      #WeightWholeTime.insert(0,"WeightWholeTime")
      WeightWholeTime[iter] =round( float(WholeTime[iter])/float(ServiceTime[iter]),2) #float make sure division makes decimal,round controls the accuracy
   AverageWT = round(np.mean(WholeTime),2)
   AverageWWT = round(np.mean(WeightWholeTime),2)
   answer = (FinishTime,WholeTime,WeightWholeTime) 
  
   #test output arrvial time 
   #for iter in range(process_num):
   #   print ArrivalTime[iter],'\n'
  
   return (answer,AverageWT,AverageWWT)

if selection == 1:
#FCFS.
 print '-------------------------FCFS-------------------------------------'
 (answer,AverageWT_FCFS,AverageWWT_FCFS) = FCFS_release()
 
 for iter in range(0,3):
    if iter == 0:
      for it in range(process_num):
       print 'Process',it,"'s finish time:",answer[iter][it],'\n'
    if iter == 1:
      for it in range(process_num):
       print 'Process',it,"'s whole time:",answer[iter][it],'\n'
    if iter == 2:
      for it in range(process_num):
       print 'Process',it,"'s WeightWhole time:",answer[iter][it],'\n'
 print 'AverageWholeTime_FCFS',AverageWT_FCFS,'\n'
 print 'AverageWeightWholeWeight_FCFS',AverageWWT_FCFS,'\n'
else:
 print'--------------------------JFS--------------------------------------'
 (answer,AverageWT_JFS,AverageWWT_JFS) = SJF_release()
 print 'test1\n' 
 for iter in range(0,3):
    if iter == 0:
      for it in range(process_num):
       print 'Process',it,"'s finish time:",answer[iter][it],'\n'
    if iter == 1:
      for it in range(process_num):
       print 'Process',it,"'s whole time:",answer[iter][it],'\n'
    if iter == 2:
      for it in range(process_num):
       print 'Process',it,"'s WeightWhole time:",answer[iter][it],'\n'
 print 'AverageWholeTime_FCFS',AverageWT_JFS,'\n'
 print 'AverageWeightWholeWeight_FCFS',AverageWWT_JFS,'\n'

