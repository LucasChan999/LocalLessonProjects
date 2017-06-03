#test file
#test 1:passed

internal_storage  = [16,'test1',8,32,64,32,8,16,64]

for iter in range(len(internal_storage)):
   if iter == 3: #ignore the string part in list 
     internal_storage.pop(5)
     internal_storage.insert(5,'Programme A')
   print 'Internal Storage',iter,':',internal_storage[iter],'\n'
print '-----------------------------------1'
#test 2
judge = 2>1 and  -9>-5
print judge


