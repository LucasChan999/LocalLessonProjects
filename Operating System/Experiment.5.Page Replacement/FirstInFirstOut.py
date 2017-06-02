#Page Replacement:FIFO
#Chen Xinlei
#2017/6/2
#Python 2.7 64bit
import numpy as np

def FIFO():
 #input 
 block_num = 3
 PageNum = 7
 PageOrder = [4,3,2,1,4,3,5,4,3,2,1,5,6,2,3,7,1,2,6,1]  
 #local
 block = [] #store the page in physical block
 block_time = [] #store the read-in time of page stroed in block
 #block_time_D = [] #d-value between the read-in time and time now
 temp_PO = []
 #finished = []
 #output
 LackNum = 0
 LackPageRate = round(0,2)
 
 for iter in range(len(PageOrder)):
    temp_PO.append(PageOrder[iter]);
 #for iter in range(PageNum):
 #   finished.append(0)
  
 for iter1 in range(len(PageOrder)):
  #to to find the local page
    judge = False
    for iter2 in range(len(block)):#try to find the fit page
        if PageOrder[iter1] == block[iter2]:
           judge = True
    print 'Page Now:',PageOrder[iter1]
    print 'Block Time before Replace:',block_time
    if not judge :#not found
        print 'Page not found'
        LackNum = LackNum + 1
        if len(block) < block_num:
           block.append(PageOrder[iter1])
           #block_time[len(block) - 1] = iter1
           block_time.append(iter1)
           print 'len of block:',len(block),'len of time',len(block_time)
        #find the earlist page so far 
        else:
         #refresh the block_time_D 
         block_time_D = []
         for iter in range(block_num):
             block_time_D.append(iter1 - block_time[iter])
         earliest = max(block_time_D) #compare d-value between the read-in time and time now  !!!
         index = 0 #index need to be raplaced 
         for iter in range(len(block_time_D)):
            if earliest == block_time_D[iter]:
               index = iter
         block[index] = PageOrder[iter1] #replace the page of index 
         block_time[index] = iter1 #time changes 
    else:
        print 'Page Found'
    print 'Block Time:',block_time
    print 'Time',iter1,' page needed',PageOrder[iter1],':',block
    print '--------------------------------------' 
 LackPageRate = round(float(LackNum)/float(len(PageOrder)),2)  
 print 'LackNum:',LackNum,'\nLackPageRate:',LackPageRate     
FIFO();
 
    
 

 
 