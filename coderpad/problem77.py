def solution(intervals):
    sorted_interval = sorted(intervals)
    merged_interval = []
    for interval in sorted_interval:
        if merged_interval and interval[0] <= merged_interval[-1][1]:
            merged_interval[-1] = (merged_interval[-1][0], max(merged_interval[-1][1], interval[1]))
        else:
            merged_interval.append(interval)
    return merged_interval