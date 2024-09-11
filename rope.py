N = int(input())

min = 0
array = []
# 돌아가면서 첫번째부터 돌아가기. 
for _ in range(N):
  k = int(input())
  array.append(k)

max = 0
array.sort()
for j in range(N):
  k = array[j]
  t = k * (N-j)
  if max < t:
    max = t
  

print(max)
