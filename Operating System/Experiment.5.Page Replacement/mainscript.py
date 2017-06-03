#Page Replacement:main
#Chen Xinlei
#2017/6/3
#Python 2.7 64bit

determination = 1
while determination:
 selection = input('Please choose algorithm:\n1-FIFO 2-OPI 3-LRU\n')
 if selection == 1:
    import FirstInFirstOut as FIFO
    FIFO.FIFO()
 else:
  if selection == 2:
    import Optional as OPI 
    OPI.OPI()
  else:  
    if selection == 3:
      import LeastRecentlyUsed as LRU 
      LRU.LRU()
    else:
      temp = input("Please the right number!\n1-FIFO 2-OPI 3-LRU\n")
 determination = input("1->Go on\n0->Exit\n")

