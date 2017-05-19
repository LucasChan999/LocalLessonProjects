#Process Shceduling�� main
#Chen Xinlei
#2017/5/20
#Python 2.7 64bit

#process_num = 5           #test data from homework   
#ArrivalTime = [0,1,2,3,4]
#ServiceTime = [6,2,5,9,8]
import math
import numpy as np
import InputFromKeyboard as IFKB
#import InputFromKeyboard
import HighestResponseRatioNext as HRRN
import RoundRobin as RR 

#test the function
#RR.RR_beta()


#test for pop function:PASS
#ArrivalTime = [0,1,2,3,4]
#ArrivalTime.pop(0)
#ArrivalTime.pop(2)
#ArrivalTime.append(0)
#for iter in range(0,len(ArrivalTime)):
#      print ArrivalTime[iter],'\n'
def RR_release(selection):
 MaxNum = 100
 #process_num = 5           #test data from homework   
 #ArrivalTime = [0,1,2,3,4]
 #ServiceTime = [6,2,5,9,8]
 #value_Q = 2; # set q default value = 2 time 
 #parameter
 process_num,ArrivalTime,ServiceTime,value_Q = IFKB.InputFromKeyboard(selection)

 #process_num = main.process_num          #test data from homework   
 #ArrivalTime = main.ArrivalTime
 #ServiceTime = main.ServiceTime
 #value_Q = main.value_Q; # set q default value = 2 time 
 ##parameter
 
 timer = 0
 tempA = [] #temp  for arrvial time 
 tempS = [] #process service time left for running
 tempU = [] #list shows whether process is in order or not
 tempF = [] #list of process finished
 order = [] #store the index of process which are waiting for running in order 0->not exist 1-> exist
 
 index0 = 0
 FinishTime = []
 WholeTime = []
 WeightWholeTime = []
 
 for iter in range(0,process_num):
    FinishTime.append(0)
 for iter in range(process_num):
    tempA.append(ArrivalTime[iter])
 for iter in range(process_num):
    tempS.append(ServiceTime[iter])
 for iter in range(process_num):
    tempU.append(0)
 for iter in range(0,process_num):
      WholeTime.append(0)
 for iter in range(0,process_num):
      WeightWholeTime.append(0)
  
 #running loop
 print "Welcome Use Round Robin system.......\n"
 while len(tempF) != 5:
    ti = 0 #every time added into timer
    #get the available process:1)arrival time  2) in  order 
    print 'Timer:',timer,'\n'
    for iter in range(0,process_num):#already add position 0's progress
      if tempA[iter] <= timer and tempU[iter] == 0 :#!!!!!!try to avoid repeating
         order.append(iter)
         tempU[iter] = 1
    print 'order in timer before refresh is',order,'\n'  #for test
    print 'length of order is:',len(order),'\n'
    
    #refresh ti,timer
    index = order[0]
    print 'Process',index,'start running...\n'
    if value_Q >= tempS[index]:
        ti = tempS[index]
    else:
        ti = value_Q
    timer = timer + ti
    #timer changed
    for iter in range(0,process_num):#already add position 0's progress
      if tempA[iter] <= timer and tempU[iter] == 0 :#!!!!!!try to avoid repeating
         order.append(iter)
         tempU[iter] = 1

    #refresh tempS,tempA,FinishTime
    if tempS[index] != 0:
       #FinishTime[index] = timer + ti 
       tempS[index] = tempS[index] - ti
       print 'Process',index,"'s Service time left:",tempS[index],'\n'
   
   #remove process(index)  if temps[index] == 0
    if tempS[index] == 0:
       tempA[index] = MaxNum #process index finished   
       FinishTime[index] = timer 
       tempF.append(index)
       order.pop(0) #remove it from order
       tempU[index] = 0
       print 'Prodcess Finished is:',tempF,'\n'
    
    #refresh the order 
    if len(order) > 1 and tempS[index] != 0:
       temp = order[0]
       order.pop(0)
       order.append(temp)#put the first to the last
    print 'order in timer after refresh is',order,'\n'  #for test
    print '-------------------------------------\n'
    
 for  iter in range(process_num):
        print 'Process',iter,"'s FinishTime",FinishTime[iter],'\n' 
 for iter in range(0,process_num):
      #WholeTime.insert(0,"WholeTime")
      WholeTime[iter] = FinishTime[iter] - ArrivalTime[iter] 
      #WeightWholeTime.insert(0,"WeightWholeTime")
      WeightWholeTime[iter] =round( float(WholeTime[iter])/float(ServiceTime[iter]),2) #float make sure division makes decimal,round controls the accuracy
 AverageWT = round(np.mean(WholeTime),2)
 AverageWWT = round(np.mean(WeightWholeTime),2)
 answer = (FinishTime,WholeTime,WeightWholeTime) 
 return (answer,AverageWT,AverageWWT,process_num)

def HRRN_release(selection):
  #parameter
  MaxNum = 1000
  #process_num = 5           #test data from homework   
  #ArrivalTime = [0,1,2,3,4]
  #ServiceTime = [6,2,5,9,8]
  #value_Q = 2 # useless in TRRN 
  timer = 0  #time clock
  process_num,ArrivalTime,ServiceTime,value_Q = IFKB.InputFromKeyboard(selection) #value_Q not used 
  
  
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

terminate = 1
while terminate:
 selection = input('Please choose the algorithm:1->RR,2->TRRN\n')

 #process_num,ArrivalTime,ServiceTime,value_Q,selection = IFKB.InputFromKeyboard()

 if selection == 1 :
   print '-------------------------Round Robin----------------------------\n'
   (answer,AverageWT_FCFS,AverageWWT_FCFS,process_num) = RR_release(selection)

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
   terminate = input('Input 1 for Go on! Input 0 for Exit\n')
   print '--------------------------------------------------------------\n'
 else :
   print '-----------------HighestResponseRatioNext-----------------------\n'
   (answer,AverageWT_FCFS,AverageWWT_FCFS,process_num) = HRRN_release(selection)

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
   terminate = input('Input 1 for Go on! Input 0 for Exit\n')
   print '--------------------------------------------------------------\n'


#print "Welcome Use Round Robin system.......\n"
##process_num,ArrivalTime,ServiceTime,value_Q = InputFromKeyboard.InputFromKeyboard()

#print '-------------------------Round Robin-----------------------------'
#(answer,AverageWT_FCFS,AverageWWT_FCFS,process_num,selection) = RR_release()

#for iter in range(0,3):
#    if iter == 0:
#      for it in range(process_num):
#       print 'Process',it,"'s finish time:",answer[iter][it],'\n'
#    if iter == 1:
#      for it in range(process_num):
#       print 'Process',it,"'s whole time:",answer[iter][it],'\n'
#    if iter == 2:
#      for it in range(process_num):
#       print 'Process',it,"'s WeightWhole time:",answer[iter][it],'\n'
#print 'AverageWholeTime_FCFS',AverageWT_FCFS,'\n'
#print 'AverageWeightWholeWeight_FCFS',AverageWWT_FCFS,'\n'

