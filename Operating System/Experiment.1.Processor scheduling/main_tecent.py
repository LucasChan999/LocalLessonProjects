import sys
reload(sys)
sys.setdefaultencoding('utf8')

ad = open("ad.csv") #
app_cat = open("app_categories.csv")
pos = open("position.csv")
test = open("test.csv")
train = open("train.csv")
user = open("user.csv")
u_app_act = open("user_app_actions.csv")
u_ins_apps = open("user_installedapps.csv")

context = test.readlines()

import numpy as np
i = 1;
app_clicked = []#测试数据中已经点击过的数据
for line in context:
    line = line.replace('\n','')
    array = line.split(',')
    if array[0] == 'instanceID':
        continue
    
    app_clicked.append(array[0])

#print "----------------------------------------\n"
#app_clicked = list(set(app_clicked))
#for line in app_clicked:
#      print line

#print len(line)




test.close()

#print"-------------------"
#wf = open('submission.csv','w')
#wf.write('instanceID,prob\n')
#for i in range(1,50):   #去除第一行列名字
#    item = app_cat1[i]
#    wf.write('%s\n'%(item))
