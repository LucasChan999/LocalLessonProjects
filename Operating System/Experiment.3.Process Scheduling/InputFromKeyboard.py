#Job Scheduling:InputFromKeyboard
#Chen XingLei
#2017/5/5
#Python 2.7 64bit

def InputFromKeyboard():
 process_num = input('Input Process Number:')
 ArrivalTime = []
 ServiceTime = []
 for iter in range(process_num):
    ArrivalTime.append(0)
 for iter in range(process_num):
    ServiceTime.append(0)


 for iter in range(0,process_num):
    ArrivalTime[iter] = input("Process's Arrival Time:")
    ServiceTime[iter] = input("Process's Service Time:")
    print "Process",iter + 1,'AT:',ArrivalTime[iter],'ST',ServiceTime[iter],'\n'

 value_Q = input("Please input value of Q: ")
 return process_num,ArrivalTime,ServiceTime,value_Q