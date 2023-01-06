import random

def makeRandomList(realRandomList,geshu,fanwei):
    #随机生成整数的一维数组（确定数字个数和范围）
    for i in range(geshu):
        randomNum = random.randint(0,fanwei)
        realRandomList.append(randomNum)