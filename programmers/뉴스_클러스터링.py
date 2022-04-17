def solution(str1, str2):
    answer = 0
    first = set()
    second = set()

    str1 = list(filter(lambda x: x.isalpha(), str1))
    str2 = list(filter(lambda x: x.isalpha(), str2))

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            first.add(str1[i].lower()+str1[i+1].lower())
    
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            second.add(str2[i].lower()+str2[i+1].lower())
    
    # print(first, second)

    inter = first.intersection(second)
    union = first.union(second)

    print(inter, union)

    answer = int((len(inter)/len(union)) * 65536)
    print(answer)

    return answer

solution("FRANCE", "french")
solution("handshake", "shake hands")
solution("aa1+aa2",	"AAAA12")
solution("E=M*C^2",	"e=m*c^2")