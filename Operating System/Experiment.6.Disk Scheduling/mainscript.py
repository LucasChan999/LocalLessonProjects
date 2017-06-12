#Disk Scheduling:main
#Chen Xinlei
#2017/6/9
#Python 2.7 64bit

determination = 1
while determination:
 selection = input('Please choose an Algorithm:\n1-FCFS,2-SSTF,3-SCAN,4-CSCAN\n')
 if selection == 1:
   import FisrtComeFirstServe as FCFS
   FCFS.FCFS()
 if selection == 2:
   import ShortestSearchTimeFirst as SSTF 
   SSTF.SSTF_beta()
 if selection == 3:
   import Scan as SC
   SC.Scan_beta()
 if selection == 4:
   import CScan as CS
   CS.CSCAN()
 determination = input("End input 0\nGoOn input 1\n")