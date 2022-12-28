def bubble_sort(li):
    for i in range(len(li) - 1):
        mark = False
        for j in range(len(li) - i -1):
            if li[j] > li[j+1]:
                li[j] , li[j+1] = li[j+1], li[j]
                mark = True
                print(li)
    if not mark:
        return

def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


def binarySearch(li,val):
    left = 0
    right = len(li) - 1
    while left <= right :
        mid = (left + right) // 2
        if li[mid] == val:
            print(mid)
            return mid
        if val > li[mid]:
            left = mid + 1
        if val < li[mid]:
            right = mid - 1
    else:
        return left

def whileelse():
    i = 0;
    while i < 5:
        print(i)
        i += 1
    else:
        print("else")
    while i < 10:
        print(i)
        i += 1
        if i == 7:
            break
    else:
        print("else")
tesiLi = [1,3,5,6]
testVal = 2


a = binarySearch(tesiLi,testVal)
print(a)


# def InsertSort(li):
    # for i in range(1,len(li)):
# TestLi = [3,2,7,6,10,9,11,12,1,8]
# TestLi.sort(reverse=True)
# result = select_sort(TestLi)

# print(TestLi)
