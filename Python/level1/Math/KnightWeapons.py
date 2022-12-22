#약수의 개수를 효율적으로 구하는 방법
#1. 1부터 해당 숫자까지 for문을 수행하는 것이 아니라 그 수의 제곱근까지만 수행
#2. 제곱근은 +1, 그 이외에는 +2씩(짝을 이루기 때문에)
#주의 할점은 range 설정시 최대 범위 +1 해줘야 된다..


def solution(number, limit, power):
    answer = 0
    result = 0
    for i in range(1, number+1):
        tmp = i
        cnt = 0
        for j in range(1, int((i**0.5)) + 1):
            if i % j == 0:
                if i // j == j:
                    cnt += 1
                else:
                    cnt += 2
        
        if cnt > limit:
            cnt = power
        
        result += cnt
    answer = result
            
    return answer