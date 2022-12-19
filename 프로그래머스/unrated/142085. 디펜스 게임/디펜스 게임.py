import heapq
def solution(n, k, enemy):
    minHeap = enemy[:k]
    heapq.heapify(minHeap)
    for i in range(k, len(enemy)):
        heapq.heappush(minHeap, enemy[i])
        n -= heapq.heappop(minHeap)
        if n < 0:
            return i
    return len(enemy)
