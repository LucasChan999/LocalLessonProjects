#Process Synchronization:Producer
#Chen Xinglei
#2017/5/12
#Python 2.7 64bit
import random
import main

def Producer_bate():
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
      nextp = random()
      #produce a producet
      if main.empty > 0:
         if mutex == 1 :
              main.buffer[value_in] = nextp
              main.value_in = (main.value_in + 1)% main.value_n
              print 'Produce',value_in,"'s product:",main.buffer(value_in),'\n'
              main.mutex = 0
              main.full = main.full + 1
 
 







