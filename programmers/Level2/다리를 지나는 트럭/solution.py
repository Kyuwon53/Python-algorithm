def solution(bridge_length, weight, truck_weights):
    bridge = [0 for _ in range(bridge_length)]
    time = 0
    done = []
    count = len(truck_weights)
    while len(done) != count:
        if bridge[0] != 0:
            done.append(bridge[0])

        del bridge[0]
        truck_weight = truck_weights[0] if len(truck_weights) > 0 else 0
        if (truck_weight + sum(bridge)) <= weight:
            bridge.append(truck_weights.pop(0) if truck_weight != 0 else 0)
        else:
            bridge.append(0)
        time += 1
    return time


print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
