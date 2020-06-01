'''
@Author: rudy
@Date: 2020-05-29 09:49:26
@LastEditTime: 2020-06-01 15:38:23
@Description: 设计一个支持push ,pop ,top,最重要的是可以常数时间内返回最小值的栈。
@analysis:
1. 我之前有个错误想法：就是每次存入的时候，就将栈重新排序，虽然浪费时间，但是至少可以满足常数时间内返回最小栈，但是这里有个巨大的bug,
就是丧失了栈的本质，后进入的元素在栈顶。准确的来说，常数时间内返回最小元素的栈（什么是栈：先入后出，且是一个连续的内存块）

@thinking: 算法里面有一句话，叫做以时间换空间，以空间换时间。想要求得一个无序集合的最小元素，至少也应该遍历一遍,所以至少是O(n)，这里需要常数
时间，所以只能采用以空间换时间，引出辅助栈。
'''

class  CTStack:
    def __init__(self):
        super().__init__()
        self.list_data = []
        self.list_supp = []
    
    def push(self,elem):
        #  or 前面为正，后面就不再判断。列表为空，转化成boolean 就是fulse
        self.list_data.append(elem)
        if not self.list_supp or elem <= self.list_supp[-1] :
            self.list_supp.append(elem)

    def pop(self):
        assert self.list_data ,"栈为空，没法弹出元素"
        last_element  =  self.list_data.pop(-1)
        if last_element <= self.list_supp[-1]:
            self.list_supp.pop(-1)

    def top(self):
        # 获取栈顶元素，如果没有就报异常。
        assert self.list_data,"空栈没有栈顶元素"
        return self.list_data[-1]

    def getMin(self):
        # self.supp 为空，就报异常（或者说只要True，才会执行下边的话）
        assert self.list_supp ,'空栈没有最小值'
        return self.list_supp[-1]

if __name__ == "__main__":
    ctstack = CTStack()
    ctstack.push(-2)
    ctstack.push(0)
    ctstack.push(-3)
    print("当前最小值{}".format(ctstack.getMin()))
    ctstack.pop()
    print("当前栈顶元素为{}".format(ctstack.top()))
    print("当前最小值{}".format(ctstack.getMin()))
    
