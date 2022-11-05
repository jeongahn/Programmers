def solution(babbling):
    answer = 0
    
    possible = ["aya", "ye", "woo", "ma"]
    possible_cant = ["ayaaya", "yeye", "woowoo", "mama"]
    
    for i in babbling:
        if "ayaaya" in i or "yeye" in i or "woowoo" in i or "mama" in i:
            continue
        if len(i.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", "")) == 0:
            answer += 1
    return answer