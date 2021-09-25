# 서로소 집합 알고리즘 소스
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 최종 루트 노드 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기(union)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 작은 번호가 부모 노드
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0]*(v+1)  #부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a,b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ',end='')
for i in range(1, v+1):
    print(find_parent(parent,i),end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

# 노드의 개수가 V개이고 find 혹은 union 연산의 개수가 M개일 때, 전체 시간복잡도 : O(VM) => 비효율적
# find 함수는 최적화 가능 => 경로 압축기법(Path Compression)=> find 함수를 재귀적으로 호출 => 부모 테이블 갱신

def find_parent2(parent, x):
    if parent[x] != x:
        parent[x] = find_parent2(parent, parent[x])
    return  parent[x]
