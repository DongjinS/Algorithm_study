def solution(brown, yellow):
    answer = []
    brown_candidate = 0
    i = 1
    while brown != brown_candidate:
        if yellow%(i) == 0:
            answer = [yellow//(i)+2,i+2]
            brown_candidate = answer[0]*2 + (answer[1]-2)*2
        i+=1       
        
    answer.sort(reverse = True)
    return answer