#Process Deadlock: DL
#Chen Xinlei
#2017/5/26
#Python 2.7 64bit

import math
import numpy as np

def DeadLock():
    #vectors known
    Resource = [10,5,7]  #all resources sums up
    Max = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
    Allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
    Need = [[7,4,3],[1,2,2],[6,0,0],[0,1,1],[4,3,1]]
    Avaiable = [] #need to be set
    #answer vector
    Work = []  #
    Need = []
    Allo = []
    Work_Allo = []
    





