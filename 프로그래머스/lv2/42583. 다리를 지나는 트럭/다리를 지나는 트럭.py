from collections import deque
def solution(bridge_length, weight, truck_weights):
    t = deque(truck_weights)
    bridge = deque()
    elapsed_time = 0
    
    while t:
        elapsed_time += 1
        truck = t.popleft()
        
        if bridge and bridge[-1][1] == 1:
            bridge.pop()
            
        current_weight = 0
        for i, v in enumerate(bridge):
            bridge[i][1] -= 1
            current_weight += v[0]
            
        while current_weight + truck > weight or len(bridge) >= bridge_length:
            b = bridge.pop()
            elapsed_time += b[1]
            current_weight = 0
            for i, v in enumerate(bridge):
                current_weight += v[0]
                bridge[i][1] -= b[1]
        
        bridge.appendleft([truck, bridge_length])
        
    if bridge:
        elapsed_time += bridge[0][1]

    return elapsed_time