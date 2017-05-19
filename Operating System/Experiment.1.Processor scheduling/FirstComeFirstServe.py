#Job Scheduling:FCFS
#Chen XingLei
#2017/5/5
#Python 2.7 64bit

#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

import math
import numpy as np

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