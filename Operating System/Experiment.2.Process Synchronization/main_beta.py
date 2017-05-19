#Process Synchronization:main
#Chen Xinlei
#2017/5/12
#Python 2.7 64bit

value_n = 16
value_in = 0
value_out = 0
item = []
buffer = []
full = 0
empty = value_n
mutex = 0

import Producer as p
import Customer as c
import random as ram

def Producer_beta(value_in,full):
 #value_n = 16
 #value_in = 0
 #value_out = 0
 #mutex = 0
 #full = 0
 #empy = value_n
 #buffer = []
 
 for iter in range(value_n):
    buffer.append(0)  

 while True:
      nextp = '007'
      #produce a producet
      if empty > 0:
         if mutex == 1 :
              buffer[value_in] = nextp
              value_in = (value_in + 1)% value_n
              print 'Produce',value_in,"'s product:",buffer(value_in),'\n'
              mutex = 0
              full = full + 1


def Customer_beta(value_out,empty):
 #value_n = 16
 #value_in = 0
 #value_out = 0
 #mutex = 0
 #full = 0
 #empy = value_n
 #buffer = []
 
 for iter in range(value_n):
    buffer.append(0)  

 while True:
      #produce a producet
      if full <= value_n :
         if mutex == 1 :
              nextp = buffer(value_out)
              value_out = (value_out + 1)% value_n
              print 'Custom',value_out,"'s product:",buffer(value_out),'\n'
              mutex = 0
              empty = empty + 1

for iter in range(value_n):
    buffer.append(0)

while True:
     Producer_beta(value_in,full)
     Customer_beta(value_out,empty)



