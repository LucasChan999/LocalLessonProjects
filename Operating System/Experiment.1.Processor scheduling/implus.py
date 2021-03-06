# coding= utf-8

f = open("./data.csv")
context = f.readlines()

#选取线下训练和线上评估的对象#

import numpy as np

train_day29 = []
offline_candidate_day30 = []
online_candidate_31 = []

for line in context:
    lien = line.replace('\n','')
    array = line.split(',')
    if array[0] == 'user_id':
        continue
    day = int(array[-1])
    uid = (array[0],array[1],day+1)
    if day ==28:
        train_day29.append(uid)
    if day == 29:
        offline_candidate_day30.append(uid)
    if day == 30:
        online_candidate_31.append(uid)

train_day29 = list(set(train_day29)) #使用set去除重复的对象
offline_candidate_day30 = list(set(offline_candidate_day30))
online_candidate_31 = list(set(online_candidate_31))

print 'training item number:\t',len(train_day29)
print '-----------------------\n'
print 'offline candidate item number :\t',len(offline_candidate_day30)
print '-----------------------\n'

#第二部分
import math
ui_dict = [{} for i in range(4)]
for line in context:
    line  = lien.replace('\n','')
    array = line.split(',')
    if array[0] == 'user_id':
        continue
    day = int(array[-1])
    uid = (array[0],array[1],day)
    type = int(array[2]) - 1
    if uid in ui_dict[type]:
        ui_dict[type][uid] += 1
    else:
        ui_dict[type][uid]  = 1

ui_buy = {}
for line in context:
    line = line.replace('\n','')
    array = line.split(',')
    if array[0] == 'usr_id':
        continue
    uid = (array[0],array[1],int(array[-1]))

    if array[2] == '4':
        ui_buy[uid] = 1

#get train x y
X = np.zeros((len(train_day29),4))
y = np.zeros((len(train_day29)))
id = 0
for uid in train_day29:
    last_uid = (uid[0],uid[1],uid[2] - i)
    for i in range(4):
        X[id][i] = math.log1p(ui_dict[i][last_uid] if last_uid in ui_dict[i] else 0)
    y[id]  = 1 if uid in ui_buy else 0
    id += 1
print 'X = ',X,'\n\n','y =',y
print '------------------\n\n'
print 'train nbumber = ',len(y),'positibve number = ',sum(y),'\n'

###get predict
pX = np.zeros((len(offline_candidate_day30),4))
id = 0
for uid in  offline_candidate_day30:
    last_uid = (uid[0],uid[1],uid[2] - 1)
    for i in range(4):
        pX[id][i] = math.log1p(ui_dict[i][last_uid] if last_uid in  ui_dict else 0)
    id += 1


####training
from sklearn.linear_model import  LogisticRegression
model = LogisticRegression()
model.fit(X,y)


#评估预测ecalute
py = model.predict_proba(pX)
npy = []
for a in py:
    npy.append(a[1])
py = npy

print 'pX = '
print pX

###combine
lx = zip(offline_candidate_day30,py)
print '---------------------\n'
lx = sorted(lx,key=lambda  x:x[1],reverse = True)
print '---------------------\n'

wf = open('ans.csv','w')
wf.write('usr_id,item_id\n')
for i in range(437):
    item = lx[i]
    wf.write('%s,%s\n'%(item[0][0],item[0][1]))