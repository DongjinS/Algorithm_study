from collections import defaultdict
def solution(id_list, report, k):
  answer = []
  
  reported = defaultdict(int)
  reporting = defaultdict(list)
  get_mailed = defaultdict(int)

  for id in id_list:
      reported[id] = 0
      reporting[id] = []
  for r in report:
      id = r.split(' ')
      if id[1] not in reporting[id[0]]:
          reporting[id[0]].append(id[1])
          reported[id[1]]+=1

  for id in id_list:
    if reported[id] >= k:
      for reporter in reporting:
        if id in reporting[reporter]:
          get_mailed[reporter]+=1
  
  for id in id_list:
    answer.append(get_mailed[id])
    
  return answer

solution(["muzi", "frodo", "apeach", "neo"]	,["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],	2)

# 