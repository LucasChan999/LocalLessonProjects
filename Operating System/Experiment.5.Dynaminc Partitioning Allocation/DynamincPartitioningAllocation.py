#Dynaminc Partitioning Allocation based on Sequential Search: include 4 algorithms 
#allocate internal storage to programmes dynamicly
#Chen Xinlei
#2017/6/1
#Python 2.7 64bit

import math
import numpy as np
import string

#parameters  given 
program_num = 5;
internal_stroage  = [16,16,8,32,64,32,8,16,64] #list the internal storge in order 
Need = [7,18,9,20,35,8] #list programmes' need for internal storge in order  
Name = []

def FirstFit():
 partition_num =  len(internal_stroage) 
 temp_need = [] #temp set for Need 
 temp_IS = [] #temp set for internal_storge 
 unfinished = []
 
 answer_allocation = [] #interal storage after allocated 

 for iter in range(program_num):
    temp_need.append([iter])
    unfinished.append(0)
 for iter in range(partition_num):
    temp_IS.append( internal_stroage[iter] )
 for iter in range(partition_num):
    answer_allocation.append(internal_stroage[iter])
 for iter in string.lowercase:  #write in 27 letter as names of programmes
    Name.append(iter);
 
 end = program_num - sum(unfinished)
 while end:#pop the need value whose programme is finished 
  for iter1 in range(partition_num):
   #find the programme which fits this partition
   for iter2 in range(program_num):
    judge = Need[iter2]<= temp_IS[iter1] and unfinished[iter2] == 0 
    if judge :
       index = iter2 #index for programme 
       answer_allocation.pop(iter1)#remove the original value
       answer_allocation.insert(iter1,Name[index]) 
       d_value = Need[index] - temp_IS[iter1]
       if d_value >0:
          answer_allocation.insert(iter1+1,d_vale)#put it behind the programme  
       unfinished[index] = 1  
       print 'Programme',index,'Finished\n'
  end = program_num - sum(unfinished)
 print answer_allocation
 return answer_allocation

FirstFit();

#def NextFit():


#def BestFit():


#def WorstFit():



