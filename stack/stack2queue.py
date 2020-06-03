'''
@Author: rudy
@Date: 2020-06-03 23:01:41
@LastEditTime: 2020-06-04 00:02:08
@Description: 使用标准栈实现队列（标准栈：push ,pop,top,size,isempty())。需要强调的问题是：python里面没有栈，使用
列表（list)替代栈，但是其中的切片是万万不能使用的，否则，队列，栈都是轻轻松松实现。
'''

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        pop_ele = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return pop_ele




    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        pop_ele = self.stack2[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return pop_ele


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if self.stack1 else False

