# a = 222
# a = str(a)

# print(a[1])
# print(len(a))

'''
classTry
'''

class Girl():
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height

Hemiao = Girl("maomi",24,5.6)

# print(Hemiao.name)
# print(Hemiao.age)

class fruit():
    def __init__(self, size, number):
        self.s = size
        self.n = number

apple = fruit("big", 1)
print(apple.s)


class signal():
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def hemiao(self):
        a = self.s1
        b = self.s2
        return a+b
    def maomi(self):
        return a
s = signal(1, 2)

test = s.maomi()
print(test)







