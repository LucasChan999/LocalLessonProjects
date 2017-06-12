#Disk Scheduling:Scan
#Chen Xinlei
#2017/6/9
#Python 2.7 64bit
import numpy as np
def Scan_beta():
 #input
 disk_n = 3
 disk_m = 100 #disk start point
 track_order = [78,30,9,15,102,140,156,54,45,127]
 #move_direction = 0 #only useful in Scan,CScan
 #temp
 temp_order = [] #running order 
 track_order_sorted = sorted(track_order)
 temp_order_1 = []
 temp_order_2 = []
 #output
 move_distance = []
 average_distance = float(0)
 
 times = len(track_order)
 #divide the track_order_sorted 
 index_divide = 0
 position_now = disk_m
 print 'track_order_sorted:',track_order_sorted
 for iter in range(times):
      if track_order_sorted[iter] >= position_now:
         index_divide = iter
         break
 print 'index_divide',index_divide
 for iter in range(index_divide,times):
      temp_order_1.append(track_order_sorted[iter])
 for iter in range(index_divide):
      temp_order_2.append(track_order_sorted[iter])
 temp_order_3 = []
 for iter in reversed(temp_order_2):
     temp_order_3.append(iter)
 print temp_order_3
 temp_order = temp_order_1 + temp_order_3
 print 'test len(track_order)',len(track_order)
 print 'temp_order:',temp_order
 for iter in range(times):
     if iter == 0:
        position_now = disk_m
     else:
        position_now = temp_order[iter-1]
     position_next = temp_order[iter]
     move_dis = abs(position_now - position_next)
     move_distance.append(move_dis)
     print 'From',position_now,' to',position_next
     print 'Move Distance;',move_dis
     print '-----------------------------------'
 average_distance = round(np.mean(move_distance),2)
 print 'Average Distance:',average_distance

Scan_beta()
 








