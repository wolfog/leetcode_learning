'''
@Author: rudy
@Date: 2020-06-01 16:11:36
@LastEditTime: 2020-06-01 17:26:59
@Description: 使用队列实现栈
'''
from  collections import deque
import time

class MyStack:
    def __init__(self):
        super().__init__()
        self.deque = deque()

    def push(self,elem):
        self.deque.append(elem)

    def pop(self):
        assert self.deque ,'栈为空，请添加元素后在pop'
        return self.deque.pop()

    def top(self):
        assert self.deque , '栈为空，请添加元素后在top' 
        return self.deque[-1]

    def empty(self):
        return False if self.deque else True

if __name__ == "__main__":
    start = time.time()
    obj = MyStack()
    obj.push(2)
    obj.push(2)
    param_3 = obj.top()
    param_2 = obj.pop()
    param_4 = obj.empty()
    print(param_2)
    print(param_3)
    print(param_4)
    print(time.time()-start)
