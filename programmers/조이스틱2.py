def solution(name):
    answer = 0
    name = list(name)
    init_r = [0,1,0,["A" for x in name]]
    init_l = [0,-1,0,["A" for x in name]]
    box = [init_l, init_r]
    cnt=0
    change_num = len(list(filter(lambda x:x != 'A', name)))
    while box and change_num>0:
        container = []
        for cur in box:
            cursor = cur[0]
            if name[cursor] != cur[3][cursor]:
                cur[3][cursor] = name[cursor]
                cur[2] += min(ord(name[cursor])-ord("A"),(ord("Z")+1)-ord(name[cursor]))
                if cur[3] == name:
                    answer = cnt+cur[2]
                    return answer
                next_r = [cursor+1, 1, cur[2],list(cur[3])]
                next_l = [cursor-1, -1, cur[2],list(cur[3])]
                container.append(next_r)
                container.append(next_l)
            else:
                if cur[1]==1:
                    cur[0]+=1
                else:
                    cur[0]-=1
                container.append(cur)
        box = container
        cnt+=1    

    return answer

print(solution("BBABAAAABBBAAAABABB" ),26)
print(solution("BBAAAAAABBBAAAAAABB" ),20)
print(solution("BBBAAAAAAAB") ,8)
# print(solution("ABAAAAAAAAABB"), 7)
print(solution("BBAABB"), 8)
# print(solution("BBBAAAAABAAAAAAAAAAA" ),12)
# print(solution("BAAAAAAAAAABAAAAAABB" ),13)
# print(solution("AAABBAB") ,7)

# print(solution("AABAAAAABBB"),11)
# print(solution("LABLPAJM"),61)
# print(solution("BMOABA"),30)
# print(solution("LAABAA"),15)
# print(solution("AAAAAAAAJAAAA"),14)
# print(solution("SAAAAAARRM"),41)
print(solution("RABAMATAWADLAFAVAAE") ,"answer:78")
# print(solution("XAAAAAABA"),"/ answer:6")
# print(solution("AYOZAAVADAY"),"/ answer:35")
# print(solution("AAFEASAAVA"),"/ answer:30")
# print(solution("UAGAAASAAFAFXZA"),"/ answer:47")
# print(solution("AAAAZAATAEA"),"/ answer:19")
# print(solution("AACALATLAHABAA"),"/ answer:50")
# print(solution("FAWJAAAFV"),"/ answer:35")
# print(solution("AACAVAAPSAAOAA"),"/ answer:49")
# print(solution("AKAAWAKX"),"/ answer:33")
print(solution("LOAAAHAJAAFAEBAWO"),"/ answer:79")
# print(solution("AWAWVAQVAAA"),"/ answer:35")
# print(solution("RCETAAAAVUEAETZAAAK"),"/ answer:75")
# print(solution("GTAASKKAE"),"/ answer:52")
# print(solution("AAAABAAAAAAKSAIQ"),"/ answer:49")
# print(solution("ADASAAAUAAAPAA"),"/ answer:39")
# print(solution("AAAAADBAAELSPUAAAOA"),"/ answer:70")
# print(solution("VJAAIAFNAAAAA"),"/ answer:47")
# print(solution("AARUAUAAHTBJAAYS"),"/ answer:69")
# print(solution("IASAGITUPHE"),"/ answer:74")
# print(solution("AAALAAAAAA"),"/ answer:14")
# print(solution("AAAEASAHQAYTAAAJ"),"/ answer:60")
# print(solution("BAALEAAAPMAAAHSRAV"),"/ answer:83")
# print(solution("ASWAAATDAJAXA"),"/ answer:45")
# print(solution("DYAOAAAARQANAWA"),"/ answer:66")
# print(solution("AAIAPB")," answer:24 ")


# # input:LABLPAJM / answer:61
# # input:BMOABA / answer:30
# # input:LAABAA / answer:15
# # input:AAAAAAAAJAAAA / answer:14
# # input:SAAAAAARRM / answer:41
# # input:RABAMATAWADLAFAVAAE / answer:78
# # input:XAAAAAABA / answer:6
# # input:AYOZAAVADAY / answer:35
# # input:AAFEASAAVA / answer:30
# # input:UAGAAASAAFAFXZA / answer:47
# # input:AAAAZAATAEA / answer:19
# # input:AACALATLAHABAA / answer:50
# # input:FAWJAAAFV / answer:35
# # input:AACAVAAPSAAOAA / answer:49
# # input:AKAAWAKX / answer:33
# # input:LOAAAHAJAAFAEBAWO / answer:79
# # input:AWAWVAQVAAA / answer:35
# # input:RCETAAAAVUEAETZAAAK / answer:75
# # input:GTAASKKAE / answer:52
# # input:AAAABAAAAAAKSAIQ / answer:49
# # input:ADASAAAUAAAPAA / answer:39
# # input:AAAAADBAAELSPUAAAOA / answer:70
# # input:VJAAIAFNAAAAA / answer:47
# # input:AARUAUAAHTBJAAYS / answer:69
# # input:IASAGITUPHE / answer:74
# # input:AAALAAAAAA / answer:14
# # input:AAAEASAHQAYTAAAJ / answer:60
# # input:BAALEAAAPMAAAHSRAV / answer:83
# # input:ASWAAATDAJAXA / answer:45
# # input:DYAOAAAARQANAWA / answer:66
# # input:AAIAPB / answer:24