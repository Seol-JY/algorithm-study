import sys

def solve() -> int:
  def prime_list(n: int) -> list[int]:
    isPrime = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
      if isPrime[i] == True:
        for j in range(i+i, n, i): isPrime[j] = False
    return [i for i in range(2, n) if isPrime[i] == True]

  N = int(sys.stdin.readline().rstrip())
  result = 0
  if N == 1: return result
  sequence = prime_list(N+1)

  start = 0
  end = 0
  partial_sum = sequence[0]

  while True:
    if partial_sum > N:
      partial_sum -= sequence[start]
      start += 1
    else:
      if partial_sum == N: result += 1
      end += 1
      if end >= len(sequence): break
      partial_sum += sequence[end]
  return result

print(solve())