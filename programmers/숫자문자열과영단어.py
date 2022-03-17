from collections import defaultdict
def solution(s):
    answer = ''
    num_dict = defaultdict(str)
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        num_dict[num[i]] = str(i)
        
    # print(num_dict)
    tmp = ''
    for c in s:
        if c.isdigit():
            answer+=c
        else:
            tmp += c
            if tmp in num:
                answer+=num_dict[tmp]
                tmp = '' 
    
    return int(answer)