from myTool import makeRandomList

class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None


def createHead(li):
    head = Node(li[0])
    for elem in li[1:]:
        node = Node(elem)
        node.next = head
        head = node
    return head

testList = []
makeRandomList(testList,10,10)
print(testList)

def creatTail(li):
    head = Node(li[0])
    tail = head
    # Why tail = Node(li[0]) do not work?
    for elem in li[1:]:
        node = Node(elem)
        tail.next = node
        tail = node
    return head



def printList(head):
    while head:
        print(head.item,end=' ')
        head = head.next

testVal = creatTail(testList)

print(testVal)