def solution(array, commands):
    return [sorted(list(array[ i[0]-1 : i[1] ]))[i[2]-1] for i in commands ]