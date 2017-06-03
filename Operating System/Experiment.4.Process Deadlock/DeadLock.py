#Process Deadlock: Bank Algorithm
#Chen Xinlei
#2017/5/26
#Python 2.7 64bit

import math
import numpy as np

def DeadLock():
    #vectors known
    process_num = 5
    Resource = [10,5,7]  #all resources sums up
    Max = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
    Allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
    Need = [[7,4,3],[1,2,2],[6,0,0],[0,1,1],[4,3,1]]
    #running vector 
    Available = [] #need to be set
    temp_available = []
    temp_available_I = []
    process_uf = []  #index of process unfinished ,0 -> unfinished
    #answer vector
    Work = [0,0,0]  
    #Allo = [0,0,0]
    ne = []  #need in answer 
    Work_Allo = []
    Finish = []
    safe_order = []
    
    #for iter in range(len(Available)):
    #   Work.append(Avaiable[iter])
    for iter in range(process_num):
       Finish.append(0)
    for iter in range(process_num):
       process_uf.append(0)

    #find the first vector of work
    temp0 = [0,0,0]
    for iter1 in range(len(Allocation)):
      temp1 = Allocation[iter1]
      for iter2 in range(3): 
         temp0[iter2] = temp0[iter2] + temp1[iter2]
    Work = [x - y for x, y in zip(Resource, temp0)] 
    print 'First work is ',Work[0],'\n'
    print '---------------------------\n'    

    end_flag = 5 - sum(Finish)
    #while end_flag:
    print process_uf,'\n'
    for iter0 in range(process_num):  
        Allo = [0,0,0]
        #find the available process under work[iter] and store in temp_available
        bool_process = 0 #judge if there is process available for now 
        for iter1 in range(process_num):
            if Need[iter1][0] <= Work[0] and Need[iter1][1] <= Work[1] and Need[iter1][2] <= Work[2] and process_uf[iter1] == 0:
               temp_available.append(Need[iter1])
               temp_available_I.append(iter1)
               bool_process = 1
        if bool_process:
           print 'there is process avalilable for now\n'
        else:
           print 'Could not find process available for now\n '
        #run the first one in work
        print 'temp index:',temp_available_I,'\n'
        index = temp_available_I[0]         #2017_5_27 test for bug 
        safe_order.append(index)
        print 'safe order is :',safe_order,'\n'
        print 'len of process:',len(process_uf),' and index:',index,'\n'
        process_uf[index] = 1 # process index finished 
        Allo = Allocation[index]
        ne.append(Need[index])

        #compute the Work_Allo.append(Work[iter0]+Allo[iter0])
        temp0 = [0,0,0]
        for iter2 in range(3):
            temp0[iter2] = Work[iter2] + Allo[iter2]
        Work_Allo.append(temp0)
        print 'Work_Allo in order ',iter0,'is:',temp0
        
        Work = Work_Allo[iter0]
        Finish[index] = 1
        temp_available = [] #clear the temp set 
        temp_available_I = [] 
        print 'end flag is ',5 - sum(Finish),'\n' #nums of process which are not finished 
        print '---------------------------\n'
    if len(safe_order) == 5:
          print 'Safe order generated :',safe_order,'\n'
    else:
          print 'Could not generate safe order now!'

DeadLock();    


    
    





