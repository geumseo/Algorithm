def solution(progresses, speeds):
    day_list = []
    answer = []
    cnt = 0
    
    for i in range(len(progresses)):
        day = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            day = day + 1
        day_list.append(day)

    max = day_list[0]
    for d in day_list:
        if max >= d:
            cnt += 1
        else:
            answer.append(cnt)
            max = d
            cnt = 1
    answer.append(cnt)
    return answer
            
        
        
        
    
    
    
    
    
    
    
    
    
    
#     day = []
#     ans = []
#     count = 0
    
#     for pro, sp in zip(progresses, speeds):
#         cnt = 0
#         while(True):
#             pro += sp
#             cnt += 1
#             if pro >= 100:
#                 break
#         day.append(cnt)
        
#     Max = day[0]
    
#     for i in day:
#         if i <= Max:
#             count += 1
#         else:
#             ans.append(count)
#             Max = i
#             count = 1
#     ans.append(count)
    
#     return ans
            
            
        