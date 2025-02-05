def solution(array, commands):
    answer = []
    for i in commands:
        slice_array = array[i[0]-1:i[1]]
        slice_array.sort()
        answer.append(slice_array[i[2]-1])
    return answer
