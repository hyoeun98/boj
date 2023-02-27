import heapq as hq
def solution(numbers):
    answer = [-1] * len(numbers)
    heap = []
    for i, v in enumerate(numbers):
        while heap and heap[0][0] < v:
            _, idx = hq.heappop(heap)
            answer[idx] = v
            
        hq.heappush(heap, [v, i])
    return answer