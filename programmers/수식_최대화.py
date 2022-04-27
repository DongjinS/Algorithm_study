def calc(first, second, operator):
    result = 0
    if operator == "*":
        result = first*second
    elif operator == "+":
        result= first+second
    elif operator == "-":
        result = first-second
    return result


def solution(expression):
    from collections import defaultdict
    from itertools import permutations
    answer = 0
    operator_dict = defaultdict(list)
    
    nums = ''
    split_exp = []
    j = -1
    for i in range(len(expression)):
        if expression[i] in {"*","+","-"}:
            split_exp.append(int(nums))
            j+=1
            split_exp.append(expression[i])
            j+=1
            operator_dict[expression[i]].append(j)
            nums = ''
        else:
            nums += expression[i]
            
    split_exp.append(int(nums))
            
    operator = list(operator_dict.keys())
    operator_per = list(permutations(operator,len(operator)))
    candidate = []
    
    for opers in operator_per:
        tmp = list(split_exp)
        indexs = []
        for oper in opers:
            for i in operator_dict[oper]:
                n = len(list(filter(lambda x: x<i, indexs)))*2
                result = calc(tmp[i-1-n],tmp[i+1-n],oper) 
                if len(tmp)-1>=i+2-n:
                    tmp = tmp[:i-1-n]+[result]+tmp[i+2-n:]   
                else:
                    tmp = tmp[:i-1-n]+[result]
                indexs.append(i)
                
        answer = max(abs(tmp[0]),answer)
        
    return answer