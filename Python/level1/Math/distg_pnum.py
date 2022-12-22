from itertools import combinations

def aristoSieve(size):
    aristo = [True] * (size + 1)
    aristo[0], aristo[1] = False, False
    
    for i in range(2, int(size**0.5) + 1):
        if aristo[i] == True:
            for j in range(i+i, size + 1, i):
                aristo[j] = False
    
    return aristo

def solution(nums):
    answer = 0
    
    aristo = aristoSieve(3000)
    
    arr = list(combinations(nums,3))
    
    for i in arr:
        if aristo[sum(i)]:
            answer += 1
    

    return answer