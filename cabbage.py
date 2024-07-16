# 백준 1012번
import sys
sys.setrecursionlimit(1000000)


T = int(input())
answer = []
d = [(0,1), (0,-1), (1, 0), (-1, 0)]

for _ in range(T):
  M, N, K = map(int, input().split())

  visit = [[0 for _ in range(M)] for _ in range(N)]
  arr = [[0 for _ in range(M)] for _ in range(N)]

  for _ in range(K):
    x, y = map(int, input().split())
    arr[y][x] = 1

  

  def dfs(r, c):
    for dr, dc in d:
      ddr, ddc = dr + r, dc + c
      if 0 <= ddr < N and 0 <= ddc < M and arr[ddr][ddc] == 1 and visit[ddr][ddc] == 0:
        visit[ddr][ddc] = 1
        dfs(ddr, ddc)

  count = 0
  for i in range(N):
    for j in range(M):
      if arr[i][j] == 1 and visit[i][j] == 0:
        count += 1
        visit[i][j] = 1
        dfs(i, j)
  answer.append(count)

for i in range(T):
  print(answer[i])
  
  
