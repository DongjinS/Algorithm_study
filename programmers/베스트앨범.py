def solution(genres, plays):
    from collections import defaultdict
    answer = []
    
    hashTable = defaultdict(list)
    for i, genre in enumerate(genres):
        hashTable[genre].append([plays[i],10001-i])
    
    for genre in hashTable.values():
        genre.sort(key=lambda x:(x[0],x[1]), reverse=True)
        total_play = 0
        for song in (genre):
          total_play += song[0]
        genre.append(total_play)
    
    sorted_genre = list(hashTable.values())
    sorted_genre.sort(key=lambda x:x[-1], reverse=True)
    print(sorted_genre)

    for genre in sorted_genre:
      genre = genre[:-1]
      for song in genre:
        answer.append(10001 - song[1])
    print(answer)
    return answer

solution(["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500])