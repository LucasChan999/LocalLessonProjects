#Page Replacement:FIFO
#Chen Xinlei
#2017/6/2
#Python 2.7 64bit




def FIFO_beta():
 #input 
 m = 3
 PageNum = 7
 PageOrder = [4,3,2,1,4,3,5,4,3,2,1,5,6,2,3,7,1,2,6,1]  
 #local
 temp_PO = []
 finished = []
 #output
 LackNum = 0
 LackPageRate = round(0,2)
 
 for iter in range(len(PageOrder)):
    temp_PO.append(PageOrder[iter]);
 for iter in range(PageNum):
    finished.append(0)
 

 
 