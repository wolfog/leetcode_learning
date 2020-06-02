'''
@Author: rudy
@Date: 2020-06-01 17:24:52
@LastEditTime: 2020-06-02 09:27:32
@Description:  给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    有效字符串需满足：
        1. 左括号必须用相同类型的右括号闭合。
        2. 左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。

@viewpoint: :使用栈实现，如果遇见小，中，大括号的结尾括号，就判断栈顶是否是对应的开始括号。如果是则出栈，否则直接结束。
'''

class Lawful_brack:
    def isValid(self,s:str) -> bool:
        temp_stack  = []
        brackets_dict = {')':'(',']':'[','}':'{'}
        for item in s:
            # 列表为空，添加元素
            if not temp_stack:
                temp_stack.append(item)
            else:
                if item in brackets_dict.keys() and temp_stack[-1] == brackets_dict[item] :
                    temp_stack.pop(-1)
                elif item in brackets_dict.keys() and temp_stack[-1] != brackets_dict[item]:
                    return False
                else:
                    temp_stack.append(item)
        return temp_stack==[]


if __name__ == "__main__":
    lb = Lawful_brack()
    print(lb.isValid(''))
    print(lb.isValid('()'))



