def solution(arr):
    answer = [arr[0]]
    #answer.append(arr[0])
    
    for i in range(1,len(arr)) :
        if arr[i] != arr[i-1] :
            answer.append(arr[i])
                          
    #if answer[len(answer)-1] != arr[len(arr)-1] : answer.append(arr[len(arr)-1])                                
    return answer