import random
from myTool import makeRandomList

def partition(li, l, r):
    tmp = li[l]
    while l < r:
        while l < r and li[r] >= tmp:
            r = r - 1
        li[l] = li[r]
        while l < r and li[l] <= tmp:
            l = l + 1
        li[r] = li[l]
    li[l] = tmp
    return l

def quickSort(li,left,right):
    if left < right:
        mid = partition(li,left,right)
        quickSort(li,left,mid-1)
        quickSort(li,mid+1,right)

checkList = [5,7,4,6,3,1,2,9,8]

randomlist = [i for i in range(100)]
random.shuffle(randomlist)
#print(randomlist)


# listTry = []
# makeRandomList(listTry,100,2000)
# print(listTry)
# quickSort(listTry,0,len(listTry)-1)
# print(listTry)

#partition(checkList,0,len(checkList)-1)
# quickSort(randomlist,0,len(randomlist)-1)
# print(randomlist)

a = "11"
b = "1"

print(bin(int(a,2) + int(b,2))[2:])




