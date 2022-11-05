def solution(a, b, n):
    answer = 0
    cnt = 0
    tmp = 0
    while(True):
        if n % a == 0:
            cnt += (n // a) * b # b 즉 돌려주는 병의 값을 고려
            n = (n // a) * b
            tmp = 0 # 초기화를 해주어야 한다
            
        elif n % a != 0:
            cnt += (n // a) * b
            tmp = (n % a)
            n = (n // a) * b
        
        n = n + tmp
        
        if n < a:
            break
    
    answer = cnt
    return answer