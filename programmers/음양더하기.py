def solution(absolutes, signs):
    answer = 123456789
    for i in range(len(absolutes)):
        if not signs[i]:
            absolutes[i] = absolutes[i] * -1
    
    return sum(absolutes)