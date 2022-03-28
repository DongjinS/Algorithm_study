def solution(lines):
    answer = 1
    timestamps = []
    
    for line in lines:
        endTimeStamp = 0
        startTimeStamp = 0
        end = line.split()[1].split(":")
        endTimeStamp = int(float(end[2])*1000 + (int(end[1]) * 1000 * 60) +  (int(end[0]) * 1000 * 60 * 60))
        startTimeStamp = endTimeStamp - int(float(line.split()[2].split("s")[0])*1000) + 1
        timestamps.append([startTimeStamp, endTimeStamp])
    

    for i in range(len(timestamps)):
        cnt = 0
        for j in range(i,len(timestamps)):
            if timestamps[j][0] - timestamps[i][1] < 1000:
                cnt += 1
        answer = max(cnt, answer)
        
    return answer