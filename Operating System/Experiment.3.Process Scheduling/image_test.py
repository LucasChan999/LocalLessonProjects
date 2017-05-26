import numpy as np
import scipy as sp
import pylab as pl
import matplotlib.pyplot as plt

#pl.plot(x,y)
#pl.show()

def RR_release():
 #import mainscript as ma
 MaxNum = 100
 process_num = 5           #test data from homework   
 ArrivalTime = [0,1,2,3,4]
 ServiceTime = [6,2,5,9,8]
 value_Q = 2; # set q default value = 2 time 
 #parameter
 
 #process_num,ArrivalTime,ServiceTime,value_Q = InputFromKeyboard.InputFromKeyboard()
 #process_num = ma.process_num          #test data from homework   
 #ArrivalTime = ma.ArrivalTime
 #ServiceTime = ma.ServiceTime
 #value_Q = ma.value_Q;
  
 timer = 0
 tempA = [] #temp  for arrvial time 
 tempS = [] #process service time left for running
 tempU = [] #list shows whether process is in order or not
 tempF = [] #list of process finished
 order = [] #store the index of process which are waiting for running in order 0->not exist 1-> exist

 image_x = [] #image parameter                                                                              #added  2017/5/26 
 image_y = [] 

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

    image_x.append(timer)                                                                                 #add the x  2017/5/26 
    timer = timer + ti      #2017/5/19
    image_x.append(timer)   #add the x 2017/5/26
    image_y.append(index+1) #add the process index as y value 2017/5/26
    image_y.append(index+1)

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
 pl.plot(image_x,image_y)        # base function satisfied                                           #added  2017/5/26 
 pl.title('Round Robin')# give plot a title
 pl.xlabel('time')# make axis labels
 pl.ylabel('process')
 pl.show()  
 

 #AverageWT = round(np.mean(WholeTime),2)
 #AverageWWT = round(np.mean(WeightWholeTime),2)
 #answer = (FinishTime,WholeTime,WeightWholeTime) 
 #return (answer,AverageWT,AverageWWT,process_num)
 #add the image function part 
 

RR_release()