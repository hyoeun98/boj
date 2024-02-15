import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    
    for op in operations:
        a, b = op.split()
        b = int(b)
        if a == "I":
            heapq.heappush(max_heap, (-b, b))
            heapq.heappush(min_heap, b)
        elif min_heap:
            if b == 1:
                max_num = heapq.heappop(max_heap)[1]
                min_heap.remove(max_num)
            else:
                min_num = heapq.heappop(min_heap)
                max_heap.remove((-min_num, min_num))
    
    return [0, 0] if not min_heap else [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]