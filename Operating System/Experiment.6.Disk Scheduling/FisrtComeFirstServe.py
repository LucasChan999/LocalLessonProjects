#Disk Scheduling:FCFS
#Chen Xinlei
#2017/6/9
#Python 2.7 64bit

import numpy as np
def FCFS():
 #input
 disk_n = 3
 disk_m = 100 #disk start point
 track_order = [78,30,9,15,102,140,156,54,45,127]
 #move_direction = 0 #only useful in Scan,CScan
 #temp
 temp_order = [] #running order 
 #output
 move_distance = []
 average_distance = float(0)
  
 times = len(track_order)
 for iter in range(times):
  move_dis = 0
  if iter == 0:
     temp_order.append(track_order[iter])
     move_dis = abs(disk_m - track_order[iter])
     move_distance.append(move_dis)
     print 'From',disk_m,' to',track_order[iter]
     print 'Move Distance;',move_dis
     print '-----------------------------------'
  else:
     temp_order.append(track_order[iter])
     move_dis = abs(temp_order[iter] - temp_order[iter - 1])
     move_distance.append(move_dis)
     print 'From',temp_order[iter-1],' to',temp_order[iter]
     print 'Move Distance;',move_dis
     print '-----------------------------------'
 average_distance = round(np.mean(move_distance),2)
 print 'Average Distance:',average_distance
 
FCFS()