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
 #block_time = []
 
 #output
 LackNum = 0
 LackPageRate = float(0)
 
 for iter1 in range(len(PageOrder)):
  judge = False
  for iter2 in range(len(block)):#try to find the fit page
     if PageOrder[iter1] == block[iter2]:
         judge = True
  if not judge :#not found
     print 'Page not found'
     LackNum = LackNum + 1
  else:
     print 'Page Found'
