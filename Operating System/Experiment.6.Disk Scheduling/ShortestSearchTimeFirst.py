#Disk Scheduling:SSTF
#Chen Xinlei
#2017/6/9
#Python 2.7 64bit

import numpy as np
def SSTF_beta():
 #input
 disk_n = 3
 disk_m = 100 #disk start point
 track_order = [78,30,9,15,102,140,156,54,45,127]
 #move_direction = 0 #only useful in Scan,CScan
 #temp
 temp_order = [] #running order 
 disk_left = [] #disk unread
 disk_fin_statue = [] #0:unfinished 1:finished
 direction = 0
 #output
 move_distance = []
 average_distance = float(0)
 
 times = len(track_order)
 for iter in range(times):
    disk_left.append(track_order[iter])
    disk_fin_statue.append(1)

 move_direction = 0
 for iter1 in range(times):
   #find position now
   if iter1 == 0:
      position_now = disk_m
   else:
      position_now = temp_order[iter1-1]
   #find the nearest disk
   disk_left_num = len(disk_left)
   distance_min = 200
   #disk whose position is nearest to the disk now 
   position_next_index = 0
   for iter2 in range(len(disk_left)):
    if disk_fin_statue[iter2]:
      #print 'start searching',iter2,disk_left[iter2]
      subtract = abs(disk_left[iter2] - position_now)
      if distance_min > subtract:
         distance_min = subtract
         position_next = disk_left[iter2]
         position_next_index = iter2
         #print 'test1',position_next_index
      if distance_min == subtract:
         if iter1 == 0:
            continue
         else:
            direction_temp = (disk_left[iter2] - position_now)/subtract
            if direction == direction_temp:
               distance_min = subtract
               position_next = disk_left[iter2]
               position_next_index = iter2
               #print 'test3',position_next_index
            else:
               continue
   distance_min = 200
   #start move
   position = disk_left[position_next_index]
   print 'From',position_now,' to',position_next
   move_dis = abs(position_now - position_next)
   print 'Move distance',move_dis
   move_distance.append(move_dis)
   temp_order.append(position_next)
   disk_fin_statue[position_next_index] = 0 #make it cannot be read again
   if move_dis == 0:
      print 'Error'
   else:
      direction = (position_next - position_now)/move_dis
   print '-----------------------------------'     
 #end of loop iter1
 average_distance = round(np.mean(move_distance),2)
 print 'Average Distance:',average_distance          
  
SSTF_beta()            