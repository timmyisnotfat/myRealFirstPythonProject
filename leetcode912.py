import random
from quickSort import list1
def findmedian(li, left, right):
    l, r = random.randint(left, right), random.randint(left, right)
    a = li[left]
    c = li[right]
    mid = (left + right) // 2
    b = li[mid]
    if a > b:
        if a < c:
            li[left], li[right] = li[right], li[left]
        elif b > c:
            li[mid], li[right] = li[right], li[mid]
        else:
            pass
    else:
        if a > c:
            li[left], li[right] = li[right], li[left]
        elif b < c:
            li[mid], li[right] = li[right], li[mid]
        else:
            pass

def findmedian1(li, left, right):
    li[left], li[right] = li[right], li[left]

def partition(li, l, r):
    left = l
    right = r
    findmedian(li, left, right)
    pivot = li[right]
    right -= 1
    while True:
        while li[left] <= pivot and left < r:
            left += 1
        while li[right] >= pivot and right >=l:
            right -= 1
        if left < right:
            li[left], li[right] = li[right], li[left]
        else:
            break
    li[right+1], li[r] = pivot, li[right+1]
    return (left + right + 1) // 2

def quickSortlearn(li, left, right):
    if right - left > 0:
        p = partition(li, left, right)
        if p - left > 1:
            quickSortlearn(li, left, p - 1)
        if right - p > 1:
            quickSortlearn(li, p + 1, right)



def sortArray(nums):
        random.shuffle(nums)
        quickSortlearn(nums,0,len(nums)-1)
        return nums

sortArray(list1)
print(list1)


