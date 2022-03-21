def solution(clothes):
    from collections import defaultdict
    answer = 1
    cloth_dict = defaultdict(list)
    for cloth, category in clothes:
        cloth_dict[category].append(cloth)
    
    for category in cloth_dict:
        answer *= len(cloth_dict[category])+1
    
    return answer-1