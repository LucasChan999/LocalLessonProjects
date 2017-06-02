#Job Scheduling:InputFromKeyboard
#Chen XingLei
#2017/5/5
#Python 2.7 64bit

def InputFromKeyboard():
 #process_num = input('Input Process Number:')
 #ArrivalTime = []
 #ServiceTime = []
 #for iter in range(process_num):
 #   ArrivalTime.append(0)
 #for iter in range(process_num):
 #   ServiceTime.append(0)

 #for iter in range(0,process_num):
 #   ArrivalTime[iter] = input("Process's Arrival Time:")
 #   ServiceTime[iter] = input("Process's Service Time:")
 #   print "Process",iter + 1,'AT:',ArrivalTime[iter],'ST',ServiceTime[iter],'\n'

 ##selection = input("Please choose algorithm:1->RR,2->TRRN\n")
 #value_Q = 1 #set default value in case 
 Resource = [10,5,7]

 re_index = input("Please input process number: ")
 re_index = re_index - 1
 re_vector = []
 for iter in range(len(Resource)):
   re_vector.append(input("Please input requset resource:"))
 return re_index,re_vector