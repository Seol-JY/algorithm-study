# 제출 시 자료형 지정 제거해야함 
import collections
def solution(arr: list[list[int]]) -> list[int]:
    answer = [0, 0]

    def recur(arr: list[list[int]]) -> None:
        cnt = collections.Counter(sum(arr, []))
        if len(cnt) == 1:
            if 0 in cnt: answer[0] += 1
            else: answer[1] += 1
            return

        recur([i[0:int(len(i)/2)] for i in arr[0:int(len(arr)/2)]])
        recur([i[0:int(len(i)/2)] for i in arr[int(len(arr)/2):len(arr)]])
        recur([i[int(len(i)/2):len(i)] for i in arr[0:int(len(arr)/2)]])
        recur([i[int(len(i)/2):len(i)] for i in arr[int(len(arr)/2):len(arr)]])

    recur(arr)
    return answer
