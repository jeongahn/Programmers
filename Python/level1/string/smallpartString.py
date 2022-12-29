def solution(t, p):
    answer = 0
    
    
    for i in range(0, len(t)):
        tmp = ""
        if i >= len(t) - len(p) + 1:
            break
        for j in range(i, i+len(p)):
            tmp += t[j]
        if int(tmp) <= int(p):
            answer += 1
    
        
    
    return answer