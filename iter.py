"""
1.迭代器协议：迭代器协议是指：对象必须提供一个next方法，要么返回迭代的下一项，要么跑出stopIteration异常终止迭代。
2.可迭代对象：实现了__iter__的对象
3.协议是一种约定
"""

# 自定义满足迭代器协议对象
class Iter(object):

    def __init__(self, num):
        self.m_End = num
        self.m_Start = 0

    def __iter__(self):
        return Iteration(self.m_End)

class Iteration(object):

    def __init__(self, num):
        self.m_Start = 0
        self.m_End = num

    def __next__(self):
        if self.m_Start < self.m_End:
            result = self.m_Start
            self.m_Start += 1
            return result
        else:
            raise StopIteration

# 生成器，可以理解为自动实现了迭代器协议的数据类型，生成器是可迭代对象
#1.生成器函数

def TestGenerator(n):

    for i in range(n):
        yield(i)
        print("is")
    print("end")

#2.生成器表达式，类似于列表推导，但是返回的是生成器对象，并没有存储值

TestGenerator2 = ("表达式：%s" % i for i in range(10))

if __name__ == "__main__":
     
    for i in Iter(10):
        print(i)

    for i in TestGenerator(10):
        print(i)

    for i in TestGenerator2:
        print(i)