#Job Scheduling:SJF
#Chen XingLei
#2017/5/5
#Python 2.7 64bit

#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

import math
import numpy as np
import mainscript as main

def SJF_release():
   
   process_num = main.process_num
   ArrivalTime = main.ArrivalTime
   ServiceTime = main.ServiceTime

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