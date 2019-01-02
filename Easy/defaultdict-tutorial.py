# problem: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
from collections import defaultdict
words = defaultdict(list)
m,n = input().split()

for _ in range(int(m)):
    words['A'].append(input())
for _ in range(int(n)):
    words['B'].append(input())

for word in words['B']:
    indices = [i+1 for i, x in enumerate(words['A']) if x == word]
    if len(indices)==0:
        print(-1)
    else:
        print(*indices)