def solution(str1, str2):
    answer = 0
    first = list()
    second = list()

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            first.append(str1[i].lower()+str1[i+1].lower())
    
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            second.append(str2[i].lower()+str2[i+1].lower())
    
    inter = []
    uni = list(map(lambda x:x, second))

    for elem in first:
        if elem in second:
            inter.append(elem)
            second.remove(elem)
        else:
            uni.append(elem)

    j_sim = 1
    if uni:
        j_sim = float(len(inter))/len(uni)
    
    answer = int(j_sim * 65536)
    
    return answer

solution("FRANCE", "french")
solution("handshake", "shake hands")
solution("aa1+aa2",	"AAAA12")
solution("E=M*C^2",	"e=m*c^2")
solution("A+C","DEF")