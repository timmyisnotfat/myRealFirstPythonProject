def bubbleSortlearn(li):
    for i in range(len(li) - 1):
        flag = False#
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                flag = True
        if not flag:#
            return#




# test
#
list11 = [3, 2, 1, 5, 6, 7, 4, 3, 2, 1]
checkList = []
# bubbleSortlearn(list11)
# print(list11)


from myTool import makeRandomList
def bubbleRetryOn9thJan(li):
    for i in range(len(li)- 1):
        for j in range(len(li) - i- 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

makeRandomList(checkList,10,10)

bubbleRetryOn9thJan(checkList)
print(checkList)














