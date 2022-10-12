"""
N명 사람들의 이름과 키 정보로 출석부
출석부는 이름을 기준으로 사전 정렬
이름이 같다면 키순으로 오름차순

출석부를 완성하고 k번째 이름과 키를 공백을 두고 출력하라
"""

n, k = map(int, input().split())
absent = []
for _ in range(n):
    name, height = input().split()
    info = [name.rstrip(), height]
    absent.append(info)
absent.sort(key=lambda x: (x[0], x[1]))
print(absent[k - 1][0] + ' ' + absent[k - 1][1])
