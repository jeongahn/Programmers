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