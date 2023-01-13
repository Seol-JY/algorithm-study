import sys
sys.setrecursionlimit(10**6)
def solution() -> None:
    arr = []

    def dfs(i: int, j: int, arr: list[list[int]]) -> None:
        if not (0 <= i < len(arr)) or \
            not (0 <= j < len(arr[0])) or \
            not arr[i][j]:
                return
        arr[i][j] = 0

        dfs(i + 1, j, arr)
        dfs(i - 1, j, arr)
        dfs(i, j + 1, arr)
        dfs(i, j - 1, arr)
        dfs(i - 1, j -  1, arr)
        dfs(i - 1, j +  1, arr)
        dfs(i + 1, j -  1, arr)
        dfs(i + 1, j +  1, arr)

    def numberOfIsland(arr: list[list[int]]) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j]:
                    dfs(i, j, arr)
                    count += 1
        return count

    while True:
        width, height =  map(int, sys.stdin.readline().rstrip().split())
        if width == height == 0: break
        tmp = []
        for _ in range(height):
            tmp.append(list(map(int, sys.stdin.readline().rstrip().split())))
        arr.append(tmp[:])

    for i in range(len(arr)): print(numberOfIsland(arr[i]))

solution()