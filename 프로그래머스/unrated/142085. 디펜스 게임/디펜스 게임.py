import heapq
def solution(n, k, enemy):
    minHeap = enemy[:k]
    heapq.heapify(minHeap)
    for i in range(k, len(enemy)):
        n -= heapq.heappushpop(minHeap, enemy[i])
        if n < 0:
            return i
    return len(enemy)
