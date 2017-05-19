#Process Synchronization:main
#Chen Xinlei
#2017/5/12
#Python 2.7 64bit

value_n = 16
value_in = 0
value_out = 0
mutex = 0
item = []
buffer = []
full = 0
empty = value_n

import Producer as p
import Customer as c
import main
import random as ran

def Producer_beta():
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
      nextp = ran.random()
      #produce a producet
      if main.empty > 0:
         if main.mutex == 1 :
              main.buffer[value_in] = nextp
              main.value_in = (main.value_in + 1)% main.value_n
              print 'Produce',value_in,"'s product:",main.buffer(value_in),'\n'
              main.mutex = 0
              main.full = main.full + 1


def Customer_beta():
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
         if main.mutex == 1 :
              main.nextp = main.buffer(value_out)
              value_out = (value_out + 1)% value_n
              print 'Custom',value_out,"'s product:",main.buffer(value_out),'\n'
              main.mutex = 0
              main.empty = main.empty + 1

for iter in range(value_n):
    buffer.append(0)

while True:
     Producer_beta()
     Customer_beta()



