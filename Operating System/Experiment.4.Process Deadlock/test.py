#test for 2 dem vector:passed 
maxnum = 10 
v = [4,5,6]
matrix = []

for i in range(3): #add new vector
   matrix.append(v);

for i  in range(3): #output
    for j in range(3):
       print matrix[i][j],'\n'    
print '--------------------------------'
#test 2 
for i  in range(3): #output
        matrix[i] = matrix[i] - [1,2,3]
for i  in range(3): #output
    for j in range(3):
       print matrix[i][j],'\n' 