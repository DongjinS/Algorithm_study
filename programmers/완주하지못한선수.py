def solution(participant, completion):
    from collections import defaultdict
    answer = ''
    
    complete_dict = defaultdict(int)
    for name in completion:
        complete_dict[name] += 1
    
    for name in participant:
        if complete_dict[name] >= 1:
            complete_dict[name] -= 1
        elif complete_dict[name] == 0:
            answer = name
    return answer

