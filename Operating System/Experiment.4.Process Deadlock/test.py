#test file
#test for 2 dem vector:passed 
maxnum = 10 
v = [4,5,6]
matrix = []

for i in range(3): #add new vector
   matrix.append(v);

for i  in range(3): #output
    for j in range(3):
       print matrix[i][j],'\n'    
print '-----------------------------------1'
#test 2   
#for i  in range(3): #output
#        matrix[i] = matrix[i] - [1,2,3]   
#for i  in range(3): #output
#    for j in range(3):
#       print matrix[i][j],'\n' 

#print 'vector of 2d length:',len(matrix),'\n'

#print '----------------------------------'
#test 3:sum up 2 demension vector :passed
Allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
temp0 = [0,0,0]
for iter1 in range(len(Allocation)):
    temp1 = Allocation[iter1]
    for iter2 in range(3): 
       temp0[iter2] = temp0[iter2] + temp1[iter2]
print temp0,'\n'
print  '----------------------------------3'
#test 4
print [x - y for x, y in zip(temp0, [5,5,5])]  #return the value vector of "a - b"
print  '----------------------------------4'
#test 5:
test5 = [4,3,2,1,0]
for iter in test5:
    print Allocation[iter],'\n'
print  '----------------------------------5'
#test 6:
Allocation.pop(2) #remove the third vector in Allocation
print Allocation,'\n'
print  '----------------------------------6'
#test 7:
Need = [[7,4,3],[1,2,2],[6,0,0],[0,1,1],[4,3,1]]
for iter in range(5):
    for iter1 in range(3):
      print Need[iter][iter1],'\n'
print  '----------------------------------7'