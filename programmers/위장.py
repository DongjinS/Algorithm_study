def solution(clothes):
    from collections import defaultdict
    from itertools import product
    answer = 0
    cloth_dict = defaultdict(list)
    for cloth, category in clothes:
        cloth_dict[category].append(cloth)
        
    for category in cloth_dict:
        answer += len(cloth_dict[category])
      
    print(answer)
    if len(cloth_dict.keys())>1:
        combi_list = set()
        container = []
        for value in cloth_dict.values():
                   for value2 in cloth_dict.values():
                     
            container.append(value)
            combi_list.add((product(*container)))
          
        combi_list = list(map(list, combi_list))
        for combi in combi_list:
          print(combi)
          answer += len(list(map(list,combi)))
    
    print(answer)
    return answer

solution([["oneface", "face"], ["twoface", "face"], ["oneshirt", "shirt"], ["onepants", "pants"], ["oneouter", "outer"]])