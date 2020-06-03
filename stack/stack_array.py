'''
@Author: rudy
@Date: 2020-06-03 10:55:43
@LastEditTime: 2020-06-03 11:14:29
@Description: 给一个目标列表（严格递增）和一个整数（n>=len(目标列表)）。根据目标列表返回操作列表：
1 push,没有2，push ,pop ,3push break
'''
target = [1,3]

handle_pair = ["Push",'Pop']
return_array = []

return_array.extend(handle_pair*(target[0]-1))
return_array.append('Push')

for index in range(1,len(target)):
    handle_nums = target[index]-target[index-1]-1
    temp_handle = handle_pair*handle_nums
    temp_handle.append("Push")
    return_array.extend(temp_handle)
print(return_array)

