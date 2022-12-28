from math import exp,log,sqrt
import re
from datetime import date,time,datetime,timedelta
from operator import itemgetter
import sys

# 读取单个文本文件
# sys.argv列表获取了要读取的文件的路径名
input_file=sys.argv[1]
#print('Output:')
# 创建filereader文件对象,‘r’只读模式

try:
    filereader = open(input_file, 'r')
    # print(filereader.read())
    board = []
    for row in filereader:
        str = list(row.rstrip().replace(',', ''))
        board.append(str)
        # print(l)
    print(board)
except:
    print('open file wrong')


# 完成逐行读取后，关闭文件对象
filereader.close()
