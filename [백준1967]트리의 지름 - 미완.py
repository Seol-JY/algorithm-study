import sys
sys.setrecursionlimit(10 ** 9)

def solution() -> int:
    def dfs(x, y):
        for a, b in graph[x]:
            if visited[a] == -1:
                visited[a] = y + b 
                dfs(a, y + b)





    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(n - 1):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    visited = [-1] * (n + 1) # 탐색 확인, 가중치 확인
    visited[1] = 0 # 시작 노드는 가중치를 0으로 초기화
    dfs(1, 0) # 첫 번재 노드를 dfs 탐색

    # 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
    start = visited.index(max(visited))

    visited = [-1] * (n + 1)
    visited[start] = 0
    dfs(start, 0)
    return max(visited)

print(solution())