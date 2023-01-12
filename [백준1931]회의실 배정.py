import sys

def solve() -> int:
    N = int(sys.stdin.readline().rstrip())

    time_info = [ tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N) ]
    time_info.sort(key = lambda x: (x[1], x[0]))
    end_time = time_info[0][1]

    result = 1
    for i in range(1,N):
        if end_time <= time_info[i][0]:
            result += 1
            end_time = time_info[i][1]

    return result

print(solve())