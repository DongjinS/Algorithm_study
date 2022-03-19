def solution(answers):
    answer = []
    scores = [ 0,0,0 ]
    
    supo1 = [ 1, 2, 3, 4, 5 ]
    supo2 = [ 2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == supo1[i%5]:
            scores[0]+=1
        
        if answers[i] == supo2[i%8]:
            scores[1]+=1
        
        if answers[i] == supo3[i%10]:
            scores[2]+=1
            
    max_scores = max(scores)
    for i in range(len(scores)):
        if scores[i] != 0 and scores[i] >= max_scores:
            answer.append(i+1)
            
    
    return answer