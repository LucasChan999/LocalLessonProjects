#Process Synchronization:Customer
#Chen Xinglei
#2017/5/12
#Python 2.7 64bit
import random
import main

def Customer_bate():
 #value_n = 16
 #value_in = 0
 #value_out = 0
 #mutex = 0
 #full = 0
 #empy = value_n
 #buffer = []
 
 for iter in range(value_n):
    main.buffer.append(0)  

 while True:
      #produce a producet
      if main.full <= value_n :
         if mutex == 1 :
              main.nextp = main.buffer(value_out)
              value_out = (value_out + 1)% value_n
              print 'Custom',value_out,"'s product:",main.buffer(value_out),'\n'
              main.mutex = 0
              main.empty = main.empty + 1
 
 







