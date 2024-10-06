from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque(truck_weights)  
    bridge = deque([0] * bridge_length)  
    time = 0  
    bridge_weight = 0  

    while q or bridge_weight > 0:
        time += 1 

        bridge_weight -= bridge.popleft()

        
        if q and bridge_weight + q[0] <= weight:
            truck = q.popleft()
            bridge.append(truck)
            bridge_weight += truck
        else:
            bridge.append(0)  

    return time
