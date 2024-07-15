import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
array = []

for _ in range(n):
  array.append(list(map(int, input().split())))

visit = [[0 for i in range(m)] for j in range(n)]

i_num = 0

nl = [-1, 0, 1, 0]
nc = [0, -1, 0, 1]

i_size = 0

def dfs(l, c):
  global visit
  global i_size
  i_size += 1
  visit[l][c] = i_size

  for i in range(4):
    nnl = l + nl[i]
    nnc = c + nc[i]
    #만약 범위를 벗어나면 for문 시작으로
    if nnl < 0 or nnl >= n or nnc < 0 or nnc >= m:
      continue
    # 만약 visit이 1이면 이미 본 곳이므로 for문 시작ㅇ으로
    if visit[nnl][nnc] != 0:
      continue
    # 만약 array가 0이면 섬이 아니므로 for문 시작으로
    if array[nnl][nnc] == 0:
      continue
    # if 0<= nnl <= n and 0<=nnc<=m and visit[nnl][nnc] == 0 and array[nnl][nnc] == 1:
    #   visit[nnl][nnc] = i_size
    #   dfs(nnl, nnc)
    #visit[nnl][nnc] = i_size
    dfs(nnl, nnc)
    
  
  
maxN = 1

for i in range(n):
  for j in range(m):
    # visit 하지 않았고 섬인 array가 1일 때 
    if visit[i][j] == 0 and array[i][j] == 1:
      i_num += 1
      # 섬 크기 시작, 초기화
      i_size = 1
      #visit[i][j] = i_size
      dfs(i, j)
      maxN = max(maxN, i_size)

print(i_num)
print(maxN - 1)