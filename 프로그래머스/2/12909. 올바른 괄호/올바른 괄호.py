def solution(s):
    data_list = []
    
    for i in range(len(s)):
        if s[i] == '(':
            data_list.append(s[i])
        else:
            if data_list == []:
                return False 
            else: 
                data_list.pop() 
            
    if data_list != []:
        return False
    
    return True













# def solution(s):
    
#     stack = []
    
#     for i in s:
#         if i == '(':
#             stack.append(i)
            
#         else:
#             if stack ==[]:
#                 return False
#             else:
#                 stack.pop()
#     if stack != []:
#         return False
    
#     return True
            