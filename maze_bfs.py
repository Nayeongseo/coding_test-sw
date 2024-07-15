# 백준 2178번

from collections import deque

N, M = map(int, input().split())

board = []
for _ in range(N):
  board.append(list(input()))

d = [(-1,0), (0,1), (1,0), (0,-1)]

sn, sm = 0, 0
en, em = N-1, M-1

visit = [[0 for _ in range(M)] for _ in range(N)]

q = deque()

q.append((sn, sm))
visit[sn][sm] = 1

while q:
  r, c = q.popleft()
  for dr, dc in d:
    ddr, ddc = dr + r, dc + c
    if 0 <= ddr < N and 0 <= ddc < M and visit[ddr][ddc] == 0 and board[ddr][ddc] == '1':
      visit[ddr][ddc] = visit[r][c] + 1
      q.append((ddr, ddc))



print(visit[en][em])