import sys
import heapq as hq

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    sync = dict()
    for _ in range(k):
        i, n = sys.stdin.readline().split()
        n = int(n)
        if i == "I":
            if n in sync:
                sync[n] += 1
            else:
                sync[n] = 1
                hq.heappush(min_heap, n)
                hq.heappush(max_heap, -n)
        else:
            flag = False
            for i in sync.values():
                if i > 0:
                    flag = True
                    break
            if not flag:
                pass
            elif n == 1:
                while -max_heap[0] not in sync or sync[-max_heap[0]] < 1:
                    temp = -hq.heappop(max_heap)
                    if temp in sync:
                        del(sync[temp])
                sync[-max_heap[0]] -= 1
            else:
                while min_heap[0] not in sync or sync[min_heap[0]] < 1:
                    temp = hq.heappop(min_heap)
                    if temp in sync:
                        del(sync[temp])
                sync[min_heap[0]] -= 1
                
    if not sum([sync[k] for k in sync]):
        print("EMPTY")
    else:
        while min_heap[0] not in sync or sync[min_heap[0]] < 1:
            hq.heappop(min_heap)
        while -max_heap[0] not in sync or sync[-max_heap[0]] < 1:
            hq.heappop(max_heap)
        print(-hq.heappop(max_heap), hq.heappop(min_heap))
        