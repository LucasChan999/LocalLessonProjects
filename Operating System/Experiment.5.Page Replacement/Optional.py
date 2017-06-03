#Page Replacement:OPI
#Chen Xinlei
#2017/6/2
#Python 2.7 64bit

import numpy as np 

def OPI():
 #input 
 block_num = 3
 PageNum = 7
 PageOrder = [4,3,2,1,4,3,5,4,3,2,1,5,6,2,3,7,1,2,6,1]  
 #local
 block = [] #store the page in physical block
 #block_time = []
 
 #output
 LackNum = 0
 LackPageRate = float(0)
 
 for iter1 in range(len(PageOrder)):
  print 'Read Page:',PageOrder[iter1]
  judge = False
  for iter2 in range(len(block)):#try to find the fit page
      if PageOrder[iter1] == block[iter2]:
         judge = True
  if not judge :#not found
        print 'Page not found'
        LackNum = LackNum + 1
        if len(block) < block_num:
           block.append(PageOrder[iter1])
           print 'len of block:',len(block)
           #block_time.append(iter1)
        else:
           #find the farest uesd block[page] 
           index = 0
           use_future = []
           use_index = []
           use_found = False 
           for iter3 in range(iter1,len(PageOrder)):
               for iter4 in range(len(block)):
                   no_repeat = True
                   temp = []
                   for iter in use_future:
                       temp.append(PageOrder[iter])
                   no_repeat = PageOrder[iter3] not in temp 
                   check_equal = True
                   check_equal = PageOrder[iter3] == block[iter4] 
                   if check_equal and no_repeat:                  
                      use_future.append(iter3)
                      use_index.append(iter4)
                      use_found = True
                        
           if use_found:
                   print 'Use Found'
                   print 'Block',block
                   print 'use_future',use_future
                   print 'use_index',use_index
                   if len(use_future) == block_num:
                      temp = 0
                      temp = max(use_future)
                      for iter in range(len(use_future)):
                          if temp == use_future[iter]:
                             index = use_index[iter]
                      #print 'use_future',use_future
                   else :
                      print 'len(use_future) != block_num'
                      #find the page which is in block now but does not appear any more
                      temp1 = []
                      for iter in use_future:
                          temp1.append(PageOrder[iter])
                      for iter in block:
                          if iter not in temp1:
                             value = iter
                      for iter in range(block_num):
                          if block[iter] == value:
                             index = iter
           else:
               #none of the pages in block were found in the PageOrder[left]
               print 'Use not found'
               index = 0 #first page in block
           print 'test iter1:',iter1,'index',index
           block[index] = PageOrder[iter1] #replace the page of index 
  else:
        print 'Page Found'
  print 'Time',iter1,' page needed',PageOrder[iter1],':',block
  print '--------------------------------------'
 LackPageRate = round(float(LackNum)/float(len(PageOrder)),2)   
 print 'LackNum:',LackNum,'\nLackPageRate:',LackPageRate     
 
OPI()