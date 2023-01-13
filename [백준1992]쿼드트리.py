import sys
input = sys.stdin.readline

def solution() -> None:
    N = int(sys.stdin.readline().rstrip())
    field = [list(map(int, input().strip())) for _ in range(N)]

    def quad(x, y, n):
        st = field[y][x]
        for i in range(y, y+n):
            for j in range(x, x + n):
                if field[i][j] != st:
                    half = n // 2
                    print("(", end="")
                    quad(x, y, half)
                    quad(x + half, y, half)
                    quad(x, y + half, half)
                    quad(x + half, y + half, half)
                    print(")", end="")
                    return;
        print(st, end="")    
    quad(0, 0, len(field))

solution()