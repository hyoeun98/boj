from collections import deque
def solution(cacheSize, cities):
    if cacheSize  == 0:
        return len(cities) * 5
    
    cities = list(map(str.lower, cities))
    cache = deque(cities[:cacheSize])
    answer = sum([1 if cities[i] in cities[i+1:cacheSize] else 5 for i in range(cacheSize)])
    for i in cities[cacheSize:]:
        if i in cache:
            answer += 1
            cache.remove(i)
        else:
            answer += 5
            cache.popleft()
            
        cache.append(i)
            
    return answer