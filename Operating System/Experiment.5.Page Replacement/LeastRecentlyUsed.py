#Page Replacement:LRU 
#Chen Xinlei
#2017/6/2
#Python 2.7 64bit

def LRU():
 #input 
 block_num = 3
 PageNum = 7
 PageOrder = [4,3,2,1,4,3,5,4,3,2,1,5,6,2,3,7,1,2,6,1]  
 #local
 block = [] #store the page in physical block
 block_ru = [] #store the ru page
 block_ru_index = 0 #store the ru page's index
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
     print 'Page not found in Block'
     LackNum = LackNum + 1
     if len(block) < block_num:
           block.append(PageOrder[iter1])
           block_ru.append(PageOrder[iter1]) 
           
     else:
           #find the LRU page in block and refresh the block_ru
           replace_page = block_ru[0]
           index = 0
           for iter in range(block_num):
               if block[iter] ==  replace_page:
                  index =  iter
           block[index] = PageOrder[iter1]
           block_ru.pop(0) 
           block_ru.append(PageOrder[iter1])
  else:
     print 'Page Found in Block'
     for iter in range(len(block_ru)):
         if block_ru[iter] == PageOrder[iter1]:
            block_ru_index = iter
     #make the block_ru[0] -> LRU page
     block_ru.pop(block_ru_index)
     block_ru.append(PageOrder[iter1])
  print 'Block',block 
  print '------------------------------------'   
 LackPageRate = round(float(LackNum)/float(len(PageOrder)),2)  
 print 'LackNum:',LackNum,'\nLackPageRate:',LackPageRate    

LRU();