# def hanoi(n, a, b, c):
#     if n > 0:
#
#         hanoi(n - 1, a, c, b)
#         print('from %s move to %s' % (a,c))
#         hanoi(n - 1, b, a, c)
#
# # hanoi(3, 'a', 'b', 'c')
#
# def liebao(li ,val):
#     for i, v in enumerate(li):
#         if v == val :
#             return i;
#         else:
#             return None;

def BinarySearch(li, val):
    left = 0
    right = len(li)
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            print('found\r\n')
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

hi = [1,2,3,4,5.1,6,7,8]
num = 4

result = BinarySearch(hi, num)
print("index={0}, num={1}".format(result, hi[result]))
hi=hi[2:]+hi[0:2]
hi=[4,5,6,7,0,1,2]
print(hi)
left = 0
right = len(hi)-1
mid = -1
while mid != (left + right+1) // 2:
        mid = (left + right+1) // 2
        if hi[left]>hi[mid]:
            right = mid
        elif hi[right]<hi[mid]:
            left = mid

print("k",mid)
k = mid
left = k - len(hi)
right = k - 1
val=0
mid = 0.1
while mid != (left + right + 1) // 2:
    mid = (left + right + 1) // 2
    print(left, mid, right)
    if hi[mid] == val:
            print('found\r\n')
            print(mid)
            print(hi[mid])
            break
    elif hi[mid] > val:
        right = mid
    elif hi[mid] < val:
        left = mid
print(-0.1)





