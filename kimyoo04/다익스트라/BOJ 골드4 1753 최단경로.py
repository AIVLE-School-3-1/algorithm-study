# https://www.acmicpc.net/problem/1753

"""
문제
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

입력
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

출력
첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

예제 입력 1
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

예제 출력 1
0
2
3
7
INF
"""

import sys; input=sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split()) # 정점의 개수 V, 간선의 개수 E
K = int(input()) # 시작점 K

# 인접 리스트
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    # u -> v 로 가는 가중치 w
    u, v, w = map(int, input().split()) # w는 10 이하의 자연수
    graph[u].append((v, w)) # 가중치도 같이 저장

visited = [False for _ in range(V + 1)] # 방문 여부
distance = [sys.maxsize for _ in range(V + 1)] # 최단거리 저장

q = PriorityQueue()
q.put((0, K))  # K를 시작점으로 설정
distance[K] = 0

while q.qsize() > 0:
    now_distance, now = q.get()

    # 현재 노드 방문 여부 확인
    if visited[now]:
        continue
    visited[now] = True

    # 다음 노드 반복 확인
    for next, weight in graph[now]:
        if distance[next] > distance[now] + weight:  # 최소 거리로 업데이트
            distance[next] = distance[now] + weight
            q.put((distance[next], next))


for i in range(1, V + 1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")
