# programmers level1 햄버거 만들기
# stack으로 계속 재료들을 push하고 1,2,3,1 의 조건이 만족되면
# 개수를 count하고 그 재료들을 pop 해준다

def solution(ingredient):
    answer = 0
    cnt = 0
    
    stack = []
    
    for i in ingredient:
        stack.append(i)
        
        if len(stack) >= 4:
            bread2 = stack[len(stack) - 1]
            meet = stack[len(stack) - 2]
            veg = stack[len(stack) - 3]
            bread1 = stack[len(stack) - 4]
            
            if(bread2 == 1 and meet == 3 and veg == 2 and bread1 == 1):
                cnt+=1
                
                for i in range(0,4):
                    stack.pop()
            
    answer = cnt
    return answer