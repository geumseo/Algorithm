def solution(array, commands):
    answer = []
    
    for i in commands:
        slice_array = array[i[0]-1:i[1]]
        slice_array.sort()
        answer.append(slice_array[i[2]-1])
        
    return answer
        
        
        










# def solution(array, commands):
#     answer = []
#     for i in range(len(commands)):
#         new_arr = array[commands[i][0]-1:commands[i][1]]
#         new_arr.sort()
#         answer.append(new_arr[commands[i][2]-1])
#     return answer