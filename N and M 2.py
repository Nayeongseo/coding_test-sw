import itertools

x, y = map(int, input().split())

arr = [i for i in range(1, x+1)]
prob = itertools.combinations(arr, y)
proba = list(prob)
if proba[0] == 1:
  print(proba[0][0])
else:
  for i in range(len(proba)):
    print(*proba[i])