from myTool import makeRandomList

def sift(li, low, high):
    """
    :param li: 列表
    :param low:堆的第一个元素的下标（堆顶）
    :param high:堆的最后一个元素下标
    :return:
    """
    i = low
    j = 2 * i + 1 #左边叶子
    temp = li[low] #i? 存堆顶
    while j <= high: #i为最后一层时跳出循环
        if j+1 <= high and li[j] < li[j + 1]:
            j = j + 1 #指向右边
        if li[j] > temp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = temp
            break
    li[i] = temp

def heapSortLearn(li):
    n = len(li)
    for a in range((n-2)//2,-1,-1):
        sift(li, a, n-1)
    for a in range((n-1),-1,-1):
        li[a], li[0] = li[0], li[a]
        sift(li, 0, a-1)

testLi = []
makeRandomList(testLi,10,20)
print(testLi)
heapSortLearn(testLi)
print(testLi)




