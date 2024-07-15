# 백준 7576번

from collections import deque

M, N = map(int, input().split())

q = deque()

arr = []
visit = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
  arr.append(list(map(int, input().split())))

d = [(-1,0), (0,1), (0,-1), (1, 0)]

maxV = 0

for i in range(N):
  for j in range(M):
    if arr[i][j] == 1:
      q.append((i,j))
      visit[i][j] = 1
      maxV = 1

while q:
  l, c = q.popleft()
  for nl, nc in d:
    nnl, nnc = nl + l, nc + c
    if 0 <= nnl < N and 0 <= nnc < M and visit[nnl][nnc] == 0 and arr[nnl][nnc] == 0:
      visit[nnl][nnc] = visit[l][c] + 1
      q.append((nnl, nnc))
      maxV = max(maxV, visit[nnl][nnc])

# -1이 있으면 삭제
for i in range(N):
  for j in range(M):
    if visit[i][j] == 0 and arr[i][j] == 0:
      maxV = 0

print(maxV - 1)
