# 탐색
def solution(info, edges):
    answer = 0
    sheep = 1
    wolf = 0
    visted = [False]*len(info)
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        graph[edge[0]].append(edge[1])
    print(graph)
    for i in range(len(graph)):
        for idx in graph[i]:
            if visted[idx] == False :
                if info[idx] == 0:
                    sheep += 1
                if info[idx] == 1:
                    wolf += 1
                if sheep > wolf:
                    visted[idx] = True
                else:
                    sheep -= 1
                    wolf -= 1
    print('sheep: ', sheep,'wolf:',wolf)
    print(visted)
    # 0이 양 1이 늑대
    return answer


info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

print(solution(info, edges))